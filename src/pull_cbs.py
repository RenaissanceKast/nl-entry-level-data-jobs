"""Download CBS table 85081NED (job vacancies by occupation group / industry) via the open OData API.

Source: Statistics Netherlands (CBS), licence CC-BY 4.0 - credit CBS when publishing.
Run:  python src/pull_cbs.py
Output: data/raw/cbs_85081NED_<name>.csv for every table in the dataset, plus data/raw/cbs_meta.json.
"""
import json
import pathlib

import pandas as pd
import requests

BASE = "https://opendata.cbs.nl/ODataApi/OData/85081NED"
OUT = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)


def fetch_all(url):
    """Follow OData paging links and return all rows."""
    rows = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        rows += j["value"]
        url = j.get("odata.nextLink")
    return rows


info = requests.get(f"{BASE}/TableInfos", timeout=60).json()["value"][0]
(OUT / "cbs_meta.json").write_text(json.dumps(info, indent=2, ensure_ascii=False))
print("Table:", info.get("Title"), "| modified:", info.get("Modified"))

# list the entities (TypedDataSet, dimension tables, ...)
entities = [e["name"] for e in requests.get(BASE, timeout=60).json()["value"]]
print("Entities:", entities)

for name in entities:
    if name in ("TableInfos", "DataProperties", "UntypedDataSet"):
        continue
    df = pd.DataFrame(fetch_all(f"{BASE}/{name}"))
    df.to_csv(OUT / f"cbs_85081NED_{name}.csv", index=False)
    print(f"{name}: {df.shape}")
