from flask import Flask,render_template
#from flask_pymongo import PyMongo
#from config import MongoDB
import pymongo

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/my"
client = pymongo.MongoClient('mongodb://localhost:27017/')
#mongo = PyMongo(app)

collection = client.my.userinfo

@app.route('/')
def index():
    online_users = collection.find({"online": True})
    return render_template("index.html",
        online_users=online_users)

@app.route('/add/')
def add():
    result = collection.insert({"name":"swper"})
    print(result)
    print(collection.find().count())
    return "用户已经存在！" 

@app.route('/find/')
def find():
    myfind = collection.find()
    for data in myfind:
        print(data)
    print(myfind.count())
    return "ss" 

if __name__ == '__main__':
    app.run(debug = True)
