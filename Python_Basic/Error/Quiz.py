class SoldOutError(Exception):
    def __init__(self):
        self.msg = "재고가 소진되어 더 이상 주문을 받지 않습니다."
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨] : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("Not enough chickens")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기 번호 {0}]: {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("Wrong input!")
    except SoldOutError as err:
        print(err)
        break