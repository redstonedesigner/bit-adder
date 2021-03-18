from lib import adderhandler
from lib.validation import BinaryNumberValidator
import lib.utils

from PyInquirer import prompt


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

num1 = lib.utils.str_to_list(num1)
num2 = lib.utils.str_to_list(num2)

num1.reverse()
num2.reverse()

result = []

for i in range(0, len(num1)):
    try:
        output = adderhandler.FullAdder(int(num1[i]), int(num2[i]), output.c)
    except NameError:
        output = adderhandler.FullAdder(int(num1[i]), int(num2[i]), 0)
    result.append(str(output.s))

if output.c == 1:
    result.append(str(output.c))

result.reverse()

final = "".join(result)

print("Your final answer is: "+final)
