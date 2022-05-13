import pyrebase


firebaseConfig = {"apiKey": "AIzaSyAeQtvt8zN0yLikTwVcxUhO5rx2wvduOGY",
                        "authDomain": "planitpk-cf006-restore.firebaseapp.com",
                        "databaseURL": "https://planitpk-cf006-restore-default-rtdb.firebaseio.com",
                        "projectId": "planitpk-cf006-restore",
                        "storageBucket": "planitpk-cf006-restore.appspot.com",
                        "messagingSenderId": "999842759391",
                        "appId": "1:999842759391:web:1df0a55e04e431db425f6a",
                        "measurementId": "${config.measurementId}"

                        }

firebase=pyrebase.initialize_app(firebaseConfig)

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote


db=firebase.database()



def funcLake():

    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("Lake").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values



def funcValley():
    
    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("Valley").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values
        


def funcNationalParks():
    
    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("National Park").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values


def funcMosques():
    
    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("Mosque").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values

def funcHill():
    
    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("Hill Station").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values


def funcWaterfall():
    
    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("Waterfall").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values



def funcMountain():
    
    

    #locations = db.child("Locations").order_by_child("category").get()
    
    
    locations = db.child("Locations").order_by_child("category").equal_to("Mountainous").get();

    tempArr=[]
    for loc in locations.each():
        tempArr.append(loc.val()['name'])
        tempArr.append("Rating:")
        tempArr.append(loc.val()['rating'])
        tempArr.append(loc.val()['Desc'])
       
       
    values = '\n'.join([str(i) for i in tempArr])
    
    return values



