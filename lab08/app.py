from flask import Flask, render_template, request, flash, redirect, url_for, abort

app = Flask("lab08")
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page2():
    return render_template('page3.html')

@app.route('/page4')
def page5():
    return render_template('page6.html')

@app.route('/go_to_index', methods=['GET', 'POST'])
def redir():
    if request.method == 'GET':
        p = request.args.get('pass')
        if p != '123':
            return abort(403)
    return redirect(url_for('index'))
    
@app.route('/password', methods=['GET', 'POST'])
def password():
    if request.method == 'POST':
        entered_password = request.form.get('pass')
        if entered_password == '123':
            return redirect(url_for('index'))
        else:
            return abort(403)
    return render_template('password.html')  

@app.route('/send_msg', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        m = request.form.get('txt')
        flash(m)
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
	
        

