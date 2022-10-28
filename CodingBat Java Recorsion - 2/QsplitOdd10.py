def splitOdd10(arr):
    sum1 = 0
    sum2 = 0
    def helper(sum1, sum2, arr):
        if len(arr) == 0:
            return sum1 % 10 == 0 and  sum2 % 2 == 1
        elif helper(sum1 + arr[0], sum2, arr[1:]):
            return True
        elif helper(sum1, sum2 + arr[0], arr[1:]):
            return True
        else:
            return False
    return helper(sum1,sum2,arr)
test_inputs = [[5,5,5],[5, 5, 6],[5, 5, 6, 1],[6, 5, 5, 1],[6, 5, 5, 1, 10],[6, 5, 5, 5, 1],[1],[],[10, 7, 5, 5],[10, 0, 5, 5]]
expected = [True,False,True,True,True,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if splitOdd10(test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)