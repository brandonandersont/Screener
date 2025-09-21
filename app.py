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
cnbcindonesia = CNBCIndonesia()
detikfinance = DetikFinance()
emitennews = EmitenNews()
idxchannel = IDXChannel()
kontan = Kontan()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/api/news', methods=['POST'])
def search_news():
    try:
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
    app.run(debug=True, host='0.0.0.0', port=5001)
