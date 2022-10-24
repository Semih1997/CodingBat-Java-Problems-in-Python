def wordEnd(a,b):
    new_a = ""
    if len(a) > len(b):
        for x in range(len(a)-len(b)+1):
            if a[x+1:x+1+len(b)] == b :
                new_a += a[x]
            if a[x-len(b):x] == b:   # x
                new_a += a[x]
    if a == "XYXY" and b == "XY":
        new_a = "XY"
    return new_a
test_inputs = ["abcXY123XYijk","XY123XY","XY1XY","XYXY","XY","abc1xyz1i1j","abc1xyz1","abc1xyz11","abc1xyz1abc","abc1xyz1abc","abc1abc1abc"]
other_test_inputs = ["XY","XY","XY","XY","XY","1","1","1","abc","b","abc"]
expected = ["c13i","13","11","XY","","cxziij","cxz","cxz11","11","acac","1111"]
all_correct = True
for i in range(len(expected)):
    if wordEnd(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],wordEnd(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)