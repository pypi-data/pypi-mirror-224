import sqlite3

conn = sqlite3.connect('data/todo.db')
conn.execute("create table if not exists todo (id INTEGER PRIMARY KEY,task char(255) NOT NULL,status bool NOT NULL)")

conn.execute("insert into todo (task,status) values('加10个小姐姐微信',0)")
conn.execute("insert into todo (task,status) values('赚它1个亿',1)")
conn.execute("insert into todo (task,status) values('大笑10下',1)")
conn.commit()

from bottle import route, run, template, request, error


@route('/todo1')
def todo_list():
    conn = sqlite3.connect("data/todo.db")
    c = conn.cursor()
    c.execute("select id,task,status from todo where status is 1")
    result = c.fetchall()
    c.close()
    return str(result)


@route('/todo')
def todo_list():
    conn = sqlite3.connect("data/todo.db")
    c = conn.cursor()
    c.execute("select id,task,status from todo where status is 1")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@route('/new', method='GET')
def new_task():
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect("data/todo.db")
        c = conn.cursor()

        c.execute("insert into todo (task,status) values(?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>added data successfully,the id is : %s </p>' % new_id
    else:
        return template('new_task.tpl')


@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('data/todo.db')
        c = conn.cursor()
        c.execute('update todo set task = ?,status = ? where id like ?', (edit, status, no))
        conn.commit()

        return '<p>successfully commit the plan ID: %s </p>' % no

    else:

        conn = sqlite3.connect('data/todo.db')
        c = conn.cursor()
        c.execute('select task from todo where id like ?', (str(no)))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)


@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('data/todo.db')
    c = conn.cursor()
    c.execute('select task from todo where id like ?', (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}

@error(404)
def mistake404(err):
    return 'Sorry,the page you want is swollowed by dogs!'

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(reload=True, host='localhost', port=8888)
