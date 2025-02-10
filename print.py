import json

PATH = "DATA/guestlist.json"

with open(PATH, 'r') as file:
    guestlist = json.load(file)

print("")
print(f"Lanza Family Baby Shower {guestlist[0]["date"]}")
print(f"==========================================")
print("")
print("Full Guestlist:")
print(f"------------------------------------------")
print("")
print("")

for guest in guestlist:
    print(f"Name:  {guest["name"]}")
    print(f"Email: {guest["email"]}")
    print("")

print("")
print(f"------------------------------------------")
print(f"             ~ End of List ~")
print("")