🎓 Sistema de Gerenciamento de Conferências Científicas
Aplicação completa para organização, submissão e avaliação de eventos científicos, construída com Python, Flet e MySQL Workbench.


📌 Visão Geral
Este sistema foi desenvolvido para facilitar a administração de conferências científicas, permitindo o cadastro e gerenciamento de conferências, sessões temáticas, participantes, apresentações, submissões de artigos e avaliações por revisores.

A aplicação conta com uma interface gráfica moderna feita em Flet e integração completa com banco de dados MySQL, utilizando o MySQL Workbench para modelagem e administração do banco.

🧠 Funcionalidades Principais
📅 Cadastro e edição de Conferências

👥 Gerenciamento de Participantes (palestrantes, ouvintes e organizadores)

🗓️ Sessões com subtemas e horários definidos

🧾 Submissão e avaliação de trabalhos científicos

🗂️ Relacionamento completo entre Apresentações, Sessões e Conferências

🧑‍🔬 Avaliações por Revisores com feedback e decisões

💻 Interface em Flet para gerenciamento visual dos dados

🧱 Modelo de Dados
O sistema segue uma modelagem estruturada e normalizada com as seguintes entidades principais:

Conferência

Sessão

Participante

Apresentação

Submissão

Revisor

Avaliação

📌 Veja o Modelo ER (Conceitual) completo no diretório /docs.

🛠️ Tecnologias Utilizadas

Tecnologia	Descrição
🐍 Python	Lógica da aplicação
🎨 Flet	Framework para UI nativa com Python
🐬 MySQL	Banco de dados relacional principal
🛠️ MySQL Workbench	Ferramenta para modelagem e gerenciamento
📝 SQL	Script de criação e inserção de dados
🧰 Visual Paradigm	Modelagem conceitual e lógica
🧰 Instalação do MySQL Workbench
🔧 Passos para Instalar
Acesse: https://dev.mysql.com/downloads/workbench/

Selecione o sistema operacional (Windows, macOS, Linux)

Siga as instruções de instalação e configure a conexão com o banco local ou remoto

📸 Veja imagens de referência em /docs/mysql_screenshots/ com os passos de conexão e execução do script.

🏗️ Criação do Banco de Dados
Para criar as tabelas e popular o banco de dados:

Abra o MySQL Workbench

Conecte-se ao seu servidor MySQL

Execute o conteúdo do arquivo /data/populacao_inicial.sql

Esse script irá:

Criar o banco ConferenciaCientifica

Criar todas as tabelas com relacionamentos

Inserir registros iniciais para testes

📂 Estrutura do Projeto

conferencia_sistem/

├── crud/

│   ├── conferencia_crud.py

│   ├── participante_crud.py

│   └── ...

├── ui/

│   ├── home.py

│   ├── participantes_view.py

│   └── ...

├── db/

│   └── conexao.py

├── data/

│   └── populacao_inicial.sql

├── docs/

│   ├── ERD_visualizacao.png

│   └── mysql_screenshots/

├── main.py

└── README.md

⚙️ Como Executar

✅ Pré-requisitos
Python 3.10+

MySQL Server instalado

MySQL Workbench (opcional, mas recomendado)

VSCode (recomendado)

🚀 Passo a passo

# Clone o projeto
git clone https://github.com/seuusuario/conferencia-sistema.git
cd conferencia-sistema

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o script de criação de banco
mysql -u usuario -p < data/populacao_inicial.sql

# Inicie o sistema
python main.py

👨‍💻 Autor
Desenvolvido por Luiz André de Souza
📫 GitHub: @brodyandre

📄 Licença
Distribuído sob a licença MIT.
Veja LICENSE para mais informações.
