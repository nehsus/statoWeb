from flask import Flask, request, render_template


application = Flask(__name__)  # Change assignment here


@application.route("/")        # Change your route statements
def hello():
    return render_template('index.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/team')
def team():
    return render_template('team.html')

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=5005)
