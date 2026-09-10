# Projeto de Funções em Python

Este projeto foi desenvolvido para uma atividade acadêmica com foco em funções básicas de Python e testes automatizados com pytest.

## Funções implementadas

- `dividir_seguro(a, b)`: divide `a` por `b` e lança `ValueError` quando o divisor é zero.
- `porcentagem(valor, percentual)`: calcula o percentual informado de um valor.
- `media_ponderada(notas, pesos)`: calcula a média ponderada das notas. As listas devem ter o mesmo tamanho, não podem estar vazias e a soma dos pesos deve ser diferente de zero.
- `raiz_quadrada(numero)`: calcula a raiz quadrada de um número e lança `ValueError` para números negativos.
- `fatorial(numero)`: calcula o fatorial de um número inteiro não negativo e lança `ValueError` para números negativos.

Todas as funções possuem testes automatizados para casos de sucesso e entradas inválidas.


## Estrutura do projeto

- `funcoes.py`: contém as implementações das funções.
- `test_funcoes.py`: contém os testes automatizados em pytest.
- `requirements.txt`: lista as dependências do projeto.

## Como rodar os testes

1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute os testes:
   ```bash
   pytest -v
   ```

## Resultado esperado

Todos os testes devem passar com sucesso, confirmando que as funções estão funcionando corretamente.

# PARTICIPANTES : Robson 
Herick 
João Guilherme 
Ricardo
Alice
Maria Luana
