def array667(a):
    if len(a) < 3:
        return 0
    elif len(a) > 2:
        count = 0
        for x in range(len(a)-1):
            if a[x] == 6 and (a[x+1] == 6 or a[x+1] == 7):
                count += 1
    return count
test_inputs = [[6, 6, 2],[6, 6, 2, 6],[6, 7, 2, 6],[6, 6, 2, 6, 7],[1, 6, 3],[6, 1],[],[3, 6, 7, 6],[3, 6, 6, 7],[6, 3, 6, 6],[6, 7, 6, 6],[1, 2, 3, 5, 6],[1, 2, 3, 6, 6]]
expected = [1,1,1,2,0,0,0,1,2,1,2,0,1]
all_correct = True
for i in range(len(expected)):
    if array667(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)