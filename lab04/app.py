from flask import Flask, request

app = Flask("lab04")


@app.route('/checkboxes', methods=['GET', 'POST'])
def checkboxes():
    if request.method == 'GET':
        opt1 = request.args.get('opt1')
        opt2 = request.args.get('opt2')
        if opt1 is None and opt2 is None:
            return 'Опции не выбраны'
        elif opt1 is None:
            return 'Опция 1 не выбрана'
        elif opt2 is None:
            return 'Опция 2 не выбрана'
        return 'Обе опции выбраны'
    if request.method == 'POST':
        opt1 = request.form.get('opt1')
        opt2 = request.form.get('opt2')
        if 'opt1' not in request.form and 'opt2' not in request.form:
            return 'Опции не выбраны'
        elif 'opt1' not in request.form :
            return 'Опция 1 не выбрана'
        elif 'opt2' not in request.form:
            return 'Опция 2 не выбрана'
        return 'Обе опции выбраны'
    
@app.route('/radiobuttons', methods=['GET', 'POST'])
def radiobuttons():
    if request.method == 'GET':
        grp1 = request.args.get('grp1')
        grp2 = request.args.get('grp2')
        grp3 = request.args.get('grp3')

        if grp3 == 'red':
            return '<font color="red"> Опция ' + grp3 + ' выбрана в группе 3</font>'
        if grp3 == 'green':
            return '<font color="green"> Опция ' + grp3 + ' выбрана в группе 3</font>'
        if grp3 == 'blue':
            return '<font color="blue"> Опция ' + grp3 + ' выбрана в группе 3</font>'
        if 'grp1' not in request.args:
            return 'В первой группе ничего не выбрано'
        if 'grp2' not in request.args:
            return 'Во второй группе ничего не выбрано'
        
        else:
            if grp1 == 'one' and grp2 == 'one1':
                return 'В группе 1 и группе 2 выбран 1 пункт'
            if grp1 == 'two' and grp2 == 'one1':
                return 'В группе 1 выбран 2 пункт, в группе 2 выбран 1 пункт'
            if grp1 == 'one' and grp2 == 'two1':
                return 'В группе 1 выбран 1 пункт, в группе 2 вбран 2 пункт'
            if grp1 == 'two' and grp2 == 'two1':
                return 'В группе 1 и группе 2 выбран 2 пункт'
        return 0
    if request.method == 'POST':
        grp1 = request.form.get('grp1')
        grp2 = request.form.get('grp2')
        grp3 = request.form.get('grp3')

        if grp3 == 'red':
            return '<font color="red"> Опция ' + grp3 + ' выбрана в группе 3</font>'
        if grp3 == 'green':
            return '<font color="green"> Опция ' + grp3 + ' выбрана в группе 3</font>'
        if grp3 == 'blue':
            return '<font color="blue"> Опция ' + grp3 + ' выбрана в группе 3</font>'
        if 'grp1' not in request.args:
            return 'В первой группе ничего не выбрано'
        if 'grp2' not in request.args:
            return 'Во второй группе ничего не выбрано'
        
        else:
            if grp1 == 'one' and grp2 == 'one1':
                return 'В группе 1 и группе 2 выбран 1 пункт'
            if grp1 == 'two' and grp2 == 'one1':
                return 'В группе 1 выбран 2 пункт, в группе 2 выбран 1 пункт'
            if grp1 == 'one' and grp2 == 'two1':
                return 'В группе 1 выбран 1 пункт, в группе 2 вбран 2 пункт'
            if grp1 == 'two' and grp2 == 'two1':
                return 'В группе 1 и группе 2 выбран 2 пункт'
        return 0

@app.route('/lists1', methods=['GET', 'POST'])
def lists1():
    if request.method == 'GET':
        list1 = request.args.get('list1')
        return 'Вы выбрали ' + list1 + ' элемент'
    if request.method == 'POST':
        list1 = request.form.get('list1')
        return 'Вы выбрали ' + list1 + ' элемент'
    
@app.route('/lists2', methods=['GET', 'POST'])
def lists2():
    if request.method == 'GET':
        list2 = request.args.get('list2')
        return 'Вы выбрали ' + list2 + ' элемент'
    if request.method == 'POST':
       list2 = request.form.get('list2')
       return 'Вы выбрали ' + list2 + ' элемент'
    
@app.route('/lists3', methods=['GET', 'POST']) 
def lists3():
    if request.method == 'GET':
        list3 = request.args.get('list3')
        return '<font color="' + list3 + '"> Вы выбрали ' + list3 + ' цвет</font>' 
    if request.method == 'POST':
        list3 = request.form.get('list3')
        return '<font color="' + list3 + '"> Вы выбрали ' + list3 + ' цвет</font>'
        
