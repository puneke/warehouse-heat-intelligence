from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILES = [
    RAW_DIR / "daily-temperature-for-30-sites-to-2022-part1.csv",
    RAW_DIR / "daily-temperature-for-30-sites-to-2022-part2.csv",
    RAW_DIR / "daily-temperature-for-30-sites-to-2022-part3.csv",
]

SITES_TO_KEEP = [
    "Whangārei (Northland)",
    "Auckland (Auckland)",
    "Hamilton (Waikato)",
    "Tauranga (Bay of Plenty)",
    "Napier (Hawke's Bay)",
    "New Plymouth (Taranaki)",
    "Dannevirke (Manawatū-Whanganui)",
    "Wellington (Wellington)",
    "Blenheim (Marlborough)",
    "Christchurch (Canterbury)",
    "Queenstown (Otago)",
    "Dunedin (Otago)",
]

SITE_MAPPING = {
    "Whangārei (Northland)": "Whangarei",
    "Auckland (Auckland)": "Auckland",
    "Hamilton (Waikato)": "Hamilton",
    "Tauranga (Bay of Plenty)": "Tauranga",
    "Napier (Hawke's Bay)": "Napier",
    "New Plymouth (Taranaki)": "New Plymouth",
    "Dannevirke (Manawatū-Whanganui)": "Palmerston North",
    "Wellington (Wellington)": "Wellington",
    "Blenheim (Marlborough)": "Blenheim",
    "Christchurch (Canterbury)": "Christchurch",
    "Queenstown (Otago)": "Queenstown",
    "Dunedin (Otago)": "Dunedin",
}


def require_files(paths: list[Path]) -> None:
    missing = [path for path in paths if not path.exists()]
    if missing:
        missing_list = "\n".join(f"- {path.relative_to(PROJECT_DIR)}" for path in missing)
        raise FileNotFoundError(f"Missing required raw data files:\n{missing_list}\n\nSee data/README.md.")


def main() -> None:
    require_files(CSV_FILES)

    parts = [pd.read_csv(path) for path in CSV_FILES]
    daily_temperature = pd.concat(parts, ignore_index=True)

    filtered = daily_temperature[daily_temperature["site"].isin(SITES_TO_KEEP)].copy()
    filtered["site"] = filtered["site"].map(SITE_MAPPING)

    output_path = PROCESSED_DIR / "daily-temperature-for-depots.csv"
    filtered.to_csv(output_path, index=False)

    print(f"Combined rows: {len(daily_temperature):,}")
    print(f"Depot rows: {len(filtered):,}")
    print(f"Saved: {output_path.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
