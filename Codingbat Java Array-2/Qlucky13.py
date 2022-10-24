def lucky13(a):
    luck_control = True
    if 1 in a or 3 in a:
        luck_control = False
    return luck_control
test_inputs = [[0, 2, 4],[1, 2, 3],[1, 2, 4],[2, 7, 2, 8],[2, 7, 1, 8],[3, 7, 2, 8],[2, 7, 2, 1],[1, 2],[2, 2],[2],[3],[]]
expected = [True,False,False,True,False,False,False,False,True,True,False,True]
all_correct = True
for i in range(len(expected)):
    if lucky13(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)