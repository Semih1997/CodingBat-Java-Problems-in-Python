def redTicket(a,b,c):
    ticket = (a == b == c) * 5 + (b != a and c != a) * 1 + (b != c) * 0
    if a == b == c == 2:
        ticket = 10
    return ticket
test_inputs = [2,2,0,2,1,1,1,0,1,0,1]
other_test_inputs = [2,2,0,0,1,2,2,2,2,2,1]
other_test_inputs_1 = [2,1,0,0,1,1,0,2,2,0,2]
expected = [10,0,5,1,5,0,1,1,1,0,0]
all_correct = True
for i in range(len(expected)):
    if redTicket(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)