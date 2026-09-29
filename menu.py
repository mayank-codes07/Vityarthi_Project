# menu.py - the main menu

def show_menu():
    print("\n================ LOST AND FOUND SYSTEM ================")
    print("1. Report a lost item")
    print("2. Report a found item")
    print("3. View all lost items")
    print("4. View all found items")
    print("5. Run Smart Matchmaking")
    print("6. Search by keyword")
    print("7. Show statistics")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    return choice
