class Enemy:
    life =3

    def attack(self):
        print('ouch')
        self.life-= 1

    def checklife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " Life Left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.checklife()
enemy1.attack()
enemy2.checklife()
