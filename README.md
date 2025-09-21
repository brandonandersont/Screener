# Screener with News Integration

This application combines a broker screener with news scraping functionality.

## Features

- **Broker Search**: Search and filter Indonesian stock brokers by code, name, or category
- **News Search**: Search for financial news across multiple Indonesian news sources:
  - CNBC Indonesia
  - Detik Finance
  - Emiten News
  - IDX Channel
  - Kontan

## Setup

### Local Development

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and go to `http://localhost:5001`

## Deployment Options

### Option 1: Railway (Recommended)
1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway will automatically detect the Python app and deploy it
4. Your app will be available at a Railway-provided URL

### Option 2: Heroku
1. Install Heroku CLI
2. Create a Heroku app:
   ```bash
   heroku create your-app-name
   ```
3. Deploy:
   ```bash
   git push heroku main
   ```

### Option 3: Render
1. Go to [Render.com](https://render.com)
2. Connect your GitHub repository
3. Select "Web Service"
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Python Version: 3.11

### Option 4: Netlify (Static Version Only)
For a static version without news search functionality:
1. Run: `python build_static.py`
2. Deploy the `static_site` folder to Netlify

## Usage

### Broker Search
- Use the "Broker Search" section to search for brokers by code or name
- Filter by category using the filter buttons (Ritel, Asing, Institusi)

### News Search
- Use the "News Search" section to search for financial news
- Enter a keyword (e.g., "Bank BCA", "Telkomsel")
- Click "Search News" or press Enter
- Results will be displayed organized by news source

## File Structure

```
Screener/
├── app.py                 # Flask web application
├── requirements.txt       # Python dependencies
├── styles.css            # CSS styles
├── templates/
│   └── index.html        # Main HTML template
└── news scraper copy/    # News scraping modules
    ├── main.py
    └── sources/          # Individual news source scrapers
```

## API Endpoints

- `GET /` - Main application page
- `POST /api/news` - Search for news by keyword
  - Request body: `{"keyword": "search term"}`
  - Returns: JSON with news results from all sources