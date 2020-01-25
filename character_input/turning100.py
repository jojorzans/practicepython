import datetime;

today = str(datetime.date.today());
curr_year = int(today[:4]);


yourage = input("How old are you?")
yourage = int(yourage)

if yourage >= 100:
    print("Congraulations you've already made it to 100!")
else:
    yearto100 = 100 - yourage
    dateto100 = curr_year + yearto100
    print("You'll turn 100 in the year", dateto100)
