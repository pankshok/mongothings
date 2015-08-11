#! /usr/bin/env python3

import bottle
import pymongo

from bottle import Bottle, template
from pymongo import MongoClient


app = Bottle()

def collection(name):
    return MongoClient("mongodb://localhost:27017/").test_db[name]

@app.route("/")
@app.route("/index")
def index():
    return template("hello_world", things=list(collection("test_collection").find()), username="stranger")

@app.route("/hello/<name>")
def hello(name):
    collection("test_collection").insert_one({"name" : name, "posts" : 0})
    return template("<b>Hello, {{name}}</b>!", name=name)

@app.route("/posts/<name>")
def posts(name):
    return template("hello_world", things=list(collection("test_collection").find({"name" : name})), username=name)

@app.post("/favourite_fruit", ["GET", "POST"])
def favourite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if not fruit:
        fruit = "No fruit selected!"
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")

@app.route("/redirect_fruit")
    fruit = bottle.request.get("fruit")
    return template("fruit_selection", fruit=fruit)

if __name__ == "__main__":
    bottle.debug(True)
    app.run(host="localhost", port=8080)
