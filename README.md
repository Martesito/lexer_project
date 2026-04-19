
## Description

This project implements two **finite automata** based on the reference material (Section 3.4.2 from *Compilers: Principles, Techniques, & Tools* by Aho et al.).

The system simulates part of a **lexical analyzer**, recognizing:

* **Identifiers (ID)**
* The reserved keyword **`then`**

It follows the transition diagrams provided in the assignment and includes proper handling of the **retract operation (`*`)**, which allows the lexer to step back one character when needed.

---

## Technologies Used

* **Programming Language:** Python 3.x
* **IDE:** Visual Studio Code
* **Operating System:** (Fill this with your OS, e.g., Windows 10/11, Linux, etc.)

---

##  How It Works

The program is designed using **Object-Oriented Programming (OOP)** principles:

### Main Components

* **Token** → Represents a recognized lexeme and its type
* **Lexer** → Handles input reading and character navigation
* **Automaton (Abstract Class)** → Base class for all automata
* **IdentifierAutomaton** → Recognizes identifiers
* **ThenAutomaton** → Recognizes the keyword `then`
* **LexerEngine** → Controls execution and automata priority

---

## Recognition Strategy

1. The input string is processed character by character.
2. The lexer ignores whitespace.
3. The system attempts recognition in this order:

   * First: `then` keyword
   * Second: identifiers
4. If a match fails, the lexer **retracts** the last character.
5. If no automaton recognizes the input, a **lexical error** is reported.

---

## How to Run

1. Open a terminal in the project folder.


2. Run the program:

python main.py


3. Enter an input string when prompted:

Ingrese la cadena a analizar:


4. Example input: 

then thenextvalue total


5. Example output:

Tokens encontrados:
(THEN, 'then')
(ID, 'thenextvalue')
(ID, 'total')

---

## Project Structure

lexer_project/
│
├── token.py
├── lexer.py
├── automaton.py
├── identifier_automaton.py
├── then_automaton.py
├── lexer_engine.py
└── main.py
```

---

##  Notes

* The keyword `then` has **higher priority** than identifiers.
* Strings like `thenext` are correctly recognized as identifiers.
* The implementation strictly follows the behavior of the transition diagrams.

---

## Video Explanation

A short video (max 5 minutes) is included explaining:

* The implementation of both automata
* The use of retract (`*`)
* The overall algorithm

---

## References

Aho, Alfred V., et al.
*Compilers: Principles, Techniques, & Tools*, 2nd Edition. Pearson.

---

## Authors

Daniel Osorio Velez
Maria Camila Rodriguez Gonzalez

---
