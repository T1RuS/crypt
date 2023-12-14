import flet as ft
from flet import ElevatedButton, Page, Text, TextField, icons

import check_number_is_prime
import create_private_public_key
import encryption_and_decryption
import generate_prime_number
import sending_receiving


def main(page: Page):
    page.window_min_width = 1200
    page.window_min_height = 700
    page.window_max_height = 700
    page.window_max_width = 1200
    page.padding = 0

    lv = ft.ListView(auto_scroll=True, height=500)

    main = ft.Container(
        content=lv,
        bgcolor=ft.colors.SURFACE_VARIANT,
        width=page.window_width,
        height=500,
        padding=5,
        border_radius=8,
        margin=5
    )

    generate_prime_number_button = generate_prime_number.main(
        page=page,
        lv=lv
    )
    is_prime_number_button = check_number_is_prime.main(
        page=page,
        lv=lv
    )

    create_private_public_key_button = create_private_public_key.main(
        page=page,
        lv=lv
    )

    generate_message_button = encryption_and_decryption.generate_message(
        page=page,
        lv=lv
    )

    random_sequence_bits_button = encryption_and_decryption.random_sequence_bits(
        page=page,
        lv=lv
    )

    encryption_button = encryption_and_decryption.encryption(
        page=page,
        lv=lv
    )

    decryption_button = encryption_and_decryption.decryption(
        page=page,
        lv=lv
    )

    sending_button = sending_receiving.sending(page=page, lv=lv)
    receiving_button = sending_receiving.receiving(page=page, lv=lv)

    header = ft.Container(
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    controls=[
                        generate_prime_number_button,
                        is_prime_number_button,
                        create_private_public_key_button
                    ]
                ),
                ft.Row(
                    controls=[
                        generate_message_button,
                        random_sequence_bits_button
                    ]
                ),
                ft.Row(
                    controls=[
                        sending_button,
                        receiving_button
                    ]
                ),
                ft.Row(
                    controls=[
                        encryption_button,
                        decryption_button
                    ]
                )
            ]
        ),
        bgcolor=ft.colors.SURFACE_VARIANT,
        width=page.window_width,
        padding=5,
        border_radius=8,
        margin=5
    )

    page.add(header)
    page.add(main)


ft.app(target=main)
