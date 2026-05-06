import subprocess
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
RECIPE_PATH = TESTS_DIR / "test-wfde5-anemoi-recipe.yaml"
OUTPUT_PATH = Path(
    "/ec/res4/scratch/ecm6845/wfde5-ml/anemoi/datasets/wfde5_ml_test.zarr"
)


def _tail(text: str, lines: int = 80) -> str:
    items = text.splitlines()
    return "\n".join(items[-lines:])


@pytest.mark.build_dataset
def test_build_recipe_succeeds():
    result = subprocess.run(
        [
            "anemoi-datasets",
            "create",
            str(RECIPE_PATH),
            str(OUTPUT_PATH),
            "--overwrite",
        ],
        cwd=TESTS_DIR,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, (
        "dataset build failed\n"
        f"stdout tail:\n{_tail(result.stdout)}\n\n"
        f"stderr tail:\n{_tail(result.stderr)}"
    )
    assert OUTPUT_PATH.exists(), f"Expected dataset output at {OUTPUT_PATH}"
