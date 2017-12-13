# --- Flask Hello World --- #

# import Flask class from flask package
from flask import Flask

# create app obj
app = Flask(__name__)

# use decorators to link function to url
@app.route("/")
@app.route("/hello")

# define view using a function which returns a string
def hello_world():
	return "Hello, World!"

# start development server using the run() method
if __name__ == "__main__":
	app.run()