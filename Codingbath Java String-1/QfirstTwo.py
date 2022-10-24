def firstTwo(a):
    if len(a) < 2:
        last_string = a
    else:
        last_string = a[:2]
    return last_string
test_inputs = ["Hello","abcdefg","ab","a","","Kitten","hi","hiya"]
expected = ["He","ab","ab","a","","Ki","hi","hi"]
all_correct = True
for i in range(len(expected)):
    if firstTwo(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)