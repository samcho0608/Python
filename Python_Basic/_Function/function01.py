# 계좌 신설
def open_acc():
    print("계좌 신설!")

# 입금
def deposit(balance, money):
    print("입금 완료. 잔액: {0}원".format(balance + money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance < money:
        print("잔액 부족!")
        return balance
    else:
        print("출금 완료!")
        return balance - money

# 야간 출금
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 100
open_acc()
balance = deposit(balance,20)
print(balance)

balance = withdraw(balance, 50)
print(balance)
balance = withdraw(balance, 10000)
print(balance)

balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 20)
print(commission, balance)