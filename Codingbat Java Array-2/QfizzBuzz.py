def fizzBuzz(a,b):
    last_list = []
    for i in range(a,b):
        if i % 3 == 0 and i % 5 == 0:
            last_list.append("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            last_list.append("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            last_list.append("Buzz")
        else:
            last_list.append(str(i))
    return last_list
test_inputs = [1,1,1,1,1,1]
other_test_inputs = [6,8,11,16,4,2]
expected = [["1", "2", "Fizz", "4", "Buzz"],["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"],["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"],["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"],["1", "2", "Fizz"],["1"]]
all_correct = True
for i in range(len(expected)):
    if fizzBuzz(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)