def stringTimes(a,b):
    a = a * b
    return a
test_inputs = ["Hi","Hi","Hi","Hi","Hi","Oh Boy!","x","","code","code"]
other_test_inputs = [2,3,1,0,5,2,4,4,2,3]
expected = ["HiHi","HiHiHi","Hi","","HiHiHiHiHi","Oh Boy!Oh Boy!","xxxx","","codecode","codecodecode"]
all_correct = True
for i in range(len(expected)):
    if stringTimes(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)