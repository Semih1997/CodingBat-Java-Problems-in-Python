def last2(a):
    if len(a) < 3 :
        return 0
    else:
        last_2 = a[len(a)-2:len(a)]
        repeat_count = 0
        for x in range(len(a)-2):
            findings = a[x:x+2]
            if findings == last_2:
                repeat_count += 1
        return repeat_count
test_inputs = ["hixxhi","xaxxaxaxx","axxxaaxx","xxaxxaxxaxx","xaxaxaxx","xxxx","13121312","11212","13121311","1717171","hi","h",""]
expected = [1,1,2,3,0,2,1,1,0,2,0,0,0]
all_correct = True
for i in range(len(expected)):
    if last2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)