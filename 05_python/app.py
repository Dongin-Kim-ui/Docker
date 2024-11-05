import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

# (1) 테스트용 기본 내용
# 외부에서 요청: http://server/
@app.route('/')
def hello_world():
  return 'Hello, Docker!'

# (2) 레코드 가져오기
# 외부에서 요청: http://server/widgets
@app.route('/widgets')
def get_widgets():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="password",
    database="inventory"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.execute("use inventory")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.execute("INSERT INTO widgets (name, description) VALUES ('lee', 'test1')")
  cursor.execute("INSERT INTO widgets (name, description) VALUES ('kim', 'test2')")
  cursor.execute("INSERT INTO widgets (name, description) VALUES ('baik', 'test3')")

  cursor.execute("SELECT * FROM widgets")

  #this will extract row headers
  row_headers=[x[0] for x in cursor.description] 

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

# (3) 레코드 삽입
# 외부에서 요청: http://server/initdb
@app.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="password"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="password",
    database="inventory"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS widgets")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')

  