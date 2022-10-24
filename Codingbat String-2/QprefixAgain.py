def prefixAgain(a,b):
    correction = (a[:b] in a[b:]) * True + (not(a[:b] in a[b:])) * False
    return correction
test_inputs = ["abXYabc","abXYabc","abXYabc","xyzxyxyxy","xyzxyxyxy","Hi12345Hi6789Hi10","Hi12345Hi6789Hi10","Hi12345Hi6789Hi10","Hi12345Hi6789Hi10","a","aa","ab"]
other_test_inputs = [1,2,3,2,3,1,2,3,4,1,1,1]
expected = [True,True,False,True,False,True,True,True,False,False,True,False]
all_correct = True
for i in range(len(expected)):
    if prefixAgain(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)