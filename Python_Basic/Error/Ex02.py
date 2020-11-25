class BigNumberError(Exception): # customized error(programmer-created error)
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("1st integer: "))
    num2 = int(input("2nd integer: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2)) # calls customized error
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("Wrong input. 1 digit integers only.")
except BigNumberError as err:
    print("에러발생! 1 digit only")
    print(err)
finally: # called no matter what(unerroneous or erroneous)
    print("이용해주셔서 감사합니다.")