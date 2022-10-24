def midThree(a):
    if len(a) % 2 != 0:
        a = a[len(a)//2-1:len(a)//2+2]
    return a 
test_inputs = [[1, 2, 3, 4, 5],[8, 6, 7, 5, 3, 0, 9],[1, 2, 3]]
expected = [[2, 3, 4],[7, 5, 3],[1, 2, 3]]
all_correct = True
for i in range(len(expected)):
    if midThree(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)