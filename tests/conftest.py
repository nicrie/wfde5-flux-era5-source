import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-build-tests",
        action="store_true",
        default=False,
        help="run optional dataset build tests",
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "build_dataset: optional end-to-end dataset build test",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-build-tests"):
        return

    skip_build = pytest.mark.skip(
        reason="need --run-build-tests option to run dataset build tests",
    )
    for item in items:
        if "build_dataset" in item.keywords:
            item.add_marker(skip_build)
