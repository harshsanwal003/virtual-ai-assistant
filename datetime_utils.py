from datetime import datetime


def get_current_date():
    """Return the current date."""
    current_date = datetime.now()
    return current_date.strftime("%d %B %Y")


def get_current_time():
    """Return the current time."""
    current_time = datetime.now()
    return current_time.strftime("%I:%M:%S %p")


def get_current_datetime():
    """Return the current date and time."""
    current_datetime = datetime.now()
    return current_datetime.strftime("%d %B %Y, %I:%M:%S %p")