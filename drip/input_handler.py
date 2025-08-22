# handles user inputs
from drip.constant import EXIT

class InputHandler:

    @staticmethod
    def get_positive_int(prompt: str):
        """Gets Positive Integer Input"""
        while True:
            try:
                x = int(input(prompt))
                if x > 0:
                    return x
                else:
                    print('Please enter a positive integer.')
            except ValueError:
                print('Enter an Integer')

    @staticmethod
    def get_positive_float(prompt: str):
        """Gets Positive Float Input"""
        while True:
            try:
                x = float(input(prompt))
                if x > 0:
                    return x
                else:
                    print('Please enter a positive value.')
            except ValueError:
                print('Enter a value')

    @staticmethod
    def choose_from_list(prompt: str, menu):
        """Selection handler"""
        while True:
            try:
                choice = int(input(prompt))
                selection = menu.get(choice)
                if selection is None:
                    print("Invalid choice, try again.")
                    continue
                else:
                    return selection
            except ValueError:
                print('Enter selection number.')