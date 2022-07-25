import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request,Flask
# from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/fetchall')
def fetchall():
    print ('start')
    app.config['MYSQL_DATABASE_DB'] = 'Content'
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT meta FROM episodes")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/fetch_one/<int:id>')
def fetch_one(id):
    app.config['MYSQL_DATABASE_DB'] = 'Content'
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Series_idSeries from series_has_users where users_id_users=%s",id)
        IDSER = cursor.fetchall()
        row1=[]
        for idser in IDSER:
            cursor.execute(
                "select unlocked from series_has_users where users_id_users= % s and Series_idSeries= % s",(id,idser));
            unl= cursor.fetchone()
            cursor.execute(
                "SELECT * FROM episodes WHERE  Series_idSeries =%s and ep_no<=%s ", (idser,unl))
            row1.append(cursor.fetchall())
        cursor.execute(
            "SELECT sum(unlocked) FROM series_has_users WHERE users_id_users=%s ", id)
        row2 = cursor.fetchone()
        cursor.execute(
            "SELECT sum(episodes) FROM series")
        row3 = cursor.fetchone()
        row={"meta":row1,"unlocked":row2,"total":row3}
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        return(e)
    finally:
        cursor.close()
        conn.close()

# request body:
# {
#   {series1
#       Series: book1 , time:2021-08-02 20:58:28.000000
#       Series_id: 1 , episodes:2, new :no
#       meta:{episodes1{name:a,id:1,meta:}},{episode2},..}
#   }
#   {series2
#       Series: book6, time:2021-08-02 20:58:28.000000
#       Series_id: 6 , episodes:4, new :yes
#       meta:{episodes1},{episode2},..}
#   }
#   {series3
#       Series: book7, time:2021-08-02 20:58:28.000000
#       Series_id:  7, episodes:3, new:yes
#       meta:{episodes1},{episode2},..}
#   }
#}
@app.route('/upload', methods=['POST'])
def upload():
    app.config['MYSQL_DATABASE_DB'] = 'Content'
    conn = None
    cursor = None
    try:
        _Json = request.json
        count=0
        for _json in _Json:
            _series_id = _json['Series_id']
            _series_name=_json['Series']
            _episodes = _json['episodes']
            _meta = _json['meta']
            _upload_time=_json['time']
            index = 1
            if _json['new']=='yes':
                Sql = "INSERT INTO  Series VALUES(%s, %s, %s, %s)"
                Data=(_series_id,_series_name,_episodes ,_upload_time)
                print(Data)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(Sql, Data)
                conn.commit()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()
                Data = (_series_id, _series_name, _episodes, _upload_time)
                print(Data)
                cursor.execute(
                    "SELECT episodes FROM series WHERE idSeries=%s ", _series_id)
                index= cursor.fetchone()[0]
                print(index)
                add = index + _episodes
                cursor.execute(
                    "update series set episodes=%s where idSeries=%s",(add,_series_id))
                conn.commit()
            for ep in _meta:
                _name=ep['name']
                _epid=ep['id']
                _Ep_meta=ep['meta']
                sql = "INSERT INTO episodes VALUES(%s, %s, %s, %s,%s,%s)"
                data = (_epid,_name,_Ep_meta,_upload_time,_series_id,index)
                cursor.execute(sql, data)
                conn.commit()
                print(data)
                index=index+1
            count=count+1
        resp = jsonify(count,' successful Updates!')
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
