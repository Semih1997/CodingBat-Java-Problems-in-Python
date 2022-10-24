def sum67(a):
    sum_control = True
    sum_67 = 0
    i = 0
    while i  < len(a):
        if a[i] == 6:
            sum_control = False
            i += 1
            continue
        elif a[i] == 7 and sum_control == False:
            sum_control = True
            i += 1
            continue
        elif a[i] == 7 and sum_control == True:
            sum_67 += 7
            i += 1
            continue        
        if sum_control == True:
            sum_67 += a[i]
            i += 1
        else:
            i += 1
    return sum_67
test_inputs = [[1, 1, 6, 7, 2],[1, 6, 2, 2, 7, 1, 6, 99, 99, 7],[1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7],[2, 7, 6, 2, 6, 7, 2, 7],[2, 7, 6, 2, 6, 2, 7],[1, 6, 7, 7],[6, 7, 1, 6, 7, 7],[6, 8, 1, 6, 7],[],[6, 7, 11],[11, 6, 7, 11],[2, 2, 6, 7, 7]]
expected = [4,2,2,18,9,8,8,0,0,11,22,11]
all_correct = True
for i in range(len(expected)):
    if sum67(test_inputs[i]) != expected[i]:
        print(test_inputs[i],sum67(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)