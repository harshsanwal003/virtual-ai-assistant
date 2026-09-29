from datetime import datetime


AI_CONCEPTS = {
    "ai": (
        "Artificial Intelligence, or AI, is the field of creating "
        "computer systems that can perform tasks that normally require "
        "human intelligence."
    ),

    "machine learning": (
        "Machine Learning is a part of AI where computers learn patterns "
        "from data and use those patterns to make predictions or decisions."
    ),

    "ml": (
        "Machine Learning is a part of AI where computers learn patterns "
        "from data and use those patterns to make predictions or decisions."
    ),

    "generative ai": (
        "Generative AI is a type of AI that can create new content such "
        "as text, images, audio or code."
    ),

    "genai": (
        "Generative AI is a type of AI that can create new content such "
        "as text, images, audio or code."
    ),

    "llm": (
        "An LLM, or Large Language Model, is an AI model trained on large "
        "amounts of text to understand and generate human-like language."
    ),

    "python": (
        "Python is a high-level programming language known for its simple "
        "syntax and wide use in web development, automation, data science "
        "and artificial intelligence."
    )
}


def get_ai_concept(concept):
    """Return an explanation for a supported AI concept."""

    concept = concept.strip().lower()

    return AI_CONCEPTS.get(
        concept,
        "I don't have an explanation for that concept yet."
    )


def recommend_activity():
    """
    Recommend an activity based on the current hour.

    This is a simple rule-based decision demonstration.
    """

    current_hour = datetime.now().hour

    if current_hour < 12:
        activity = "It is morning. A good activity would be having breakfast."
    elif current_hour < 17:
        activity = "It is afternoon. A good activity would be working or studying."
    elif current_hour < 21:
        activity = "It is evening. A good activity would be exercising or relaxing."
    else:
        activity = "It is night. A good activity would be resting and preparing for tomorrow."

    return activity


def perceptron_demo():
    """
    Demonstrate a simple non-trained perceptron.

    The user provides three numeric inputs.
    Fixed weights and a bias are used to calculate the output.
    """

    print("\n===== SIMPLIFIED PERCEPTRON =====")
    print("Enter three numeric inputs.")

    try:
        input_1 = float(input("Input 1: "))
        input_2 = float(input("Input 2: "))
        input_3 = float(input("Input 3: "))

        weight_1 = 0.5
        weight_2 = 0.3
        weight_3 = 0.2
        bias = -0.5

        weighted_sum = (
            input_1 * weight_1
            + input_2 * weight_2
            + input_3 * weight_3
            + bias
        )

        if weighted_sum > 0:
            output = 1
        else:
            output = 0

        print(f"Weighted sum: {weighted_sum}")
        print(f"Perceptron output: {output}")
        print("================================\n")

    except ValueError:
        print("Please enter numeric values only.\n")