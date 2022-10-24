def mixString(a,b):
    mix_string = ""
    common_len = min(len(a),len(b))
    for x in range(common_len):
        mix_string += a[x] + b[x]
    if len(a) < len(b):
        mix_string += b[common_len:]
    else:
        mix_string += a[common_len:]
    return mix_string
test_inputs = ["abc","Hi","xxxx","So","xxx","2/","","Abc","","Long"]
other_test_inputs = ["xyz","There","There","Long","X","27 around","Hello","","","So"]
expected = ["axbycz","HTihere","xTxhxexre","SLoong","xXxx","22/7 around","Hello","Abc","","LSoong"]
all_correct = True
for i in range(len(expected)):
    if mixString(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)