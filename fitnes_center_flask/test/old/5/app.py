from flask import Flask, request, render_template
from SqlLIteDB import Dbsql

app = Flask(__name__)



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

    return render_template('register_add.html', login=from_data['login'])


@app.get('/register')
def user_register_invitation():
    return render_template("register.html")


@app.post('/login')
def user_login():
    return 'new user is login in'


@app.get('/login')
def user_login_form():
    return render_template('login.html')


@app.post('/user')
def add_user_info():
    return 'user data were modified'


@app.get('/user')
def user_info():
    table = 'user'
    colons = None
    condition = {'id': 1}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return render_template("user.html", res = res)


@app.put('/user')
def user_update():
    return 'user info was successfully updated'


@app.post('/funds')
def add_funds():
    return 'user accound was successfully funds'


@app.get('/funds')
def user_deposit_info():
    table = 'user'
    colons = 'funds'
    condition = {'id': 1}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return render_template("funds.html", res = res)


@app.post('/reservations')
def add_reservations():
    return ' new reservations was successfully'


@app.get('/reservations')
def user_reservations_list_info():
    table = 'reservation'
    colons = 'service_id'
    condition = {'user_id': 1}

    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return render_template("reservations.html", res = res)


@app.get('/reservations/<reservation_id>')
def user_reservations_info(reservation_id):
    table = 'reservation'
    colons = None
    condition = {'user_id': 1}
    with Dbsql('db') as db:

        res = db.fetch_oll(table, colons, condition)

    return render_template("reservation_id.html", reservation_id=reservation_id, res = res)


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
    table = 'service'
    colons = ['name', 'price']
    condition = None
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return render_template("checkout.html", res=res)


@app.put('/checkout')
def update_checkout_order_service():
    return 'checkout order service was successfully updated'


@app.get('/fitness_center')
def get_fitness_center():

    table = 'fitness_center'
    colons = ['name', 'address']
    condition = None
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return render_template("fitness_center.html", res = res)

@app.get('/fitness_center/<gym_id>')
def get_fitness_center_info(gym_id):

    table = 'fitness_center'
    colons = None
    condition = {'id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_one(table, colons, condition)
    return render_template("gym_id.html", res = res, gym_id=gym_id)


@app.get('/fitness_center/<gym_id>/service')
def get_service(gym_id):
    table = 'service'
    colons = ['name']
    condition = {'fitness_center_id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return render_template("service.html", res = res, gym_id=gym_id)


@app.get('/fitness_center/<gym_id>/service/<service_id>')
def get_service_info(gym_id, service_id):
    table = 'service'
    colons = None
    condition = {'fitness_center_id': gym_id, 'id': service_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return render_template("service_id.html", res = res, service_id=service_id, gym_id=gym_id)


@app.get('/fitness_center/<gym_id>/trainer')
def get_trainer(gym_id):
    table = 'trainer'
    colons = ['name']
    condition = {'fitness_center_id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return render_template("trainer.html", res = res,  gym_id=gym_id)


@app.get('/fitness_center/<gym_id>/trainer/<trainer_id>')
def get_coach_info(gym_id, trainer_id):
    table = 'trainer'
    colons = None
    condition = {'fitness_center_id': gym_id, 'id': trainer_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)

    return render_template("trainer_id.html", res = res, trainer_id=trainer_id, gym_id=gym_id)


@app.get('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def get_coach_score(gym_id, trainer_id):
    print(gym_id, trainer_id)
    return render_template('score.html', gym_id=gym_id, trainer_id=trainer_id)

#


@app.post('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def set_coach_score(gym_id, trainer_id):
    from_data = request.form


    table_bd = "review_rating"
    k_r = {'user_id': '1', 'point': from_data['point'], 'text': from_data['text'], 'trainer_id': from_data['trainer_id'], 'gym_id': from_data['gym_id']}
    with Dbsql('db') as db:
        db.insert_to_db(table_bd, k_r)
    return render_template('score_add.html', gym_id=from_data['gym_id'], trainer_id=from_data['trainer_id'])


@app.put('/fitness_center/<gym_id>/trainer/<trainer_id>/score')
def update_coach_score(gym_id, trainer_id):
    return f'fitness center {gym_id} trainer {trainer_id} score was updated'


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs(gym_id):
    table = 'fitness_center'
    colons = ['name']
    condition = {'id': gym_id}
    with Dbsql('db') as db:
        res = db.fetch_oll(table, colons, condition)
    return render_template('loyality_programs.html', res=res)



if __name__ == '__main__':
    app.run()
