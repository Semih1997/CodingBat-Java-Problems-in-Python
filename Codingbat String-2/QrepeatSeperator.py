def repeatSeperator(a,b,c):
    final_string = ""
    for x in range(c):
        final_string += a + b
    final_string = final_string[:len(final_string) - len(b)]
    return final_string
test_inputs = ["Word","This","This","Hi","AAA","AAA","A","abc","abc","abc","XYZ"]
other_test_inputs = ["X","And","And","-n-","","","B","XX","XX","XX","a"]
other_test_inputs_1 = [3,2,1,2,1,0,5,3,2,1,2]
expected = ["WordXWordXWord","ThisAndThis","This","Hi-n-Hi","AAA","","ABABABABA","abcXXabcXXabc","abcXXabc","abc","XYZaXYZ"]
all_correct = True
for i in range(len(expected)):
    if repeatSeperator(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)