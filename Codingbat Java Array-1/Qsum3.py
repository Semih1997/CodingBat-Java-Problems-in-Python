def sum3(a):
    sum_3 = sum(a)
    return sum_3
test_inputs = [[1, 2, 3],[5, 11, 2],[7, 0, 0],[1, 2, 1],[1, 1, 1],[2,7,2]]
expected = [6,18,7,4,3,11]
all_correct = True
for i in range(len(expected)):
    if sum3(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)