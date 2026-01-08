from flask import Flask, redirect, request, jsonify
from nyaa_scrap import NyaaScrap
import json

app = Flask(__name__)
scraper = NyaaScrap()

@app.route('/')
def index():
    return '''
    <h1>Nyaa Scraper API</h1>
    <p>Para usar la API:</p>
    <ul>
        <li><strong>/fun?q=termino</strong> - Búsqueda en nyaa.si</li>
        <li><strong>/fap?q=termino</strong> - Búsqueda en sukebei.nyaa.si</li>
    </ul>
    <p>Ejemplo: <a href="/fun?q=naruto">/fun?q=naruto</a></p>
    '''

@app.route('/fun')
def search_fun():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Parámetro "q" requerido'}), 400
    
    try:
        result = scraper.search_fun(query)
        return app.response_class(
            response=result,
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/fap')
def search_fap():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Parámetro "q" requerido'}), 400
    
    try:
        result = scraper.search_fap(query)
        return app.response_class(
            response=result,
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)