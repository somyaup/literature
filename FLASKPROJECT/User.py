#Apis required for users
#- Fetch all users  :    fetchusers
#- Fetch by id      :    fetchid
#- Create user      :    createuser

from flaskext.mysql import MySQL
from flask import jsonify,request,Flask

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'USERBASE'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Fetchusers or fetchid/<id>'

@app.route('/Fetchusers')
def fetchusers():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT details FROM users")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/Fetchid/<id>',methods=['GET'])
def fetchid(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT details FROM users where id_users=%s",id)
        rows = cursor.fetchone()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#request body
#{
#   user_id:1,
#   user_name: DDD,
#   joined:2022-08-02 20:58:28.000000,
#   details:{Adress:ayz,payment:abc,email:a@gmail.com..},
# }
@app.route('/createuser', methods=['POST'])
def createUser():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json['user_id']
        _user_name = _json['user_name']
        _joined=_json['joined']
        _details=_json['details']
        sql = "INSERT INTO users VALUES(%s, %s, %s, %s)"
        data = ( _user_id,_user_name, _joined ,_details)
        print('data=',data)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify(' User successful added !')
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
    app.run(debug=False, host=0.0.0.0)
