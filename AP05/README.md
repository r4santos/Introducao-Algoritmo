# AP05 - Estruturas de Repetição com while

## Sobre a atividade
A AP05 tem como foco principal o uso de repetição com while, combinando:

- contadores
- acumuladores
- validação de entrada
- estruturas condicionais
- repetição aninhada
- construções de séries numéricas

Ao longo dos exercícios, os problemas evoluem de contagens simples para cenários mais completos, como controle de vendas, monitoramento de temperaturas e um desafio de caixa com menu interativo.

## Objetivos de aprendizagem
Ao concluir esta atividade, você deve ser capaz de:

- usar while para controlar repetições com quantidade fixa e variável
- aplicar contadores e acumuladores corretamente
- validar dados de entrada antes de processar
- calcular médias, máximos, mínimos e somatórios
- construir sequências numéricas e séries com frações
- organizar menus e fluxo de programa de forma clara

## Lista de exercícios

### 1. Contagem crescente
Mostra os números de 1 até 10, um por linha.

Arquivo: contagem_crescente.py

### 2. Contagem regressiva
Mostra os números de 10 até 1, um por linha e, ao final, exibe a mensagem:

Fim da contagem

Arquivo: contagem_regressiva.py

### 3. Soma de 1 até n
Lê um inteiro positivo n e calcula:

1 + 2 + 3 + ... + n

Arquivo: soma_1_a_N.py

### 4. Tabuada de um número
Lê um número inteiro e mostra sua tabuada de 1 a 10.

Arquivo: tabuada_de_N.py

### 5. Média de 5 notas
Lê 5 notas e calcula a média aritmética.

Arquivo: media_5_notas.py

### 6. Contador de pares e ímpares
Lê 10 inteiros e informa quantos são pares e quantos são ímpares.

Arquivo: contador_n_pares_e_impares.py

### 7. Maior e menor valor informado
Lê 8 inteiros e determina o maior e o menor valor.

Arquivo: maior_menor_valor_informado.py

### 8. Soma até valor de parada
Lê números inteiros até o usuário digitar 0.

- O 0 não entra na soma.
- Ao final, mostra soma e quantidade de números digitados.

Arquivo: somar_ate_parar.py

### 9. Controle de vendas de uma loja
Lê valores de venda até 0 e calcula:

- total vendido
- quantidade de vendas
- valor médio

Arquivo: controle_vendas.py

### 10. Monitoramento de temperaturas de uma máquina
Lê temperaturas em Celsius até -1 e informa:

- quantidade registrada
- maior temperatura
- menor temperatura
- média
- quantas ficaram acima de 80 graus

Arquivo: monitoramento_temp_maquina.py

### 11. Tabuada completa de 1 a 9
Exibe todas as tabuadas de multiplicação de 1 a 9.

Arquivo: tabuada_completa_1_ao_9.py

### 12. Retângulo de símbolos
Lê linhas e colunas e desenha um retângulo com *.

Arquivo: retangulo_simbolos.py

### 13. Triângulo crescente de números
Lê n e mostra o padrão:

```
1
12
123
...
```

Arquivo: triangulo_crescente.py

### 14. Monitoramento de material radioativo
Dada uma massa inicial (g), calcula o tempo necessário para a massa ficar menor que 0,5 g, considerando perda de metade a cada 50 segundos.

Arquivo: monitoramento_material_radioativo.py

### 15. Soma harmônica simples
Lê n e calcula:

S = 1 + 1/2 + 1/3 + ... + 1/n

Arquivo: soma_hamonica_s.py

### 16. Soma com sinais alternados
Lê n e calcula os n primeiros termos de:

S = 1 - 1/2 + 1/3 - 1/4 + ...

Arquivo: soma_c_sinais_alternados.py

### 17. Soma com padrão triangular
Lê n e calcula os n primeiros termos de:

S = 1/1 + 2/3 + 3/6 + 4/10 + 5/15 + ...

Os denominadores seguem os números triangulares: 1, 3, 6, 10, 15...

Arquivo: soma_c_padrao_triangular.py

## Desafio - Sistema simples de caixa com validação de produto
O desafio propõe um sistema com menu interativo para registrar vendas, validando:

- código do produto (1, 2 ou 3)
- valor da venda (maior que zero)

Menu esperado:

- 1 Registrar venda
- 2 Mostrar total vendido
- 3 Mostrar quantidade de vendas
- 4 Mostrar valor médio das vendas
- 5 Mostrar quantidade vendida por tipo de produto
- 0 Encerrar sistema

Tipos de produto:

- 1 Lanche
- 2 Bebida
- 3 Sobremesa

Ao final, o sistema deve apresentar um relatório com total vendido, quantidade de vendas, média e quantidade por tipo.

Arquivo: desafio.py

## Exemplos de entrada e saída

### Exemplo 1 - Soma de 1 até n
Entrada:

```
Informe o valor de N: 5
```

Saída esperada:

```
Resultado: 15
```

### Exemplo 2 - Tabuada de um número
Entrada:

```
Informe um número: 7
```

Saída esperada:

```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

### Exemplo 3 - Soma até valor de parada
Entrada:

```
10
5
3
0
```

Saída esperada:

```
Soma: 18
Quantidade: 3
```

### Exemplo 4 - Controle de vendas
Entrada:

```
10
20
30
0
```

Saída esperada:

```
Total vendido: R$ 60.00
Quantidade de vendas: 3
Média das vendas: R$ 20.00
```

### Exemplo 5 - Soma com sinais alternados
Entrada:

```
Informe o valor de N: 4
```

Saída esperada:

```
S = 0.583333
```

### Exemplo 6 - Soma com padrão triangular
Entrada:

```
Informe o valor de N: 5
```

Saída esperada:

```
S = 2.666667
```

## Observações
- A maioria dos exercícios foram pensados para treino de lógica com while.
- Em exercícios com valor de parada (0 ou -1), esse marcador não entra nos cálculos.
- Para manter padrão de saída, prefira imprimir resultados com mensagem descritiva.
