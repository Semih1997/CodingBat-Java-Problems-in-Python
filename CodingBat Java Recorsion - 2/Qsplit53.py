# split53 in Python
def split53(arr):
    sum1 = 0
    sum2 = 0
    def helper(sum1, sum2, arr):
        if len(arr) == 0:
            return sum1 == sum2
        elif helper(sum1 + arr[0], sum2, arr[1:]) and arr[0] % 3 != 0:
            return True
        elif helper(sum1, sum2 + arr[0], arr[1:]) and arr[0] % 5 != 0:
            return True
        else:
            return False
    return helper(sum1,sum2,arr)
test_inputs = [[1,1],[1,1,1],[2, 4, 2],[2, 2, 2, 1],[3, 3, 5, 1],[3, 5, 8],[2, 4, 6],[3, 5, 6, 10, 3, 3]]
expected = [True,False,True,False,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if split53(test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)
