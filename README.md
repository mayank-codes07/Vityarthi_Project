# Vityarthi_Project
# Lost and Found - Smart Matchmaking System

A simple console-based Python project for the **CSE1021 - Introduction to
Problem Solving and Programming** course project.

## Idea

People lose things, and people find things - but they rarely reach the
right person. This program lets users report a **lost** item or a
**found** item, and then runs a small "smart matchmaking" routine that
compares the two descriptions word-by-word to work out how likely a
found item is to be someone's lost item.

There is no external AI/ML library involved. The "smart" part is plain
logic built from the topics covered in class - it looks at the common
words between a lost description and a found description and turns
that into a match percentage.

## How it works

1. A lost item and a found item are each stored as a **dictionary**
   (name, description, location, date, contact, keywords).
2. The date typed by the user (`dd-mm-yyyy`) is split into a
   **tuple** `(day, month, year)` using tuple assignment.
3. Every description is broken into a **set** of lowercase keywords,
   after removing common filler words (a, the, is, and ...). Using a
   set automatically removes duplicate words.
4. To compare a lost item with a found item, the program takes the
   **intersection** (common words) and the **union** (all words) of
   the two keyword sets and calculates:

   ```
   match score = (common words / all words) * 100
   ```

   This is basic set theory, applied as a simple similarity check.
5. For every lost item, the program loops through **all** found items
   and keeps the one with the **highest score** - a hand-written
   version of the "Finding the Maximum" algorithm instead of using
   a built-in shortcut.
6. Based on the score, the match is labelled:
   - **60% and above** -> Strong Match
   - **30% - 59%** -> Possible Match
   - **below 30%** -> Weak Match

## Features (menu options)

1. Report a lost item
2. Report a found item
3. View all lost items
4. View all found items
5. Run Smart Matchmaking (shows the best match for every lost item)
6. Search items by keyword
7. Show statistics (counts of lost/found items and strong matches)
8. Exit

The program pre-loads two example items on startup (one lost water
bottle and one found bottle) so option 5 has something to show
immediately, even before entering your own data.

## Python / syllabus topics used

Only topics covered in Units 1-5 of CSE1021 were used:

- Variables, expressions, statements, tuple assignment
- Conditional statements: `if / elif / else`
- Iteration statements: `while`, `for`, `break`
- Functions with parameters and arguments
- Lists, Sets (union, intersection), Dictionaries, Tuples
- Fundamental algorithms: Counting, Finding the Maximum,
  Removal of Duplicates (via sets)

No classes/OOP, no external matching libraries, and no file handling
were used, since these are outside the course syllabus.

## How to run

```
python3 lost_and_found.py
```

Requires Python 3. No extra installations needed - it only uses
Python's built-in features.

## Files

- `lost_and_found.py` - the complete program
- `README.md` - this file

