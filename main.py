from re import S
from letters import run_letters
from nums import run_numbers

while True:



    opponent = input(
        "Choose your opponent: Rachel('R') OR Susie('S')\nType 'X' to quit.\n>>> "
    )

    if opponent.capitalize() in ("R", "Rachel"):
        run_numbers()
    elif opponent.capitalize() in ("S", "Susie"):
        run_letters()
    elif opponent.capitalize() == "X":
        break
    else:
        print("I don't understand what you mean with '" + opponent + "'.")