import datetime

from SqlLIteDB import Dbsql


def clac_slots(user_id, trainer_id, service_id):

    with Dbsql('test/old/09,08/db') as db:

        table = 'reservation'
        colons = None
        condition = {'trainer_id': trainer_id, 'date' : '31.05.2024'}
        join_condition = {'service.id': 'reservation.service_id'}
        booket_time = db.fetch_oll(table, colons, condition, join_table='service', join_condition=join_condition)

        table = 'trainer_schedule'
        colons = None
        condition = {'trainer_id': trainer_id, 'date' : '31.05.2024'}
        trainer_schedule = db.fetch_one(table, colons, condition)

        table = 'trainer_service'
        colons = None
        condition = {'trainer_id': trainer_id, 'service_id': service_id}
        trainer_capacity = db.fetch_one(table, colons, condition)

        start_dt = datetime.datetime.strptime(trainer_schedule["date"] + ' ' + trainer_schedule["start_time"], '%d.%m.%Y %H:%M')
        end_dt = datetime.datetime.strptime(trainer_schedule["date"] + ' ' + trainer_schedule["end_time"], '%d.%m.%Y %H:%M')
        cur_dt = start_dt
        trainer_schedul = {}

        while cur_dt < end_dt:
            trainer_schedul[cur_dt] = trainer_capacity['max_attendees']
            cur_dt = cur_dt + datetime.timedelta(minutes=15)

        for one_booking in booket_time:
            booking_date = one_booking['date']
            booking_time = one_booking['time']
            booking_duration = one_booking['duration']
            one_booking_start = datetime.datetime.strptime(booking_date + " " + booking_time,  '%d.%m.%Y %H:%M')
            booking_end = one_booking_start + datetime.timedelta(minutes=booking_duration)
            cur_dt = one_booking_start
            while cur_dt < booking_end:
                trainer_schedul[cur_dt] -= 1
                cur_dt += datetime.timedelta(minutes=15)




    print(trainer_schedule)
    print(booket_time)
    print(trainer_schedul)
clac_slots(1,1,2)
