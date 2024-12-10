# Estrutura do Projeto

```plaintext
project/
├── data/                  # Diretório para arquivos de dados (Excel, CSV, etc.)
│   └── PPH Daily 12.04.2024.xlsx
├── scripts/               # Scripts Python modulares
│   ├── db_connection.py   # Configuração do banco de dados e engine
│   ├── models.py          # Definição dos modelos ORM (Declarative Base)
│   ├── data_loader.py     # Código para carregar arquivos Excel
│   ├── data_cleaning.py   # Código para limpar e transformar dados
│   └── db_operations.py   # Código para manipulação e inserção de dados no banco
├── logs/                  # Diretório para armazenar logs do sistema
├── tests/                 # Testes unitários e funcionais
│   ├── test_data_cleaning.py
│   ├── test_db_connection.py
│   └── test_db_operations.py
├── .env                   # Arquivo para variáveis de ambiente (não compartilhar!)
├── requirements.txt       # Lista de dependências do projeto
└── README.md              # Documentação do projeto
