def get_user_name():
    """Ask the user for their name and return it."""
    name = input("What is your name? ").strip()

    # Use a default name if the user enters nothing.
    if not name:
        name = "User"

    return name


def build_greeting(name):
    """Create a personalized welcome message."""
    return f"Nice to meet you, {name}! I am your Virtual AI Assistant."