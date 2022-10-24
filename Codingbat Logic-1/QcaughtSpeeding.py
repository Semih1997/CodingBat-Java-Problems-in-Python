def caughtSpeeding(a,b):
    ticket_type = 0
    if b == False:
        if a in range(61,81):
            ticket_type = 1
        elif a > 80:
            ticket_type = 2
    elif b == True:
        if a in range(66,86):
            ticket_type = 1
        elif a > 85:
            ticket_type = 2
    return ticket_type
test_inputs = [60,65,65,80,85,85,70,75,75,40,40,90]
other_test_inputs = [False,False,True,False,False,True,False,False,True,False,True,False]
expected = []
all_correct = True
for i in range(len(expected)):
    if caughtSpeeding(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)