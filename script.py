import requests as rq
import json as js
import random as rand

zaehl = 1000
for i in range (0, 10000):
    f = open("skytickets.txt", "a")
    r = rq.post("https://sky.milka.de/Service/Participate", data = {
        #"Code1": "OOV028" + str(zaehl) + "",
    #"Code2": "OOV028" + str(zaehl + 1) + "",
    #makes use of milka not blocking codes
    "Code1": "OOV0281034",
    "Code2": "OOV0281033",
    "FirstName": "asdas",
    "LastName": "asdasd",
    "Birthday": "04.04.1957",
    "Country":"" ,
    #random email
    "Email": str(zaehl) + "@" + str(zaehl * rand.random()) + ".de",
    "TermsOfUse": "true",
    })
    #zaehl += 2
    data = js.loads(r.text)
    d = data["metadata"]
    #write ticket to txt
    try:
        print (data)
        f.write(d["ticket"] + "\n")
    except:
        f.write(data["result"] + "\n")
    print("run" + str(i))
