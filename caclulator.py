import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"


    page.window.width = 350
    page.window.height = 500


    page.bgcolor = ft.colors.WHITE


    display = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=330,
        height=80,
        read_only=True,
        border_radius=10,
        text_size=30,
        filled=True,
        bgcolor=ft.colors.WHITE,
    )


    current_value = "0"
    last_value = ""
    operator = ""


    def on_click(e):
        nonlocal current_value, last_value, operator

        button_text = e.control.text


        if button_text == "C":
            current_value = "0"
            last_value = ""
            operator = ""
            display.value = current_value
            page.update()
            return


        if button_text.isdigit() or button_text == ".":
            if current_value == "0" and button_text != ".":
                current_value = button_text
            else:
                current_value += button_text
            display.value = current_value

        # Handle operators
        elif button_text in ["+", "-", "*", "/"]:
            operator = button_text
            last_value = current_value
            current_value = ""
            display.value = "0"


        elif button_text == "=":
            try:
                if operator and last_value:
                    expression = last_value + operator + current_value
                    result = eval(expression)
                    current_value = str(result)
                    display.value = current_value
            except:
                display.value = "Error"

        page.update()


    def create_button(label, color=ft.colors.LIGHT_BLUE_400, bgcolor=ft.colors.BLUE_GREY_100):
        return ft.ElevatedButton(
            text=label,
            on_click=on_click,
            width=70,
            height=70,
            style=ft.ButtonStyle(
                color=color,
                bgcolor=bgcolor,
                shape=ft.RoundedRectangleBorder(radius=10),
                elevation=2,
            )
        )


    button_rows = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"]
    ]


    operator_color = ft.colors.ORANGE_600
    equal_color = ft.colors.GREEN_600
    clear_color = ft.colors.RED_400


    rows = []
    for row in button_rows:
        button_row = ft.Row(
            controls=[
                create_button(
                    label=label,
                    color=ft.colors.WHITE if label in ["+", "-", "*", "/", "=", "C"] else ft.colors.BLACK,
                    bgcolor=equal_color if label == "=" else clear_color if label == "C" else operator_color if label in [
                        "+", "-", "*", "/"] else ft.colors.LIGHT_BLUE_100,
                )
                for label in row
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            spacing=10
        )
        rows.append(button_row)


    page.add(
        ft.Column(
            controls=[
                ft.Container(content=display, margin=ft.margin.only(top=20, bottom=20)),
                ft.Column(controls=rows, alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)