import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width = 300
    page.window_height = 400

    # Display area
    display = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=290)

    # Store the current value and operation
    current_value = "0"
    last_value = ""
    operator = ""

    # Handle button click
    def on_click(e):
        nonlocal current_value, last_value, operator

        button_text = e.control.text

        # Clear display
        if button_text == "C":
            current_value = "0"
            last_value = ""
            operator = ""
            display.value = current_value
            page.update()
            return

        # Handle digits
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

        # Handle equals
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

    # Create calculator buttons
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"],
    ]

    grid = ft.GridView(expand=True, runs_count=4, max_extent=70, spacing=5, run_spacing=5)

    for row in buttons:
        for label in row:
            grid.controls.append(
                ft.ElevatedButton(text=label, on_click=on_click, width=70, height=70)
            )

    # Add display and buttons to the page
    page.add(display, grid)


# Run the app
ft.app(target=main)
