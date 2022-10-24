def fizzString(a):
    last_string = a
    if a[0] == "f":
        last_string = "Fizz"
    if a[len(a)-1] == "b":
        last_string = "Buzz"
    if a[0] == "f" and a[len(a)-1] == "b":
        last_string = "FizzBuzz"
    return last_string
test_inputs = ["fig","dib","fib","abc","fooo","booo","ooob","b","f"]
expected = ["Fizz","Buzz","FizzBuzz","abc","Fizz","booo","Buzz","Buzz","Fizz"]
all_correct = True
for i in range(len(expected)):
    if fizzString(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)