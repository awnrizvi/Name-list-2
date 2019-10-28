names = []

for x in range (0,10) :
    nl = input("enter name: ")
    names.append(nl)

keepsearching = True
while keepsearching:
    search = input('search for name or type "End" to stop: ')
    if search in names:
        print("name found")
    elif search == "End":
        keepsearching = False
    else:
        print("name not found")
