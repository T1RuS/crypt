import flet as ft
from flet_core import ElevatedButton

from mathematical_operations import is_prime, is_prime_two


def main(page, lv):
    int_input = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        )
    )

    def check_is_prime(number):
        error = None
        if not is_prime(number):
            error = True
            lv.controls.append(
                ft.Text(
                    f"Число {number} не прошло проверку первого метода.", selectable=True
                )
            )
            page.update()

        if not is_prime_two(number):
            error = True
            lv.controls.append(
                ft.Text(
                    f"Число {number} не прошло проверку вторго метода.", selectable=True
                )
            )
            page.update()

        return error

    def confirm_button(e):
        close_dlg(e)
        error = check_is_prime(
            number=int(int_input.value)
        )

        lv.controls.append(ft.Text(f"Число {int_input.value} {'не' if error else ''} является простым.", selectable=True))

        int_input.value = ''
        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите число, которое хотите проверить на простоту."),
        content=int_input,
        actions=[
            ft.TextButton(text="Проверить", on_click=confirm_button),
            ft.TextButton(text="Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Проверить число на простоту", on_click=open_dlg_modal)
