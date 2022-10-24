def copyEndy(a,b):
    i = 0
    last_array = []
    array_lenght = 0
    while array_lenght < b:
        if a[i] in range(0,11) or a[i] in range(90,101):
            last_array.append(a[i])
            i += 1
            array_lenght += 1
        else:
            i += 1
    return last_array
test_inputs = [[9, 11, 90, 22, 6],[9, 11, 90, 22, 6],[12, 1, 1, 13, 0, 20],[12, 1, 1, 13, 0, 20],[0],[10, 11, 90],[90, 22, 100],[12, 11, 10, 89, 101, 4]]
other_test_inputs = [2,3,2,3,1,2,2,1]
expected = [[9, 90],[9, 90, 6],[1, 1],[1, 1, 0],[0],[10, 90],[90, 100],[10]]
all_correct = True
for i in range(len(expected)):
    if copyEndy(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)