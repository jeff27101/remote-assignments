import json
from flask import Flask, request, make_response, render_template, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask.wrappers import Request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data(number=None):
    if request.method == "POST":
        number = request.form["number"]
        if number == '':
            number = "Lack of Parameter"
        elif not number.isdigit():
            number = "Wrong Parameter"
        else:
            result = (int(number)+1)*int(number)//2
            number = str(result)
        return number
    else:
        number = request.args.get('number',number)
        if number == None:
            return "Lack of Parameter"
        elif not number.isdigit():
            return "Wrong Parameter"
        else:
            number = int(number)
            result = (number+1)*number//2
            return str(result)

    
# (Optional) Think about what will happen when N is very large?
# N > 10000000, the result stops at '50000005000000'

@app.route('/myName', methods=['GET', 'POST'])
def myName():
    data = get_saved_data()
    if data == None:
        return render_template('set_user.html')
    elif data == '':
        return render_template('set_user.html')
    else:
        return """
        <!doctype html>
        <html>
        <head><title>Show the User</title></head>
        <body>
        <h1>Hi~ Username Cookie: {}</h1>
        </body>
        </html>
        """.format(data) #.get('name','')
    pass

@app.route('/trackName', methods= ['GET','POST'])
def trackName(name=None):
    if request.method == 'POST':
        name = request.form['username']
        resp = make_response(redirect(url_for('myName')))
        resp.set_cookie('username', name)
    return resp

def get_saved_data():
    try:
        data = request.cookies.get('username')
    except TypeError:
        data = None
    return data

@app.route('/sum.html')
def sum():
    return app.send_static_file('sum.html')


app.run(debug=True,port=3000)