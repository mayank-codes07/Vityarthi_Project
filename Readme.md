# Lost and Found Smart Matchmaking System

**Course:** Python Essentials

Repository: "https://github.com/mayank-codes07/Vityarthi_Project"

## Overview
A terminal-based Python program that helps match lost items with found items. A user reports
an item with a short description; the program pulls out keywords and compares lost and found
items with a percentage score, then shows the best match with a confidence label and the
finder's contact details. See [statement.md](statement.md) for the full problem statement.

## Features
- Report lost items and found items (with auto-generated IDs like `L1` and `F1`)
- Keyword extraction that ignores common words such as "the", "with", "near"
- Smart matchmaking: match score in percent, labelled STRONG (60+), POSSIBLE (30+) or WEAK
- View all lost / all found items
- Search by keyword across both lists
- Statistics: total lost, total found, strong matches
- Two sample items are pre-loaded so option 5 works straight away

## Technologies / Tools Used
- Python 3.8 or newer
- Python standard library only (no third-party packages)
- Git and GitHub for version control

Python concepts used: variables, `input()`/`print()`, f-strings, string methods, lists,
dictionaries, sets (`intersection`, `union`), tuples, functions, `while` loop,
`if / elif / else`, and modules (`import`).

## Project Structure
```
.
├── README.md
├── statement.md
├── requirements.txt
├── src/
│   ├── main.py        # entry point and main loop
│   ├── menu.py        # prints the menu
│   ├── config.py      # list of ignored words
│   ├── text_utils.py  # keyword extraction
│   ├── items.py       # lost/found storage, add items, sample data
│   ├── matching.py    # match score and smart matchmaking
│   └── display.py     # view, search and statistics
└── docs/
    ├── diagrams.md    # architecture, workflow, UML diagrams
    ├── testing.md     # test cases
    └── report_draft.md
```

## How to Install and Run

There is no environment setup, dependency installation or configuration file needed,
because the project uses only built-in Python.

1. **Check Python is installed** (3.8 or newer):
   ```
   python --version
   ```
   On some systems the command is `python3 --version`.
   If Python is missing, install it from https://www.python.org/downloads/
2. **Get the code:**
   ```
   git clone https://github.com/{github-username}/{repo-name}.git
   cd {repo-name}
   ```
   (Or download the repository as a ZIP from GitHub and extract it.)
3. **Dependencies:** none. (`requirements.txt` is included only to state this.)
4. **Run the program from the repository root:**
   ```
   python src/main.py
   ```
   Use `python3 src/main.py` if `python` does not work.
5. **Use the menu:** type a number from 1 to 8 and press Enter.
   - Enter dates in the format `dd-mm-yyyy` (for example `15-09-2026`).
   - Try option `5` first to see matchmaking on the pre-loaded sample items.
   - Option `8` exits the program.

## How to Test
Testing is done by running the program and following the test cases in
[docs/testing.md](docs/testing.md). Each case lists the inputs to type and the output
to expect. Quick check:

1. Run `python src/main.py`
2. Choose `5` - expected: `Water bottle (L1)` matches `Bottle (F1)` with `40.0%` and `[POSSIBLE MATCH]`
3. Choose `9` - expected: `Please enter a number between 1 and 8.`

## Known Limitations
- Data is kept in memory only and is lost when the program is closed.
- The date must be typed exactly as `dd-mm-yyyy`; other formats are not handled.
- Matching is based on words, so different words for the same thing (for example
  "purse" and "wallet") are not matched.



## Documentation
- [statement.md](statement.md) - problem statement, scope, users, features
- [docs/diagrams.md](docs/diagrams.md) - design diagrams
- [docs/testing.md](docs/testing.md) - test cases

