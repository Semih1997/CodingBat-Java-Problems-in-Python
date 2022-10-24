def twoTwo(a):
    twotwo_control = True
    i = 0
    a += "s"
    while i < len(a) - 1:
       if a[i] == 2:
           twotwo_control = False
           if a[i+1] == 2 or a[i-1] == 2:
               twotwo_control = True
               i += 2
           else:
               i += 1
       else:
           i += 1
    return twotwo_control
test_inputs = [[4, 2, 2, 3],[2, 2, 4],[2, 2, 4, 2],[1, 3, 4],[1, 2, 2, 3, 4],[1, 2, 3, 4],[2,2],[2, 2, 7],[2, 2, 7, 2, 1],[4, 2, 2, 2],[2, 2, 2],[1, 2],[2],[1],[],[5, 2, 2, 3],[2, 2, 5, 2]]
expected = [True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False]
all_correct = True
for i in range(len(expected)):
    if twoTwo(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct) 