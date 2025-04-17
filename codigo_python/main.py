# main.py
import flet as ft
from conexao import connect_to_database
from menus import *

connection = None

def main(page: ft.Page):
    page.title = "Conferência Científica"
    global connection

    host_input = ft.TextField(label="Host", value="localhost", width=300)
    user_input = ft.TextField(label="Usuário", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)
    database_input = ft.TextField(label="Banco de Dados", value="conferenciacientifica", width=300)

    def show_main_menu():
        page.clean()
        page.add(ft.Text("Menu Principal", size=30))

        menu_row = ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.ElevatedButton("Gerenciar Conferências", on_click=lambda e: show_conferences_menu(page, connection, show_main_menu), color=ft.Colors.BLUE),
                ft.ElevatedButton("Avaliações", on_click=lambda e: show_reviews_menu(page, connection, show_main_menu), color=ft.Colors.ORANGE),
                ft.ElevatedButton("Gerenciar Participantes", on_click=lambda e: show_participants_menu(page, connection, show_main_menu), color=ft.Colors.GREEN),
                ft.ElevatedButton("Gerenciar Sessões", on_click=lambda e: show_sessions_menu(page, connection, show_main_menu), color=ft.Colors.PURPLE),
                ft.ElevatedButton("Gerenciar Apresentações", on_click=lambda e: show_presentations_menu(page, connection, show_main_menu), color=ft.Colors.RED),
                ft.ElevatedButton("Gerenciar Submissões", on_click=lambda e: show_submissions_menu(page, connection, show_main_menu), color=ft.Colors.YELLOW),
                ft.ElevatedButton("Gerenciar Revisores", on_click=lambda e: show_reviewers_menu(page, connection, show_main_menu), color=ft.Colors.CYAN)
            ],
            spacing=15
        )
        page.add(menu_row)

    def connect_button_click(e):
        global connection
        connection = connect_to_database(
            host_input.value,
            user_input.value,
            password_input.value,
            database_input.value
        )
        if connection:
            page.add(ft.Text("Conexão bem-sucedida!", color=ft.Colors.GREEN))
            show_main_menu()
        else:
            page.add(ft.Text("Falha na conexão!", color=ft.Colors.RED))

    connect_button = ft.ElevatedButton("Conectar", on_click=connect_button_click)

    page.add(
        host_input,
        user_input,
        password_input,
        database_input,
        connect_button
    )

ft.app(target=main)
