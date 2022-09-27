Este repositório tem como fim apresentar os códigos referentes as questões solicitadas no teste prático da Qipu. Os códigos foram desenvolvidos em Python 3.x, podendo ser executados em qualquer IDE. Não foram desenvolvidas interfaces gráficas para os códigos.

Para a execução dos mesmos, é necessário instalar as seguintes bibliotecas:
 - 1ª Questão:
  - num2words
 - 2ª Questão:
  - requests
  - html5lib
  - bs4

A partir disso, a entrada de ambos os códigos é recebida conforme informado nos enunciados das próprias questões. 

1ª Questão: Escreva um código que leia no terminal um valor numérico representando um valor em reais, e tenha como saída este valor escrito por extenso. O programa deve aceitar valores sempre com dois digitos após a virgula e com até 9 dígitos antes da vírgula. Importante: o algoritmo deve ser escrito por você.

2ª Questão: Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada, assim como a existência de cartas disponíveis e horários de nascer e pôr do sol. No Brasil, estas informações são disponibilizadas pelo site https://aisweb.decea.mil.br/. Nesta página é possível encontrar links para cartas, horarios do sol e as informações de TAF e METAR, que são boletins meteorológicos codificados. Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) e imprima na tela: i) As cartas disponíveis; ii) Os horários de nascer e pôr do sol de hoje; e iii) A informação de TAF e METAR disponíveis. Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.
