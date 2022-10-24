def rotateLeft(a):
    a = [a[1],a[2],a[0]]
    return a
test_inputs = [[1, 2, 3],[5, 11, 9],[7, 0, 0],[1, 2, 1],[0, 0, 1]]
expected = [ [2, 3, 1],[11, 9, 5], [0, 0, 7], [2, 1, 1], [0, 1, 0]]
all_correct = True
for i in range(len(expected)):
    if rotateLeft(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)