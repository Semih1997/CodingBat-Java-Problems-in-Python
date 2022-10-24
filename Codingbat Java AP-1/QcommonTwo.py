def commonTwo(a,b):
    same_counter = 0
    same_list = []
    for i in range(len(b)):
        if b[i] in a and not(b[i] in same_list):
            same_counter += 1
            same_list.append(b[i])
    return same_counter
test_inputs = [["a", "c", "x"],["a", "c", "x"],["a", "b", "c"],["a", "a", "b", "b", "c"],["a"]]
other_test_inputs = [["b", "c", "d", "x"],["a", "b", "c", "x", "z"],["a", "b", "c"],["b", "b", "b", "x"],["b"]]
expected = [2,3,3,1,0]
all_correct = True
for i in range(len(expected)):
    if commonTwo(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)