from flask import Flask, render_template, request, redirect,session

from flask_app import app
from flask_app.models.users import User

@app.route('/users/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html",users=users)

@app.route('/users/new')
def new():
    return render_template("new.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.guardar(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.borrar(data)
    return redirect('/users')


@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    user = User.obtener_user_by_id(data)
    return render_template('edit.html', user=user)

@app.route('/users/update', methods=['POST'])
def update():
    User.actualizar(request.form)
    return redirect('/users')


@app.route('/users/<int:id>')
def show_one(id):
    data = {
        "id": id
    }
    user = User.obtener_user_by_id(data)
    return render_template('read.html', user=user)

if __name__=="__main__":
    app.run(debug=True)