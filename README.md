## Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
R: Para cada site, só é preciso criar uma classe que estenda/implemente a classe Crawlable e adicionar a mesma na chamada do Crawling.

## Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
R: Se não for possível pegar a requisição através do AJAX que a página chama, pode ser utilizado o Selenium, de preferência com um browser head-less como o PhantomJS.

## Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
R: Intervalos randômicos de espera.

## Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?
R: Poderia negociar um horário que não fosse custoso, ou poderia fazer o crawling por partes/períodos de tempo. 