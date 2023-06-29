from flask import Flask, render_template

from controllers.manufacturer_controller import manufacturer_blueprint
from controllers.car_controller import car_blueprint

app = Flask(__name__)


app.register_blueprint(manufacturer_blueprint)
app.register_blueprint(car_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)