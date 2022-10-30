# splitArray in Python
def splitArray(arr):
    sum1 = 0
    sum2 = 0
    def helper(sum1, sum2, arr):
        if len(arr) == 0:
            return sum1 == sum2
        elif helper(sum1 + arr[0], sum2, arr[1:]):
            return True
        elif helper(sum1, sum2 + arr[0], arr[1:]):
            return True
        else:
            return False
    return helper(sum1,sum2,arr)
test_inputs = [[2,2],[3,2],[2,3,5],[5, 2, 2],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[],[1],[3,5],[5,3,2],[2, 2, 10, 10, 1, 1],[1, 2, 2, 10, 10, 1, 1],[1, 2, 3, 10, 10, 1, 1]]
expected = [True,False,True,False,True,False,True,False,False,True,True,False,True]
all_correct = True
for i in range(len(expected)):
    if splitArray(test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)
