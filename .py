import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")),5

    phone_book = []

    print(phone_book)
    for i in range(rows):
      print("\n Enter contacts %d details in the following order (ONLY):"% (i+1))
      print("NOTE: * indicate mandotary field")
      temp = []
      for j in range(cols):
        if j == 0:
           temp.append(str(input("Enter name*: ")))
           if temp[j] == '' or temp[j] == '':
              sys.exit("Name is mandotary field. Process exiting due to blank field...")
        if j == 1:
           temp.append(str(input("Enter number*: ")))
           if temp[j] == '' or temp[j] == '':
             if temp[j] == '' or temp[j] == ' ':
                 temp[j] = None
        if j == 2:
           temp.append(str(input("Enter e-mail address: ")))
           if temp[j] == '' or temp[j] == '':
              if temp[j] == '' or temp[j] == ' ':
                 temp[j] = None
        if j == 3:
           temp.append(str(input("Enter DOB(dd/mm/yy): ")))
           if temp[j] == '' or temp[j] == '':
             if temp[j] == '' or temp[j] == ' ':
                 temp[j] = None
        if j == 4:
           temp.append(str(input("Enter category(Family/Friend/work/Oyher): ")))
           if temp[j] == '' or temp[j] == '':
             if temp[j] == '' or temp[j] == ' ':
                 temp[j] = None
                 
        phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():
   print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
   print("\tYou can now perform the following operations on this phonebook\n")
   print("1. Add a new Contact")
   print("2. Remove an existing contact")
   print("3. Delete all contacts")
   print("4. Search for a contact")
   print("5. Display all contacts")
   print("6. Exit Phonebook")

   choice = int(input("Please enter your choice: "))

   return choice

def add_contact(pb):
   dip = []
   for i in range(len(pb[0])):
      if i == 0:
         dip.append(str(input("Enter name:")))
      if i == 1:
         dip.append(str(input("Enter number:")))
      if i == 2:
         dip.append(str(input("Enter e-mail address:")))
      if i == 3:
         dip.append(str(input("Enter DOB(dd/mm/yy):")))
      if i == 4:
         dip.append(str(input("Enter category(Family/friends/Work/other):")))
   
   pb.append(dip)
   return pb
def remove_existing(pb):
   query = str(input("Please enter the name of the contact you wish to remove"))
   temp = 0

   for i in range(len(pb)):
      if query == pb[i][0]
        temp += 1
        print(pb.pop(i))
        print("This query has now been removed")
        return pb
   if temp == 0:
      print("Sorry you have entered an invalid query.\nPlease recheck and try again later.")
      return pb

def delete_all(pb):
   return pb.clear

def display_all(pb):
   if not pb:
      print("List is empty: []")
   else:
      for i in range(len(pb)):
         print(pb[i])

def thanks():
   print("Thank you for using our Smartphone directory system.")
   print("Please visit again!")

   print("********************************************************************")

sys.exit("Goodbye, have a nice day ahead!")
print("....................................................................")

print("Hello dear user, welcome to our smartphone directory system")

print("You may now proceed to explore this directory")

print("....................................................................")
ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
  ch = menu()
  if ch == 1:
   pb = add_contact(pb)
  elif ch == 2:
   pb = remove_existing(pb)
  elif ch == 3:
   pb = delete_all(pb)
  elif ch == 5:
   display_all(pb)
  else:
   thanks()