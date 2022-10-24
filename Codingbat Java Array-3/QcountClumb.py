def countClumb(a):
    i = 0
    count_clumb = 0
    while i < len(a) - 1:
        if i == 0 and a[i] == a[i+1]:
            count_clumb += 1
            i += 1            
        if a[i] == a[i+1] and a[i-1] != a[i]:
            count_clumb += 1
            i += 1
        else: 
            i += 1
    return count_clumb
test_inputs = [[1, 2, 2, 3, 4, 4],[1, 1, 2, 1, 1],[1, 1, 1, 1, 1],[1, 2, 3],[2, 2, 1, 1, 1, 2, 1, 1, 2, 2],[0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2],[0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2],[0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2],[]]
expected = [2,2,1,0,4,4,5,5,0]
all_correct = True
for i in range(len(expected)):
    if countClumb(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
        