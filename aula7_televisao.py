class  Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


    def aumenta_canal(self):
        if self.ligada:
           self.canal +=1

    def diminui_canal(self):
        if self.ligada:
           self.canal -=1

    def aumenta_volume(self):
        if self.ligada:
            self.volume += 1

    def diminui_volume(self):
        if self.ligada:
            self.volume -= 5

if __name__ == '__main__':

    televiasao = Televisao()
    print("televisão está ligada = {}".format(televiasao.ligada))
    televiasao.power()
    print("televisão está ligada = {}".format(televiasao.ligada))
    televiasao.power()
    print("televisão está ligada = {}".format(televiasao.ligada))
    print('canal :{}'.format(televiasao.canal))
    televiasao.power()
    print("televisão está ligada = {}".format(televiasao.ligada))
    televiasao.aumenta_canal()
    print("canal :{}".format(televiasao.canal))
    televiasao.diminui_canal()
    print("canal :{}".format(televiasao.volume))
    print("volume aumentado :{}" .format(televiasao.volume))
    televiasao.aumenta_volume()
    televiasao.aumenta_volume()
    print("volume aumentado :{}" .format(televiasao.volume))









