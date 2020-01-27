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
    years_turned_100 = yourage - 100
    date_turned_100 = curr_year - years_turned_100
    print("Congraulations you turned 100 in the year", date_turned_100)
else:
    yearto100 = 100 - yourage
    dateto100 = curr_year + yearto100
    print("You'll turn 100 in the year", dateto100)
