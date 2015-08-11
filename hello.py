#! /usr/bin/env python3

import pymongo

from bottle import run, route, template, debug
from pymongo import MongoClient

def connection():
    return MongoClient("mongodb://localhost:27017/")

@route("/hello/<name>")
def index(name):
    conn = connection()
    db = conn.test_db
    coll = db.test_collection
    coll.insert_one({"name" : name, "posts" : 0})
    return template("<b>Hello, {{name}}</b>!", name=name)

@route("/posts/<name>")
def posts(name):
    conn = connection()
    db = conn.test_db
    return template("{{post}}", post=db["test_collection"].find_one({"name" : name}))

if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8080)
