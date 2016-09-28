# Pré-Requisitos
* Python 2.7+ (Recomendado 2.7.12)

# Como Configurar
* Basta executar o comando:
```
pip install -r requirements.txt
```

* Caso julgue necessário: alterar o arquivo start_crawling.py para usar o max_delay,
que é um valor máximo definido para um range de intervalo randômico, para tornar
mais difícil de ser bloqueado.

# Como executar
* Basta executar o comando:
```
python start_crawling.py
```

# Testes
* Para executar os testes, é necessário instalar requisitos de teste:
```
pip install -r test-requirements.txt
```

* E depois executar:
```
python run_tests.py
```

## Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
R: Para cada site, só é preciso criar uma classe que estenda/implemente a classe Crawlable e adicionar a mesma na chamada do Crawling.
As chamadas poderiam ser assíncronas e poderiam receber como callback a geração do csv.

## Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
R: Se não for possível pegar a requisição através do AJAX que a página chama, pode ser utilizado o Selenium, de preferência com um browser head-less como o PhantomJS.

## Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
R: Intervalos randômicos de espera e/ou proxies.

## Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?
R: Poderia negociar um horário que não fosse custoso, ou poderia fazer o crawling por partes/períodos de tempo. 