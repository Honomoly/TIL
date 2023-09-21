class Television:
    def __init__(self):
        self.channel = 9
        self.volume = 10
        self.on = True

    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

    def set_on(self, on):
        self.on = on
    
    def show_tv_info(self):
        print('채널 : ', self.channel)
        print('볼륨 : ', self.volume)
        print('전원 ON : ', self.on)
        print()

tv1 = Television()
tv1.show_tv_info()

tv1.set_channel(11)
tv1.set_volume(15)
tv1.show_tv_info()