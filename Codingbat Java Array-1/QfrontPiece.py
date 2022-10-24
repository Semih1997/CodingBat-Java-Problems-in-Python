def frontPiece(a):
    last_shit = []
    if len(a) < 2:
        last_shit = a
    else:
        last_shit = a[:2]
    return last_shit
test_inputs = [[1, 2, 3],[1, 2],[1],[],[6, 5, 0],[6, 5],[3, 1, 4, 1, 5],[6]]
expected = [[1, 2],[1, 2],[1],[],[6,5],[6,5],[3,1],[6]]
all_correct = True
for i in range(len(expected)):
    if frontPiece(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)