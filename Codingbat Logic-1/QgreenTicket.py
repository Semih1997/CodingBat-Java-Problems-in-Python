def greenTicket(a,b,c):
    ticket_result = (a == b and b == c) * 20 + (a == b and b != c) * 10 + (a != c and b == c) * 10 + (a == c and a != b) * 10 + (a != b and a != c and b != c) * 0
    return ticket_result
test_inputs = [1,2,1,2,1,3,0,2,0,0,9,9]
other_test_inputs = [2,2,1,1,2,2,0,0,9,10,9,0]
other_test_inputs_1 = [3,2,2,1,1,1,0,0,10,0,9,9]
expected = [0,20,10,10,10,0,20,10,0,10,20,10]
all_correct = True
for i in range(len(expected)):
    if greenTicket(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i,greenTicket(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]))
        all_correct = False
print("All Correct: ", all_correct)