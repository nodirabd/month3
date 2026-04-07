import flet as ft

def main_page(page: ft.Page):
    page.title = 'Homework 3'
    text_age = ft.Text('Please type your age', color=ft.Colors.BLUE)
    age_input = ft.TextField(label='How old are you?')

    def age_color(e):
        if age_input.value.isdigit():
            age = int(age_input.value)
            if age >= 18:
                text_age.value = "Dostup razreshen"
                text_age.color = ft.Colors.GREEN
            else:
                text_age.value = "Dostup zapreshen"
                text_age.color = ft.Colors.RED
        else:
            text_age.value = "Vvedite korrektnyy vozrast"
            text_age.color = ft.Colors.YELLOW
        
        page.update()

    check_button = ft.ElevatedButton("Check Age", on_click=age_color)

    page.add(text_age, age_input, check_button)

ft.app(target=main_page)