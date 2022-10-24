def withoutEnd(a):
    a = a[1:len(a)-1] # len = 2 olan "ab" stringini boş olarak çıkartabildi. Tam doğru seçenek bu olmayabilir ama ulaştırdı.
    return a
test_inputs = ["Hello","java","coding","code","ab","Chocolate!","kitten","woohoo"]
expected = ["ell","av","odin","od","","hocolate","itte","ooho"]
all_correct = True
for i in range(len(expected)):
    if withoutEnd(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)