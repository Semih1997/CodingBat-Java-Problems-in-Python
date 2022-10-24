def teaParty(a,b):
    party_point = 0
    if a >= 5 and b >= 5:
        party_point = 1
        if a >= 2 * b or b >= a * 2:
            party_point = 2
    return party_point
test_inputs = [6,3,20,12,11,11,4,5,6,5,5,10,10]
other_test_inputs = [8,8,6,6,6,4,5,5,6,10,9,4,20]
expected = [1,0,2,2,1,0,0,1,1,2,1,0,2]
all_correct = True
for i in range(len(expected)):
    if teaParty(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)