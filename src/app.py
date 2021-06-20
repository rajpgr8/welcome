# app.py
import os
from flask import Flask           # import flask

app = Flask(__name__)             

@app.route("/")                   
@app.route('/hindi')
def Welcome():                      # call method hello
    return "Aapka Swagat Hai"    

@app.route('/english')
def Welcome2():                      # call method Welcome2
    return "Welcome"   

@app.route('/german')
def Welcome3():                      # call method Welcome3
    return " herzlich willkommen" 
   
if __name__ == "__main__":        # on running python app.py
    port = int(os.environ.get("PORT", 9091))
    app.run(debug=True, host='0.0.0.0', port=port)
