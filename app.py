from lib import adderhandler
import lib.utils


numbers = lib.utils.get_numbers()

num1 = lib.utils.str_to_list(numbers[0])
num2 = lib.utils.str_to_list(numbers[1])

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
