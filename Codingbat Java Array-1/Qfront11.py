def front11(a,b):
    if len(a) > 0 and len(b) > 0:
        last_array = [a[0],b[0]]
    elif len(a) == 0 and len(b) > 0:
        last_array = [b[0]]
    elif len(b) == 0 and len(a) > 0:
        last_array = [a[0]]
    else:
        last_array = []
    return last_array
test_inputs = [[1, 2, 3],[1],[1, 7],[],[],[3],[1, 4, 1, 9]]
other_test_inputs = [[7, 9, 8],[2],[],[2, 8],[],[1, 4, 1, 9],[]]
expected = [[1, 7],[1, 2],[1],[2],[],[3, 1],[1]]
all_correct = True
for i in range(len(expected)):
    if front11(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
    