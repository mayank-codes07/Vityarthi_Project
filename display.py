# display.py - viewing, searching and statistics

from items import lost_items, found_items
from matching import find_best_match_for


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
