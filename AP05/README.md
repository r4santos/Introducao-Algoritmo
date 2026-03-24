# AP05 - Estruturas de Repeticao com while

## Sobre a atividade
A AP05 tem como foco principal o uso de repeticao com `while`, combinando:

- contadores
- acumuladores
- validacao de entrada
- estruturas condicionais
- repeticao aninhada
- construcoes de series numericas

Ao longo dos exercicios, os problemas evoluem de contagens simples para cenarios mais completos, como controle de vendas, monitoramento de temperaturas e um desafio de caixa com menu interativo.

## Objetivos de aprendizagem
Ao concluir esta atividade, voce deve ser capaz de:

- usar `while` para controlar repeticoes com quantidade fixa e variavel
- aplicar contadores e acumuladores corretamente
- validar dados de entrada antes de processar
- calcular medias, maximos, minimos e somatorios
- construir sequencias numericas e series com fracoes
- organizar menus e fluxo de programa de forma clara

## Lista de exercicios

### 1. Contagem crescente
Mostra os numeros de 1 ate 10, um por linha.

Arquivo: `contagem_crescente.py`

### 2. Contagem regressiva
Mostra os numeros de 10 ate 1, um por linha e, ao final, exibe:

`Fim da contagem`

Arquivo: `contagem_regressiva.py`

### 3. Soma de 1 ate n
Le um inteiro positivo `n` e calcula:

`1 + 2 + 3 + ... + n`

Arquivo: `soma_1_a_N.py`

### 4. Tabuada de um numero
Le um numero inteiro e mostra sua tabuada de 1 a 10.

Arquivo: `tabuada_de_N.py`

### 5. Media de 5 notas
Le 5 notas e calcula a media aritmetica.

Arquivo: `media_5_notas.py`

### 6. Contador de pares e impares
Le 10 inteiros e informa quantos sao pares e quantos sao impares.

Arquivo: `contador_n_pares_e_impares.py`

### 7. Maior e menor valor informado
Le 8 inteiros e determina o maior e o menor valor.

Arquivo: `maior_menor_valor_informado.py`

### 8. Soma ate valor de parada
Le numeros inteiros ate o usuario digitar `0`.

- O `0` nao entra na soma.
- Ao final, mostra soma e quantidade de numeros digitados.

Arquivo: `somar_ate_parar.py`

### 9. Controle de vendas de uma loja
Le valores de venda ate `0` e calcula:

- total vendido
- quantidade de vendas
- valor medio

Arquivo: `controle_vendas.py`

### 10. Monitoramento de temperaturas de uma maquina
Le temperaturas em Celsius ate `-1` e informa:

- quantidade registrada
- maior temperatura
- menor temperatura
- media
- quantas ficaram acima de 80 graus

Arquivo: `monitoramento_temp_maquina.py`

### 11. Tabuada completa de 1 a 9
Exibe todas as tabuadas de multiplicacao de 1 a 9.

Arquivo: `tabuada_completa_1_ao_9.py`

### 12. Retangulo de simbolos
Le linhas e colunas e desenha um retangulo com `*`.

Arquivo: `retangulo_simbolos.py`

### 13. Triangulo crescente de numeros
Le `n` e mostra o padrao:

```
1
12
123
...
```

Arquivo: `triangulo_crescente.py`

### 14. Monitoramento de material radioativo
Dada uma massa inicial (g), calcula o tempo necessario para a massa ficar menor que `0,5 g`, considerando perda de metade a cada 50 segundos.

Arquivo: `monitoramento_material_radioativo.py`

### 15. Soma harmonica simples
Le `n` e calcula:

`S = 1 + 1/2 + 1/3 + ... + 1/n`

Arquivo: `soma_hamonica_s.py`

### 16. Soma com sinais alternados
Le `n` e calcula os `n` primeiros termos de:

`S = 1 - 1/2 + 1/3 - 1/4 + ...`

Arquivo: `soma_c_sinais_alternados.py`

### 17. Soma com padrao triangular
Le `n` e calcula os `n` primeiros termos de:

`S = 1/1 + 2/3 + 3/6 + 4/10 + 5/15 + ...`

Os denominadores seguem os numeros triangulares: `1, 3, 6, 10, 15...`

Arquivo: `soma_c_padrao_triangular.py`

## Desafio - Sistema simples de caixa com validacao de produto
O desafio propoe um sistema com menu interativo para registrar vendas, validando:

- codigo do produto (`1`, `2` ou `3`)
- valor da venda (maior que zero)

Menu esperado:

- `1` Registrar venda
- `2` Mostrar total vendido
- `3` Mostrar quantidade de vendas
- `4` Mostrar valor medio das vendas
- `5` Mostrar quantidade vendida por tipo de produto
- `0` Encerrar sistema

Tipos de produto:

- `1` Lanche
- `2` Bebida
- `3` Sobremesa

Ao final, o sistema deve apresentar um relatorio com total vendido, quantidade de vendas, media e quantidade por tipo.

Arquivo: `desafio.py`

## Como executar os programas
No terminal, entre na pasta AP05 e execute o arquivo desejado.

Exemplo no Windows:

```powershell
cd "c:\Users\rafae\Documents\Dev\Introduçao-Algoritmos\AP05"
python .\controle_vendas.py
```

Se voce estiver usando ambiente virtual, ative-o antes de executar os scripts.

## Observacoes
- A maioria dos exercicios foi pensada para treino de logica com `while`.
- Em exercicios com valor de parada (`0` ou `-1`), esse marcador nao entra nos calculos.
- Para manter padrao de saida, prefira imprimir resultados com mensagem descritiva.
