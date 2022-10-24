def scoreUp(a,b):
    total_score = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            total_score += 4
        elif b[i] == "?":
            total_score += 0
        elif a[i] != b[i]:
            total_score -= 1
    return total_score
test_inputs = [["a", "a", "b", "b"],["a", "a", "b", "b"],["a", "a", "b", "b"],["a", "a", "b", "b"],["a", "a", "b", "b"]]
other_test_inputs = [["a", "c", "b", "c"],["a", "a", "b", "c"],["a", "a", "b", "b"],["?", "c", "b", "?"],["c", "?", "b", "?"]]
expected = [6,11,16,3,3]
all_correct = True
for i in range(len(expected)):
    if scoreUp(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)