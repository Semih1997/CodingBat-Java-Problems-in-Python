def countXX(a):
    count_x = a.count('x') - 1
    if a.count(" ") > 0:
        count_x = count_x - a.count(" ")
    if count_x < 0:
        count_x = 0
    return count_x
test_inputs = ["abcxx","xxx","xxxx","abc","Hello there","Hexxo thxxe","","Kittens","Kittensxxx"]
expected = [1,2,3,0,0,2,0,0,2]
all_correct = True
for i in range(len(expected)):
    if countXX(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)