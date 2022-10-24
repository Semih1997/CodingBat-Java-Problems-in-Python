def middleWay(a,b):
    new_array = [a[(len(a)//2)],b[(len(b)//2)]]
    return new_array
test_inputs = [[1, 2, 3],[7, 7, 7],[5, 2, 9],[1, 9, 7],[1, 2, 3],[1, 2, 3]]
other_test_inputs = [[4, 5, 6], [3, 8, 0], [1, 4, 5], [4, 8, 8], [3, 1, 4], [4, 1, 1]]
expected = [[2, 5], [7, 8],[2, 4],[9, 8],[2, 1],[2, 1]]
all_correct = True
for i in range(len(expected)):
    if middleWay(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(middleWay(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)