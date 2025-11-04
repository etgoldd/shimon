from garage import Garage
from typing import Callable
from collections import defaultdict


ERROR_TEXT = "Not a valid option, please try again and select from the menu above (just the number!)"


def main():
    garage = Garage()
    prompt_options: dict[int, tuple[str, Callable]] = {
        1: ("Add Vehicle", garage.add_vehicle),
        2: ("Get Fastest Vehicle", garage.get_fastest_vehicle),
        3: ("Get Nicest Plates", garage.get_pretty_plates), 
        4: ("Get Trucks Contents", garage.get_trucks_contents),
        5: ("Empty Database (Remove all vehicles)", garage.empty_db),
    }
    actions = defaultdict(lambda: (lambda: None))
    actions.update({i: val[1] for i, val in prompt_options.items()})
    prompt_text = "0 - Exit Program\n"
    prompt_text += "\n".join([f"{i} - {val[0]}" for i, val in prompt_options.items()])
    prompt_text += "\nEnter Command: "

    while (user_command_str := input(prompt_text)) != "0":
        try: 
            user_command = int(user_command_str)
        except Exception:
            print(ERROR_TEXT)
            continue
        actions[user_command]()


if __name__ == '__main__':
    main()