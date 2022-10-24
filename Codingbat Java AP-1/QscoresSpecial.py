def scoresSpecial(a,b):
    large_a = 0
    large_b = 0
    a.sort()
    b.sort()
    if len(a) > 0:
        for i in range(len(a)):
            if a[i] % 10 == 0:
                large_a = a[i]
    if len(b) > 0:
        for i in range(len(b)):
            if b[i] % 10 == 0:
                large_b = b[i]
    return (large_a + large_b)
test_inputs = [[12, 10, 4],[20, 10, 4],[12, 11, 4],[10, 4, 20, 30],[3, 4, 5],[],[]]
other_test_inputs = [[2, 20, 30],[2, 20, 10],[2, 20, 31],[20],[1, 50, 2, 20],[20],[2]]
expected = [40,40,20,50,50,20,0]
all_correct = True
for i in range(len(expected)):
    if scoresSpecial(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)