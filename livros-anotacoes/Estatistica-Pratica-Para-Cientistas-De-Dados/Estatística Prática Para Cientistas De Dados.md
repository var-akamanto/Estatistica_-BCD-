# media

media = soma de todos os valores, dividido por todos os valores

A fórmula para computar a média para um conjunto de valores n x1, x2, ..., xN é:

![alt text](image.png)

## media aparada

media aparada se calcula excluindo  um numero fixo de valores selecionados em cada ponta, e entao tirando uma media desses valores

![alt text](image-1.png)

elimina influencia de outliers

## media ponderada

multiplicacao de cada valor de dado x por um peso w e divisao da somatoria pela soma de todos os pesos

![alt text](image-2.png)

razooes principais para uso da media ponderada:

- observacoes altamente variaveis recebem um peso menor. ex : um sensor com baixa precisao

- quando os dados coletados nao refletem igualmente os diferentes grupos que estamos medindo

# medianas e estimativas robustas

numero central em uma lista de dados classificada.1

nao e influenciada por outliers.

em caso de um numero par de dados, a mediana é a media dos dois valores que dividem a lista nas metades superior e inferior.

"
Digamos que queiramos observar os rendimentos familiares em bairros próximos a Lake Washington, em Seattle. Ao comparar o bairro Medina com o bairro Windermere, usando a média teríamos resultados muito diferentes, pois Bill Gates mora em Medina. Se usarmos a mediana, não importa a fortuna de Bill Gates — a posição da observação central permanecerá a mesma.
"

## mediana ponderada

primeiro classificamos os dados, e depois definimos os pesos da amostragem e relacionamos a cada um dos dados.

A mediana ponderada é usada com agregaçoes.

""
Considere um exemplo de renda mensal em que cada valor representa a renda média de um bairro, e o peso corresponde ao número de moradores.

Suponha os seguintes dados (já ordenados):

R$ 1.500 (peso 100 moradores)
R$ 2.000 (peso 300 moradores)
R$ 4.000 (peso 50 moradores)
R$ 10.000 (peso 10 moradores)

Peso total = 100 + 300 + 50 + 10 = 460
Metade do peso total = 230

Agora calculamos a soma acumulada dos pesos:

R$ 1.500 → 100
R$ 2.000 → 400

Ao incluir o valor de R$ 2.000, a soma acumulada ultrapassa 230. Portanto, a mediana ponderada é R$ 2.000.
"

é como se o peso definisse o numero de linhas em que os valores aparecem. Exemplo:

peso de 1500 = 4

lista: 1500,1500,1500,1500 - 4 familias tem essa renda.

# outliers

qualquer valor que seja muito distante dos outros valores.

podem enviesar os resultados.

nao sao valores errados, mas merecem investigaçao, pois podem ser o resultado de coletas ruins.





