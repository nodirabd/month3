import flet as ft

def main_page(page: ft.Page):
    page.title = "counting numbers of press button"
    
    count = 0
    text_pressed = ft.Text("Pressed: 0 times", size=20) 

    def button_clicked(e):
        nonlocal count
        count += 1
        text_pressed.value = f"Pressed: {count} times"
        page.update()

    # Увеличиваем через width и height
    butttn = ft.ElevatedButton(
        "Press me", 
        on_click=button_clicked,
        width=200,   # Ширина в пикселях
        height=100,  # Высота в пикселях
    )

    page.add(butttn, text_pressed)

ft.app(target=main_page)
