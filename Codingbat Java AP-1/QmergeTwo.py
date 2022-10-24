def mergeTwo(a,b,c):
    merged_list = []
    for i in range(len(a)):
        merged_list.append(a[i])
    for i in range(len(b)):
        if not(b[i] in merged_list):
            merged_list.append(b[i])
    if len(merged_list) >= c:
        merged_list.sort()
        merged_list = merged_list[:c]
    return merged_list
test_inputs = [["a", "c", "z"],["a", "c", "z"],["f", "g", "z"],["x", "y", "z"],["a", "c", "z"]]
other_test_inputs = [["b", "f", "z"],["c", "f", "z"],["c", "f", "g"],["a", "b", "z"],["a", "c", "z"]]
other_test_inputs_1 = [3,3,3,3,2]
expected = [["a", "b", "c"],["a", "c", "f"],["c", "f", "g"],["a", "b", "x"],["a", "c"]]
all_correct = True
for i in range(len(expected)):
    if mergeTwo(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],mergeTwo(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]))
        all_correct = False
print("All Correct: ", all_correct)