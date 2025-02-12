from PyQt6.QtWidgets import QFileDialog


def import_image():
    options = QFileDialog.Option.DontUseNativeDialog
    file, _ = QFileDialog.getOpenFileName(None, "Выберите изображение", "",
                                          "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)

