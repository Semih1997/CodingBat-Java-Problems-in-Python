def zeroMax(a):
    max_odd = 0                                 # tersten gelerek baktık ki zaten sonraki büyükler bizi ilgilendiriyo.
    for i in range(len(a)):
        if a[len(a)-1-i] % 2 == 1:
            max_odd = max(max_odd,a[len(a)-1-i])
        if a[len(a)-1-i] == 0:
            a[len(a)-1-i] = max_odd
    return a
test_inputs = [[0, 5, 0, 3],[0, 4, 0, 3],[0, 1, 0],[0, 1, 5],[0, 2, 0],[1],[0],[],[7, 0, 4, 3, 0, 2],[7, 0, 4, 3, 0, 1],[7, 0, 4, 3, 0, 0],[7, 0, 1, 0, 0, 7]]
expected = [[5, 5, 3, 3],[3, 4, 3, 3],[1, 1, 0],[5, 1, 5],[0, 2, 0],[1],[0],[],[7, 3, 4, 3, 0, 2],[7, 3, 4, 3, 1, 1],[7, 3, 4, 3, 0, 0],[7, 7, 1, 7, 7, 7]]
all_correct = True
for i in range(len(expected)):
    if zeroMax(test_inputs[i]) != expected[i]:
        print(test_inputs[i],zeroMax(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)