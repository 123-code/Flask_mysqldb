from flask import Flask,render_template
from flask_mysqldb import MySQL


app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='sql_123'
app.config['MYSQL_PASSWORD']='JoseNaranj0!'
app.config['MYSQL_DB']='contacts_flask'
my_sql = MySQL(app)
@app.route('/')
def HomePage():
    return "Home Page"
@app.route('/addcontact')
def Add():

  return "Add Contact"
@app.route('/delete')
def delete():
  return "delete"
@app.route('/edit')
def edit():
    return "edit"
if __name__ == '__main__':
    
  app.run(port=3000,debug=True)
