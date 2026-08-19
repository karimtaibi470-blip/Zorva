from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.core.window import Window
import math

class ZorvaGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.03, 0.05, 0.08, 1)
        self.player_x = 200
        self.player_y = 200
        self.joy_cx = 110
        self.joy_cy = 110
        self.joy_dx = 0
        self.joy_dy = 0
        self.joy_active = False
        Clock.schedule_interval(self.update, 1/60)

    def on_touch_down(self, touch):
        self.joy_active = True
        self.joy_cx = touch.x
        self.joy_cy = touch.y
        return True

    def on_touch_move(self, touch):
        if self.joy_active:
            dx = touch.x - self.joy_cx
            dy = touch.y - self.joy_cy
            d = (dx*dx+dy*dy)**0.5
            if d > 70:
                ang = math.atan2(dy, dx)
                dx = math.cos(ang)*70
                dy = math.sin(ang)*70
                d = 70
            self.joy_dx = dx/70 if d>10 else 0
            self.joy_dy = dy/70 if d>10 else 0

    def on_touch_up(self, touch):
        self.joy_active = False
        self.joy_dx = 0
        self.joy_dy = 0

    def update(self, dt):
        if self.joy_dx or self.joy_dy:
            self.player_x += self.joy_dx * 300 * dt
            self.player_y += self.joy_dy * 300 * dt
        self.canvas.clear()
        with self.canvas:
            Color(0,0.8,1,1)
            Ellipse(pos=(self.player_x-10, self.player_y-10), size=(20,20))
            Color(0.2,0.2,0.3,0.5)
            Line(circle=(self.joy_cx, self.joy_cy, 70), width=2)
            Color(0,0.8,1,0.8)
            Ellipse(pos=(self.joy_cx+self.joy_dx*50-18, self.joy_cy+self.joy_dy*50-18), size=(36,36))

class ZorvaApp(App):
    def build(self):
        return ZorvaGame()
ZorvaApp().run()
