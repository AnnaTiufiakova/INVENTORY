from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class InventoryApp(MDApp):
    def build(self):
        return MDLabel(text="Inventario del Bar", halign="center")


InventoryApp().run()
