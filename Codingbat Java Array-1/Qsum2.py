def sum2(a):
    if len(a) < 2:
        sum_2 = sum(a)
    else:
        sum_2 = sum(a[:2])
    return sum_2
test_inputs = [[1, 2, 3],[1, 1],[1, 1, 1, 1],[1, 2],[1],[],[4, 5, 6],[4]]
expected = [3,2,2,3,1,0,9,4]
all_correct = True
for i in range(len(expected)):
    if sum2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)