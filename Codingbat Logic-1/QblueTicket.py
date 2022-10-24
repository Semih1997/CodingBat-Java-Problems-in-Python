def blueTicket(a,b,c):
    result = 0
    if a + b == 10 or b + c == 10 or a + c == 10:
        result = 10 
    elif (a + b - 10 == b + c) or (a + b - 10 == a + c):
        result = 5
    return result
test_inputs = [9,9,6,6,10,15,5,4,13,8,8,8]
other_test_inputs = [1,2,1,1,0,0,15,11,2,4,4,4]
other_test_inputs_1 = [0,0,4,5,0,5,5,1,3,3,2,1]
expected = [10,0,10,0,10,5,10,5,5,0,10,0]
all_correct = True
for i in range(len(expected)):
    if blueTicket(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i,blueTicket(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]),expected[i])
        all_correct = False
print("All Correct: ", all_correct)