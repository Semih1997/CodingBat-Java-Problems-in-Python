def scoresAverage(a):
    first_sum = 0
    second_sum = 0
    divider = 0
    for i in range(len(a)//2):
        first_sum += a[i]
        second_sum += a[i+(len(a)//2)]
        divider += 1
    average_first = first_sum / divider
    average_second = second_sum / divider
    if average_first > average_second:
        return average_first
    else:
        return average_second
test_inputs = [[2, 2, 4, 4],[4, 4, 4, 2, 2, 2],[3, 4, 5, 1, 2, 3],[5, 6],[5, 4],[5, 4, 5, 6, 2, 1, 2, 3]]
expected = [4,4,4,6,5,5]
all_correct = True
for i in range(len(expected)):
    if scoresAverage(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)