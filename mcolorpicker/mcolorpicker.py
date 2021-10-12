import json, os

from kivy.lang import Builder
from kivy import properties as p
from kivy.utils import get_hex_from_color, get_color_from_hex
from kivy.uix.behaviors import ButtonBehavior

from kivymd.uix.picker import BaseDialogPicker
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    FakeCircularElevationBehavior
)


def get_absolut_path() -> str:
    """
        Return current folder
    """
    workspace = os.path.dirname(__file__)
    abs_path = os.path.join(workspace, 'colors')
    return abs_path


KV = '''

<ColorItem>:
    size_hint_y: None
    height: self.width
    on_parent: self.height = self.width
    ripple_behavior: True
    radius: [dp((self.width * .2))]
    elevation: 6
    on_release: self.parent.rt.set_button_color(self.md_bg_color)


<MaterialColorPicker>:
    colorRecycleView: colorRecycleView
    size_hint: .8, .84
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: app.root_window.height * .84 if app.root_window else dp(400)
        size_hint_min_x: dp(200)
        size_hint_max_x: dp(400)
        size_hint_max_y: dp(600)
        minimum_height: dp(400)
        MDCard:
            orientation: 'vertical'
            md_bg_color: 1,1,1,1
            padding: [dp(5), dp(5), dp(5), dp(10)]
            radius: [dp(10)]
            spacing: dp(5)
            MDTabs:
                background_color: 1,1,1,1
                indicator_color: app.theme_cls.primary_color
                text_color_normal: .8,.8,.8,1
                text_color_active: app.theme_cls.primary_dark
                tab_indicator_anim: True
                tab_hint_x: True
                Tab:
                    icon: 'ray-vertex' # drag-horizontal-variant
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDCard:
                            md_bg_color: root.palette_color
                            size_hint_y: .8
                            elevation: 8
                            # radius: [0,0, dp(15), dp(15)]
                        MDSeparator:
                            color: [.8,.8,.8,1]
                        MDBoxLayout:
                            md_bg_color: 1,1,1,1
                            orientation: 'vertical'
                            padding: [dp(5), dp(5), dp(5), dp(15)]
                            BoxLayout:
                                Label:
                                    text: str(int(red_widget.value))
                                    color: [1,.2,0]
                                    bold: True
                                    size_hint_x: None
                                    width: self.texture_size[0]
                                    padding: dp(10), dp(5)
                                MDSlider:
                                    id: red_widget
                                    min: 0
                                    max: 255
                                    color: [1,.2,0]
                                    show_off: False
                                    steep: 1
                                    value: root.red * 255
                                    on_value_normalized: root.set_r(self.value_normalized)
                            BoxLayout:
                                Label:
                                    text: str(int(green_widget.value))
                                    color: [.4,1,.2]
                                    bold: True
                                    size_hint_x: None
                                    width: self.texture_size[0]
                                    padding: dp(10), dp(5)
                                MDSlider:
                                    id: green_widget
                                    min: 0
                                    max: 255
                                    color: [.4,1,.2]
                                    show_off: False
                                    steep: 1
                                    value: root.green * 255
                                    on_value_normalized: root.set_g(self.value_normalized)
                            BoxLayout:
                                Label:
                                    text: str(int(blue_widget.value))
                                    color: [0,.4,1]
                                    bold: True
                                    size_hint_x: None
                                    width: self.texture_size[0]
                                    padding: dp(10), dp(5)
                                MDSlider:
                                    id: blue_widget
                                    min: 0
                                    max: 255
                                    color: [0,.4,1]
                                    show_off: False
                                    steep: 1
                                    value: root.blue * 255
                                    on_value_normalized: root.set_b(self.value_normalized)
                            BoxLayout:
                                spacing: dp(10)
                                padding: [dp(10), dp(10), dp(10), 0]
                                BoxLayout:
                                    spacing: dp(5)
                                    pos_hint: {'center_y': .5}
                                    Label:
                                        text: '#'
                                        color: .7,.7,.7
                                        bold: True
                                        size_hint: None, None
                                        size: self.texture_size
                                        pos_hint: {'center_y': .5}
                                        font_size: sp(21)
                                    MDTextField:
                                        id: color_hex_input
                                        text: root.string_color
                                        bold: True
                                        font_size: sp(21)
                                        cursor_width: sp(2)
                                        on_text_validate: root.set_hex_color(self.text)
                                        input_filter: root.input_filter
                                        pos_hint: {'center_y': .5}
                                MDCard:
                                    on_release: root.on_color_selected()
                                    size_hint: None, None
                                    height: dp(40)
                                    md_bg_color: .85,.85,.85,1
                                    width: dp(110)
                                    radius: [dp(8)]
                                    ripple_behavior: True
                                    pos_hint: {'center_y': .5}
                                    Label:
                                        pos_hint: {'center_y': .5}
                                        text: 'SELECT'
                                        font_size: sp(14)
                                        bold: True
                                        color: 0,0,0
                Tab:
                    icon: 'dots-grid'
                    MDBoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            RecycleView:
                                id: colorRecycleView
                                viewclass: 'ColorItem'
                                RecycleGridLayout:
                                    rt: root
                                    cols: 6
                                    padding: dp(10), dp(10)
                                    spacing: dp(5)
                                    default_size_hint: 1, None
                                    size_hint_y: None
                                    height: self.minimum_height
                                    orientation: 'lr-tb'
                        BoxLayout:
                            padding: dp(10), dp(10)
                            size_hint_y: None
                            height: self.minimum_height
                            MDCard:
                                on_release: root.on_color_selected()
                                size_hint: None, None
                                height: dp(40)
                                md_bg_color: .85,.85,.85,1
                                width: dp(110)
                                radius: [dp(8), 0, 0, dp(8)]
                                ripple_behavior: True
                                pos_hint: {'center_y': .5}
                                Label:
                                    pos_hint: {'center_y': .5}
                                    text: 'SELECT'
                                    font_size: sp(14)
                                    bold: True
                                    color: 0,0,0
                            BoxLayout:
                            MDCard:
                                size_hint: None, None
                                height: dp(40)
                                md_bg_color: root.palette_color
                                width: dp(110)
                                radius: [0, dp(8), dp(8), 0]
                                pos_hint: {'center_y': .5}
                                Label:
                                    pos_hint: {'center_y': .5}
                                    text: '# {0}'.format(root.string_color)
                                    font_size: sp(14)
                                    bold: True
                                    color: [0,0,0] if ((root.red >= .5) and (root.green >= .5) and (root.blue >= .5)) else [1,1,1]
'''


