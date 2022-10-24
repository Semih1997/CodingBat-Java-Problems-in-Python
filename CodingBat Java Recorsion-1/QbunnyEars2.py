def bunnyEars2(a):
    if a == 0:
        return 0
    if a % 2 == 1:
        return 2 + bunnyEars2(a-1)
    elif a % 2 == 0:
        return 3 + bunnyEars2(a-1)
test_inputs = [0,1,2,3,4,5,6,10]
expected = [0,2,5,7,10,12,15,25]
all_correct = True
for i in range(len(expected)):
    if bunnyEars2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)