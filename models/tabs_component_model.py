import inspect
from models.base_component_model import BaseComponentModel


class TabsComponentModel(BaseComponentModel):
    def __init__(self):
        self._tab_images_map = {}  # Приватный атрибут

    @property
    def tab_images_map(self):
        return self._tab_images_map

    @tab_images_map.setter
    def tab_images_map(self, value):
        # Выводим значение и точку программы
        print(f"Установлено новое значение tab_images_map: {value}")
        print("Вызов из:")
        # Получаем текущий стек вызовов
        for frame in inspect.stack()[1:]:
            print(f"  Файл: {frame.filename}, Строка: {frame.lineno}, Функция: {frame.function}")

        self._tab_images_map = value