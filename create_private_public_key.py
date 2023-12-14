import flet as ft
from flet_core import ElevatedButton

from mathematical_operations import find_mod_inv, get_quadratic_deduction, is_coprime
from random_my import random


def get_keys(mod, quantity_num):
    private_keys = []
    public_keys = []

    for i in range(quantity_num):
        while True:
            random_num = random(mod - 1)
            mod_inv = find_mod_inv(random_num, mod)
            if mod_inv:
                quadratic_deduction_num = get_quadratic_deduction(mod_inv, mod)
                if random_num not in public_keys and quadratic_deduction_num is not None and is_coprime(random_num, mod):
                    public_keys.append(random_num)
                    private_keys.append(quadratic_deduction_num)
                    break

    return public_keys, private_keys


def main(page, lv):
    int_input_n = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Открытое число n'
    )

    int_input_k = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Длина ключей k'
    )

    def confirm_button(e):
        close_dlg(e)

        if not int_input_n and not int_input_k:
            lv.controls.append(
                ft.Text(
                    f"Заполнены не все поля.", selectable=True
                )
            )
            return page.update()

        public_keys, private_keys = get_keys(int(int_input_n.value), int(int_input_k.value))
        lv.controls.append(
            ft.Text(
                f"Ваш открытый ключ public_keys: {public_keys} \n Ваш закрытый ключ private_keys: {private_keys}",
                selectable=True
            )
        )
        int_input_n.value = None
        int_input_k.value = None
        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    inputs_column = ft.Column(spacing=10, controls=[int_input_n, int_input_k])

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите открытое число n = p * q и длину желаемых ключей."),
        content=inputs_column,
        actions=[
            ft.TextButton(text="Создать", on_click=confirm_button),
            ft.TextButton(text="Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Сгенерировать открытый и закрытый ключ", on_click=open_dlg_modal)
