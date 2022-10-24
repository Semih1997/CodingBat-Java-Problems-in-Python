def start1(a,b):
    count = 0
    if len(a) > 0 or len(b) > 0:
        if 1 in a:
            count += 1
        if 1 in b:
            count += 1
    return count
test_inputs = [[1, 2, 3],[7, 2, 3],[1, 2],[],[7],[7],[1],[7],[],[1, 3]]
other_test_inputs = [[1, 3],[1],[],[1, 2],[],[1],[1],[8],[],[1]]
expected = [2,1,1,1,0,1,2,0,0,2]
all_correct = True
for i in range(len(expected)):
    if start1(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)