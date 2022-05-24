<h1>Portifólio de Matheus Albernaz</h1><br>
<p>Este repositório é destinado ao desenvolvimento de um portifólio de <b>Matheus Augusto de Jesus Albernaz</b>, aluno no curso de Desenvolvimento de Software Multiplataforma, da <b>FATEC Professor Jessen Vidal</b>, em São José dos Campos, interior de São Paulo.</p>

<h2>Estrutura de pastas</h2>

<h3>doc</h3>
<p>Na pasta <b>"doc"</b> encontra-se um PDF com os protótipos do tipo wireframe, da versão desktop e versão mobile do sistema.</p>

<h3>src</h3>
<p>Na pasta <b>"src"</b> encontra-se as pastas <b>"templates"</b> e <b>"static"</b>.</p>

<h3>templates</h3>
<p>Na pasta <b>"templates"</b> encontra-se os arquivos HTML das páginas do sistema.</p>

<h3>static</h3>
<p>Na pasta <b>"static"</b> encontra-se as imagens utilizadas no sistema e também a pasta <b>"css"</b>.</p>

<h3>css</h3>
<p>Na pasta <b>"css"</b> contém os arquivos CSS de estilização.</p>

## Rodar a aplicação <a id="rodar-app"></a>

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
6. Então, é só instalar o *requirements.txt*: 
```
pip install flask
```
7. Certifique-se que está na pasta `src`, caso não esteja, retorne até a pasta principal utilizando o primeiro comando, e depois vá até a pasta
```
cd ..
cd src
```
8. Agora ainda no terminal, digite o seguinte código para começar a rodar o sistema:
```
flask run
```
9. Clique no link disponibilizado (com ctrl + clique). Pronto! Agora é só utilizar.
