from flask import Flask
import datetime
import requests
import model

from flask_restful import Resource, Api
from flask import jsonify
import json

app = Flask(__name__)

api = Api(app)

def mainWindow():
    print("--------------------------------------------------------------------------")
    print("/id -> one json element by id")
    print("/del/id -> delete one by id")
    print("/add/id/temperature/weather -> add with new id, temperature and weather")
    print("--------------------------------------------------------------------------")


def deleteId(id):
    res = model.delById(id)
    if not res is None:
        return model.getAll()
    return "not Found"




def add(id,t,w):
    if model.add(id,t,w):
        return "Success! Id:"+str(id)
    return False



    #classes
class GetAll(Resource):
    mainWindow()
    def get(self):
        return jsonify(model.getAll())
class GetById(Resource):
    def get(self,id):
        return model.getById(id)
class Del(Resource):
    def get(self,id):
        return jsonify(deleteId(id))
class Add(Resource):
    def get(self,id,temperature,weather):
        return jsonify(add(id,temperature,weather))

api.add_resource(GetById,'/<int:id>')
api.add_resource(Del,'/del/<int:id>')
api.add_resource(Add,'/add/<int:id>/<int:temperature>/<string:weather>')
api.add_resource(GetAll,'/')



if __name__ == '__main__':

    app.run(debug=True)