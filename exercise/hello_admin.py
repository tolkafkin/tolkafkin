#Hello Admin
from time import sleep

users = ['user1','user2', 'admin', 'programmer', 'manager', 'user3', 'director']
upper_users = []
lower_users = []
title_users = []
    

new_users = ['programmer', 'director','lola','morgenshtern','san sanich', 'Morgenshter', 'LOLA','Lola','User3','USER2']

if users:
    for user in users:
        upper_users.append(user.upper())
        lower_users.append(user.lower())
        title_users.append(user.title())
        if user != 'admin':
            print(f"Hello {user}, thank you for logging in again")
        else:
            print(f"Hello {user}, would you like  to see a status report?")
            
else:
    print("Sorry, we need to find some users")

for new_user in new_users:
    if new_user in users or new_user.upper() in upper_users or new_user.lower() in lower_users or new_user.title() in title_users:
        print(f"Please, choose different name of {new_user}")
        sleep(2)
    else:
        print(f"Nice to meet you, {new_user}")
        users.append(new_user)
        sleep(2)