def repeat_Front(a,b):
    b_downer = b
    last_string = ""
    for x in range(b):
        last_string += a[:b_downer]
        b_downer -= 1
    return last_string
test_inputs = ["Chocolate","Chocolate","Ice Cream","Ice Cream","Ice Cream","","xyz","Java","Java"]
other_test_inputs = [4,3,2,1,0,0,3,4,1]
expected = [ "ChocChoChC","ChoChC","IcI","I","","","xyzxyx","JavaJavJaJ","J"]
all_correct = True
for i in range(len(expected)):
    if repeat_Front(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)