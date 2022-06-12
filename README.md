<h1>Portifólio de Matheus Albernaz</h1><br>
<p>Este repositório é destinado ao desenvolvimento de um portifólio de <b>Matheus Augusto de Jesus Albernaz</b>, aluno no curso de Desenvolvimento de Software Multiplataforma, da <b>FATEC Professor Jessen Vidal</b>, em São José dos Campos, interior de São Paulo.</p>

<p>Esta aplicação já está implantada no Heroku, para visualizar acesse https://portifoliomts.herokuapp.com/ .</p>

<h2>Estrutura de pastas</h2>
<p>Esta é a estrutura de pastas atual, que possibilita a implatação no Heroku, mas também possibilita rodar a aplicação localmente.</p> 
<p>A raiz de nome <b>repo_portifolio_design-digital</b> contém os arquivos <b>.gitignore</b>, que ignora os arquivos criados pela implatação local(venv). Contém também o arquivo <b>LICENSE</b>, com dados sobre a licença desta aplicação, o arquivo <b>Procfile</b> com o código utilizado pelo <b>Heroku</b> para a implatação, o <b>README</b>, que contém estas informações que está lendo, o <b>app.py</b> arquivo de roterização do sistema, que contém o código de rotas para a implatação e por último o <b>requirements.txt</b> que contém todas bibliotecas necessárias para rodar a aplicação.
  
<h3>doc</h3>
<p>Na pasta <b>"doc"</b> encontra-se um PDF com os protótipos do tipo wireframe, da versão desktop e versão mobile do sistema.</p>

<h3>static</h3>
<p>Na pasta <b>"static"</b> encontra-se a pasta <b>images</b> com as imagens utilizadas no sistema e também a pasta <b>"css"</b>.</p>

<h3>css</h3>
<p>Na pasta <b>"css"</b> contém os arquivos CSS de estilização.</p>

<p>Também contém a pasta <b>bootstrap</b> que contém outras 2 pastas, <b>"css"</b> e <b>js</b>, que contém arquivos de estilização CSS e Javascript respectivamente</p>

<h3>templates</h3>
<p>Na pasta <b>"templates"</b> encontra-se os arquivos HTML das páginas do sistema.</p>

# Executando a aplicação <a id="configuracoes"></a>
- Primeiramente, clique em tags, na navegação lateral desta página e na página que abrir escolha a tag v3.0 e clique no zip para baixá-la.

## Rodar a aplicação localmente<a id="rodar-app"></a>

1. Após a instalação, verifique se possui o Phyton já instalado em sua máquina. Apartir do comando no terminal: 
```
python --version
```
2. Caso não possua siga os passos de instalação do site oficial do Python: https://www.python.org/
3. Caso a resposta seja positiva, pelo terminal de sua preferência, se dirija até a pasta criada pelo arquivo *.zip*. 
```
cd <nome da pasta>
```
4. Vamos criar agora um ambiente virtual, pelo comando: 
```
py -3 -m venv venv
```
5. Criada, vamos ativa-la: 
```
.\venv\Scripts\activate
```
6. Então, é só instalar o flask: 
```
pip install flask
```
7. Agora ainda no terminal, digite o seguinte código para começar a rodar o sistema:
```
flask run
```
8. Clique no link disponibilizado (com ctrl + clique). Pronto! Agora é só utilizar.
