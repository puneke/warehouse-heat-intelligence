from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

REQUIRED_RAW_FILES = [
    RAW_DIR / "daily-temperature-for-30-sites-to-2022-part1.csv",
    RAW_DIR / "daily-temperature-for-30-sites-to-2022-part2.csv",
    RAW_DIR / "daily-temperature-for-30-sites-to-2022-part3.csv",
    RAW_DIR / "mean_relative_humidity_1991-2020_0.xlsx",
]

PROCESSED_FILE = PROCESSED_DIR / "daily-temperature-for-depots.csv"


def file_size_mb(path: Path) -> float:
    return path.stat().st_size / (1024 * 1024)


def main() -> None:
    missing = [path for path in REQUIRED_RAW_FILES if not path.exists()]
    if missing:
        print("Missing required raw data files:")
        for path in missing:
            print(f"- {path.relative_to(PROJECT_DIR)}")
        print("\nSee data/README.md for source links and expected filenames.")
        raise SystemExit(1)

    print("Raw data files found:")
    for path in REQUIRED_RAW_FILES:
        print(f"- {path.relative_to(PROJECT_DIR)} ({file_size_mb(path):.1f} MB)")

    if PROCESSED_FILE.exists():
        print(f"\nProcessed file found: {PROCESSED_FILE.relative_to(PROJECT_DIR)} ({file_size_mb(PROCESSED_FILE):.1f} MB)")
    else:
        print("\nProcessed file not found. Run: make preprocess")


if __name__ == "__main__":
    main()
