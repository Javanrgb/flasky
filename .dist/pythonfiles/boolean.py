"""user = 'User'
logged_in = True

if user == 'Admin' and logged_in:
    print("Admin logged in")
elif user != 'Admin' and not logged_in:
    print("Regular user not logged in")
elif user != 'Admin' and logged_in:
    print("Regular user logged in")
elif user == 'Admin' and not logged_in:
    print('Admin not logged in')
else:
    print("Not a valid selection")
"""
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
