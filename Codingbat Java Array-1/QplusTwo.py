def plusTwo(a,b):
    a_b = []
    for x in a:
        a_b.append(x)
    for y in b:
        a_b.append(y)
    return a_b
test_inputs = [[1, 2],[4, 4],[9, 2],]
other_test_inputs = [[3, 4],[2, 2],[3, 4]]
expected = [[1, 2, 3, 4],[4, 4, 2, 2],[9, 2, 3, 4]]
all_correct = True
for i in range(len(expected)):
    if plusTwo(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)