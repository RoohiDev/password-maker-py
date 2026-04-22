from random import sample
from string import ascii_letters

letters = ascii_letters
symbols = '!"@#$%^&*()_+=<>-?'
numbers = "0123456789"
all = letters + symbols + numbers

print("========= Welcome To Password Maker Program =========\n")
while True:
    choice = input("Select Option: \n\t1)Create Password\n\t2)Exit\nYour Option: ")
    if choice == "1":
        length = int(input("Enter your password lenght: "))
        password = "".join(sample(all, length))
        print("\nYour password:", password)
        print("\n" + "=" * 53 + "\n")


    elif choice == "2":
        print("\nProgram Closed")
        break
    else:
        print("\nInvalid input! Try again")
        print("\n" + "=" * 53 + "\n")
