def bunnyEars(a):
    if a == 0:
        return 0
    return 2 + bunnyEars(a-1)
test_inputs = [0,1,2,3]
expected = [0,2,4,6]
all_correct = True
for i in range(len(expected)):
    if bunnyEars(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)