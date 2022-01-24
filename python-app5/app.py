import time
import random
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def new():
    return 'OK'

@app.route('/metrics')
@metrics.do_not_track()
@metrics.histogram('http_request_duration_seconds', 'Duration of HTTP requests in seconds',buckets= [0.1, 0.3, 0.5, 0.7, 1, 3, 5, 7, 10],
         labels={'item_type': lambda: request.view_args['type']})
@metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
def metric():
    pass


@app.route('/order')
def test():
    
    time.sleep(random.random() * 0.8)
    return 'Order created successfully'

@app.route('/error')
def oops():
    return ':(', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)