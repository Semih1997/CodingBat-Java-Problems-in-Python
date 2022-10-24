def wordsWithout(a,b):
    last_array = []
    for i in range(len(a)):
        if a[i] != b:
            last_array.append(a[i])
    return last_array
test_inputs = [["a", "b", "c", "a"],["a", "b", "c", "a"],["a", "b", "c", "a"],["xx", "yyy", "x", "yy", "x"]]
other_test_inputs = ["a","b","c","yy"]
expected = [["b", "c"],["a", "c", "a"],["a", "b", "a"],["xx", "yyy", "x", "x"]]
all_correct = True
for i in range(len(expected)):
    if wordsWithout(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
        