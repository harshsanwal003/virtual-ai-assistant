# Virtual AI Assistant (Mini Alexa)

## Nexbridge Technologies — AI Internship Program Project 1

A beginner-level, offline, terminal-based Virtual AI Assistant built using
Python standard library modules.

The project demonstrates rule-based command processing along with simplified
AI, ML and DL concepts.

---

## Project Objective

The objective of this project is to build a simple command-line assistant
that can:

- Understand predefined text commands
- Respond using rule-based logic
- Remember the user's name during the current session
- Perform basic calculations
- Display date and time
- Provide quotes, jokes and facts
- Run a number guessing game
- Demonstrate rule-based recommendation
- Demonstrate a simplified perceptron

---

## Features

### Greeting and Name

- Greets the user when the program starts
- Asks for the user's name
- Reuses the name during the current session

### Date and Time

- Displays the current date
- Displays the current time
- Displays the current date and time

### Calculator

Supports:

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero protection
- Invalid input handling

Examples:

    calculate 10 + 5
    calculate 10 - 3
    calculate 4 * 6
    calculate 20 / 4

### Content

- Random motivational quote
- Random joke
- Random fact

The content is selected from predefined Python lists.

### Number Guessing Game

- Random number from 1 to 10
- Three attempts
- Higher/lower feedback
- Invalid input handling

### AI Concepts

The assistant includes educational explanations for:

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Generative AI (GenAI)
- Large Language Models (LLM)
- Python

These are predefined educational responses and do not use real AI models
or external services.

### Rule-Based Recommendation

The assistant recommends an activity based on the current time using
if/elif/else rules.

### Simplified Perceptron

The project demonstrates a non-trained perceptron using:

- Numeric inputs
- Fixed weights
- Bias
- Weighted sum
- Step activation function
- Output of 0 or 1

---

## Project Structure

    virtual-ai-assistant/
    |
    |-- main.py
    |-- greetings.py
    |-- datetime_utils.py
    |-- calculator.py
    |-- content.py
    |-- game.py
    |-- ai_concepts.py
    |-- help_menu.py
    |-- README.md

---

## Module Responsibilities

### main.py

- Program entry point
- Main input/response loop
- Command routing
- Top-level exception handling

### greetings.py

- User name capture
- Greeting generation

### datetime_utils.py

- Current date
- Current time
- Current date and time

### calculator.py

- Expression parsing
- Arithmetic calculations
- Error handling

### content.py

- Motivational quotes
- Jokes
- Facts
- Random selection

### game.py

- Number guessing game

### ai_concepts.py

- AI/ML/GenAI/LLM educational responses
- Rule-based recommendation
- Simplified perceptron demonstration

### help_menu.py

- Displays all supported commands

---

## How to Run

Make sure Python 3 is installed.

Open a terminal inside the project folder and run:

    python main.py

---

## Example Commands

    help
    hello
    date
    time
    datetime
    quote
    joke
    fact
    calculate 10 + 5
    game
    ai
    ml
    genai
    llm
    recommend
    perceptron
    exit

---

## Rule-Based Processing

The assistant follows this basic flow:

    User Input
        |
        v
    Normalize Text
        |
        v
    Match Command / Keyword
        |
        v
    Select Rule
        |
        v
    Call Function
        |
        v
    Display Response
        |
        v
    Return to Main Loop

The project uses predefined rules rather than machine learning inference.

---

## AI / ML / DL Learning Demonstrations

### AI

The assistant uses predefined rules and pattern matching to respond to
different categories of user input.

### Machine Learning

The project demonstrates ML concepts through simplified examples such as
classification-style decisions, recommendation rules and session-based
information reuse.

No real machine learning model is trained.

### Deep Learning

The perceptron feature demonstrates the basic calculation of a neural
network unit using inputs, weights, bias and an activation function.

No neural network is trained.

---

## Project Constraints

This project is intentionally beginner-level.

The application is:

- Offline
- Terminal/console based
- Rule-based
- Built with Python standard library functionality

The project does not use:

- External APIs
- Databases
- Datasets
- Cloud services
- Persistent storage
- Real ML training
- Real DL training
- pandas
- NumPy
- scikit-learn
- TensorFlow
- PyTorch
- Keras
- OpenCV

All user information is stored only during the current program session.

---

## Testing

The project was manually tested for:

- Name capture and reuse
- Date
- Time
- Date and time
- Addition
- Subtraction
- Multiplication
- Division
- Division by zero
- Invalid calculator input
- Random quote
- Random joke
- Random fact
- Number guessing game
- Higher/lower feedback
- Attempt limit
- Help menu
- AI concept commands
- Rule-based recommendation
- Perceptron calculation
- Invalid perceptron input
- Unknown commands
- Uppercase commands
- Graceful exit

The Nexbridge PRD requires the project to demonstrate all 14 functional
requirements and survive at least 20 manual test inputs, including invalid
inputs.