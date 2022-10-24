def squareUp(a):
    last_list = []
    minus = a - 1
    b = a - 1
    for k in range(a):
        j = 0
        for i in range(a):
            if k == 0:
                last_list.append(a - minus + j)
                j += 1
            else:
                if j > b:
                    last_list.append(0)
                elif j < b:
                    last_list.append(a - minus + j)
                    j += 1
                elif j == b:
                    last_list.append(0)
                    b -= 1
    last_list.reverse()
    return last_list
test_inputs = [3,2,4]
expected = [[0, 0, 1, 0, 2, 1, 3, 2, 1],[0, 1, 2, 1],[0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]]
all_correct = True
for i in range(len(expected)):
    if squareUp(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)