def arrayCount9(a):
    count_9 = 0
    for x in a:
        if x == 9:
            count_9 += 1
    return count_9
test_inputs = [[1, 2, 9],[1, 9, 9],[1, 9, 9, 3, 9],[1, 2, 3],[],[4, 2, 4, 3, 1],[9, 2, 4, 3, 1]]
expected = [1,2,3,0,0,0,1]
all_correct = True
for i in range(len(expected)):
    if arrayCount9(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)