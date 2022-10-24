def makeChocolate(a,b,c):     # a = count of 1 kilo /// b = count of 5 kilos /// c = goal's of kilos
    small_bar_left = 0
    if c // 5 > b:
        small_bar_left = c - b * 5 
    elif c / 5 == b:
        small_bar_left = 0
    elif c // 5 <= b:
        small_bar_left = c - (c // 5) * 5
    if small_bar_left > a:
        small_bar_left = -1
    return small_bar_left
test_inputs = [4,4,4,6,4,4,5,9,3,1,1,1,6,6,6,6,6,6,6,60,1000,7,7,7]
other_test_inputs = [1,1,1,2,1,1,4,3,1,2,2,2,1,1,1,1,2,2,2,100,1000000,1,1,2]
other_test_inputs_1 = [9,10,7,7,5,4,9,18,9,7,6,5,10,11,12,13,10,11,12,550,5000006,12,13,13]
expected = [4,-1,2,2,0,4,4,3,-1,-1,1,0,5,6,-1,-1,0,1,2,50,6,7,-1,3]
all_correct = True
for i in range(len(expected)):
    if makeChocolate(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i,makeChocolate(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]))
        all_correct = False
print("All Correct: ", all_correct)