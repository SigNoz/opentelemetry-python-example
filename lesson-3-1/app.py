import os
from random import randrange

import requests
from bson import ObjectId  # For ObjectId to work
from flask import redirect  # For flask implementation
from flask import Flask, render_template, request, url_for
from pymongo import MongoClient

app = Flask(__name__, template_folder='../templates', static_folder='../static')
title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

mongo_host = os.getenv("MONGO_HOST", "127.0.0.1")
mongo_port = os.getenv("MONGO_PORT", "27017")

client = MongoClient("mongodb://" + mongo_host + ":" + mongo_port)
db = client.mymongodb  # Select the database
todos_coll = db.todo  # Select the collection name


def redirect_url():
    return request.args.get("next") or request.referrer or url_for("index")


@app.route("/list")
def lists():
    todos = todos_coll.find()
    if randrange(10) % 2:
        response = requests.get(
            "https://run.mocky.io/v3/b851a5c6-ab54-495a-be04-69834ae0d2a7"
        )
        response.close()
    else:
        response = requests.get(
            "https://run.mocky.io/v3/1cb67153-a6ac-4aae-aca6-273ed68b5d9e"
        )
        response.close()

    return (
        render_template("index.html", todos=todos, t=title, h=heading),
        500,
    )


@app.route("/")
@app.route("/uncompleted")
def tasks():
    # Display the Uncompleted Tasks
    todos = todos_coll.find({"done": "no"})
    return render_template("index.html", todos=todos, t=title, h=heading)


@app.route("/completed")
def completed():
    # Display the Completed Tasks
    todos = todos_coll.find({"done": "yes"})
    return render_template("index.html", todos=todos, t=title, h=heading)


@app.route("/done")
def done():
    # Done-or-not ICON
    id = request.values.get("_id")
    task = todos_coll.find({"_id": ObjectId(id)})
    if task[0]["done"] == "yes":
        todos_coll.update_one({"_id": ObjectId(id)}, {"$set": {"done": "no"}})
    else:
        todos_coll.update_one({"_id": ObjectId(id)}, {"$set": {"done": "yes"}})
    redir = redirect_url()

    return redirect(redir)


@app.route("/action", methods=["POST"])
def action():
    # Adding a Task
    name = request.values.get("name")
    desc = request.values.get("desc")
    date = request.values.get("date")
    pr = request.values.get("pr")
    todos_coll.insert_one(
        {"name": name, "desc": desc, "date": date, "pr": pr, "done": "no"}
    )
    return redirect("/")


@app.route("/remove")
def remove():
    # Deleting a Task with various references
    key = request.values.get("_id")
    todos_coll.delete_one({"_id": ObjectId(key)})
    return redirect("/")


@app.route("/update")
def update():
    id = request.values.get("_id")
    task = todos_coll.find({"_id": ObjectId(id)})
    return render_template("update.html", tasks=task, h=heading, t=title)


@app.route("/action3", methods=["POST"])
def action3():
    # Updating a Task with various references
    name = request.values.get("name")
    desc = request.values.get("desc")
    date = request.values.get("date")
    pr = request.values.get("pr")
    id = request.values.get("_id")
    todos_coll.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": name, "desc": desc, "date": date, "pr": pr}},
    )
    return redirect("/")


@app.route("/search", methods=["GET"])
def search():
    # Searching a Task with various references

    key = request.values.get("key")
    refer = request.values.get("refer")
    if key == "_id":
        todos_l = todos_coll.find({refer: ObjectId(key)})
    else:
        todos_l = todos_coll.find({refer: key})
    return render_template("searchlist.html", todos=todos_l, t=title, h=heading)


@app.route("/generate-error", methods=["GET"])
def generate_error():
    if randrange(10) % 2:
        response = requests.get(
            "https://rufn.fmoceky.io/v3/b851a5c6-ab54-495a-be04-69834ae0d2a7"
        )
        response.close()
    elif randrange(10) % 2:
        not_a_defined_function()
    elif randrange(10) % 2:
        raise Exception("This is a test exception")
    else:
        div_by_zero = 1 / 0


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False, use_reloader=False)
