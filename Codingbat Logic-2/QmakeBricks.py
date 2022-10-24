def makeBricks(a,b,c):                # a = count of 1 inch////b = count of 5 inch////c = brick goal
    goal_brick = ((c // 5 <= b) and (c % 5 <= a)) + (c // 5 > b) and (c - (5 * b) <= a)
    return goal_brick
test_inputs = [3,3,3,3,3,6,6,1,0,1,3,1,2,7,7,7,43,40,40,40,40,22,0,1000000,20,2,20,20,20]
other_test_inputs = [1,1,2,2,2,1,0,4,3,4,1,1,1,1,1,1,1,1,2,2,2,2,2,1000,0,1000000,0,4,4]
other_test_inputs_1 = [8,9,10,8,9,11,11,11,10,12,7,7,7,11,8,13,46,46,47,50,52,33,10,1000100,19,100003,21,51,39]
expected = [True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if makeBricks(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i,makeBricks(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]))
        all_correct = False
print("All Correct:", all_correct)