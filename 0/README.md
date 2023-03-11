# 0
This software system is a command line game written in python.

# Class Structure
`todo`

# Code Smells
*The refactoring column is optional, `na` if not done*
| Smell | Description | Refactoring |
| - | - | - |
| Long Parameter List | In `barberian.py`, the `barberian` class has the method `attack` which has 13 parameters | We can combine parameters `h1` to `h6` into a list `h: List[]` and parameters `c1` to `c3` to a list `c: List[]` |
| Duplicated Code | In `barberian.py`, the `barberian` class has the method `attack` which has a large if-elif ladder where each block carries ut similar functionality of causing damage to particular object and removing the object, if its health is less than or equal to zero | if the above refactoring suggestion is followed, we have arrays, for the huts and cannons, so we can use simple string matching to reduce the amount of conditionla blocks required|

# Bugs
| Bug | Description | Refactoring |
| - | - | - |
