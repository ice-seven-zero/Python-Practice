class gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹了...")

        else:
            self.bullet_count -= 3
            print("%s 发射三颗子弹，剩余[%d]颗" % (self.model, self.bullet_count))


class soldier:
    def __init__(self, name, gun=None):  # 缺省参数，灵活给枪
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
        else:
            print("冲啊...[%s]" % self.name)
            self.gun.add_bullet(50)
            self.gun.shoot()


if __name__ == '__main__':
    ak47 = gun('ak47')
    man1 = soldier("许三多")
    man2 = soldier("王老五")
    man2.gun = ak47
    man1.fire()
    man2.fire()
