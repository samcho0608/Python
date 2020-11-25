from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 상속
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없스니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False     # I guess this is a static variable for the whole class?

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드로 해제".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# airborne units
class Airborne:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 다중 상속
class AirborneAttackUnit(AttackUnit, Airborne):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Airborne.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(AirborneAttackUnit):
    def __init__(self):
        AirborneAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloaked = False

    def cloaking(self):
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제".format(self.name))
            self.cloaked = False
        else:
            print("{0} : 클로킹 모드".format(self.name))
            self.cloaked = True

def game_start():
    print("[알림] 새로운 게임 시작")

def game_over():
    print("Player: gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


(m1, m2, m3) = (Marine(), Marine(), Marine())
(t1, t2) = (Tank(), Tank())
w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

# seize tank can now use seize mode
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine): # if unit is an object instance of the 2nd argument
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))

game_over()