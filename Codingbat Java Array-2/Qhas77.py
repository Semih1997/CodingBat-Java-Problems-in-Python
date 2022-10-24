def has77(a):
    control_77 = False
    a += "h" + "h"
    for i in range(len(a) - 1):
        if (a[i] == 7 and a[i+1] == 7) or (a[i] == 7 and a[i+2] == 7):
            control_77 = True
    return control_77
test_inputs = [[1, 7, 7],[1, 7, 1, 7],[1, 7, 1, 1, 7],[7, 7, 1, 1, 7],[2, 7, 2, 2, 7, 2],[2, 7, 2, 2, 7, 7],[7, 2, 7, 2, 2, 7],[7, 2, 6, 2, 2, 7],[7, 7, 7],[7, 1, 7],[7, 1, 1],[1, 2],[1, 7],[7]]
expected = [True,True,False,True,False,True,True,False,True,True,False,False,False,False]
all_correct = True
for i in range(len(expected)):
    if has77(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)