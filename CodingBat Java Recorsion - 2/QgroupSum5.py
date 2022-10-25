def groupSum5(startindx, arr, target):
    def helper(startindx, arr):
        if startindx == 0:
            return True
        elif arr[startindx - 1] % 5 == 0 and arr[startindx] == 1:
            return False
        else:
            return True
    if startindx >= len(arr):
        return target == 0
    elif groupSum5(startindx + 1, arr, target - arr[startindx]) and helper(startindx, arr):
        return True
    elif groupSum5(startindx + 1, arr, target) and arr[startindx] % 5 != 0:
        return True
    else:
        return False
test_inputs = [0,0,0,0,0,0,0,0]
other_test_inputs = [[2, 5, 10, 4],[2, 5, 10, 4],[2, 5, 10, 4],[2, 5, 4, 10],[3, 5, 1],[3, 5, 1],[1, 3, 5],[3, 5, 1]]
other_test_inputs_1 = [19,17,12,12,4,5,5,9]
expected = [True,True,False,False,False,True,True,False]
all_correct = True
for i in range(len(expected)):
    if groupSum5(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)