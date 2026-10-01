from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# Попытка импортировать инструменты Android для управления физической вспышкой
try:
    from plyer import flashlight
except:
    flashlight = None

class FlashlightApp(App):
    def build(self):
        # Главный контейнер
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Устанавливаем начальный белый фон экрана
        with self.layout.canvas.before:
            self.bg_color = Color(1, 1, 1, 1) # Белый
            self.rect = Rectangle(size=Window.size, pos=self.layout.pos)
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Кнопка включения/выключения физической вспышки
        self.flash_active = False
        self.btn_flash = Button(
            text="Включить вспышку (Вкл/Выкл)", 
            font_size='18sp',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.btn_flash.bind(on_press=self.toggle_physical_flash)
        self.layout.add_widget(self.btn_flash)

        # Палитра цветов для изменения фона экрана (эффект цветного фонарика)
        colors = {
            "Красный": (1, 0, 0, 1),
            "Зеленый": (0, 1, 0, 1),
            "Синий": (0, 0, 1, 1),
            "Фиолетовый": (0.5, 0, 0.5, 1),
            "Желтый": (1, 1, 0, 1),
            "Белый": (1, 1, 1, 1)
        }

        # Создаем кнопки для каждого цвета
        for color_name, rgba in colors.items():
            btn = Button(text=color_name, font_size='16sp')
            # Используем lambda, чтобы передать конкретный цвет в функцию
            btn.bind(on_press=lambda instance, c=rgba: self.change_screen_color(c))
            self.layout.add_widget(btn)

        return self.layout

    def _update_rect(self, instance, value):
        """Обновляет размер фонового прямоугольника при изменении экрана"""
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def change_screen_color(self, rgba):
        """Меняет цвет подложки экрана и выкручивает яркость (имитация фонаря)"""
        self.bg_color.rgba = rgba

    def toggle_physical_flash(self, instance):
        """Управляет настоящей вспышкой телефона, если доступно"""
        if flashlight:
            try:
                if not self.flash_active:
                    flashlight.on()
                    self.flash_active = True
                    self.btn_flash.text = "Физическая вспышка: РАБОТАЕТ"
                else:
                    flashlight.off()
                    self.flash_active = False
                    self.btn_flash.text = "Включить вспышку (Вкл/Выкл)"
            except Exception as e:
                self.btn_flash.text = "Ошибка вспышки на этом устройстве"

if __name__ == '__main__':
    FlashlightApp().run()
