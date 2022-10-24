def delDel(a):
    if a[1:4] == "del":
        a = a[0] + a[4:len(a)]
        return a
    else:
        return a
test_inputs = ["adelbc","adelHello","adedbc","abcdel","add","ad","a","","del","adel","aadelbb"]
expected = ["abc","aHello","adedbc","abcdel","add","ad","a","","del","a","aadelbb"]
all_correct = True
for i in range(len(expected)):
    if delDel(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(delDel(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)