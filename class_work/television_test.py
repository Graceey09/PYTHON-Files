import unittest
from television import TV


class test_TV(unittest.TestCase):

    def test_tv_can_turn_on(self):
        self.star = TV()
        self.star.turn_on()
        self.assertTrue(self.star.on)

    def test_tv_can_turn_off(self):
        self.star = TV()
        self.star.turn_on()
        self.star.turn_off()
        self.assertFalse(self.star.on)

    def test_get_channel(self):
        self.star = TV()
        self.star.turn_on()
        self.star.get_channel()
        self.assertEqual(self.star.get_channel(), 0)

    def test_set_channel(self):
        self.star = TV()
        self.star.turn_on()
        self.star.set_channel(50)
        self.assertEqual(self.star.get_channel(), 50)

    def test_set_volume(self):
        self.star = TV()
        self.star.turn_on()
        self.star.get_volume()
        self.assertEquals(self.star.get_volume(), 0)

    def test_get_volume(self):
        self.star = TV()
        self.star.turn_on()
        self.star.get_volume()
        self.assertEquals(self.star.get_volume(), 0)

    def test_channel_up(self):
        self.star = TV()
        self.star.turn_on()
        self.star.set_channel(10)
        self.star.channel_up()
        newcheck = self.star.get_channel()
        self.assertEqual(11, newcheck)

    def test_channel_down(self):
        self.star = TV()
        self.star.turn_on()
        self.star.set_channel(10)
        self.star.channel_down()
        newcheck = self.star.get_channel()
        self.assertEqual(9, newcheck)

    def test_volume_up(self):
        self.star = TV()
        self.star.turn_on()
        self.star.set_volume(50)
        self.star.volume_up()
        newcheck = self.star.get_volume()
        self.assertEqual(51, newcheck)

    def test_volume_down(self):
        self.star = TV()
        self.star.turn_on()
        self.star.set_volume(90)
        self.star.volume_down()
        newcheck = self.star.get_volume()
        self.assertEqual(89, newcheck)
