from flask import Flask, request, render_template
from SqlLIteDB_test import Dbsql

app = Flask(__name__)

import sqlite3


@app.route('/')
def home():
    return render_template('home.html')


@app.post('/register')
def new_user_register():
    from_data = request.form
    table_bd = "user"
    k_r = {'login' : from_data['login'], 'password' : from_data['password'], 'birth_date' : from_data['birth_date'], 'phone' : from_data['phone']}
    with Dbsql('db') as db:
        db.insert_to_db(table_bd, k_r)

    # Dbsql.insert_to_db(a)
    return 'new user register'


@app.get('/register')
def user_register_invitation():
    return render_template("register.html")


@app.post('/login')
def user_login():
    return 'new user is login in'


@app.get('/login')
def user_login_form():
    return f""" <form id="loginForm">
        <label for="login">login:</label>
        <input type="text" id="login" name="login" required>
        <br>
        <label for="password">password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Войти">
    </form>"""


@app.post('/user')
def add_user_info():
    return 'user data were modified'


@app.get('/user')
def user_info():
    table = 'user'
    with Dbsql('db') as db:
        res = db.fetch_oll(table)
    return res


@app.put('/user')
def user_update():
    return 'user info was successfully updated'


@app.post('/funds')
def add_funds():
    return 'user accound was successfully funds'


@app.get('/funds')
def user_deposit_info():
    # a = 'select funds from user where id=1'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'user'
    colons = 'funds'
    condition = None
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    # return res

    return f'user deposit {res}'


@app.post('/reservations')
def add_reservations():
    return ' new reservations was successfully'


@app.get('/reservations')
def user_reservations_list_info():
    # a = 'select service_id from reservation where user_id=1'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'reservation'
    colons = 'service_id'
    condition = {'user_id': 1}

    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    # return res
    return f'user reservations list {res}'


@app.get('/reservations/<reservation_id>')
def user_reservations_info(reservation_id):
    # a = f'select * from reservation where user_id=1'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'reservation'
    colons = None
    condition = {'user_id': 1}
    with Dbsql('db') as db:

        res = db.fetch_oll(table, colons, condition)
    # return res

    return f'user reservations {reservation_id} info {res}'


@app.put('/reservations/<reservation_id>')
def update_reservations(reservation_id):
    return f'reservations {reservation_id} was successfully updated'


@app.delete('/reservations/<reservation_id>')
def delete_reservations(reservation_id):
    return f'user reservations {reservation_id} was successfully deleted'


@app.post('/checkout')
def add_checkout_order_service():
    return 'add checkout order service'


@app.get('/checkout')
def checkout_info():
    # a = f'select name, price from service '
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'service'
    colons = ['name', 'price']
    condition = None
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return f'checkout info oll servises {res}'


@app.put('/checkout')
def update_checkout_order_service():
    return 'checkout order service was successfully updated'


@app.get('/fitness_center')
def get_fitness_center():
    # a = 'select name, address from fitness_center'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'fitness_center'
    colons = ['name', 'address']
    condition = None
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return res


@app.get('/fitness_center/<gym_id>')
def get_fitness_center_info(gym_id):
    # table = 'fitness_center'
    # conditions =
    a = f'select name, address from fitness_center where id={gym_id}'
    table = 'fitness_center'
    colons = ['name', 'address']
    condition = {'id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_one(table, colons, condition)
    return res


@app.get('/fitness_center/<gym_id>/service')
def get_service(gym_id):
    a = f'select name from service where fitness_center_id={gym_id}'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'service'
    colons = ['name']
    condition = {'fitness_center_id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return f'fitness center {gym_id} service list {res}'


@app.get('/fitness_center/<gym_id>/service/<service_id>')
def get_service_info(gym_id, service_id):
    # a = f'select * from service where fitness_center_id={gym_id} AND id={service_id}'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'service'
    colons = None
    condition = {'fitness_center_id': gym_id, 'id': service_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return f'fitness center {gym_id} service {service_id} info {res}'


@app.get('/fitness_center/<gym_id>/trainer')
def get_trainer(gym_id):
    # a = f'select name from trainer where fitness_center_id={gym_id}'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'trainer'
    colons = ['name']
    condition = {'fitness_center_id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return f'fitness center {gym_id} trainer list {res}'


@app.get('/fitness_center/<gym_id>/trainer/<trainer_id>')
def get_coach_info(gym_id, trainer_id):
    # a = f'select * from trainer where fitness_center_id={gym_id} AND id={trainer_id}'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'trainer'
    colons = None
    condition = {'fitness_center_id': gym_id, 'id': trainer_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return f'fitness center {gym_id} trainer {trainer_id} info {res}'


@app.get('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def get_coach_score(gym_id, trainer_id):
    return f"""<form action='/fitness_center/<gym_id>/trainer/<trainer_id>/score' method="POST">
  <label for="number">gym_id:</label><br>
   <textarea id="gym_id" name="gym_id" rows="1" cols="3">{gym_id}</textarea><br>
  <label for="number">trainer_id:</label><br>
     <textarea id="trainer_id" name="trainer_id" rows="1" cols="3">{trainer_id}</textarea><br>
  <label for="text">text:</label><br>
  <input type="text" id="text" name="text"><br>
  <label for="number">point:</label><br>
  <input type="number" id="point" name="point">


  <input type="submit" value="Submit">
</form>"""


@app.post('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def set_coach_score(gym_id, trainer_id):
    from_data = request.form


    table_bd = "review_rating"
    k_r = {'user_id': '1', 'point': from_data['point'], 'text': from_data['text'], 'trainer_id': from_data['trainer_id'], 'gym_id': from_data['gym_id']}
    with Dbsql('db') as db:
        db.insert_to_db(table_bd, k_r)
    return f'fitness center {gym_id} trainer {trainer_id} score was added'


@app.put('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def update_coach_score(gym_id, trainer_id):
    return f'fitness center {gym_id} trainer {trainer_id} score was updated'


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs(gym_id):
    # a = f'select name from fitness_center where id={gym_id}'
    # with Dbsql('db') as db:
    #     res = db.fetch_oll(a)
    table = 'fitness_center'
    colons = ['name']
    condition = {'id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return f'fitness center {res} loyality_programs list'



if __name__ == '__main__':
    app.run()
