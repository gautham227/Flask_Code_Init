import os
import sys
import json
from flask import request, redirect, render_template, url_for, flash, session
from flask import current_app as app
from similarsearch import search
from application.utils import get_lost, get_found

@app.route("/mllost", methods=["GET"])
def mllost():
    query=request.json
    dataset=get_found()
    data=search(query, dataset)
    # data={'match': 'test', 'score': 0.9}
    #convert dictionary data returned from search function to json
    jsondata=json.dumps(data)
    print(jsondata)
    return jsondata

@app.route("/mlfound", methods=["GET"])
def mlfound():
    query=request.json
    dataset=get_lost()
    data=search(query, dataset)
    #convert dictionary data returned from search function to json
    jsondata=json.dumps(data)
    print(jsondata)
    return jsondata


# mllost(1, 2)