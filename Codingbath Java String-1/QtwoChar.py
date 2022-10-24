def twoChar(a,b):
    if b < 0 :
        a = a[:2]
    elif b < len(a)-1:
        a = a[b:b+2]
    else:
        a = a[:2]
    return a
test_inputs = ["java","java","java","java","java","Hello","Hello","Hello","Hello","Hello","Hello","Hello","Hello","Hello","yay",]
other_test_inputs = [0,2,3,4,-1,0,1,99,3,4,5,-7,6,-1,0]
expected = ["ja","va","ja","ja","ja","He","el","He","lo","He","He","He","He","He","ya"]
all_correct = True
for i in range(len(expected)):
    if twoChar(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)