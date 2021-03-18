from lib.validation import BinaryNumberValidator
from PyInquirer import prompt


def str_to_list(string):
    value = []
    for i in string:
        value.append(int(i))
    return value


def get_numbers():
    questions = [
        {
            "type": "input",
            "name": "num1",
            "message": "Enter Number 1",
            "validate": BinaryNumberValidator
        },
        {
            "type": "input",
            "name": "num2",
            "message": "Enter Number 2",
            "validate": BinaryNumberValidator
        }
    ]

    answers = prompt.prompt(questions)
    num1 = answers['num1']
    num2 = answers['num2']

    while len(num1) != len(num2):
        print("Error: The two numbers must be of the same length!")

        answers = prompt.prompt(questions)
        num1 = list(answers['num1'])
        num2 = list(answers['num2'])

    return_value = [num1, num2]

    return return_value
