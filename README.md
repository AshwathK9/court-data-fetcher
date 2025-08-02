# Court Data Fetcher

## 🔍 Description
This Flask app fetches court case metadata from Delhi High Court.  
Users input Case Type, Number, and Filing Year, and the app returns parties involved, hearing dates, and order PDFs.

## ⚙️ Setup

```bash
git clone https://github.com/your-username/court-data-fetcher.git
cd court-data-fetcher
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install
sqlite3 db.sqlite3 < schema.sql
python app.py
