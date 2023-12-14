import random_my

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

    def generate_number(number: int):
        while True:
            prime_number = int(str(random_my.random(11**(number+1)))[:-1])
            if not is_prime(prime_number):
                lv.controls.append(
                    ft.Text(
                        f"Число {prime_number} не прошло проверку первого метода.", selectable=True
                    )
                )
                page.update()

            if not is_prime_two(prime_number):
                lv.controls.append(
                    ft.Text(
                        f"Число {prime_number} не прошло проверку вторго метода.", selectable=True
                    )
                )
                page.update()
            else:
                return prime_number

    def confirm_button(e):
        close_dlg(e)
        prime_number = generate_number(
            number=int(int_input.value)
        )
        lv.controls.append(ft.Text(f"Все проверки пройдены простое число {prime_number}", selectable=True))
        page.update()
        int_input.value = ''

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите длину желаемого простого числа."),
        content=int_input,
        actions=[
            ft.TextButton(text="Сгенерировать", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Cгенерировать простое число", on_click=open_dlg_modal)
