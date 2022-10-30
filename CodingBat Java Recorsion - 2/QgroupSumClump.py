# groupSumClump in Python
def groupSumClump(start, arr, target):
    if start >= len(arr):
        return (target == 0)
    def helper(arr):
        counter1 = 0
        for i in range(len(arr)):
            if arr[start] == arr[i]:
                counter1 += 1
        return counter1 
    if groupSumClump(start + 1, arr, target - (arr[start]*helper(arr))):
        return True
    elif groupSumClump(start + 1, arr, target):
        return True
    else:
        return False
test_inputs = [0,0,0,0,0,0,0]
other_test_inputs = [[2, 4, 8],[1, 2, 4, 8, 1, 1, 1],[2, 4, 4, 4, 8],[8, 2, 2, 1],[8, 2, 2, 1],[1],[9]]
other_test_inputs_1 = [10,16,18,9,11,1,1]
expected = [True,True,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if groupSumClump(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)
