def fibonacci(a):
    if a <= 1:
        return a
    return fibonacci(a-1) + fibonacci(a-2)
test_inputs = [0,1,2,3,4,5,6,7]
expected = [0,1,1,2,3,5,8,13]
all_correct = True
for i in range(len(expected)):
    if fibonacci(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)