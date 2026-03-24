# AP03 - Lista de Exercícios: Entrada, Processamento e Saída

## Sobre a atividade
Esta lista foi desenvolvida para praticar a estrutura fundamental de construção de algoritmos:

Entrada -> Processamento -> Saída

O foco está na leitura de dados, realização de cálculos e exibição organizada dos resultados.

## Regras da lista

- Utilizar apenas input(), operações matemáticas e print().
- Não utilizar condicionais (if).
- Não utilizar laços de repetição (for/while).
- Seguir a estrutura lógica: Entrada -> Processamento -> Saída.

## Objetivos de aprendizagem
Ao concluir a AP03, você deve ser capaz de:

- ler e interpretar dados informados pelo usuário
- aplicar fórmulas matemáticas em problemas práticos
- organizar o fluxo de resolução de forma clara
- apresentar resultados de forma legível

## Lista de exercícios

### 1. Consumo de Energia
Uma residência deseja estimar o consumo mensal de energia de um equipamento.

Entradas:

- potência do aparelho (Watts)
- horas de uso por dia
- dias de uso no mês
- preço da energia (R$/kWh)

Processamento esperado:

- consumo diário (kWh) = (potência * horas) / 1000
- consumo mensal (kWh) = consumo diário * dias
- custo mensal (R$) = consumo mensal * preço da energia

Saída esperada:

Relatório de consumo
--------------------
Consumo diário (kWh): ...
Consumo mensal (kWh): ...
Custo mensal (R$): ...

Arquivo: cosumo_energia.py

### 2. Planejamento de Viagem
Um motorista deseja estimar o custo de combustível de uma viagem.

Entradas:

- distância da viagem (km)
- consumo do carro (km/l)
- preço do combustível (R$/l)

Processamento esperado:

- litros necessários = distância / consumo
- custo estimado = litros necessários * preço do combustível

Saída esperada:

Planejamento de viagem
----------------------
Litros necessários: ...
Custo estimado: ...

Arquivo: planejamento_viagem.py

### 3. Boletim Simplificado
Ler três notas e calcular:

- soma das notas
- média das notas
- pontos que faltam para o total máximo

Observação: cada prova vale 10 pontos, então o total máximo é 30.

Saída esperada:

Relatório de notas
------------------
Soma das notas: ...
Média: ...
Pontos para média máxima: ...

Arquivo: boletim_simplificado.py

### 4. Compra Online
Calcular o valor final de um produto comprado pela internet.

Entradas:

- preço do produto
- percentual de imposto (0 a 100)
- valor do frete

Processamento esperado:

- valor do imposto = preço * (percentual / 100)
- valor total = preço + imposto + frete

Saída esperada:

Resumo da compra
----------------
Valor do imposto: ...
Valor total: ...

Arquivo: compra_online.py

### 5. Planejamento de abastecimento de uma frota
Uma empresa de entregas deseja estimar o gasto semanal de combustível de um veículo.

Entradas:

- distância média por entrega (km)
- número médio de entregas por dia
- número de dias de trabalho na semana
- consumo do veículo (km/l)
- preço do combustível (R$/l)

Processamento esperado:

- distância diária = distância por entrega * entregas por dia
- distância semanal = distância diária * dias de trabalho
- combustível necessário = distância semanal / consumo
- custo semanal = combustível necessário * preço do combustível

Saída esperada:

Relatório de operação do veículo
--------------------------------
Distância diária (km): ...
Distância semanal (km): ...
Combustível necessário (litros): ...
Custo semanal de combustível (R$): ...

Arquivo: planejamento_abastecimento_frota.py

### 6. Estimativa de tempo para leitura de um livro
Estimar o tempo necessário para concluir a leitura de um livro.

Entradas:

- total de páginas do livro
- média de palavras por página
- velocidade de leitura (palavras por minuto)
- minutos disponíveis por dia

Processamento esperado:

- total de palavras = páginas * palavras por página
- tempo total (minutos) = total de palavras / velocidade de leitura
- tempo total (horas) = tempo total (minutos) / 60
- dias estimados = tempo total (minutos) / minutos por dia

Saída esperada:

Planejamento de leitura
-----------------------
Total de palavras no livro: ...
Tempo total de leitura (minutos): ...
Tempo total de leitura (horas): ...
Dias estimados para terminar o livro: ...

Arquivo: estimativa_tempo_leitura.py

## Desafio da lista
Ajuste as soluções para melhorar a formatação das saídas, organizando os resultados em formato de tabela com \t e \n.

Exemplo:

Item\tValor
Consumo mensal\t...
Custo mensal\t...

## Exemplos de entrada e saída

### Exemplo 1 - Consumo de energia
Entrada:

```
Potência (W): 1000
Horas por dia: 5
Dias no mês: 30
Preço da energia (R$/kWh): 0.90
```

Saída esperada:

```
Relatório de consumo
--------------------
Consumo diário (kWh): 5.0
Consumo mensal (kWh): 150.0
Custo mensal (R$): 135.0
```

### Exemplo 2 - Planejamento de viagem
Entrada:

```
Distância (km): 300
Consumo (km/l): 12
Preço do combustível (R$/l): 5.8
```

Saída esperada:

```
Planejamento de viagem
----------------------
Litros necessários: 25.0
Custo estimado: 145.0
```

### Exemplo 3 - Estimativa de leitura
Entrada:

```
Total de páginas: 250
Palavras por página: 300
Velocidade de leitura (palavras/min): 150
Minutos disponíveis por dia: 30
```

Saída esperada:

```
Planejamento de leitura
-----------------------
Total de palavras no livro: 75000
Tempo total de leitura (minutos): 500.0
Tempo total de leitura (horas): 8.33
Dias estimados para terminar o livro: 16.67
```

## Como executar
No terminal, entre na pasta AP03 e execute o arquivo desejado.

Exemplo no Windows:

```powershell
cd "c:\Users\rafae\Documents\Dev\Introduçao-Algoritmos\AP03"
python .\planejamento_viagem.py
```

## Observações

- Priorize clareza nos nomes de variáveis.
- Escreva o processamento em etapas para facilitar revisão.
- Valide se os cálculos seguem exatamente as fórmulas do enunciado.
