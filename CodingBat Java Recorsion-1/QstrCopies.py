def strCopies(str, sub, n):
    if len(str) < len(sub):
        return n == 0
    elif str[:len(sub)] == sub:
        return strCopies(str[1:], sub, n-1)
    else:
        return strCopies(str[1:], sub, n)
test_inputs = []
other_test_inputs = []
other_test_inputs_1 = []
expected = []
all_correct = True
for i in range(len(expected)):
    if strCopies(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
    
"""
#jAVA:
public boolean strCopies(String str, String sub, int n) {
  if(str.length() < sub.length()){
    return (n == 0);
  }else if(sub.equals(str.substring(0,sub.length()))){
    return strCopies(str.substring(1), sub, n-1);
  }else{
    return strCopies(str.substring(1), sub, n);
  }
}
"""