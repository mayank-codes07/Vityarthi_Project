# project - Lost and Found Smart Matchmaking System (entry point)
from items import add_lost_item, add_found_item, load_sample_data, lost_items, found_items
from matching import smart_matchmaking
from display import view_items, search_by_keyword, count_items
from menu import show_menu


def main():
    print("Welcome to the Lost and Found Smart Matchmaking System!")
    load_sample_data()
    print("(Two sample items have been pre-loaded so you can try option 5 right away.)")

    running = True
    while running:
        choice = show_menu()

        if choice == "1":
            add_lost_item()
        elif choice == "2":
            add_found_item()
        elif choice == "3":
            view_items(lost_items, "All Lost Items", "L")
        elif choice == "4":
            view_items(found_items, "All Found Items", "F")
        elif choice == "5":
            smart_matchmaking()
        elif choice == "6":
            search_by_keyword()
        elif choice == "7":
            count_items()
        elif choice == "8":
            print("Thank you for using the Lost and Found System. Goodbye!")
            running = False
        else:
            print("Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
