def countCode(a):
    count_code = 0
    for x in range(len(a)-3):
        if a[x:x+2] == "co" and a[x+3] == "e":
            count_code += 1
    return count_code
test_inputs = ["aaacodebbb","codexxcode","cozexxcope","cozfxxcope","xxcozeyycop","cozcop","abcxyz","code","ode","c","","AAcodeBBcoleCCccoreDD","AAcodeBBcoleCCccorfDD","coAcodeBcoleccoreDD"]
expected = [1,2,2,1,1,0,0,1,0,0,0,3,2,3]
all_correct = True
for i in range(len(expected)):
    if countCode(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)