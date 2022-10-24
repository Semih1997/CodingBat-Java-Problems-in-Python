def sum13(a):
    i = 0
    sum_13 = 0
    while i < len(a):
        if a[i] == 13:
            i += 2
        else:
            sum_13 += a[i]
            i += 1
    return sum_13
test_inputs = [[1, 2, 2, 1],[1, 1],[1, 2, 2, 1, 13],[1, 2, 13, 2, 1, 13],[13, 1, 2, 13, 2, 1, 13],[],[13],[13,13],[13, 0, 13],[13, 0, 13],[5, 7, 2]]
expected = [6,2,6,4,3,0,0,0,0,0,14]
all_correct = True
for i in range(len(expected)):
    if sum13(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)