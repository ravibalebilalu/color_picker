from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDColorPicker

class ColorPickerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("style.kv")
    
    def on_start(self):
        self.picker = MDColorPicker( size_hint=(0.45, 0.65))
         
        self.picker.bind(on_select_color = self.on_select_color )
        self.picker.open()
        

    def on_select_color(self,instance_gradient_tab,color):
        picker_text = self.root.ids.picker_text
        selected_color = [round(col,1) for col in color]
        result = ""
        for col in selected_color:
            result += str(col) + ","
        picker_text.text = result[:-1]

   

ColorPickerApp().run()
    