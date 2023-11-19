# hp = 100
# def take_damage():
#     global hp
#     print("Игрок получил урон!")
#     hp -= 10
#     print()
#
#
#
#
# hp = 20
# def take_damage(damage):
#     global hp
#     hp -= damage
#     print("Осталось "+str(hp)+"хп.")
#
#
# def count_damage(damage_type):
#     if damage_type == "kripper":
#         damage = 10
#     elif damage_type == "lava":
#         damage = 5
#     return damage
#
# x=(input("Введите урон:"))
# damage=count_damage(x)
# take_damage(damage)
a = int(input("Введите число "))
def test(a):
    for i in range(1,a+1,1):
        print(i)
test(a)