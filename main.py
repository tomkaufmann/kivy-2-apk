import kivymd

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):

    def flip(self):
        self.converted.text = ""
        self.label.text = ""
        self.input.text = ""
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.hint_text = "enter a decimal number"
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.hint_text = "enter a binary number"

    def convert(self, args):
        try:
            if "." not in self.input.text:
                if self.state == 0:
                    val = str(int(self.input.text,2))
                    self.label.text = "in decimal is:"
                else:
                    val = bin(int(self.input.text))[2:]
                    self.label.text = "in binary is:"
                self.converted.text = val
            else:
                whole, fract = self.input.text.split(".")
                if self.state == 0:
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit)*2**(-(idx+1))
                    self.label.text = "in decimal is:"
                    self.converted.text = str(whole + floating)
                else:
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0."+fract)
                    floating = []
                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append("0")
                            fract *= 2
                        elif fract*2 > 1:
                            floating.append("1")
                            fract = fract*2 - 1
                        elif fract*2 == 1.0:
                            floating.append("1")
                            break
                    self.label.text = "in binary is:"
                    self.converted.text = whole + "." + "".join(floating)
        except ValueError:
            self.converted.text = ""
            if self.state == 0:
                self.label.text = "please enter a valid binary number"
            else:
                self.label.text = "please enter a valid decimal number"

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)
        self.input = MDTextField(size_hint = (0.8,1),pos_hint = {"center_x": 0.5, "center_y":0.5},on_text_validate = self.convert)
        self.input.hint_text ="enter a binary number"
        screen.add_widget(self.input)
        self.label = MDLabel(halign="center",pos_hint = {"center_x": 0.5, "center_y":0.35},theme_text_color = "Secondary")
        self.converted = MDLabel(halign="center",pos_hint = {"center_x": 0.5, "center_y":0.3},theme_text_color = "Primary",font_style = "H5")
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        screen.add_widget(MDFillRoundFlatButton(text="    CONVERT    ",font_size = 25,pos_hint = {"center_x": 0.5, "center_y":0.15},on_press = self.convert))
        return screen

if __name__ == '__main__':
    ConverterApp().run()
