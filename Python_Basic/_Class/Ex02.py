# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
# 상속
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

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

valkyrie = AirborneAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

vulture = AttackUnit("벌쳐", 80,10,20)
battlecruiser = AirborneAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("3시")
battlecruiser.move("9시")


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass    # 아무것도 안 하고 일단 넘어가라
                # 미완성이지만 완성된 것처럼(에러가 안 나도록)

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")