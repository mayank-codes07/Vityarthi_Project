# Problem Statement

## Problem
In a college campus, students lose belongings such as bottles, wallets, keys and ID cards
every day, and other students find them. The two sides rarely meet. Notice boards and
group chats are unorganised, and a person has to read through many messages to check
whether their item was found. Because the same object is described in different words
("steel blue bottle" vs "blue steel water bottle"), a simple exact-text check does not work.

## Proposed Solution
A command-line **Lost and Found Smart Matchmaking System** written in Python. Users report
lost and found items in a structured way. The program converts each description into a set
of keywords and compares every lost item with every found item using a percentage match
score. It then reports the best found item for each lost item along with a confidence label
and the finder's contact details.

## Scope
**In scope**
- Reporting lost items and found items (name, description, location, date, contact)
- Automatic keyword extraction from the description
- Match score calculation and confidence labels (Strong / Possible / Weak)
- Viewing all lost and found items
- Searching items by a keyword
- Summary statistics
- Runs fully in the terminal using only the Python standard library

**Out of scope (in this version)**
- Permanent storage (data lives in memory while the program runs)
- Graphical or web interface
- Image-based matching, user accounts, notifications

## Target Users
- Students and staff of a college who lose or find items on campus
- A lost-and-found desk / help desk operator who records items

## High-Level Features
1. Report a lost item
2. Report a found item
3. View all lost items and all found items
4. Smart matchmaking with match score and confidence level
5. Keyword search across lost and found items
6. Statistics (totals and number of strong matches)
7. Sample data pre-loaded so matchmaking can be tried immediately
