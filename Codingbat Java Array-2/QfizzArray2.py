def fizzArray2(a):
    last_array = []
    for i in range(a):
        i = str(i)
        last_array.append(i)
    return last_array
test_inputs = [4,10,2,5]
expected = [["0", "1", "2", "3"],["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],["0", "1"],["0", "1", "2", "3", "4"]]
all_correct = True
for i in range(len(expected)):
    if fizzArray2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)