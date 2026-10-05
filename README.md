# What do entry-level data roles in the Netherlands ask for?

A small, reproducible analysis of entry-level and internship data roles in the Netherlands, set against official vacancy statistics.

## Questions
1. Which skills (SQL, Python, Power BI, ...) appear most often in these roles?
2. How many require Dutch, and how many accept English only?
3. How are roles split across cities, role types and company types?
4. How do vacancy trends for ICT and data occupations (CBS) compare with the entry-level picture?

## Data
- **CBS table 85081NED** (job vacancies by occupation group and industry, annual from 2018). Licence CC-BY 4.0, source: Statistics Netherlands. Pulled with `src/pull_cbs.py`.
- **Hand-collected listing sample** (`data/sample/`). Skills coded as 1/0 per listing; no listing text is copied and no scraping is used. See the Codebook sheet for the rules.

## Limits
The listing sample is small and non-random, so results describe the sample and not the whole market.

## Layout
```
src/pull_cbs.py     download CBS data
data/raw/           CBS downloads
data/sample/        listing collection workbook / CSV export
requirements.txt
```
