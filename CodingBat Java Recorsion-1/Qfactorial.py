def factorial(a):
    factorial_num = 1
    if a <= 0:
        factorial_num = 1
    else:
        while a != 1:
            factorial_num *= a
            a -= 1
    return factorial_num
test_inputs = [1,2,3,4,5,6,7,8,12,-5]
expected = [1,2,6,24,120,720,5040,40320,479001600,1]
all_correct = True
for i in range(len(expected)):
    if factorial(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)