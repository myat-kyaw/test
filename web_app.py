from flask import Flask, request, jsonify, render_template
from advanced_calculator import evaluate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json(force=True)
    expression = data.get('expression', '')
    try:
        result = evaluate(expression)
        return jsonify({'result': result})
    except Exception as exc:
        return jsonify({'error': str(exc)}), 400


if __name__ == '__main__':
    app.run(debug=True)
