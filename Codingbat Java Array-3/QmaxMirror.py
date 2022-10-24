def maxMirror(a):
    i = 0
    reverse_going = 1
    mirror_length = 0
    mirror_list = []
    while (i < len(a)) :
        if a[i] == a[len(a) - reverse_going]:
            mirror_length += 1
            i += 1
            reverse_going += 1
        else:
            mirror_list.append(mirror_length)
            mirror_length = 0
            i += 1
            asdasdasd
    mirror_list.sort()
    return mirror_list[len(mirror_list)-1]
test_inputs = [[1, 2, 3, 8, 9, 3, 2, 1],[1, 2, 1, 4],[7, 1, 2, 9, 7, 2, 1]]   #,[1, 2, 1, 4],[7, 1, 2, 9, 7, 2, 1]
expected = [3,3,2]   #,3,2
all_correct = True
for i in range(len(expected)):
    if maxMirror(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)