# matching.py - match score and smart matchmaking

from items import lost_items, found_items


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
