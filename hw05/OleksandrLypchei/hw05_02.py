finish_num = int(input("Enter num: "))

one_before_last_fibo_num = 0
last_fibo_num = 1

while one_before_last_fibo_num <= finish_num:
    print(one_before_last_fibo_num, end="; ")
    one_before_last_fibo_num, last_fibo_num = last_fibo_num, one_before_last_fibo_num + last_fibo_num
else:
    print()
