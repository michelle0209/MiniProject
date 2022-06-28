import sys
cart = []
cartlist = []
pricelist = []

laptop = {1:{'name': 'Apple Macbook Air', 'price':1345.00, 'gst': 94.15, 'offer': 'Yes' } ,
          2:{'name':'Asus S533EQ 15.6', 'price':1448.00, 'gst': 101.36, 'offer': 'No'} ,
          3:{'name':'Lenovo IP 3', 'price':1308.00, 'gst': 91.56, 'offer': 'No'}}

tablets = {1:{'name': 'Samsung 64GB galaxy', 'price':372.00, 'gst': 26.84, 'offer': 'No'} ,
           2:{'name':'Apple 10.2-inch ipad', 'price':456.00, 'gst': 31.92, 'offer': 'Yes'} ,
           3:{'name':'Huawei HW-BAH3 LTE', 'price':372.00, 'gst': 26.04, 'offer': 'Yes'}}

gameConsole = {1:{'name':'Nintendo switch console','price': 457.00, 'gst': 31.99, 'offer': 'Yes'} ,
               2:{'name':'Sony playstation','price':560.00, 'gst': 39.20, 'offer': 'No'},
               3:{'name':'Microsoft Xbox console', 'price':653.00, 'gst': 45.71, 'offer': 'Yes'}}

# MAINMENU FUNCTION FROM LINE 21 TO 41 ---------------------------------------------------------------------------------
def pageBreak():
    print('*-'*60)
def mainMenu():
    pageBreak()
    print('''Computer shop  
1. View list of items
2. Add item
3. Show cart
4. Remove item
5. Bill ''')
    userinput = int(input('Welcome to the computer shop! What would you like to do ?: ')) #Ask the user to make a selection
    if userinput == 1:
        displayList()
    elif userinput == 2:
        addOrder()
    elif userinput == 3:
        showcart()
    elif userinput == 4:
        removeItem()
    elif userinput == 5:
        payment()
    else:
        print('Invalid selection')
        mainMenu()

#Function for displayList Line 45 to 60 --------------------------------------------------------------------------------
def displayList():
    pageBreak()
    print('--Laptops--\t\t\t\t Price Exclusive GST\t GST 7%\t\t Offer'  '\n'
          'Apple Macbook Air\t\t $1345.00\t\t\t\t $94.15\t\t Yes' '\n'
          'ASUS S533EQ 15.6\t\t $1448.00\t\t\t\t $101.36\t No' '\n'
          'Lenovo IP 3\t\t\t\t $1308.00\t\t\t\t $91.56\t\t No')
    print('\t')
    print('--Tablets--\t\t\t\t Price Exclusive GST\t GST 7%\t\t Offer'  '\n'
          'Samsung 64GB galaxy\t\t $372.00\t\t\t\t $26.04\t\t No' '\n'
          'Apple 10.2-inch ipad\t $456.00 \t\t\t\t $31.92\t\t Yes' '\n'
          'Huawei HW-BAH3 LTE\t\t $372.00\t\t\t\t $26.04\t\t Yes')
    print('\t')
    print('--Game consoles--\t\t Price Exclusive GST\t GST 7%\t\t Offer'  '\n'
          'Nintendo Switch Console\t $457.00\t\t\t\t $31.99\t\t Yes' '\n'
          'Sony Playstation 5\t\t $560.00 \t\t\t\t $39.20\t\t No' '\n'
          'Microsoft Xbox Console\t $653.00\t\t\t\t $45.71\t\t Yes')
#To go back mainMenu
    mainMenu()
#Function for addOrder Line 63 to 166-----------------------------------------------------------------------------------
def addOrder():
        pageBreak()
        print('1. Laptops \n' '2. Tablets \n' '3. Game Consoles')
        category = int(input('Which category do you want?: '))
        index = 1
#Laptops add order line 70 to 100 --------------------------------------------------------------------------------------
        if category == 1:
            for i in laptop:
                print(f"\n{index}. {laptop[i]['name']}\n"
                      f"Price: ${laptop[i]['price']} ,GST: ${laptop[i]['gst']} \n"
                      f"Offer: {laptop[i]['offer']}" )
                index+= 1
            choice = int(input("\nChoose a laptop: "))

            if choice == 1:
                quantity = int(input('Enter Quantity: '))
                price = (laptop[1]['price'] * quantity) + laptop[1]['gst']
                order = [quantity, laptop[1]['name']]
                cartlist.append(price)
                cart.append(order)

            elif choice == 2:
                quantity = int(input('Enter Quantity: '))
                price = (laptop[2]['price'] * quantity) + laptop[2]['gst']
                order = [quantity, laptop[2]['name']]
                cart.append(order)
                cartlist.append(price)

            elif choice == 3:
                quantity = int(input('Enter Quantity: '))
                price = (laptop[3]['price'] * quantity) + laptop[3]['gst']
                order = [quantity, laptop[3]['name']]
                cart.append(order)
                cartlist.append(price)

            else:
                print('Choose again')
                addOrder()
