def matchUp(a,b):
    counter_match = 0
    for x in range(len(a)):
        if len(a[x]) > 0 and len(b[x]) > 0:
            if a[x][0] == b[x][0]:
                counter_match += 1
    return counter_match
test_inputs = [["aa", "bb", "cc"],["aa", "bb", "cc"],["aa", "bb", "cc"],["", "", "ccc"]]
other_test_inputs = [["aaa", "xx", "bb"],["aaa", "b", "bb"],["", "", "ccc"],["aa", "bb", "cc"]]
expected = [1,2,1,1]
all_correct = True
for i in range(len(expected)):
    if matchUp(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)