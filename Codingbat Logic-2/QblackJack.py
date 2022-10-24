def blackJack(a,b):
    winner = 0
    if a < 22 and b < 22:
        if abs(a-21) < abs(b-21):
            winner = a
        elif abs(b-21) < abs(a-21):
            winner = b
    elif a < 22:
        winner = a
    elif b < 22:
        winner = b
    return winner
test_inputs = [19,21,19,22,22,22,33,1,34,17,18,16,3,3,21]
other_test_inputs = [21,19,22,19,50,22,1,2,33,19,17,23,4,2,20]
expected = [21,21,19,19,0,0,1,2,0,19,18,16,4,3,21]
all_correct = True
for i in range(len(expected)):
    if blackJack(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],i,blackJack(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)