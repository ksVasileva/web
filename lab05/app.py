from flask import Flask, request, render_template
from datetime import datetime



app = Flask("lab03")
arr = []

@app.route('/')
def my_time():
	n = request.args.get('param')
	t = datetime.now()
	s = t.strftime('%H:%M:%S')
	return render_template('time.html', name=str(n), times=s)
	
	

@app.route('/list', methods=['GET', 'POST'])
def my_form(id = 0):
    if request.method == "POST":
        text = request.form.get('txt')
        if text != None and str(text) != "":
            arr.append(text)
        return render_template('list.html', items = arr, ID = id)
    if request.method == "GET":
        if len(arr) != 0:
            i = request.args.get("Id")
            arr.remove(str(i))
            return render_template('list.html', items = arr)
    return render_template('list.html', items = arr)

        

