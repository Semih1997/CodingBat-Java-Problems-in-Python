def wordsWithoutList(a,b):
    last_list = []
    for i in range(len(a)):
        if len(a[i]) != b:
            last_list.append(a[i])
    return last_list
test_inputs = [["a", "bb", "b", "ccc"],["a", "bb", "b", "ccc"],["a", "bb", "b", "ccc"]]
other_test_inputs = [1,3,4]
expected = [["bb", "ccc"],["a", "bb", "b"],["a", "bb", "b", "ccc"]]
all_correct = True
for i in range(len(expected)):
    if wordsWithoutList(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)