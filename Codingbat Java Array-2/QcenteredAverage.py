def centeredAverage(a):
    a.sort()
    a = a[1:len(a)-1]
    i = 0
    divide_counter = 1
    sum_steps = 0
    while i < len(a):
        sum_steps += a[i]
        i += 1
        if i > 1:
            divide_counter += 1
    sum_steps = sum_steps // divide_counter
    return sum_steps
test_inputs = [[1, 2, 3, 4, 100],[1, 1, 5, 5, 10, 8, 7],[-10, -4, -2, -4, -2, 0],[5, 3, 4, 6, 2],[5, 3, 4, 0, 100],[100, 0, 5, 3, 4],[4, 0, 100],[0, 2, 3, 4, 100],[1, 1, 100],[7, 7, 7],[1, 7, 8],[1, 1, 99, 99],[6, 4, 8, 12, 3]]
expected = [3,5,-3,4,4,4,4,3,1,7,7,50,6]
all_correct = True
for i in range(len(expected)):
    if centeredAverage(test_inputs[i]) != expected[i]:
        print(test_inputs[i],centeredAverage(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)