from flask import Flask, render_template

from controllers.hobby_controller import hobby_blueprint
from controllers.location_controller import location_blueprint
from controllers.user_controller import user, user_blueprint

app = Flask(__name__)

app.register_blueprint(hobby_blueprint)
app.register_blueprint(location_blueprint)
app.register_blueprint(user_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
