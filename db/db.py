import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    'auto-bot-2559f-firebase-adminsdk-emjq1-43937ff21c.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://auto-bot-2559f-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# add data to firebase
userRef = db.reference('Users/')
userRef.set({
    '1': {
        'name': {
            'firstName': 'Pranjal',
            'lastName': 'Agarwal',
        },
        'phone': '8791224496',
    },
    '2': {
        'name': {
            'firstName': 'Prajesh',
            'lastName': 'Singh',
        },
        'phone': '6393318060',
    },
})

driverRef = db.reference('Drivers/')
driverRef.set({
    '1': {
        'name': 'Agarwal',
        'phone': '8791224496',
        'vehicleNumber': 'DL 1C 1234',
    },
    '2': {
        'name': 'Singh',
        'phone': '6393318060',
        'vehicleNumber': 'DL 1C 1235',
    },
})

# update data to firebase
toRef = userRef.child('2').child('name')
toRef.update({
    'lastName': 'Pratap Singh',
})

# delete data from firebase
# toRef = userRef.child('2')
# toRef.delete()

# read data from firebase
fromRef = userRef.child('1')
fromData = fromRef.get()
print(fromData)