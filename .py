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
