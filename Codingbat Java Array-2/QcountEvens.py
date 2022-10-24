def countEvens(a):
    i = 0
    count_evens = 0
    while i < len(a):
        if a[i] % 2 == 0:
            count_evens += 1
            i += 1
        else:
            i += 1
    return count_evens
test_inputs = [[2, 1, 2, 3, 4],[2, 2, 0],[1, 3, 5],[],[11, 9, 0, 1],[2, 11, 9, 0],[2],[2, 5, 12]]
expected = [3,3,0,0,1,2,1,2]
all_correct = True
for i in range(len(expected)):
    if countEvens(test_inputs[i]) != expected[i]:
        print(test_inputs[i],countEvens(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)