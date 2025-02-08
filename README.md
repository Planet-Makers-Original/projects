Sistema de ordem de serviço para uma oficina automotiva usando Python e Django, com front-end moderno em HTML, CSS e JavaScript.

Instalação de bibliotecas necessárias
Certifique-se de ter Python instalado. Em seguida, crie um ambiente virtual e instale as bibliotecas necessárias.

`bash`

<p> git clone https://github.com/Planet-Makers-Original/Potal_emeca.git</p>
<p> cd your-repo</p>

# Criar ambiente virtual

<p>python -m venv venv</p>
<p>source venv/bin/activate # Linux/Mac</p>
<p>venv\Scripts\activate # Windows</p>

# Instalar Django e bibliotecas necessárias

<p> pip install -r requirements.txt</p>

#### `ou`

<p> pip install django pillow django-crispy-forms reportlab</p>

<p> python manage.py makemigations</p>
<p> python manage.py migrate</p>
<p> python manage.py runserver</p>
<p> Abrir o navegador e acessar http://localhost:8000</p>

## Biblilhoteca do projeto

##### django: Framework principal.

##### pillow: Para lidar com imagens.

##### django-crispy-forms: Para formularios estilizados.

##### reportlab: Para geração de PDFs.

## Apps do projeto

##### usuarios : App para autenticação

##### proprietarios: App para registros de proprietários

##### veiculos : App para registros de veículos

##### ordens : App para ordens de serviço

##### financeiro : App para controle financeiro

##### relatorios : App para geração de relatórios

### Contato:

- Você pode me contatar pelo e-mail [suporte@planetmakes.com.br](mailto:suporte@planetmakes.com.br)

### Créditos:

- Autor: `Alexande Yuri`
- Data de criação: `07/02/2025`
