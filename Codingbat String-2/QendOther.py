def endOther(a,b):
    controlling = False
    if len(a) < len(b) and b[-len(a):].upper() == a.upper():
        controlling = True
    elif len(b) <= len(a) and a[-len(b):].upper() == b.upper():
        controlling = True
    return controlling
test_inputs = ["Hiabc","AbC","abc","Hiabc","Hiabc","Hiabcx","abc","xyz","yz","Z","12","abcXYZ","ab","ab"]   #14
other_test_inputs = ["abc","HiaBc", "abXabc", "abcd", "bc", "bc", "abc", "12xyz", "12xz", "12xz", "12", "abcDEF", "ab12", "12ab"]
expected = [True,True,True,False,True,False,True,True,False,True,True,False,False,True]
all_correct = True
for i in range(len(expected)):
    if endOther(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],endOther(test_inputs[i],other_test_inputs[i]),i)
        all_correct = False
print("All Correct: ", all_correct)