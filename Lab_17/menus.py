

def display_title():
    print("The Movie List program")
    print()    
    display_menu()


def display_menu():
    print("COMMAND MENU")
    print("menu - Dispay menu")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("min  - Movies by minutes")
    print("exit - Exit program")
    print() 
    
    
def display_categories(db):
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()
   