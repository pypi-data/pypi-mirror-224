import csv
import dataclasses
import uuid

import pytest

from allspice import AllSpice
from allspice.utils.bom_generation import AttributesMapping, generate_bom_for_altium

test_repo = "repo_" + uuid.uuid4().hex[:8]


@pytest.fixture
def instance():
    try:
        g = AllSpice(
            "http://localhost:3000",
            open(".token", "r").read().strip(),
            ratelimiting=None,
        )
        print("AllSpice Hub Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)

        _setup_for_bom_generation(g)

        return g
    except Exception:
        breakpoint()
        assert (
            False
        ), "AllSpice Hub could not load. Is there: \
                - an Instance running at http://localhost:3000 \
                - a Token at .token \
                    ?"


def _setup_for_bom_generation(instance):
    instance.requests_post(
        "/repos/migrate",
        data={
            "clone_addr": "https://hub.allspice.io/AllSpiceUser/ArchimajorFork.git",
            "mirror": False,
            "repo_name": test_repo,
            "service": "git",
        },
    )

    repo = instance.get_repository(instance.get_user().username, test_repo)
    files = repo.get_git_content()
    # Kick off JSON generation
    for file in files:
        try:
            repo.get_generated_json(file.path)
        except Exception:
            pass


def test_bom_generation(instance):
    repo = instance.get_repository(instance.get_user().username, test_repo)
    attributes_mapping = AttributesMapping(
        description=["PART DESCRIPTION"],
        designator=["Designator"],
        manufacturer=["Manufacturer", "MANUFACTURER"],
        part_number=["PART", "MANUFACTURER #"],
    )
    bom = generate_bom_for_altium(
        instance,
        repo,
        "Archimajor.PrjPcb",
        "Archimajor.PcbDoc",
        attributes_mapping,
        # We hard-code a ref so that this test is reproducible.
        ref="820f424555d11132123876bef04f7fb5579d40d2",
    )
    assert len(bom) == 106

    bom_as_dicts = []
    # We have to do this manually because of how csv.DictWriter works.
    for item in bom:
        entry_as_dict = {}
        for (key, value) in dataclasses.asdict(item).items():
            entry_as_dict[key] = str(value) if value is not None else ""
        bom_as_dicts.append(entry_as_dict)

    with open("tests/data/archimajor_bom_expected.csv", "r") as f:
        reader = csv.DictReader(f)
        for row, expected_row in zip(reader, bom_as_dicts):
            assert row == expected_row
