class Car:
    ''' 基本的な自動車の機能を備えたクラス '''
    def __init__(self, owner):
        self.handle = 0
        self.car_type = "nomal"
        self.owner = owner

    def turn_left(self):
        ''' ハンドルを左に回す '''
    