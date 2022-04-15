from unicodedata import name
import pymysql

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def get_users():
    # To connect MySQL database
    conn = pymysql.connect(host='localhost', user='root', password = "", db='books')
        
    cur = conn.cursor()
    cur.execute("select * from booksstore LIMIT 10")
    output = cur.fetchall()

    print(type(output)); #this will print tuple	

    for rec in output:
        print(rec);
        
    # To close the connection
    conn.close()

    return jsonify(output);

@app.route('/', methods=['GET'])
def read():
    # To connect MySQL database
    conn = pymysql.connect(host='localhost', user='root', password = "", db= "books")
    cur = conn.cursor()
    id = int(request.args.get('id'))
    cur.execute(f"select * from booksstore WHERE id = {id}");

    output = cur.fetchall()

    print(type(output)); #this will print tuple

    for rec in output:
        print(rec);

    # To close the connection
    conn.close()

    return jsonify(output);


@app.route('/', methods=['DELETE'])
def deleteRecord():
    conn = pymysql.connect(host='localhost', user='root', password = "", db='books')
    cur = conn.cursor()
    id = int(request.args.get('id'));

    query = f"delete from booksstore where id = {id}";
    #print(query)
    res = cur.execute(query);
    conn.commit();
    print(cur.rowcount, "record(s) deleted")

    return "Record deleted sussesfully"

@app.route('/', methods=['POST'])	
def insertRecord(): 
    conn= pymysql.connect(host='localhost',user='root',password= "",db='books')

    #get raw json values
    raw_json = request.get_json();
   #ss   id = raw_json['id'];
    name = raw_json['name'];
    price = raw_json['price'];
    author = raw_json['author'];
   


    sql=f"INSERT INTO booksstore(id, name, price, author) VALUES (NULL,'{name}', '{price}','{author}')";
    cur= conn.cursor()

    cur.execute(sql);
    conn.commit()
    return "Record inserted Succesfully"

@app.route('/', methods=['PUT'])
def updateRecord():
    conn= pymysql.connect(host='localhost',user='root',password= "",db='books')
    
    raw_json = request.get_json();
    
    #print(type(raw_json));
    
    raw_json = request.get_json();
    id = raw_json['id'];
    name = raw_json['name'];
    price = raw_json['price'];
    author = raw_json['author'];
  

    sql_update_quary=(f"UPDATE books.booksstore SET name = '{name}',price = '{price}' , author = '{author}' WHERE id ='{id}'");
    cur= conn.cursor()
    cur.execute(sql_update_quary);
    conn.commit()
    return "Record Updated Sussecfully"; 
	
	
if __name__ == "__main__":
    app.run(debug=True);
