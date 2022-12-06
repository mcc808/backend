import pymongo
import certifi

con_str = "mongodb+srv://fsdi456:password@cluster0.dpeuykk.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("CoffeeSupply")

me = {
    "first": "Manuel",
    "last": "Castro",
    "age": 31,
    "hobbies": [],
    "address": {
        "street":"Evergreen",
        "number": 742, 
        "city": "Springfield"
    }
}