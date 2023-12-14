import socket

import flet as ft
from flet_core import ElevatedButton

HOST = "127.0.0.1"
PORT = 65432


def sending(page, lv):
    str_input = ft.TextField()

    def confirm_button(e):
        close_dlg(e)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(bytes(str_input.value, 'utf-8'))
        lv.controls.append(ft.Text(f"Отправлено сообщение: {str_input.value}", selectable=True))
        page.update()
        str_input.value = ''

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Введите сообщение для отправки."),
        content=str_input,
        actions=[
            ft.TextButton(text="Отправить", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Отправить сообщение", on_click=open_dlg_modal)


def receiving(page, lv):
    def confirm_button(e):
        close_dlg(e)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    lv.controls.append(ft.Text(f"Полученное сообщение: {data.decode('utf-8')}", selectable=True))
                    page.update()
                    if not data:
                        break
                    conn.sendall(data)

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Получить сообщение?"),
        actions=[
            ft.TextButton(text="Получить", on_click=confirm_button),
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    return ElevatedButton(text="Получить сообщение", on_click=open_dlg_modal)
