#Hello Admin
users = ['user1','user2', 'admin', 'programmer', 'manager', 'user3', 'director']
for user in users:
    if user != 'admin':
        print(f"Hello {user}, thank you for logging in again")
    else:
        print(f"Hello {user}, would you like  to see a status report?")