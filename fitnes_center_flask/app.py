
from flask import Flask

app = Flask(__name__)


@app.post('/register')
def new_user_register():
    return 'new user register'

@app.get('/register')
def user_register_invitation():
    return 'please sing in to register'


@app.post('/login')
def user_login():
    return 'new user is login in'

@app.get('/login')
def user_login_form():
    return 'please enter credentials'


@app.post('/user')
def add_user_info():
    return 'user data were modified'

@app.get('/user')
def user_info():
    return 'user information'

@app.put('/user')
def user_update():
    return 'user info was successfully updated'


@app.post('/funds')
def add_funds():
    return 'user accound was successfully funds'

@app.get('/funds')
def user_deposit_info():
    return 'user deposit value'


@app.post('/reservations')
def add_reservations():
    return ' new reservations was successfully'

@app.get('/reservations')
def user_reservations_list_info():
    return 'user reservations list'


@app.get('/reservations/<reservation_id>')
def user_reservations_info(reservation_id):
    return f'user reservations {reservation_id} info'

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
    return 'checkout info'

@app.put('/checkout')
def update_checkout_order_service():
    return 'checkout order service was successfully updated'


@app.get('/fitness_center')
def get_fitness_center():
    return 'fitness center list'


@app.get('/fitness_center/<gym_id>')
def get_fitness_center_info(gym_id):
    return f'fitness center {gym_id} info'


@app.get('/fitness_center/<gym_id>/services')
def get_service(gym_id):
    return f'fitness center {gym_id} services list'


@app.get('/fitness_center/<gym_id>/services/<service_id>')
def get_service_info(gym_id, service_id):
    return f'fitness center {gym_id} service {service_id} info'


@app.get('/fitness_center/<gym_id>/trainer')
def get_trainer(gym_id):
    return f'fitness center {gym_id} trainer list'


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>')
def get_coach_info(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} info'


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def get_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score'

@app.post('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def set_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score was added'

@app.put('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def update_coach_score(gym_id, coach_id):
    return f'fitness center {gym_id} trainer {coach_id} score was updated'


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs(gym_id):
    return f'fitness center {gym_id} loyality_programs list'


if __name__ == '__main__':
    app.run()
