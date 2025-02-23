import json
data={"firstName":"Prashant",
"lastName":"Kumar",
"Address":[
    {
        "street":"ABC",
        "city":"Hydrabad",
        "state":"TL"
    },
    {
        "street":"XYZ",
        "city":"Pune",
        "state":"MH"
    }
]
}
#json.dump() to write data in our json object
with open("data.json","w") as file:
    json.dump(data,file,indent=4)