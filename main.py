from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World! Welcome Azure'

@app.route('/home')
def index():
	return render_template('home.html')


if __name__ == '__main__':
  app.run(debug=True)
