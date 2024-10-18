
class Starfighter(object):
    def __init__(self):
        self.weapons = []

    def addWeapon(self, weaponName):
        self.weapons.append(weaponName)
    
    def speak(self):
        for i in self.weapons:
            i.attack()


class Weapon(object):
    def __init__(self, charge):
        self.charge = charge      
    def attack(self):
        pass


class Lightsaber(Weapon):
    def __init__(self, charge):
        super().__init__(charge)
    def attack(self):
        print("Swish-swish-swish!")
        

class Blaster(Weapon):
    def __init__(self, charge):
        super().__init__(charge)
    def attack(self):
        print("Bah-bah-bah!")    

class PlasmaGun(Weapon):
    def __init__(self, charge):
        super().__init__(charge)
    def attack(self):
        print("Phew-phew-phew!")


weap = Weapon(50)
starkiller = Starfighter()
saber = Lightsaber(weap)
blaster = Blaster(weap)
gun = PlasmaGun(weap)

starkiller.addWeapon(saber)
starkiller.addWeapon(blaster)
starkiller.addWeapon(gun)

starkiller.speak()




