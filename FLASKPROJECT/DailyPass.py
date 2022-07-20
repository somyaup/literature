# Apis required for DailyPass
# - Api to unlock one chapters for the given user and series: unock
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request, Flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Dailypass!'

# request body
# {
#   user_id:1
#   Series_id: 3
#   Series: NAme
# }
@app.route('/unlock', methods=['POST'])
def unlock():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json['user_id']
        _Series_id = _json['Series_id']
        _Series_name=_json['Series']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT episodes FROM Series where idSeries=%s", _Series_id)
        max_ep = cursor.fetchone()[0]
        print (max_ep)
        cursor.execute("SELECT unlocked FROM series_has_users where series_idSeries=%s and users_id_users=%s",( _user_id, _Series_id))
        unlocked = cursor.fetchone()[0]
        print(unlocked)
        if unlocked==None:
            unlocked=min(4,max_ep)
            sql = "Insert into series_has_users values (%s,%s,%s,%s) "
            data = (_Series_id,_user_id,unlocked,_Series_name)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify(' unlock successful !')
            resp.status_code = 200
        if unlocked<max_ep:
            unlocked=unlocked+1
            sql = "update Series_has_users set unlocked=%s where series_idSeries=%s and users_id_users=%s "
            data = (unlocked, _user_id, _Series_id)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify(' unlock successful !')
            resp.status_code = 200
        else:
            resp = jsonify(' no more episodes to unlock!')
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()

