from xml.dom import minidom
#parse xml file by name
file=minidom.parse("models.xml")

#use getElementsByTagName() to gat a tag
models=file.getElementsByTagName("model")

#one specific item attribute 
print("\nAll attributes: ")
for elem in models:
    print(elem.attributes["name"].value)

#one specfic items data
print("\nmodel #2 data: ")
print(models[1].firstChild.data)
print(models[1].childNodes[0].data)

#all items data
print("\n All model data:")
for elem in models:
    print(elem.firstChild.data)