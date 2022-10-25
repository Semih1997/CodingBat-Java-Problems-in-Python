def groupNoAdj(startindx,arr,target):
    if startindx >= len(arr):
        return target == 0
    elif groupNoAdj(startindx + 2, arr, target - arr[startindx]):
        return True
    elif groupNoAdj(startindx+ 1, arr, target):
        return True
    else:
        return False
test_inputs = [0,0,0,0,0,0,0,0,0,0,0,0]
other_test_inputs = [[2, 5, 10, 4],[2, 5, 10, 4],[2, 5, 10, 4],[2, 5, 10, 4, 2],[2, 5, 10, 4],[10, 2, 2, 3, 3],[10, 2, 2, 3, 3],[],[1],[9],[9],[5, 10, 4, 1]]
other_test_inputs_1 = [12,14,7,7,9,15,7,0,1,1,0,11]
expected = [True,False,False,True,True,True,False,True,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if groupNoAdj(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)