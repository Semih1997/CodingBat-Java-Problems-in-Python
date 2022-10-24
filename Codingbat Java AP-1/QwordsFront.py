def wordsFront(a,b):
    fronter = []
    for i in range(b):
        fronter.append(a[i])
    return fronter
test_inputs = [["a", "b", "c", "d"],["a", "b", "c", "d"],["a", "b", "c", "d"],["a", "b", "c", "d"],["Hi", "There"],["Hi", "There"]]
other_test_inputs = [1,2,3,4,1,2]
expected = [["a"],["a", "b"],["a", "b", "c"],["a", "b", "c", "d"],["Hi"],["Hi", "There"]]
all_correct = True
for i in range(len(expected)):
    if wordsFront(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)