# Data

The analysis uses public New Zealand weather and humidity data:

- Temperature: Stats NZ, daily temperature indicator
  https://www.stats.govt.nz/indicators/temperature/
- Relative humidity: NIWA mean relative humidity normals
  https://niwa.co.nz/climate-and-weather/mean-relative-humidity

Large raw and processed files are intentionally excluded from Git by `.gitignore`; only placeholder `.gitkeep` files are committed to preserve the expected folder structure.

Automated downloading is not included because the public source pages may change their direct file URLs. The reproducible workflow starts after the source files have been downloaded into `data/raw/`.

Expected local layout:

```text
data/
  raw/
    daily-temperature-for-30-sites-to-2022-part1.csv
    daily-temperature-for-30-sites-to-2022-part2.csv
    daily-temperature-for-30-sites-to-2022-part3.csv
    mean_relative_humidity_1991-2020_0.xlsx
  processed/
    daily-temperature-for-depots.csv
```

Run `scripts/preprocess.py` to rebuild `data/processed/daily-temperature-for-depots.csv` from the raw files.

Equivalent command-line workflow:

```bash
make check-data
make preprocess
```

`01_preprocessing.ipynb` is retained as an optional interactive walkthrough, but the script is the reproducible preprocessing entry point.
