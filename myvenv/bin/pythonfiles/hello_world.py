my_message = """
Bobby's cartoon 
was a great cartoon in the 1990's
I loved it

"""

print(my_message[6:].upper())
print(my_message.count('o'))
new_message = my_message.replace("Bobby's", "Tommy's")
print(new_message)
name = "James Scoffield"
message = "Hello"

greeting = f'{message.upper()},{name} Welcome!'
print(greeting)
print(dir(name))
