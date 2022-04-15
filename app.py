from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
# from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'akash'
api = Api(app)


# jwt = JWT(app, authenticate, identity)        # /auth


# First REST Api app:
# class Student(Resource):
#     def get(self, name):
#         return {'student':name}

# api.add_resource(Student, '/student/<string:name>')         #http://127.0.0.1:5000/student/Akash

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)