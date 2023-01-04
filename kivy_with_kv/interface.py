import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

from my_redis import RedisPool


class Price(GridLayout):

    def __init__(self, **kwargs):
        self.pool = RedisPool()
        self.green = (0, 1, 0, 1)
        self.red = (1, 0, 0, 1)
        self.white = (1, 1, 1, 1)
        super().__init__(**kwargs)

    btc_price = NumericProperty(0.0)
    eth_price = NumericProperty(0.0)
    bnb_price = NumericProperty(0.0)

    def set_color(self, price: float, pair: str):
        old_price = self.pool.get_price(pair)
        if price > old_price:
            return self.green
        elif price < old_price:
            return self.red
        else:
            return self.white


class InterfaceApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pool = RedisPool()

    def update(self, *args):
        self.pool.set_price("old_btc", self.root.btc_price)
        self.pool.set_price("old_eth", self.root.eth_price)
        self.pool.set_price("old_bnb", self.root.bnb_price)

        self.root.btc_price = float(self.pool.get_price(key='btcusdt'))
        self.root.eth_price = float(self.pool.get_price(key='ethusdt'))
        self.root.bnb_price = float(self.pool.get_price(key='bnbusdt'))

    def build(self):
        Clock.schedule_interval(self.update, 1)
        Builder.load_file("ui.kv")
        return Price()


if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    Config.set('graphics', 'width', '420')
    Config.set('graphics', 'height', '300')
    Config.write()
    Window.clearcolor = (25 / 255, 26 / 255, 28 / 255)
    InterfaceApp().run()
