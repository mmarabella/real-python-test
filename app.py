# --- Flask Hello World --- #

# import Flask class from flask package
from flask import Flask

# create app obj
app = Flask(__name__)

app.config["DEBUG"] = True

# use decorators to link function to url
@app.route("/")
@app.route("/hello")

# define view using a function which returns a string
def hello_world():
	return "Hello, World!?!?!"

@app.route("/test/<search_query>")
#I'm confused
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_value(value):
	result = str(value + 1)
	return result
	# note: you can only return a string -- something that can
	# be rendered as HTML I guess

@app.route("/name/<name>")
def index(name):
	if name.lower() == "madalyn":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

# start development server using the run() method
if __name__ == "__main__":
	app.run()