def array11(a,b):
    if b == len(a):
        return 0
    if a[b] == 11:
        return 1 + array11(a,b+1)
    else:
        return array11(a,b+1)

def array11(a):
    if len(a) == 0:
        return 0
    return int(a[0] == 11) + array11(a[1:])

    """
        return array11([1, 11, 3, 11, 11])
        return (0 + array11([11, 3, 11, 11]))
        return (0 + 1 + array11([3, 11, 11]))
        return (0 + 1 + 0 + array11([11, 11]))
        return (0 + 1 + 0 + 1 + array11([11]))
        return (0 + 1 + 0 + 1 + 1 + array11([]))
        return (0 + 1 + 0 + 1 + 1 + 0)
    """

test_inputs = [[1, 2, 11],[11, 11],[1, 2, 3, 4],[1, 11, 3, 11, 11],[11],[1],[],[11, 2, 3, 4, 11, 5],[11, 5, 11]]
other_test_inputs = [0,0,0,0,0,0,0,0,0]
expected = [1,2,0,3,1,0,0,2,2]
all_correct = True
for i in range(len(expected)):
    if array11(test_inputs[i]) != expected[i]: # ,other_test_inputs[i]
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)