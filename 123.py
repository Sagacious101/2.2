import os


class Humanoid:
    def __init__(
        self,
        name="существо",
        hp=20,
        max_hp=20,
        race="human",
        basic_damage=5,
        money=0,
        equiped_weapon=None,
        inventory=[]
    ):
        self.name = name
        self.hp = hp
        self.race = race
        self.basic_damage = basic_damage
        if equiped_weapon:
            self.damage = (basic_damage + equiped_weapon.damage)
        else:
            self.damage = basic_damage
        self.equiped_weapon = equiped_weapon
        self.money = money
        self.inventory = inventory

    def back_up_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Инвентарь:")
        if self.inventory:
            for num, i in enumerate(self.inventory):
                if isinstance(i, Item):
                    print(f'{num}.{i.name}')
            print("")
        else:
            print("Пусто\n")
        input("Нажмите ENTER чтобы продолжить: ")

    def show_humanoid(self):
        if self.equiped_weapon:
            self.damage = (self.basic_damage + self.equiped_weapon.damage)
        print('Характеристики:')
        print(f'Имя: {self.name}')
        print(f'Раса: {self.race}')
        print(f'HP: {self.hp}')
        print(f'Монеты: {self.money}')
        if self.equiped_weapon:
            print(
                f'Урон: {self.damage}'
                f'({self.basic_damage} + {self.equiped_weapon.damage})'
            )
            print(
                'Оружие: '
                f'{self.equiped_weapon.name}(+{self.equiped_weapon.damage})'
            )
        else:
            print(f'Урон: {self.damage}({self.basic_damage} + 0)')
            print("Оружие: нету")
        print('')
        input("Нажмите ENTER чтобы продолжить: ")

    def equip_weapon(self):
        self.show_inventory()
        idx = input("Введите номер оружия которые хотите экипировать: ")
        if idx.isdigit():
            idx = int(idx) - 1
        else:
            print("Ошибка! Ввод должен быть целым неотрицательным числом.")
            input("Нажмите ENTER чтобы продолжить: ")
            return main_menu(hero)
        if idx < len(self.inventory):
            if isinstance(self.inventory[idx], Weapon):
                if self.equiped_weapon:
                    self.inventory.append(self.equiped_weapon)
                self.equiped_weapon = self.inventory[idx]
                self.inventory.pop(idx)
            else:
                print("Ошибка! Это не оружие.")
                input("Нажмите ENTER чтобы продолжить: ")
                return main_menu(hero)
        else:
            print("Ошибка! Такого предмета нет в инвентаре.")
            input("Нажмите ENTER чтобы продолжить: ")
            return main_menu(hero)


class Item:
    def __init__(self, name=None):
        self.name = name


class Weapon(Item):
    def __init__(self, name=None, damage=0):
        super().__init__()
        self.name = name
        self.damage = damage


def main_menu(player):
    os.system("cls")
    options = [
        ["Сражаться", lambda: start_fight(hero, enemy)],
        ["Посмотреть характеристики персонажа", lambda: hero.show_humanoid()],
        ["Посмотреть инвентарь", lambda: hero.show_inventory()],
        ["Экипировать оружие", lambda: hero.equip_weapon()]
    ]
    show_option(options)
    option = choose_option(options)
    if option == 0:
        pass


def start_fight(hero: Humanoid, enemy: Humanoid) -> None:
    text = "Выберите действие:\n"
    while hero.hp > 0 and enemy.hp > 0:
        os.system("cls")
        hero.show_humanoid()
        enemy.show_humanoid()
        print(text)
        options = [
            ["Атаковать противника", lambda: combat_turn(hero, enemy)]
        ]
        show_option(options)
        choose_option(options)
        combat_turn(enemy, hero)
        input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)


def combat_turn(attacker: Humanoid, defender: Humanoid) -> None:
    if attacker.damage > 0:
        damage = (attacker.damage)
        defender.hp -= damage
        print(f'{attacker.name} атаковал {defender.name} на {damage}!')


def combat_result(hero: Humanoid, enemy: Humanoid) -> None:
    os.system("cls")
    if hero.hp > 0 and enemy.hp <= 0:
        print(f'{hero.name} победил {enemy.name} и в награду получает:')
        hero.money += enemy.money
        print(f'{enemy.money} монет')
        input("Нажмите ENTER чтобы продолжить: ")
        return main_menu(hero)
    else:
        print("Вы умерли")


def show_option(options: list) -> None:
    for num, option in enumerate(options, 1):
        print(f"{num}. {option[0]}")


def choose_option(options: list) -> int:
    user_option = input("\nВведите номер варианта и нажмите ENTER: ")
    if not user_option.isdigit():
        print(
            "Ошибка! Введены некоректные данные. "
            "Ввод должен соответсвовать номеру варианта"
        )
        input("Нажмите ENTER чтобы продолжить: ")
        return main_menu(hero)
    idx = int(user_option) - 1
    if idx >= len(options):
        print(
            "Ошибка! Введены некоректные данные. "
            "Ввод должен соответсвовать номеру варианта"
        )
        input("Нажмите ENTER чтобы продолжить: ")
        return main_menu(hero)
    options[idx][1]()


sword_1 = Weapon(name='Ржавый меч', damage=10)
hero = Humanoid(name='Вася', money=15, inventory=[sword_1])
enemy = Humanoid(name='бандит', basic_damage=1)
while True:
    main_menu(hero)