def fizzArray(a):
    last_array = []
    for i in range(a):
        last_array.append(i)
    return last_array
test_inputs = [0,1,2,3,4,5,6,11]
expected = [[],[0],[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4],[0,1,2,3,4,5],[0,1,2,3,4,5,6,7,8,9,10]]
all_correct = True
for i in range(len(expected)):
    if fizzArray(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)