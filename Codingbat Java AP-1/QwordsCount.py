def wordsCount(a,b):
    equality_counter = 0
    for i in range(len(a)):
        if len(a[i]) == b:
            equality_counter += 1
    return equality_counter
test_inputs = [["a", "bb", "b", "ccc"],["a", "bb", "b", "ccc"],["a", "bb", "b", "ccc"],["xx", "yyy", "x", "yy", "z"],["xx", "yyy", "x", "yy", "z"],["xx", "yyy", "x", "yy", "z"]]
other_test_inputs = [1,3,4,1,2,3]
expected = [2,1,0,2,2,1]
all_correct = True
for i in range(len(expected)):
    if wordsCount(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)