# 0
This software system is a command line game written in python.

# Class Structure
![UML Diagram](https://i.ibb.co/QFTCtpn/dass-a2-uml.png)

# Code Smells
*The refactoring column is optional, `na` if not done*
| Smell | Description | Refactoring |
| - | - | - |
| Long Parameter List | In `barberian.py`, the `barberian` class has the method `attack` which has 13 parameters | We can combine parameters `h1` to `h5` into a list `h: List[]` and parameters `c1` to `c3` to a list `c: List[]` |
| Duplicated Code | In `barberian.py`, the `barberian` class has the method `attack` which has a large if-else if ladder where each block carries similar functionality of causing damage to a particular object and removing the object, if its health is less than or equal to zero | If the above refactoring suggestion is followed, we have arrays, for the huts and cannons, so we can use simple string matching to reduce the amount of conditional blocks required |
| Uncommunicative Name | In `barberian.py`, the `barberian` class has the method `move` which has parameters `a` and `b`. These variables are grids but this information is not conveyed anywhere in the class nor in the variable names. | Rename `a` to `board_grid` and `b` to `obs_grid`. |
| Refused Bequest | In `object.py`, the class `CREATE_TOWNHALL` inherits from class `scenery` but never uses any parent functions, in fact, the method `create_townhall` is identical the method `create_townhall` in the parent class `scenery`. | Remove the use of inheritance |
| Oddball Solution | In `canon.py`, class `canon` is used to represent all classes, the method `attack` loops over every canon and attacks for all of them. | The `canon` class should represent **1** canon and multiple instances of this class should be instantiated for multiple canons. |
| Oddball Solution | List variables are used in many places where a simple integer would've sufficed, for example, `count`, `c1` to `c3`, and `h1` to `h6`. These variables are never pushed to or popped from and so they are never used as lists.  | Change these variables to simple integers. |
| Duplicated Code | In `board.py`, the class `board` has a method `print_board`, which has a large if-elif ladder, where groups of the blocks execute the same code | Could concatenate the groups where the same code is executed into once condition, and thus have only one conditional block for each unique code block|
| Dead Code | In `board.py`, the class `board` has a method `print_board`, which has 14 parameters, 3 of which are unused | Removal of the unused parameters |
| Long Parameter List | In `board.py`, the `board` class has the method `print_board` which has 14 parameters | We can combine parameters `h1` to `h5` into a list `h: List[]` and parameters `c1` to `c3` to a list `c: List[]` |

# Bugs
| Bug | Description | Refactoring |
| - | - | - |
| No Win Condition | In `play_game.py:102:5`, to win the game we check if the `count` variable is `9`. However, `count` is a `List[]` and thus the game is never winnable. | The check should be `if (count[0] == 9)` but better yet, we never `push` to or `pop` from the `count` list and so it can simply be made an integer. |
| Canon attacks after death | In `play_game.py:87:26`, the canon damage is applied regardless of whether the canon is destroyed or not (the check isn't done in `canon.attack()` either). | First, we check if the canon is alive using canon health variables `c1` to `c3` and only attack if the health is non-zero. |
