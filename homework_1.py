import flet as ft

def main_page(page: ft.Page):
    page.title = "counting numbers of press button"
    
    count = 0

    text_pressed = ft.Text("Pressed: 0 times")
    def button_clicked():
        nonlocal count # Позволяет изменять переменную из внешней функции
        count += 1
        text_pressed.value = f"Pressed: {count} times"
        page.update() # обновляем страницу, чтобы увидеть изменения

    butttn = ft.ElevatedButton("Press me", on_click=button_clicked)
    page.add(butttn, text_pressed)

ft.app(main_page)
