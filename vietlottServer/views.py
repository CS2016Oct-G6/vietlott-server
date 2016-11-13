import pyrebase
from django.shortcuts import render

config = {
    "apiKey": "AIzaSyDoPhbafClVXk5JOq5oOju3cFXA5F8BAi0",
    "authDomain": "vietlott-29018.firebaseapp.com",
    "databaseURL": "https://vietlott-29018.firebaseio.com",
    "storageBucket": "vietlott-29018.appspot.com"
}

firebase = pyrebase.initialize_app(config)


def history(request):
    db = firebase.database()  
    winningNumbers = db.child("winning").child("history").get().val()
    for number in winningNumbers:
        print(number)
        print(winningNumbers[number])
    template_values = {
      "winningNumbers": winningNumbers
    }

    return render(request, "history.html", template_values)


          