def makeAbba(a,b):
    final_string = a + b + b + a
    return final_string
test_inputs = ["Hi","Yo","What","aaa","x","x","","Bo","Ya"]
other_test_inputs = ["Bye","Alice","Up","bbb","y","","y","Ya","Ya"]
expected = ["HiByeByeHi","YoAliceAliceYo","WhatUpUpWhat","aaabbbbbbaaa", "xyyx","xx", "yy","BoYaYaBo","YaYaYaYa"]
all_correct = True
for i in range(len(expected)):
    if makeAbba(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)