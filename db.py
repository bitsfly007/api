from pymongo import MongoClient
import traceback
import json
import datetime
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class Mdb:
    def __init__(self):
        # conn_str = "mongodb://%s:%s@%s:%d/%s" \
        #            % (DB_USER, DB_PASS, DB_HOST, DB_PORT, AUTH_DB_NAME)


        conn_str = "mongodb://gaurav:" \
                    "gaurav@ds149124.mlab.com:49124/gaurav"
        client = MongoClient(conn_str)
        self.db = client['gaurav']


#################################################
#                                               #
#                    ADD_TODO                   #
#                                               #
#################################################
    def add_emp(self, name, email, profile, dob, status, contact):
        try:
            ts = datetime.datetime.today().strftime("%a %b %d %X  %Y ")
            rec = {
                'name': name,
                'email': email,
                'profile': profile,
                'dob': dob,
                'status': status,
                'contact': contact,
                'creation_time': ts

            }
            self.db.employee.insert(rec)
        except Exception as exp:
            print "add_emp () :: Got exception: %s", exp
            print(traceback.format_exc())


#################################################
#                                               #
#                get_all_mep                    #
#                                               #
#################################################
    def get_all_emp(self):
        collection = self.db["employee"]
        result = collection.find({})

        ret = []
        for data in result:
            ret.append(data)
        return JSONEncoder().encode({'employee': ret})


#################################################
#                                               #
#                delete_todos                   #
#                                               #
#################################################
    def delete_emp(self, email):
        ret = []
        collection = self.db["employee"]
        collection.remove({"email": email})
        result = collection.find({})
        if not result:
            print "invalid user"
            return "invalid user"

        for data in result:
            print "<<=====got the data====>> :: %s" % data
            ret.append(data)
        return JSONEncoder().encode({'Employee': ret})


#################################################
#                                               #
#               get_all_job                     #
#                                               #
#################################################
    def get_all_job(self):
        ret = []
        collection = self.db["employee"]
        result = collection.find({"status": "job"})
        if not result:
            done = collection.find()
            for data in done:
                ret.append(data)
            return JSONEncoder().encode({'employee': ret})

        for data in result:
            ret.append(data)
        return JSONEncoder().encode({'employee': ret})


#################################################
#                                               #
        #             get_all_tranee                 #
#                                               #
#################################################
    def get_all_tranee(self):
        ret = []
        collection = self.db["employee"]
        result = collection.find({"status": "tranee"})
        if not result:
            not_done = collection.find()
            for data in not_done:
                ret.append(data)
            return JSONEncoder().encode({'employee': ret})

        for data in result:
            ret.append(data)
        return JSONEncoder().encode({'employee': ret})



if __name__ == "__main__":
    mdb = Mdb()
