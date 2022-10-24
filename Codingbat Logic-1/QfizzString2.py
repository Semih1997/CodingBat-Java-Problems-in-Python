def fizzString2(a):
    last_string = str(a) + "!"
    if a % 3 == 0:
        last_string = "Fizz!"
    if a % 5 == 0:
        last_string = "Buzz!"  
    if a % 3 == 0 and a % 5 == 0:
        last_string = "FizzBuzz!"
    return last_string
test_inputs = [1,2,3,4,5,6,7,8,9,15,16,18,19,21]
expected = ["1!","2!","Fizz!","4!","Buzz!","Fizz!","7!","8!","Fizz!","FizzBuzz!","16!","Fizz!","19!","Fizz!"]
all_correct = True
for i in range(len(expected)):
    if fizzString2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)