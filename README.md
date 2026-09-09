# Projeto de Funções em Python

Este projeto foi desenvolvido para uma atividade acadêmica com foco em funções básicas de Python e testes automatizados com pytest.

## Funções implementadas

- `is_par(numero)`: verifica se um número é par.
- `soma_lista(lista)`: calcula a soma dos elementos de uma lista.
- `inverter_string(texto)`: retorna a string invertida.
- `maior_valor(lista)`: retorna o maior valor da lista e lança `ValueError` se a lista estiver vazia.
- `eh_palindromo(texto)`: verifica se uma frase ou palavra é palíndroma, ignorando espaços e diferenças entre maiúsculas/minúsculas.

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
