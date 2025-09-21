from flask import Flask, render_template, request, jsonify, send_from_directory
import sys
import os

# Add the news scraper directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'news scraper copy'))

from sources.cnbcindonesia import CNBCIndonesia
from sources.detikfinance import DetikFinance
from sources.emitennews import EmitenNews
from sources.idxchannel import IDXChannel
from sources.kontan import Kontan

app = Flask(__name__)

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
