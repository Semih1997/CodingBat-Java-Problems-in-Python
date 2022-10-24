def firstHalf(a):
    if len(a) < 2:
        last_string = a
    else:
        last_string = a[:len(a)//2]
    return last_string
test_inputs = ["WooHoo","HelloThere","abcdef","ab","","0123456789","kitten"]
expected = ["Woo","Hello","abc", "a","", "01234","kit"]
all_correct = True
for i in range(len(expected)):
    if firstHalf(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)