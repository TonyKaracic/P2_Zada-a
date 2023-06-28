import re

regex = r"^[A][a-zA-Z]*[0-5].*[Razmak][a-zA-Z]*[S]$"
string = "Antonio Karacic"

if re.match(regex, string):
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")