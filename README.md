# Carros

Este repositório contém um projeto para gerenciamento e visualização de informações sobre carros. 
Ele é ideal para aplicações que necessitam armazenar, listar e manipular dados relacionados a veículos, como marca, modelo, ano, entre outros.

## 🚗 Funcionalidades

- **Cadastro de carros**: Registre informações detalhadas sobre cada veículo.
- **Listagem de carros**: Exiba todos os veículos cadastrados.
- **Edição de informações**: Atualize os dados de um carro existente.
- **Remoção de carros**: Exclua registros de veículos.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Django
- **Banco de Dados**: MySQL
- Outras dependências listadas no `requirements.txt` ou `package.json`.

## 💻 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/pasklan/carros.git
   cd carros
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicialize o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse a aplicação em: http://localhost:8000 (ou outra porta configurada).

## 📂 Estrutura do Projeto
- **/app**: Contém o código principal do projeto.
- **/templates**: Arquivos HTML para renderização.
- **/static**: Arquivos estáticos como CSS, JS e imagens.
- **/migrations**: Scripts para controle de alterações no banco de dados.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo.

## 👨‍💻 Desenvolvido por Renato Pasklan
