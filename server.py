from flask import Flask, render_template, request
import traceback
from db import Mdb
import json


app = Flask(__name__)
mdb = Mdb()


@app.route("/")
def index():
    template_data = {'title': 'home page'}
    # return render_template('index.html', **template_data)
    return 'Welcome to APIs'


#################################################
#                                               #
#                    ADD_EMP                    #
#                                               #
#################################################
@app.route("/add_emp", methods=['POST'])
def add_emp():
    try:
        ret = {"error": 0}
        name = request.form['name']
        email = request.form['email']
        profile = request.form['profile']
        dob = request.form['dob']
        status = request.form['status']
        contact = request.form['contact']
        mdb.add_emp(name, email, profile, dob, status, contact)
        ret["msg"] = "employee added sucessfully"
    except Exception as exp:
        print "emp_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return json.dumps(ret)


#################################################
#                                               #
#               get_all_todos                   #
#                                               #
#################################################
@app.route("/get_all_emp", methods=['GET'])
def get_all_emp():
    return mdb.get_all_emp()


#################################################
#                                               #
#                delete_todos                   #
#                                               #
#################################################
@app.route("/delete_emp", methods=['POST'])
def delete_emp():
    try:
        email = request.form['email']
        mdb.delete_emp(email)
    except Exception as exp:
        print "delete_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "%s" % mdb.delete_employee(email)


#################################################
#                                               #
#            get_all_pending_todo               #
#                                               #
#################################################
@app.route("/get_all_job", methods=['GET'])
def get_all_job():
    try:
        mdb.get_all_job()
    except Exception as exp:
        print "get_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "%s" % mdb.get_all_job()


#################################################
#                                               #
#             get_all_done_todo                 #
#                                               #
#################################################
@app.route("/get_all_tranee", methods=['GET'])
def get_all_tranee():
    try:
        mdb.get_all_tranee()
    except Exception as exp:
        print "get_done() :: Got exception: %s" % exp
        print(traceback.format_exc())
    return "%s" % mdb.get_all_tranee()


#################################################
#                                               #
#             Main Server                       #
#                                               #
#################################################
if __name__ == '__main__':
    app.run(debug=True)
