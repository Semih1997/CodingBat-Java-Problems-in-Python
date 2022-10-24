def noneStart(a,b):
    final_string = a[1:] + b[1:]
    return final_string
test_inputs = ["Hello","java","shotl","ab","ab","x","a","kit","mart"]
other_test_inputs = ["There","code","java","xy","x","ac","x","kat","dart"]
expected = ["ellohere","avaode","hotlava","by","b","c","","itat","artart"]
all_correct = True
for i in range(len(expected)):
    if noneStart(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)