# menus.py
from crud import create_crud_menu

def show_conferences_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Conferência", "Conferencia",
                     ["ID_Conferencia", "Titulo", "Data", "Local", "Tema_Central"],
                     show_main_menu)

def show_sessions_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Sessão", "Sessao",
                     ["ID_Sessao", "ID_Conferencia", "Data_Hora", "Tema_Subtematico", "Coordenador"],
                     show_main_menu)

def show_presentations_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Apresentação", "Apresentacao",
                     ["id_apresentacao", "id_sessao", "titulo", "resumo", "duracao_prevista", "id_palestrante", "materiais_suporte"],
                     show_main_menu)

def show_submissions_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Submissão", "Submissao",
                     ["ID_Submissao", "ID_Apresentacao", "Titulo", "Resumo", "Data_Submissao", "Status"],
                     show_main_menu)

def show_reviewers_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Revisor", "Revisor",
                     ["ID_Revisor", "Nome", "Filiacao_Institucional", "Contato", "Especialidade"],
                     show_main_menu,
                     custom_labels={
                         "Filiacao_Institucional": "Filiação Institucional",
                         "Contato": "Contato",
                         "Especialidade": "Área de Especialidade"
                     })

def show_reviews_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Avaliação", "Avaliacao",
                     ["ID_Avaliacao", "ID_Submissao", "ID_Revisor", "Feedback", "Decisao"],
                     show_main_menu)

def show_participants_menu(page, connection, show_main_menu):
    create_crud_menu(page, connection, "Participante", "Participante",
                     ["ID_Participante", "Nome", "Filiacao_Institucional", "Contato", "Tipo_Participacao"],
                     show_main_menu)
