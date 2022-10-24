def maxTriple(a):
    mid_value = a[len(a)//2]
    last_value = a[len(a)-1]
    first_value = a[0]
    out_num = 0
    if mid_value > last_value and mid_value > first_value:
        out_num = mid_value
    if last_value > mid_value and last_value > first_value:
        out_num = last_value
    if first_value > last_value and first_value > mid_value:
        out_num = first_value
    return out_num
test_inputs = [[1, 2, 3],[1, 5, 3],[5, 2, 3],[1, 2, 3, 1, 1],[1, 7, 3, 1, 5],[5, 1, 3, 7, 1],[5, 1, 7, 3, 7, 8, 1],[5, 1, 7, 9, 7, 8, 1],[5, 1, 7, 3, 7, 8, 9],[2, 2, 5, 1, 1]]
expected = [3,5,5,3,5,5,5,9,9,5]
all_correct = True
for i in range(len(expected)):
    if maxTriple(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(maxTriple(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)