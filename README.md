# BookBot

BookBot is a Python command-line application that analyzes text files and generates a report with statistics about a book.

The program reads a book from a text file, counts the total number of words, analyzes character frequency, sorts characters by their occurrence, and displays a formatted report.

This project was created as a Python learning exercise to practice working with files, functions, dictionaries, lists, tuples, loops, sorting, and command-line arguments.

## Features

The program can:

- Read a book from a text file
- Count the total number of words
- Count how many times each character appears in the text
- Sort characters by frequency from highest to lowest
- Generate a formatted analysis report
- Analyze different books using command-line arguments

## Project Development Steps

### 1. Reading book files

Created a function to read text files:

- Implemented `get_book_text()` function
- Used Python file handling with `open()`
- Returned the book content as a string

### 2. Counting words

Implemented word counting functionality:

- Created `count_words()` function
- Counted the total number of words in the book

### 3. Counting characters

Implemented character frequency analysis:

- Created `count_characters()` function
- Converted all characters to lowercase
- Counted every character in the text
- Stored character counts in a dictionary

Example:

```python
{
    "e": 44538,
    "t": 29421,
    "a": 25894
}
```

### 4. Sorting character statistics

Added functionality to sort character counts:

- Created `sort_on()` helper function
- Converted the character dictionary into a list of tuples
- Sorted characters by their frequency using `sorted()`

Example:

```python
[
    ("e", 44538),
    ("t", 29421),
    ("a", 25894)
]
```

### 5. Generating a report

Created `print_report()` function:

- Added formatted output
- Displayed:
  - Book path
  - Total word count
  - Character frequency statistics
- Ignored non-alphabetical characters using `.isalpha()`

Example output:

```text
--- Begin report of books/frankenstein.txt ---
75767 words found in the document

e: 44538
t: 29421
a: 25894

--- End report ---
```

### 6. Command-line arguments

Added support for passing the book path when running the program:

- Imported the built-in `sys` module
- Used `sys.argv` to get the file path
- Added validation when no file path is provided

Example:

```bash
python3 main.py books/frankenstein.txt
```

Now the program can analyze different books without changing the source code.

## How to Run

Run the program from the project directory:

```bash
python3 main.py <path_to_book>
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

Other supported books:

```bash
python3 main.py books/mobydick.txt

python3 main.py books/prideandprejudice.txt
```

## Technologies Used

- Python 3
- File handling
- Dictionaries
- Lists and tuples
- Sorting with custom functions
- Command-line arguments
- Git

## Purpose

The goal of this project was to practice Python fundamentals by building a small command-line application that processes and analyzes text data.