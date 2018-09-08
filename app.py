from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	return render_template('test.html')

@app.route('/pokemon/<user_input>', methods=['GET'])
def show_info(user_input):
	#get JSON file for identified pokemon
	url = ("http://pokeapi.co/api/v2/pokemon" + "/%s") % user_input
	response = requests.get(url)
	data = response.json()

	#check if user_input is a number or String
	message = ""
	try:
		id = float(user_input)
		#check if number input exists
		if 'name' in data:
			name = data['name']
			output = "The pokemon with id " + user_input + " is " + name
			return render_template('test.html', message=output)
		else:
			return render_template('test.html', message="Number input does not exist")
	except:
		#check if input exists
		if 'id' in data:
			id = data['id']
			output = user_input + " has id " + str(id)
			return render_template('test.html', message=output)
		else:
			return render_template('test.html', message="Input does not exist")

#handles other links that do not follow scheme
@app.errorhandler(404)
def error_404(error):
	return render_template('test.html', message="404 Page Not Found")

if __name__ == '__main__':
    app.run()