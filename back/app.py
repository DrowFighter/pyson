from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import json
import myparser
import message_handler   


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/myparser')
def index():
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    return render_template("diamonds.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

# function which connects the SQL controler with the flask messageHandler
def messageCallback(action, data):
    result = None
    if action == 'create' : 
        result = fileParser.create(data)
    elif action == 'getAll' : 
        result = fileParser.getAll(data)
    elif action == 'update' : 
        result = fileParser.update(data)
    elif action == 'delete' : 
        result = fileParser.delete(data)
    print ('result', result)
    return result 



# init of the handler classes
fileParser = myparser.MyParser()
messageHandler = message_handler.MessageHandler(messageCallback,app,cross_origin)