from greetings import get_user_name, build_greeting
from help_menu import show_help

from datetime_utils import (
    get_current_date,
    get_current_time,
    get_current_datetime
)

from calculator import calculate

from content import (
    get_random_quote,
    get_random_fact,
    get_random_joke,
    get_random_greeting,
    get_about_response,
    get_thanks_response,
    get_how_are_you_response
)

from game import play_guessing_game, get_game_help

from ai_concepts import (
    get_ai_concept,
    recommend_activity,
    perceptron_demo
)


def main():
    """Start and run the Virtual AI Assistant."""

    print("===================================")
    print("      VIRTUAL AI ASSISTANT")
    print("===================================")

    print("\nHello! I am your Mini Alexa.")

    user_name = get_user_name()

    print(build_greeting(user_name))
    print(f"Hi {user_name}! Type 'help' to see what I can do.")
    print("You can type 'exit', 'quit' or 'bye' to leave.\n")

    while True:

        # Get and normalize user input
        user_input = input(f"{user_name} > ").strip().lower()

        # Help
        if user_input == "help":
            show_help()

        # Greetings
        elif user_input in ["hello", "hi", "hey"]:
            print(f"{get_random_greeting()} {user_name}!\n")

        # How are you
        elif user_input in [
            "how are you",
            "how are you doing",
            "how are you today"
        ]:
            print(get_how_are_you_response())
            print()

        # Thanks
        elif user_input in ["thanks", "thank you", "thank"]:
            print(get_thanks_response())
            print()

        # About assistant
        elif user_input in [
            "about",
            "about you",
            "who are you",
            "what are you"
        ]:
            print(get_about_response())
            print()

        # Date
        elif user_input in [
            "date",
            "today",
            "what is the date"
        ]:
            print(f"Today is {get_current_date()}.\n")

        # Time
        elif user_input in [
            "time",
            "what time is it",
            "current time"
        ]:
            print(f"The current time is {get_current_time()}.\n")

        # Date and time
        elif user_input in [
            "datetime",
            "date and time",
            "current date and time"
        ]:
            print(
                f"The current date and time is "
                f"{get_current_datetime()}.\n"
            )

        # Motivational quote
        elif user_input in [
            "quote",
            "motivation",
            "motivational quote",
            "give me a quote"
        ]:
            print(f"Quote: {get_random_quote()}\n")

        # Joke
        elif user_input in [
            "joke",
            "tell me a joke",
            "make me laugh"
        ]:
            print(f"Here's a joke: {get_random_joke()}\n")

        # Fact
        elif user_input in [
            "fact",
            "tell me a fact",
            "give me a fact"
        ]:
            print(f"Here's a fact: {get_random_fact()}\n")

        # Number guessing game
        elif user_input in [
            "game",
            "play game",
            "guessing game",
            "play guessing game"
        ]:
            play_guessing_game()

        # Game help
        elif user_input in [
            "game help",
            "how to play"
        ]:
            print(get_game_help())
            print()

        # AI
        elif user_input in [
            "ai",
            "what is ai",
            "what is artificial intelligence"
        ]:
            print(get_ai_concept("ai"))
            print()

        # Machine Learning
        elif user_input in [
            "ml",
            "machine learning",
            "what is machine learning"
        ]:
            print(get_ai_concept("machine learning"))
            print()

        # Generative AI
        elif user_input in [
            "genai",
            "generative ai",
            "what is generative ai"
        ]:
            print(get_ai_concept("generative ai"))
            print()

        # LLM
        elif user_input in [
            "llm",
            "what is llm",
            "large language model"
        ]:
            print(get_ai_concept("llm"))
            print()

        # Python
        elif user_input in [
            "python",
            "what is python"
        ]:
            print(get_ai_concept("python"))
            print()

        # Rule-based recommendation
        elif user_input in [
            "recommend",
            "recommendation",
            "activity",
            "what should i do"
        ]:
            print(recommend_activity())
            print()

        # Simplified perceptron
        elif user_input in [
            "perceptron",
            "perceptron demo",
            "show perceptron"
        ]:
            perceptron_demo()

        # Calculator
        elif user_input.startswith("calculate "):
            expression = user_input.replace("calculate ", "", 1)
            result = calculate(expression)
            print(f"Result: {result}\n")

        # Simple calculator trigger
        elif user_input.startswith("calc "):
            expression = user_input.replace("calc ", "", 1)
            result = calculate(expression)
            print(f"Result: {result}\n")

        # Exit
        elif user_input in ["exit", "quit", "bye"]:
            print(f"Goodbye, {user_name}! Have a great day.")
            break

        # Unknown command
        else:
            print(
                f"Sorry {user_name}, I don't understand that command yet."
            )
            print("Type 'help' to see the available commands.\n")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nAssistant stopped by the user.")

    except Exception:
        print("\nAn unexpected error occurred. Please restart the assistant.")