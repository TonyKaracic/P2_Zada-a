import re

regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
email = input("Unesite e-mail: ")

if re.match(regex, email):
    print("E-mail je valjan.")
else:
    print("E-mail nije valjan.")
    
    

regex2 = r"^[a-zA-Z]+[a-zA-Z]+\d*@sum\.ba$"
edu_id = input("Unesite eduId: ")

if re.match(regex2, edu_id):
    print("eduId je valjan.")
else:
    print("eduId nije valjan.")