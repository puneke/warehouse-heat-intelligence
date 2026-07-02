import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
ANALYSIS_NOTEBOOK = PROJECT_DIR / "02_analysis.ipynb"


def run_notebook(path: Path) -> None:
    print(f"Executing {path.name}")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--execute",
            "--to",
            "notebook",
            "--inplace",
            str(path),
        ],
        cwd=PROJECT_DIR,
        check=True,
    )


def main() -> None:
    run_notebook(ANALYSIS_NOTEBOOK)


if __name__ == "__main__":
    main()
