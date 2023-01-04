from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window

from my_redis import RedisPool
from config import FONT_SIZE


class Main(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=2, rows=3)
        self.pool = RedisPool()

    def build(self):
        Clock.schedule_interval(self._update, 1)
        return self._interface()

    def _interface(self):
        self.layout.add_widget(Label(text='BTC/USDT', font_size=FONT_SIZE))
        self.layout.add_widget(Label(text='0.0', font_size=FONT_SIZE))
        self.layout.add_widget(Label(text='ETH/USDT', font_size=FONT_SIZE))
        self.layout.add_widget(Label(text='1.0', font_size=FONT_SIZE))
        self.layout.add_widget(Label(text='BNB/USDT', font_size=FONT_SIZE))
        self.layout.add_widget(Label(text='2.0', font_size=FONT_SIZE))
        return self.layout

    def _update(self, *args):
        new_btc_price = self.pool.get_price(key='btcusdt')
        new_eth_price = self.pool.get_price(key='ethusdt')
        new_bnb_price = self.pool.get_price(key='bnbusdt')

        # btc
        self.layout.children[4].color = self._set_color(
            old=float(self.layout.children[4].text),
            new=float(new_btc_price)
        )
        self.layout.children[4].text = str(new_btc_price)

        # eth
        self.layout.children[2].color = self._set_color(
            old=float(self.layout.children[2].text),
            new=float(new_eth_price)
        )
        self.layout.children[2].text = str(new_eth_price)

        # bnb
        self.layout.children[0].color = self._set_color(
            old=float(self.layout.children[0].text),
            new=float(new_bnb_price)
        )
        self.layout.children[0].text = str(new_bnb_price)

    @staticmethod
    def _set_color(old: float, new: float) -> tuple:
        green = 0, 1, 0, 1
        red = 1, 0, 0, 1
        white = 1, 1, 1, 1

        if new > old:
            return green
        elif old > new:
            return red
        else:
            return white


if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    Config.set('graphics', 'width', '420')
    Config.set('graphics', 'height', '300')
    Config.write()
    Window.clearcolor = (25 / 255, 26 / 255, 28 / 255)
    Main().run()


