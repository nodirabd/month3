import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    greeting_text = ft.Text('История приветствия:', size=16)
    text_hello = ft.Text('Как тебя зовут?', size=20, weight=ft.FontWeight.BOLD)
    text_input = ft.TextField(label='Ваше имя', expand=True)

    def text_name(e):
        name = text_input.value.strip()
        
        if not name:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900
        elif name.isdigit():
            text_hello.value = "Имя не может состоять из цифр!"
            text_hello.color = ft.Colors.RED  
        elif len(name) < 2:
            text_hello.value = "Имя слишком короткое (мин. 2 символа)!"
            text_hello.color = ft.Colors.ORANGE_700
        elif name in greeting_history:
            text_hello.value = "Это имя уже в истории!"
            text_hello.color = ft.Colors.RED
        else:
            text_hello.value = f"Привет, {name}!"
            text_hello.color = ft.Colors.BLUE
            
            greeting_history.append(name) 
            if len(greeting_history) > 5:
                greeting_history.pop(0)     
            greeting_text.value = 'История приветствия:\n' + "\n".join(greeting_history)
            text_input.value = ""   
        page.update()

    def change_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствия:"
        page.update()

    btn_send = ft.ElevatedButton('Отправить', icon=ft.Icons.SEND, on_click=text_name)
    
    top_settings_row = ft.Row(
        controls=[
            ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=change_theme, tooltip="Сменить тему"),
            ft.IconButton(icon=ft.Icons.DELETE_SWEEP, on_click=clear_history, tooltip="Очистить историю", icon_color=ft.Colors.RED_400),
        ],
        alignment=ft.MainAxisAlignment.END 
    )

    input_row = ft.Row(
        controls=[text_input, btn_send],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(top_settings_row, text_hello, input_row, greeting_text)

ft.app(target=main_page)