from flask import Flask, render_template, request, jsonify, send_from_directory
import sys
import os
import pandas as pd

# Add the news scraper directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'news scraper copy'))

from sources.cnbcindonesia import CNBCIndonesia
from sources.detikfinance import DetikFinance
from sources.emitennews import EmitenNews
from sources.idxchannel import IDXChannel
from sources.kontan import Kontan

app = Flask(__name__)

# Load stock data
try:
    _df = pd.read_excel("Daftar Saham  - 20250920.xlsx")
    _df = _df.rename(columns={
        "Kode": "code",
        "Nama Perusahaan": "name",
        "Tanggal Pencatatan": "date"
    })
    _df["code_l"] = _df["code"].str.lower()
    _df["name_l"] = _df["name"].str.lower()
    stocks_initialized = True
    print(f"Loaded {len(_df)} stocks from Excel file")
except Exception as e:
    print(f"Warning: Failed to load stock data: {e}")
    stocks_initialized = False
    _df = None

# Initialize news scrapers
try:
    cnbcindonesia = CNBCIndonesia()
    detikfinance = DetikFinance()
    emitennews = EmitenNews()
    idxchannel = IDXChannel()
    kontan = Kontan()
    scrapers_initialized = True
except Exception as e:
    print(f"Warning: Failed to initialize news scrapers: {e}")
    scrapers_initialized = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/api/news', methods=['POST'])
def search_news():
    try:
        if not scrapers_initialized:
            return jsonify({'error': 'News scrapers not available'}), 503
        
        data = request.get_json()
        keyword = data.get('keyword', '').strip()
        
        if not keyword:
            return jsonify({'error': 'Keyword is required'}), 400
        
        # Search all news sources
        results = {
            'cnbc': cnbcindonesia.keyword_cnbcindonesia([keyword.capitalize()]),
            'detikfinance': detikfinance.keyword_detikfinance([keyword.capitalize()]),
            'emitennews': emitennews.keyword_emitennews([keyword.capitalize()]),
            'idxchannel': idxchannel.keyword_idxchannel([keyword.capitalize()]),
            'kontan': kontan.keyword_kontan([keyword.capitalize()])
        }
        
        return jsonify({
            'success': True,
            'keyword': keyword,
            'results': results
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stocks')
def api_stocks():
    try:
        if not stocks_initialized:
            return jsonify({'error': 'Stock data not available'}), 503
        
        page = max(int(request.args.get("page", 1)), 1)
        size = min(max(int(request.args.get("page_size", 200)), 1), 500)
        q = (request.args.get("query") or "").strip().lower()

        df = _df
        if q:
            m = df["code_l"].str.contains(q, na=False) | df["name_l"].str.contains(q, na=False)
            df = df[m]

        total = len(df)
        start = (page - 1) * size
        items = df.iloc[start:start+size][["code", "name", "date"]].to_dict(orient="records")
        return jsonify({"total": total, "items": items})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
