import getpass


print("猜數字拉 0-100 敢不敢 傻B")
ans = int(getpass.getpass('ans:'))
max=100
min=0
if ans>100:
    print('error')
else:
    while True:
        guess=int(input("看戲喔 猜啊"))
        if guess == ans:
            print("恭喜你了!!!!")
            break
        elif guess > ans and guess < max:
            print(min, "到", guess)
            max=guess
        elif guess < ans and guess > min:
            print(guess, "到", max)  
            min=guess
        else:
            print(" 亂猜什麼東西 就說了",min,"到",max)

