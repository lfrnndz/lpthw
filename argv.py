from sys import argv
scriptname, one = argv

status = input("Did this run? ")
print(f"{status}, great.")
print("This is the first arg:", scriptname)
print("This is the second arg:", one)