Builder.load_string(KV)


class MaterialColorPicker(BaseDialogPicker):
    
    colorRecycleView = p.ObjectProperty(None)
    
    red = p.NumericProperty(0)
    
    green = p.NumericProperty(0)
    
    blue = p.NumericProperty(0)
    
    a = p.NumericProperty(1)
    
    palette_color = p.ListProperty([1,1,1,1])
    
    string_color = p.StringProperty('FFFFFF')


    def __init__(self, *args, r=1, g=1, b=1, on_colorchange=None, color_selected_callback=None, **kwargs):
        super(MaterialColorPicker, self).__init__(*args, **kwargs)

        self.on_colorchange = on_colorchange
        self.color_selected_callback = color_selected_callback

        self.set_r(r)
        self.set_g(g)
        self.set_b(b)
    
    def on_colorRecycleView(self, *_):
        if self.colorRecycleView:
            with open(get_absolut_path()) as c:
                self.colorRecycleView.data = json.loads(c.read())

    def set_r(self, r):
        self.red = r

    def set_g(self, g):
        self.green = g

    def set_b(self, b):
        self.blue = b

    def on_red(self, *_):
        self.set_palette_color()

    def on_green(self, *_):
        self.set_palette_color()

    def on_blue(self, *_):
        self.set_palette_color()

    def set_palette_color(self):
        self.palette_color = [self.red, self.green, self.blue, self.a]

    def set_button_color(self, color):
        '''
            Apply the selected color via the buttons
        '''
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    def on_color_selected(self):
        '''
            When user selects a color
        '''
        if self.color_selected_callback:
            self.color_selected_callback(self.palette_color)
        self.dismiss()

    def on_palette_color(self, *_):
        '''
            When the color of the
            widget changes
        '''
        if self.on_colorchange:
            self.on_colorchange(self.palette_color)
        self.set_string_color(self.palette_color[:3])

    def set_string_color(self, colors):
        '''
            Conversion of color to hexadecimal
        '''
        color = get_hex_from_color(colors)
        self.string_color = color.replace('#', '').upper()
    
    def set_hex_color(self, hexcolor):
        '''
            Apply the color entered by the user
        '''
        try:
            assert len(hexcolor) == 6
            color = get_color_from_hex(('#' + hexcolor))
            assert len(color) >= 3
            self.set_r(color[0])
            self.set_g(color[1])
            self.set_b(color[2])
        except:
            pass

    def input_filter(self, char, _):
        '''
            User input control
        '''
        if len(self.ids.color_hex_input.text) == 6: return ''
        NORMAL = '0123456789abcdefABCDEF'
        return char if char in NORMAL else ''


class ColorItem(
        FakeCircularElevationBehavior,
        CircularRippleBehavior,
        ButtonBehavior,
        MDBoxLayout
    ):
    '''
        Rounded color button
    '''
    pass
