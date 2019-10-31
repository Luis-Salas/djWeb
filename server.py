from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
@app.route('/')       
def hello_world():
  return render_template('index.html')    # Render the template and return it!
app.run(debug=True)                  