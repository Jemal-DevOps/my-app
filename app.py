from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return '{"status": "ok", "message": "HomeTab app running"}'

@app.route('/health')
def health():
    return '{"status": "healthy"}'

@app.route('/version')
def version():
    return '{"version": "1.1.0"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
