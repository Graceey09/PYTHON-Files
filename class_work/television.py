class TV:
    def __init__(self):
        self.channel = 0
        self.volume_level = 0
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel

    def channel_up(self):
        if self.on:
            if self.channel < 100:
                self.channel += 1

    def channel_down(self):
        if self.on:
            if self.channel > 0:
                self.channel -= 1

    def channel(self, channel):
        self.channel = channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        self.volume_level = volume_level

    def volume_up(self):
        if self.on:
            self.volume_level += 1

    def volume_down(self):
        if self.on:
            self.volume_level -= 1
