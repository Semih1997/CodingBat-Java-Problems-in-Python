def stringMatch(a,b):
    equaller = min(len(a),len(b))
    count = 0
    for x in range(equaller - 1):
        if a[x:x+2] == b[x:x+2]:
            count += 1
    return count
test_inputs = ["xxcaazz","abc","abc","hello","he","h","","aabbccdd","aaxxaaxx","iaxxai"]
other_test_inputs = ["xxbaaz","abc","axc","he","hello","hello","hello","abbbxxd","iaxxai","aaxxaaxx"]
expected = [3,2,0,1,1,0,0,1,3,3]
all_correct = True
for i in range(len(expected)):
    if stringMatch(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)