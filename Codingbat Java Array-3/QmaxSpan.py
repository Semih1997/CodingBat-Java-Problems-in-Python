def maxSpan(a):
    all_length = []
    if len(a) < 1:
        all_length.append(0)
    else:
        for i in range(len(a)):
            choosen = a[i]
            choosen_indexes = []
            for x in range(len(a)):
                if a[x] == choosen:
                    choosen_indexes.append(x+1)
            lengts = choosen_indexes[len(choosen_indexes)-1] - i
            all_length.append(lengts)
        all_length.sort()
    return all_length[len(all_length)-1]
test_inputs = [[1, 2, 1, 1, 3],[1, 4, 2, 1, 4, 1, 4],[1, 4, 2, 1, 4, 4, 4],[3, 3, 3],[3, 9, 3],[3, 9, 9],[3, 9],[3, 3],[],[1]]
expected = [4,6,6,3,3,2,1,2,0,1]
all_correct = True
for i in range(len(expected)):
    if maxSpan(test_inputs[i]) != expected[i]:
        print(test_inputs[i],maxSpan(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)