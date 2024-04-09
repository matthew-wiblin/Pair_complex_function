# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def validate_age(input("What is your birthday? (YYYY-MM-DD)"))

paramter is the users date of birth

return values will be one of two strings declaring a pass or a fail 

side effects will be a raised exception for incorrect parameter type. 
Exception will be a type error.

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

Given a birthday of a user who is over 16, return a string "Access has been granted"

Given a birthday of a user who is under 16, return a string f"Access has been denied, your age is {age} and required age is 16"

Given wrong format for the date. Raise an exception "Date in wrong format, please answer in YYYY-MM-DD format"






_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
