from kivy.uix.effectwidget import Rectangle
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDColorPicker
from kivy.graphics import Color,Rectangle
from kivy.core.window import Window

 
Window.fullscreen = True 

class ColorPickerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("style.kv")
    
    def on_start(self):
        self.picker = MDColorPicker( size_hint=(0.45, 0.65))
        self.picker.auto_dismiss = False
        self.picker.bind(on_select_color = self.on_select_color )
        self.picker.open()

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_select_color(self,instance_gradient_tab,color):
        picker_text = self.root.ids.picker_text
        picker_box = self.root.ids.picker_box
        picker_box.bind(pos=self.update_rect, size=self.update_rect)
        opacity = self.picker._opacity_value_selected_color
        selected_color = color[:-1]
        selected_color.append(opacity)
        selected_color = [round(col,1) for col in selected_color ]
        picker_text.text = ",".join(str(x) for x in selected_color)
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(picker_text.text)

        with picker_box.canvas.before:
            picker_box.canvas.before.clear()
            Color(*selected_color)
            Rectangle(pos=picker_box.pos,size=picker_box.size)

    def close_app(self):
        if hasattr(self, "picker"):
            self.picker.dismiss()
        self.stop()


ColorPickerApp().run()
    