shopping_list=[]

while True:
    print("Menu:")
    print("1 Add item")
    print("2 Remove item")
    print("3 Display List")
    print("4 Exit")

    choice=input("Enter the number what to do with the list:")
    if choice == "1":
        item=input("Enter name of the item:")
        if item:
            shopping_list.append(item)
            print("Your item added successfully.")
        else:
            print("item name can't be empty")
    elif choice=='2':
        item=input("Enter the item to remove:")
        if not shopping_list:
            print("Shopping list is empty")
        else:
            shopping_list.remove(item)
            print("Your item removed successfully.")
    elif choice=='3':
        print(shopping_list)
    elif choice=='4':
        print("Thanks for visiting.")
        break
    else:
        print("Invalid input")
