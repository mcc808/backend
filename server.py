from flask import Flask
import json 
import random
from config import me
from mock_data import catalog 
from flask import Flask, request, abort
from config import db
from bson import ObjectId

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

@app.get("/api/about")
def api_about():
    return json.dumps(me)  



@app.get("/api/catalog")
def get_catalog():
    #read from db
    cursor = db.Products.find({})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)

    return json.dumps(results)


#POST /api/catalog
@app.post("/api/catalog")
def save_product():
    product = request.get_json()

    #validations
    if "title" not in product:
        return abort(400, "Title is required")

    if len(product["title"]) < 4:
        return abort(400, "Title requires at least 5 chars")

    if "category" not in product:
        return abort(400, "Category is required")

    if "price" not in product:
        return abort(400, "Price is required")

    if not isinstance(product["price"], (float, int)):
        return abort(400, "Price must be a valid number") 

    if product["price"] < 0:
        return abort(400, "Price must be greater than 0")


    #save product to db
    db.Products.insert_one(product) #save the object, will assign an _id: ObjectId(12368713287613)
    #fix the _id value
    
    product["_id"] = str(product["_id"])

    return json.dumps(product)




@app.get("/api/test/count")
def nums_catalog():
   return len(catalog)


@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:
            results.append(product)
        
    return json.dumps(results)



@app.get("/api/catalog/search/<text>")
def search_by_text(text):
    text = text.lower()
    results = []

    for product in catalog:
        if text in product["title"].lower() or text in product["category"].lower():
            results.append(product)

    return json.dumps(results)



@app.get("/api/categories")
def find_categories():
    
    allCategories = []
    for product in catalog:
        cats = product["category"]
        if cats not in allCategories:
            allCategories.append(cats)
    
    return json.dumps(allCategories)



@app.get("/api/test/value")
def sum_goods():

    total = 0
    for product in catalog:
        total = total + product["price"]

    return json.dumps(total)



@app.get("/api/product/lowestprice")
def get_lowest_price():
    lowestprice = catalog[0]
    for product in catalog:
        if product["price"] < lowestprice["price"]:
            lowestprice = product
        
        return json.dumps(lowestprice)



@app.get("/api/product/<id>")
def find_product_by_id(id):
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    return "Error: Product was not found"
        




app.run(debug=True)