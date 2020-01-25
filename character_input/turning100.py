import datetime;

##This will grab the current date so that this code will work as the date chnages
today = str(datetime.date.today());
curr_year = int(today[:4]);

##Let's ask the user for their current age
yourage = input("How old are you?")
yourage = int(yourage)

##if the user is already 100 plus then we'll congradulate them, otherwise we'll
##caclucate and print the age they'll turn 100 
if yourage >= 100:
    print("Congraulations you've already made it to 100!")
else:
    yearto100 = 100 - yourage
    dateto100 = curr_year + yearto100
    print("You'll turn 100 in the year", dateto100)
