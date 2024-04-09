import datetime

def validate_age(string):
    try:
        date_of_birth = datetime.datetime.strptime(string, "%Y-%m-%d").date()
        date_of_today = datetime.date.today()
        age = date_of_today - date_of_birth
        age_in_years = age.days / 365
        if age_in_years >= 16:
            return "Access has been granted"
        else:
            return f"Access has been denied, your age is {int(age_in_years)} and the required age is 16"
    except ValueError:
        raise ValueError("Date in wrong format, please answer in YYYY-MM-DD format")

# = input("What is your birthday? (YYYY-MM-DD)")