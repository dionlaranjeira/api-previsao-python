# api-previsao-python
<h1>API Previsão do Tempo desenvolvida em Python</h1>


<h3 align="center">PROJETO EM CONSTRUÇÃO</h1>



<p align="center">
<a href="#sobre">Sobre | </a>
<a href="#instalacao">Instalação | </a>
<a href="#instalacao">Utilização | </a>
<a href="#atualizacoes">Atualizações</a>
</p>



<h1>#sobre</h1>
<p>Essa API tem o principal objetivo de retornar a previsão do tempo de uma determinada cidade.</p> 
<p> A lista de cidade disponíveis para obter uma previsão pode ser baixada em: http://bulk.openweathermap.org/sample/ </p>
<p>Por se tratar de um projeto em construção, não foi utilizado um banco de dados, todas as consultas as cidades são realizadas no arquivo JSON disponivel em: https://github.com/dionlaranjeira/api-previsao-python/blob/main/city.list.json</p>
<p>As previsão são feitas com a consulta ao Web Service disponivel em: https://openweathermap.org/forecast5<p>
<p>Para realizar as consultas, você precisará de uma API_KEY, é possível conseguir uma em: https://openweathermap.org/api<p>
<p>Nessa api, utilizamos a API_KEY para realizar consulta do web service "5 Day / 3 Hour Forecast"</p>


<h1>#instalacao</h1>
<p>Você precisará de python versão 3</p>
<p>Clone esse projeto e configure seu ambiente python</p>
<p>Utilizamos o Flask para o servidor back end, é possível fazer a instalação do Flask via pip instal com:</p>
>py -m venv env <br>
>env\Scripts\activate <br>
>pip install flask <br>
>set FLASK_APP=app.py <br>
>flask run <br>
set FLASK_APP=app.py <br>

<p>Você também irá precisar instalar as seguintes depências</p>
flask_restful ---> pip install flask-restful <br>
requests --->  pip install requests <br>
datetime--> pip install DateTime <br>


<p>Você precisará de uma API_KEY do recurso "5 Day / 3 Hour Forecast", para conseguir uma, cadastre-se e solicite no site: https://openweathermap.org/api</p>
<p>Após conseguir sua API_KEY, crie um arquivo chamado config.py, na raiz do projeto</p>
<p>Dentro do arquivo config.py, crie uma variável chamada, api_key, e atribua a essa variável a sua chave, como é mostrado nesse exemplo: api_key = 'DIGITE SUA CHAVE'</p>


<h1>#Utilização</h1>

<p>Após a configuração do ambiente python e framework Flask, execute o projeto.</p>
<p>Somente dois end points foram implementados nesse projeto, o primeiro retorna uma lista de cidade e suas IDS.</p>
<p>Para acessar o end point que retorn a lista de cidade, acesse o endereço http://{$IP_SERVIDOR}/cidade/{$NOME_CIDADE} .</p>
<p>A imagem a seguir, mostrar um exemplo de retorno ao acessar esse end point</p>
<figure align="center">
  <img src="https://github.com/dionlaranjeira/api-previsao-python/blob/main/json_cidade_end_poit.png" alt="end point cidade">
  <figcaption>JSON end point cidade</figcaption>
</figure>


<p>O segundo end point, retorna as previsões de tempo para uma cidade.</p>
<p>A busca de previsões é feita pelo id da cidade. para acessar esse end point utilize o endereço http://{$IP_SERVIDOR}/previsao_tempo/{$ID_CIDADE} . </p>
<p>A imagem a seguir, mostrar um exemplo de retorno ao acessar esse end point</p>
<figure align="center">
  <img src="https://github.com/dionlaranjeira/api-previsao-python/blob/main/json_previsoes.png" alt="end point previsões">
  <figcaption>JSON end point previsões</figcaption>
</figure>

<h1>#atualizacoes</h1>

<p>Atualizações futuras do app:</p>
<p>Adionar banco de dados</p>
<p>Retornar estado da cidade, de acordo com as geocoordenadas</p>
<p>Retornar bandeiras dos países das cidades</p>
