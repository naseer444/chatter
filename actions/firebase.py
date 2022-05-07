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

#locations = db.child("Locations").order_by_child("category").get()

locations = db.child("Locations").order_by_child("category").equal_to("Lake").get();

 
for loc in locations.each():
    print(loc.val()['name'])
    print(loc.val()['Desc'])
    print("\n")
    

# for task in locations.each():
#     if(task.val()['name']=="Lake"):
#         print(task.val())
        
        
        