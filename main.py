import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    # Устанавливаем начальную тему
    page.theme_mode = ft.ThemeMode.LIGHT

    # Функция для смены темы
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_btn.icon = ft.Icons.BRIGHTNESS_7  # Иконка солнца для темной темы
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_btn.icon = ft.Icons.BRIGHTNESS_4  # Иконка луны для светлой темы
        page.update()
    # Объявляем элементы заранее, чтобы функции их видели
    text_hello = ft.Text('Hello', color=ft.Colors.RED)
    text_input = ft.TextField(label='Введите свое имя')

    def text_name(e):
        name = text_input.value.strip()
        if name:
            text_hello.value = f"Hello, {name}!"
            text_hello.color = ft.Colors.GREEN
        else:
            text_hello.value = "Введи имя быстрее пожалуйста плиз!!!" 
            text_hello.color = ft.Colors.RED_900
        page.update()

    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)
    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()
    theme_btn = ft.IconButton( icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    # Добавляем все на страницу
    page.add(theme_btn,text_hello, text_input, btn,)

ft.app(main_page)


