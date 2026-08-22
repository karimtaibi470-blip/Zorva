from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.15, 1)

class ZorvaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)

        title = Label(
            text='[b]ZORVA[/b]\n\nتطبيقك الأول نجح! 🔥',
            markup=True,
            font_size='28sp',
            halign='center'
        )

        btn = Button(
            text='اضغط هنا',
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1),
            font_size='20sp'
        )
        btn.bind(on_press=lambda x: setattr(title, 'text', '[b]مبروك يا كريم! 🎉\nالـ APK خرج![/b]'))

        layout.add_widget(title)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    ZorvaApp().run()
