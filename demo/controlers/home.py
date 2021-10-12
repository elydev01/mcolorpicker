from kivy.lang import Builder
from kivy import properties as p

from kivymd.app import MDApp as App
from kivymd.uix.screen import MDScreen

from colorpicker import MaterialColorPicker


class HomeMainScreen(MDScreen):
    bg_color = p.ListProperty([1,1,1,1])
    bg_color_selected = p.ListProperty([1,1,1,1])

    def change_bg(self, color):
        self.bg_color = color
    
    def change_bg_color_selected(self, color):
        self.bg_color_selected = color

    def open_color_picker(self):
        dialog = MaterialColorPicker(
            on_colorchange=self.change_bg,
            color_selected_callback=self.change_bg_color_selected
        )
        dialog.open()


with open('views/home.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class HomeScreenApp(App):
    def build(self):
        return HomeMainScreen()


def main():
    HomeScreenApp().run()


if __name__ == '__main__':
    main()
