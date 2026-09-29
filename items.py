# items.py - storage of lost/found items and the add operations

from text_utils import get_keywords

lost_items = []
found_items = []

lost_id_counter = 1
found_id_counter = 1


def add_lost_item():
    """Ask the user for details of a lost item and store it."""
    global lost_id_counter

    print("\n--- Report a LOST item ---")
    name = input("Item name: ")
    description = input("Describe the item (color, brand, features...): ")
    location = input("Where did you lose it? ")
    date_str = input("Date lost (dd-mm-yyyy): ")
    contact = input("Your contact number/email: ")

    # tuple assignment - splitting the date into day, month, year
    day, month, year = date_str.split("-")
    date_tuple = (day, month, year)

    item = {
        "id": lost_id_counter,
        "name": name,
        "description": description,
        "keywords": get_keywords(name + " " + description),
        "location": location,
        "date": date_tuple,
        "contact": contact
    }

    lost_items.append(item)
    print(f"Lost item saved with ID L{lost_id_counter}.")
    lost_id_counter = lost_id_counter + 1


def add_found_item():
    """Ask the user for details of a found item and store it."""
    global found_id_counter

    print("\n--- Report a FOUND item ---")
    name = input("Item name: ")
    description = input("Describe the item (color, brand, features...): ")
    location = input("Where did you find it? ")
    date_str = input("Date found (dd-mm-yyyy): ")
    contact = input("Your contact number/email: ")

    day, month, year = date_str.split("-")
    date_tuple = (day, month, year)

    item = {
        "id": found_id_counter,
        "name": name,
        "description": description,
        "keywords": get_keywords(name + " " + description),
        "location": location,
        "date": date_tuple,
        "contact": contact
    }

    found_items.append(item)
    print(f"Found item saved with ID F{found_id_counter}.")
    found_id_counter = found_id_counter + 1


def load_sample_data():
    global lost_id_counter, found_id_counter

    lost_items.append({
        "id": lost_id_counter,
        "name": "Water bottle",
        "description": "Blue steel water bottle with a dent near the cap",
        "keywords": get_keywords("Water bottle Blue steel water bottle with a dent near the cap"),
        "location": "Library second floor",
        "date": ("12", "09", "2026"),
        "contact": "9876543210"
    })
    lost_id_counter = lost_id_counter + 1

    found_items.append({
        "id": found_id_counter,
        "name": "Bottle",
        "description": "Steel blue bottle found near the reading hall, small dent on it",
        "keywords": get_keywords("Bottle Steel blue bottle found near the reading hall, small dent on it"),
        "location": "Reading hall",
        "date": ("12", "09", "2026"),
        "contact": "9123456780"
    })
    found_id_counter = found_id_counter + 1
