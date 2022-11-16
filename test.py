from config import me

print(me)

#read
print(me["first"])
print(me["first"] + " " + me["last"])


#modify values 
me["first"]= "Manuel C."
print(me["first"])

#add new 
me["preferred_color"] = "Blue"
print(me)


#print the full address
#format: num street, city 
address = me["address"]
print(str(address["number"]) + " " + address["street"] + " " + address["city"])

