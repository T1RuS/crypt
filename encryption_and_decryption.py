import flet as ft
from flet_core import ElevatedButton

from mathematical_operations import multiplication_numbers
from random_my import random


#     x = (r**2) % n
#     y = (r * multiplication_numbers(s, probability_list)) % n
#     print((y**2 * multiplication_numbers(v, probability_list)) % n == x)


def generate_message(page, lv):
    str_input_r = ft.TextField(
        label='Сообщение для шифрование r'
    )

    int_input_n = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Введите открытый глобальный ключ n = p * q'
    )

    def confirm_button(e):
        close_dlg(e)
        lv.controls.append(ft.Text(f"Закодированное сообщение X {(int(hash(str_input_r.value))**2) % int(int_input_n.value)}", selectable=True))
        page.update()
        str_input_r.value = None
        int_input_n.value = None
        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    inputs_column = ft.Column(spacing=10, controls=[str_input_r, int_input_n])

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите сообщение для шифрования r и открытый глобальный ключ n"),
        content=inputs_column,
        actions=[
            ft.TextButton(text="Создать", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Зашифровать сообщение r -> x", on_click=open_dlg_modal)


def random_sequence_bits(page, lv):
    int_input_length = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Длина случайной битовой последовательности'
    )

    def confirm_button(e):
        close_dlg(e)
        lv.controls.append(ft.Text(f"Случайная последовательность битов e {[random(2) for i in range(int(int_input_length.value))]}", selectable=True))
        page.update()
        int_input_length.value = None
        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите длину случайной битовой последовательности"),
        content=int_input_length,
        actions=[
            ft.TextButton(text="Создать", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Создать случайную последовательность битов", on_click=open_dlg_modal)


def encryption(page, lv):
    int_input_r = ft.TextField(
        label='Сообщение для шифрование r'
    )

    int_input_s = ft.TextField(
        label='Секретный ключ [s]'
    )

    int_input_e_list = ft.TextField(
        label='Случайная битовая последовательность [e]'
    )

    int_input_n = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Введите открытый глобальный ключ n = p * q'
    )

    def confirm_button(e):
        close_dlg(e)
        lv.controls.append(ft.Text(f"Зашифрованное сообщение {(int(hash(int_input_r.value)) * multiplication_numbers(list(map(int, int_input_s.value.split(','))), list(map(int, int_input_e_list.value.split(','))))) % int(int_input_n.value)}", selectable=True))
        page.update()
        int_input_r.value = None
        int_input_s.value = None
        int_input_e_list.value = None
        int_input_n.value = None

        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    inputs_column = ft.Column(spacing=10, controls=[int_input_r, int_input_s, int_input_e_list, int_input_n])

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите сообщение для шифрования и секретный ключ."),
        content=inputs_column,
        actions=[
            ft.TextButton(text="Зашифровать", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Зашифровать сообщение", on_click=open_dlg_modal)


def decryption(page, lv):
    int_input_y = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Зашифрованное y сообщение'
    )

    int_input_v = ft.TextField(
        label='открытый ключ [v]'
    )

    int_input_x = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Сообщение x'
    )

    int_input_e_list = ft.TextField(
        label='Случайная битовая последовательность [e]'
    )

    int_input_n = ft.TextField(
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9]",
            replacement_string=""
        ),
        label='Введите открытый глобальный ключ n = p * q'
    )

    def confirm_button(e):
        close_dlg(e)

        decryption_massage = (int(int_input_y.value)**2 * multiplication_numbers(list(map(int, int_input_v.value.split(','))), list(map(int, int_input_e_list.value.split(','))))) % int(int_input_n.value)
        lv.controls.append(ft.Text(
            f"Расшифрованное сообщение {decryption_massage} проверка сообщения X {int_input_x.value} {'=' if int(int_input_x.value) == decryption_massage else '!='} decryption_massage {decryption_massage}",
            selectable=True))
        page.update()
        int_input_x.value = None
        int_input_y.value = None
        int_input_v.value = None
        int_input_e_list.value = None
        int_input_n.value = None

        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    inputs_column = ft.Column(spacing=10, controls=[int_input_y, int_input_v, int_input_x, int_input_e_list, int_input_n])

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите сообщение для дешифрование и открытый ключ."),
        content=inputs_column,
        actions=[
            ft.TextButton(text="Расшифровать", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Расшифровать сообщение", on_click=open_dlg_modal)