# Tablets selection Line 103 to 133 ----------------------------------------------------------------------------
        if category == 2:
            for i in tablets:
                print(f"\n{index}. {tablets[i]['name']}\n"
                      f"Price: ${tablets[i]['price']} ,GST: ${tablets[i]['gst']} \n"
                      f"Offer: {tablets[i]['offer']}" )
                index+= 1
            choice = int(input("\nChoose a Tablet: "))

            if choice == 1:
                quantity = int(input('Enter Quantity: '))
                price = (tablets[1]['price'] * quantity) + tablets[1]['gst']
                order = [quantity, tablets[1]['name']]
                cart.append(order)
                cartlist.append(price)

            elif choice == 2:
                quantity = int(input('Enter Quantity: '))
                price = (tablets[2]['price'] * quantity) + tablets[2]['gst']
                cartlist.append(price)
                order = [quantity, tablets[2]['name']]
                cart.append(order)

            elif choice == 3:
                quantity = int(input('Enter Quantity: '))
                price = (tablets[3]['price'] * quantity) + tablets[3]['gst']
                cartlist.append(price)
                order = [quantity, tablets[3]['name']]
                cart.append(order)

            else:
                print('Choose again')
                addOrder()
#Game Console selection Line 136 to 166 --------------------------------------------------------------------------------
        if category == 3:
            for i in gameConsole:
                print(f"\n{index}. {gameConsole[i]['name']}\n"
                      f"Price: ${gameConsole[i]['price']} ,GST: ${gameConsole[i]['gst']} \n"
                      f"Offer: {gameConsole[i]['offer']}" )
                index+= 1
            choice = int(input("\nChoose a Game Console: "))

            if choice == 1:
                quantity = int(input('Enter Quantity: '))
                price = (gameConsole[1]['price'] * quantity) + gameConsole[1]['gst']
                cartlist.append(price)
                order = [quantity, gameConsole[1]['name']]
                cart.append(order)

            elif choice == 2:
                quantity = int(input('Enter Quantity: '))
                price = (gameConsole[2]['price'] * quantity) + gameConsole[2]['gst']
                cartlist.append(price)
                order = [quantity, gameConsole[2]['name']]
                cart.append(order)

            elif choice == 3:
                quantity = int(input('Enter Quantity: '))
                price = (gameConsole[3]['price'] * quantity) + gameConsole[3]['gst']
                cartlist.append(price)
                order = [quantity, gameConsole[3]['name']]
                cart.append(order)

            else:
                print('Choose again')
                addOrder()
        mainMenu()

#Function for showcart line 171 to 176 ---------------------------------------------------------------------------------
def showcart():
    pageBreak()
    count = 1
    for i in cart:
        print(f"{count}." , (str(i).replace("[","").replace("]", "").replace(",", "").replace("'","")))
        count+=1
    mainMenu()

#Function for removing item line 180 to 194------------------------------------------------------------------------------
def removeItem():
    pageBreak()
    count = 1
    for i in cart:
        print(f"{count}." , (str(i).replace("[","").replace("]", "").replace(",", "").replace("'","")))
        count+=1

    x =input("\nWhich item you want to remove?: ")
    cart.remove(cart[int(x) -1 ])
    cartlist.remove(cartlist[int(x) -1 ])

    counter = 1
    for j in cart:
        print(f"{counter}." , (str(j).replace("[","").replace("]", "").replace(",", "").replace("'","")))
        counter+=1
    mainMenu()

#Function for payment Line 198 to 215-----------------------------------------------------------------------------------
def payment():
    pageBreak()
    print("Your finalised order is:")
    counter = 1
    for j in cart:
        print(f"{counter}." , (str(j).replace("[","").replace("]", "").replace(",", "").replace("'","")))
        counter+=1
    membership = input("\nDo you have a membership? Enter 'Y' or 'N': ")
    discountaftermember = []
    x = sum(discountaftermember)
    y = sum(cartlist)

    if membership == 'Y' or membership == 'y':
        discount = round(y * 85/100, 2)
        discountaftermember.append(discount)
        print("You have membership!\n")
    elif membership == 'N' or membership == 'n':
        print("You have no membership.\n")

#Print receipt 218 to 235-----------------------------------------------------------------------------------------------
    print('Receipt')
    line= 35*'='
    print(line)
    print('{}   {}'.format('Qty','Item'))
    print(line)
    count = 1
    for j in cart:
        print(str(j).replace("[","").replace("]", "").replace(",", "    ").replace("'",""))
        count+=1
    if membership == 'Y' or membership == 'y':
        print(f'\nMember: {membership}')
        print(f'Price with GST: ${y:.2f}')
        ttlDis = y - discount
        print(f'Discount amount: ${ttlDis:.2f} ')
        print(f'Final amount w discount: ${discount}')
    elif membership == 'N' or membership == 'n':
        print(f'\nMember: {membership}')
        print(f'Final amount with GST: ${y:.2f}')

mainMenu()
