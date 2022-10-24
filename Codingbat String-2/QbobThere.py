def bobThere(a):
    correction = False
    for x in range(len(a)-2):
        if a[x] == "b" and a[x+2] == "b":
            correction = True
    return correction
test_inputs = ["abcbob","b9b","bac","bbb","abcdefb","123abcbcdbabxyz","b12","b1b","b12b1b","bbc","bbb","bb","b"]
expected = [True,True,False,True,False,True,False,True,True,False,True,False,False]
all_correct = True
for i in range(len(expected)):
    if bobThere(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)