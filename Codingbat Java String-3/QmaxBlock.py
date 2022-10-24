def maxBlock(a):
    i = 0
    count_same_letter = 1
    count_same_letter_list = []
    if len(a) < 1:
        count_same_letter_list.append(0)
    else:
        count_same_letter_list.append(1)
    while i < len(a)-1:
        if a[i] == a[i+1]:
            count_same_letter += 1
            i += 1
            count_same_letter_list.append(count_same_letter)
        else:
            count_same_letter = 1
            i += 1
    count_same_letter_list.sort()
    return count_same_letter_list[-1]
test_inputs = ["hoopla","abbCCCddBBBxx","","xyz","xxyz","xyzz","abbbcbbbxbbbx","XXBBBbbxx","XXBBBBbbxx","XXBBBbbxxXXXX","XX2222BBBbbXX2222"]
expected = [2,3,0,1,2,2,3,3,4,4,4]
all_correct = True
for i in range(len(expected)):
    if maxBlock(test_inputs[i]) != expected[i]:
        print(test_inputs[i],maxBlock(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)