def fizzArray3(a,b):
    list_last = []
    if b > a:
        for i in range(a,b):
            list_last.append(i)
    return list_last
test_inputs = [5,11,1,18,18]
other_test_inputs = [10,18,3,18,11]
expected = [[5, 6, 7, 8, 9],[11, 12, 13, 14, 15, 16, 17],[1, 2],[],[]]
all_correct = True
for i in range(len(expected)):
    if fizzArray3(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)