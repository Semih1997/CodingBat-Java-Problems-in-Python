def alarmClock(a,b):
    alarm_time = "10:00"
    if b == True:
        if a == 0 or a == 6:
            alarm_time = "off"
    else:
        if a < 6 and a > 0:
            alarm_time = "7:00"
    return alarm_time
test_inputs = [1,5,0,6,0,6,1,3,5]
other_test_inputs = [False,False,False,False,True,True,True,True,True]
expected = ["7:00","7:00","10:00","10:00","off","off","10:00","10:00","10:00"]
all_correct = True
for i in range(len(expected)):
    if alarmClock(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)