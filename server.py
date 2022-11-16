from flask import Flask
import json 
from config import me

app = Flask("server")

@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "this is another endpoint"






###########################################################
#########################  CATALOG API ####################
###########################################################

@app.get("/api/version")
def version():
    version = {
        "v": "v1.0.4",
        "name":"zombie rabbit"
    }

    # parse a dict into a json string
    return json.dumps(version)


#get /api/about
#return me as jason

@app.get("/about")
def about():
    return json.dumps(me)  


app.run(debug=True)