print("Welcome to my mini menu!🍔")
print("1) Say Hello")
print("2) Tell me the time (Fake)")
print("3) Exit")

choice = input("Choose 1, 2, or 3:")

if choice == "1":
    name = input("What is your name?")
    print("Hello", name)

elif choice == "2":
    print("The time is: 10:00 (This is just practice 😄)")

elif choice =="3":
    print("Goodye!") 

else:
    print("That is not a valid choice. Try again!")
    