from flask import Flask, request
from SqlLIteDB import Dbsql

app = Flask(__name__)

import sqlite3



@app.post('/register')
def new_user_register():
    from_data = request.form
    a = f"INSERT INTO user (login, password, birth_date, phone) VALUES ('{from_data['login']}', '{from_data['password']}', '{from_data['birth_date']}', '{from_data['phone']}')"
    with Dbsql('db') as db:
        db.insert_to_db(a)

    # Dbsql.insert_to_db(a)
    return 'new user register'


@app.get('/register')
def user_register_invitation():
    return f"""<form action='/register' method="POST">
  <label for="login">login:</label><br>
  <input type="text" id="login" name="login"><br>
  <label for="password">password:</label><br>
  <input type="password" id="password" name="password">
  <label for="birth_date">birth_date:</label><br>
  <input type="date" id="birth_date" name="birth_date">
  <label for="phone">phone:</label><br>
  <input type="text" id="phone" name="phone">

  <input type="submit" value="Submit">
</form>"""


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
    a = 'select * from user where id=1'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

    return res


@app.put('/user')
def user_update():
    return 'user info was successfully updated'


@app.post('/funds')
def add_funds():
    return 'user accound was successfully funds'


@app.get('/funds')
def user_deposit_info():
    a = 'select funds from user where id=1'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

    return f'user deposit {res}'


@app.post('/reservations')
def add_reservations():
    return ' new reservations was successfully'


@app.get('/reservations')
def user_reservations_list_info():
    a = 'select service_id from reservation where user_id=1'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)
    return f'user reservations list {res}'


@app.get('/reservations/<reservation_id>')
def user_reservations_info(reservation_id):
    a = f'select * from reservation where user_id=1'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

    return f'user reservations {reservation_id} info {res[int(reservation_id) - 1]}'


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
    a = f'select name, price from service '
    with Dbsql('db') as db:
        res = db.fetch_oll(a)
    return f'checkout info oll servises {res}'


@app.put('/checkout')
def update_checkout_order_service():
    return 'checkout order service was successfully updated'


@app.get('/fitness_center')
def get_fitness_center():
    a = 'select name, address from fitness_center'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)
    return res


@app.get('/fitness_center/<gym_id>')
def get_fitness_center_info(gym_id):
    a = f'select name, address from fitness_center where id={gym_id}'
    with Dbsql('db') as db:
        res = db.fetch_one(a)
    return res


@app.get('/fitness_center/<gym_id>/service')
def get_service(gym_id):
    a = f'select name from service where fitness_center_id={gym_id}'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

    return f'fitness center {gym_id} service list {res}'


@app.get('/fitness_center/<gym_id>/service/<service_id>')
def get_service_info(gym_id, service_id):
    a = f'select * from service where fitness_center_id={gym_id} AND id={service_id}'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

    return f'fitness center {gym_id} service {service_id} info {res}'


@app.get('/fitness_center/<gym_id>/trainer')
def get_trainer(gym_id):
    a = f'select name from trainer where fitness_center_id={gym_id}'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

    return f'fitness center {gym_id} trainer list {res}'


@app.get('/fitness_center/<gym_id>/trainer/<trainer_id>')
def get_coach_info(gym_id, trainer_id):
    a = f'select * from trainer where fitness_center_id={gym_id} AND id={trainer_id}'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)

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

    a = f"INSERT INTO review_rating (user_id, point, text, trainer_id, gym_id) VALUES ('1', '{from_data['point']}', '{from_data['text']}', '{from_data['trainer_id']}', '{from_data['gym_id']}')"

    with Dbsql('db') as db:
        db.insert_to_db(a)
    return f'fitness center {gym_id} trainer {trainer_id} score was added'


@app.put('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def update_coach_score(gym_id, trainer_id):
    return f'fitness center {gym_id} trainer {trainer_id} score was updated'


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs(gym_id):
    a = f'select name from fitness_center where id={gym_id}'
    with Dbsql('db') as db:
        res = db.fetch_oll(a)
    return f'fitness center {res} loyality_programs list'



if __name__ == '__main__':
    app.run()
