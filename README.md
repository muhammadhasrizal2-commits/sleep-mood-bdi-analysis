# Sleep, Mood, and BDI Analysis

This project is a lightweight Python workspace for exploring the relationship between sleep patterns, mood, and Beck Depression Inventory (BDI) scores.

## First Presentation – Session 6 
The first presentation will focus primarily on the foundations of your project. 
The duration of your presentation should be 10min plus 2-3 min Q&A for each group. 
Please be very on-time on presentation dates because we need to fit all your 
presentations in the time we can use the lab. 
You should expect to present, at minimum: 
• Your research question 
• Your dataset 
• Relevant ethical considerations 
• Your data-cleaning and preprocessing approach 
• Descriptive statistics and initial findings 

## Section Allocations:
- Ciara: research question + dataset
- Joyce: ethical considerations
- Saif: data-cleaning + preprocessing
- Emily: descriptive statistics + inital findings

## Project goals
- Load raw CSV data from `data/raw/`
- Clean and validate the dataset in `data/processed/`
- Explore the relationships between sleep metrics, mood ratings, and depressive symptoms
- Produce reproducible analysis notebooks and summary outputs

## Suggested layout
- `data/raw/` — source CSV files
- `data/processed/` — cleaned data outputs
- `notebooks/` — exploratory analysis notebooks
- `src/` — reusable Python analysis code

## Quick start
1. Add your source CSV files to `data/raw/`
2. Create a virtual environment if needed
3. Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Run the analysis scaffold:

```bash
python -m src.analysis
```

## Notes
The repository is intentionally set up as a starting template so you can drop in your dataset and begin analysis immediately.
