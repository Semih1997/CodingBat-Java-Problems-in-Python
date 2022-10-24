def array6(a,b):
    if a[b] == 6:
        return True
    if b == len(a)-1:
        return False
    else:
        return array6(a,b+1)
    
def array6(a):
    return (not len(a) == 0) and (a[0] == 6 or array6(a[1:]))
    """
    if len(a) == 0: return False
    elif a[0] == 6: return True
    return array6(a[1:])
    """

test_inputs = [[1, 6, 4],[1, 4],[6],[1],[6, 2, 2],[2, 5],[1, 9, 4, 6, 6],[2, 5, 6]]
other_test_inputs = [0,0,0,0,0,0,0,0]
expected = [True,False,True,False,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if array6(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)