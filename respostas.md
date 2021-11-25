1) Um Framework pode ser entendido como um conjunto de códigos que visa solucionar problemas comuns no desenvolvimento. Por exemplo, um framework web possuí diversos códigos prontos para serem usados que resolvem problemas comuns no desenvolvimento de sites. 

2) pip é um gerenciador de pacotes, utilizado para instalar dependências escritas em Python. O comando "pip install Flask", instala o microframework Flask do PyPI, junto com todas as suas dependências necessárias.

3) MVC é uma abreviação para o padrão de projeto Model-View-Controller, que visa separar um projeto de software em três camadas: 
    - Model: que estabeleça as entidades do projeto
    - View: A parte de visualização, onde o usuário interage com o software
    - Controller: o local onde se une o Model com a View, permitindo a troca de dados entre os dois. 

4) Flask é um microframework web, utilizado para a produção de servidores web. 

5) Depende. Para projetos pequenos ou projetos que se quer um controle muito grande do funcionamento do software, um microframework se torna uma vantagem. No entanto, para desenvolver grandes aplicações, de forma segura e rápida, um framework como o Django pode ser vantajoso, por isso, depende muito da situação.

6) 
    a) É criada uma instancia da classe Flask, passando o parâmetro ```__name__```, que informa se aquele arquivo python está sendo executado como main ou não. 
    b) a operação que permite ela ser mostrada na url é o uso do decorator, na linha 4, que faz com que, ao acessarmos a url "/", executemos essa função

7) Para realizar o deploy do sistema, foi necessário primeiramente fazê-lo, utilizando Python, HTML, CSS, com a ferramenta VsCode. Após colocar o sistema em um repositório no GitHub, bastou então criar uma conta no Heroku e sincronizar o repositório com um projeto no Heroku, então já estava disponível para acessar na web. 

