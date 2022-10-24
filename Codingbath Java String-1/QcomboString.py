def comboString(a,b):
    if len(a) <  len(b):
        final_string = a + b + a
    elif len(b) < len(a):
        final_string = b + a + b
    return final_string
test_inputs = ["Hello","hi","aaa","b","aaa","","aaa","aaa","a","bb","xyz",]
other_test_inputs = ["hi","Hello","b","aaa","","bb","1234","bb","bb","a","ab"]
expected = ["hiHellohi","hiHellohi", "baaab","baaab","aaa","bb","aaa1234aaa","bbaaabb","abba","abba","abxyzab"]
all_correct = True
for i in range(len(expected)):
    if comboString(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)