# ETL Pipeline: CSV to BigQuery

## Description
ETL pipeline to load Electric Vehicle charging data into BigQuery.

## Prerequisites
- Python 3.14+
- Google Cloud Platform account
- BigQuery API enabled
- Service account with BigQuery permissions

## Setup Instructions

### 1. Clone the repository
\`\`\`
git clone <your-repo-url>
cd ETL_Pipline_CSVtoBigQuery
\`\`\`

### 2. Create virtual environment
\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
\`\`\`

### 3. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set up BigQuery credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable BigQuery API
4. Create a service account with BigQuery Admin role
5. Download the JSON key file
6. Create a `credentials` folder in the project root
7. Place your key file as `credentials/bigquery-key.json`

### 5. Update configuration
Edit `main.py` and update the project ID:
\`\`\`python
client = bigquery.Client(project='YOUR_PROJECT_ID')
\`\`\`

### 6. Run the pipeline
\`\`\`bash
python main.py
\`\`\`

## Project Structure
\`\`\`
ETL_Pipline_CSVtoBigQuery/
├── credentials/           # (git-ignored) Place your BigQuery credentials here
├── data/                  # Data files
├── main.py               # Main ETL script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file
\`\`\`