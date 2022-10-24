def array220(a,b):
    if b == len(a) - 1 or len(a) == 0:
        return False
    if a[b] * 10 == a[b+1]:
        return True
    else:
        return array220(a,b+1)
test_inputs = [[1, 2, 20],[3, 30],[3],[],[3, 3, 30, 4],[2, 19, 4],[20, 2, 21],[20, 2, 21, 210],[2, 200, 2000],[0,0],[1, 2, 3, 4, 4, 50, 500, 6],[1, 2, 3, 4, 5, 51, 6]]
other_test_inputs = [0,0,0,0,0,0,0,0,0,0,0,0]
expected = [True,True,False,False,True,False,False,True,True,True,True,False]
all_correct = True
for i in range(len(expected)):
    if array220(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)