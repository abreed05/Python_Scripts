import pymongo
import os
import hvac
import urllib.parse

def hcv_connect():

    return hvac.Client(url=os.environ['VAULT_ADDR'])


def mongo_connect():
    try:
        # Mongodb atlas settings
        hcv_client = hcv_connect()
        secret_version_response = hcv_client.secrets.kv.v2.read_secret_version(path='MongoAtlas', )
        mongo_pass = '{data}'.format(data=secret_version_response['data']['data']['password'], )
        conn_str = "mongodb+srv://abreeden:" + urllib.parse.quote(mongo_pass) + "@cluster0.bfnnv.mongodb.net/hcv?retryWrites=true&w=majority"
        return pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)



    except Exception:
        print("Unable to connect to Mongo")


