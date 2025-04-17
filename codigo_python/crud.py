# crud.py
import flet as ft
from mysql.connector import Error

def create_crud_menu(page, connection, title, table_name, fields, show_main_menu, custom_labels=None):
    custom_labels = custom_labels or {}
    inputs = {field: ft.TextField(label=custom_labels.get(field, field)) for field in fields}

    def add_entry(e):
        try:
            values = tuple(inputs[field].value for field in fields)
            if any(val.strip() == "" for val in values):
                page.add(ft.Text("Por favor, preencha todos os campos.", color=ft.Colors.RED))
                return

            cursor = connection.cursor()
            query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({', '.join(['%s']*len(fields))})"
            cursor.execute(query, values)
            connection.commit()
            page.add(ft.Text("Registro adicionado com sucesso!", color=ft.Colors.GREEN))
            list_entries()
        except Error as e:
            page.add(ft.Text(f"Erro ao adicionar registro: {e}", color=ft.Colors.RED))

    def edit_entry(table_name, fields, entry):
        page.clean()
        page.add(ft.Text(f"Editar {title}", size=24))
        edit_inputs = {
            field: ft.TextField(
                label=custom_labels.get(field, field), value=str(entry[i+1])
            )
            for i, field in enumerate(fields[1:])
        }

        def save_changes(e):
            try:
                cursor = connection.cursor()
                set_clause = ", ".join([f"{fields[i+1]} = %s" for i in range(len(fields)-1)])
                query = f"UPDATE {table_name} SET {set_clause} WHERE {fields[0]} = %s"
                values = tuple([edit_inputs[field].value for field in fields[1:]]) + (entry[0],)
                cursor.execute(query, values)
                connection.commit()
                page.add(ft.Text("Registro atualizado com sucesso!", color=ft.Colors.GREEN))
                list_entries()
            except Error as e:
                page.add(ft.Text(f"Erro ao atualizar registro: {e}", color=ft.Colors.RED))

        for field in fields[1:]:
            page.add(edit_inputs[field])
        page.add(ft.ElevatedButton("Salvar Alterações", on_click=save_changes))
        page.add(ft.ElevatedButton("Cancelar", on_click=lambda e: list_entries()))

    def delete_entry(table_name, entry_id):
        try:
            cursor = connection.cursor()
            query = f"DELETE FROM {table_name} WHERE {fields[0]} = %s"
            cursor.execute(query, (entry_id,))
            connection.commit()
            page.add(ft.Text("Registro deletado com sucesso!", color=ft.Colors.GREEN))
            list_entries()
        except Error as e:
            page.add(ft.Text(f"Erro ao deletar registro: {e}", color=ft.Colors.RED))

    def list_entries():
        page.clean()
        page.add(ft.Text(f"{title} Registrados", size=20))
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            entries = cursor.fetchall()
            for entry in entries:
                row = ft.Row([
                    ft.Text(" | ".join([str(val) for val in entry[1:]])),
                    ft.IconButton(ft.icons.EDIT, on_click=lambda e, entry=entry: edit_entry(table_name, fields, entry)),
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e, entry=entry: delete_entry(table_name, entry[0]))
                ])
                page.add(row)
        except Error as e:
            page.add(ft.Text(f"Erro ao buscar registros: {e}", color=ft.Colors.RED))

        page.add(ft.ElevatedButton("Voltar ao Menu Principal", on_click=lambda e: show_main_menu()))

    page.clean()
    page.add(ft.Text(title, size=24))
    for field in fields:
        page.add(inputs[field])

    page.add(ft.ElevatedButton(f"Adicionar {title}", on_click=add_entry))
    page.add(ft.ElevatedButton(f"Listar {title}", on_click=lambda e: list_entries()))
    page.add(ft.ElevatedButton("Voltar ao Menu Principal", on_click=lambda e: show_main_menu()))
