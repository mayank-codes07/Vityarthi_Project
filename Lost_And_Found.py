IGNORE_WORDS = {
    "a", "an", "the", "is", "was", "my", "it", "in", "on", "at",
    "with", "and", "of", "to", "i", "have", "has", "had", "near",
    "colour", "color"
}
lost_items = []
found_items = []

lost_id_counter = 1
found_id_counter = 1

def get_keywords(description):
    words = description.lower().split()
    keywords = set()
    for word in words:
        # strip basic punctuation a person might type
        cleaned = word.strip(".,!?")
        if cleaned not in IGNORE_WORDS and cleaned != "":
            keywords.add(cleaned)
    return keywords


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


def calculate_match_score(lost_keywords, found_keywords):
    common_words = lost_keywords.intersection(found_keywords)
    all_words = lost_keywords.union(found_keywords)

    if len(all_words) == 0:
        return 0

    score = (len(common_words) / len(all_words)) * 100
    return round(score, 1)


def find_best_match_for(lost_item):
    best_score = -1
    best_found_item = None

    for found_item in found_items:
        score = calculate_match_score(lost_item["keywords"], found_item["keywords"])
        if score > best_score:
            best_score = score
            best_found_item = found_item

    return best_found_item, best_score


def smart_matchmaking():
    print("\n--- Running Smart Matchmaking ---")

    if len(lost_items) == 0:
        print("No lost items reported yet.")
        return

    if len(found_items) == 0:
        print("No found items reported yet, nothing to match against.")
        return

    for lost_item in lost_items:
        best_found_item, best_score = find_best_match_for(lost_item)

        print(f"\nLost item: {lost_item['name']} (ID L{lost_item['id']})")

        if best_found_item is None or best_score == 0:
            print("   -> No matching found item yet.")
            continue

        # decide how confident we are, using simple if-elif-else
        if best_score >= 60:
            confidence = "STRONG MATCH"
        elif best_score >= 30:
            confidence = "POSSIBLE MATCH"
        else:
            confidence = "WEAK MATCH"

        print(f"   -> Best match: {best_found_item['name']} (ID F{best_found_item['id']})")
        print(f"   -> Match score: {best_score}%  [{confidence}]")
        print(f"   -> Found at: {best_found_item['location']}")
        print(f"   -> Contact finder: {best_found_item['contact']}")


def view_items(item_list, title, prefix):
    print(f"\n--- {title} ---")

    if len(item_list) == 0:
        print("Nothing to show yet.")
        return

    for item in item_list:
        day, month, year = item["date"]
        print(f"{prefix}{item['id']} | {item['name']} | {item['description']}")
        print(f"    Location: {item['location']}  Date: {day}-{month}-{year}  Contact: {item['contact']}")


def count_items():
    strong_matches = 0
    for lost_item in lost_items:
        _, score = find_best_match_for(lost_item)
        if score >= 60:
            strong_matches = strong_matches + 1

    print("\n--- Statistics ---")
    print(f"Total lost items reported : {len(lost_items)}")
    print(f"Total found items reported: {len(found_items)}")
    print(f"Strong matches so far     : {strong_matches}")


def search_by_keyword():
    keyword = input("\nEnter a keyword to search for: ").lower().strip()

    print(f"\n--- Search results for '{keyword}' ---")
    found_any = False

    for item in lost_items:
        if keyword in item["keywords"]:
            print(f"[LOST]  L{item['id']} - {item['name']} - {item['description']}")
            found_any = True

    for item in found_items:
        if keyword in item["keywords"]:
            print(f"[FOUND] F{item['id']} - {item['name']} - {item['description']}")
            found_any = True

    if not found_any:
        print("No items matched that keyword.")


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
            print("Thank you for using the Lost and Found System")
            running = False
        else:
            print("Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()