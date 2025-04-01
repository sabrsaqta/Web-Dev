test_ans = int(input())
stud_ans = int(input())

if test_ans == 1 and stud_ans == 1:
    print("YES")
elif test_ans == 1 and stud_ans != 1:
    print("NO")
elif test_ans != 1 and stud_ans != 1:
    print("YES")
else:
    print("NO")