def allStar(a):
    if len(a) == 1 or len(a) == 0:
        return a
    return a[0] + "*" + allStar(a[1:])
test_inputs = ["hello","abc","ab","a","","3.14","Chocolate","1234"]
expected = ["h*e*l*l*o","a*b*c","a*b","a","","3*.*1*4","C*h*o*c*o*l*a*t*e","1*2*3*4"]
all_correct = True
for i in range(len(expected)):
    if allStar(test_inputs[i]) != expected[i]:
        print(test_inputs[i],allStar(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)