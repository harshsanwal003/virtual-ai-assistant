import random


QUOTES = [
    "Believe you can and you're halfway there.",
    "Success is the sum of small efforts repeated every day.",
    "The secret of getting ahead is getting started.",
    "Do something today that your future self will thank you for.",
    "Great things are done by a series of small things brought together."
]


FACTS = [
    "The Earth revolves around the Sun.",
    "Water freezes at 0 degrees Celsius under normal atmospheric pressure.",
    "The human body has 206 bones in adulthood.",
    "The Moon is Earth's natural satellite.",
    "Python is a popular programming language."
]


JOKES = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the computer cold? It left its Windows open!",
    "Why do programmers prefer dark mode? Because light attracts bugs!"
]


GREETINGS = [
    "Hello!",
    "Hi there!",
    "Hey!",
    "Hello! Nice to hear from you."
]


def get_random_quote():
    """Return a random motivational quote."""
    return random.choice(QUOTES)


def get_random_fact():
    """Return a random fact."""
    return random.choice(FACTS)


def get_random_joke():
    """Return a random joke."""
    return random.choice(JOKES)


def get_random_greeting():
    """Return a random greeting."""
    return random.choice(GREETINGS)


def get_about_response():
    """Return information about the assistant."""
    return (
        "I am Mini Alexa, a beginner-level offline virtual AI assistant "
        "built using Python. I use rule-based commands to respond to you."
    )


def get_thanks_response():
    """Return a response to thanks."""
    return "You're welcome! I'm happy to help."


def get_how_are_you_response():
    """Return a response to how are you."""
    return "I'm doing well! Thanks for asking."