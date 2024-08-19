Bem-vindo a mais um projecto em Python

```markdown
# Gerador de palavra-passe

Este script Python gera uma palavra-passe segura com base em critérios definidos pelo usuário. O usuário pode especificar o comprimento mínimo da palavra-passe e se a palavra-passe deve incluir números e caracteres especiais. A palavra-passe é criada para garantir que atenda a esses critérios.

## Visão Geral do Código

O script usa os módulos `random` e `string` para gerar uma palavra-passe. Aqui está uma descrição detalhada do código e dos conceitos por trás dele:

### Imports

```python
import random
import string
```

- **`random`**: Fornece funções para gerar números aleatórios e fazer seleções aleatórias. É usado para selecionar caracteres aleatoriamente de um conjunto de caracteres possíveis.
- **`string`**: Contém constantes para operações comuns com strings. Usado aqui para obter conjuntos pré-definidos de caracteres, como letras, dígitos e caracteres especiais.

### Função: `generate_password`

```python
def generate_password(min_length, numbers=True, special_characters=True):
```

- **Parâmetros**:
  - `min_length`: O comprimento mínimo da palavra-passe gerada.
  - `numbers`: Um parâmetro booleano indicando se a palavra-passe deve incluir caracteres numéricos.
  - `special_characters`: Um parâmetro booleano indicando se a palavra-passe deve incluir caracteres especiais.

#### Inicialização do Conjunto de Caracteres

```python
letters = string.ascii_letters
digits = string.digits
special = string.punctuation
```

- **`letters`**: Contém todas as letras maiúsculas e minúsculas (por exemplo, `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`).
- **`digits`**: Contém todos os caracteres numéricos (por exemplo, `0123456789`).
- **`special`**: Contém todos os caracteres especiais (por exemplo, `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`).

#### Construindo o Conjunto de Caracteres

```python
characters = letters
if numbers:
    characters += digits
if special_characters:
    characters += special
```

- **Inicialização**: `characters` começa com o conjunto de letras.
- **Adicionando Dígitos**: Se `numbers` for `True`, adiciona `digits` a `characters`.
- **Adicionando Caracteres Especiais**: Se `special_characters` for `True`, adiciona `special` a `characters`.

#### Gerando a palavra-passe

```python
pwd = ""
meets_criteria = False
has_number = False
has_special = False
```

- **`pwd`**: Começa como uma string vazia. Vai acumular os caracteres da palavra-passe.
- **`meets_criteria`**: Um indicador de se a palavra-passe atual atende a todos os critérios.
- **`has_number`**: Um indicador de se a palavra-passe inclui pelo menos um caractere numérico.
- **`has_special`**: Um indicador de se a palavra-passe inclui pelo menos um caractere especial.

```python
while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(characters)
    pwd += new_char
    
    if new_char in digits:
        has_number = True
    elif new_char in special:
        has_special = True
        
    meets_criteria = True
    if numbers:
        meets_criteria = has_number
    if special_characters:
        meets_criteria = meets_criteria and has_special
```

- **Loop**: Continua até que a palavra-passe atenda a todos os critérios e tenha o comprimento mínimo.
- **`random.choice(characters)`**: Seleciona um caractere aleatório do conjunto `characters`.
- **Atualiza Indicadores**: Atualiza `has_number` e `has_special` com base no caractere recém-adicionado.
- **Atualiza `meets_criteria`**: Verifica se a palavra-passe atende a todos os critérios (inclui números e/ou caracteres especiais) e alcançou o comprimento mínimo.

```python
return pwd
```

- **Declaração de Retorno**: Retorna a palavra-passe gerada.

### Entrada do Usuário e Chamada da Função

```python
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y" 
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"             
            
pwd = generate_password(min_length, has_number, has_special)
print("Your supersafe password is: ", pwd)
```

- **Entrada do Usuário**: Solicita ao usuário que insira o comprimento mínimo e se deseja incluir números e caracteres especiais.
- **Chamada da Função**: Chama `generate_password` com os parâmetros definidos pelo usuário.
- **Saída**: Imprime a palavra-passe gerada.

## Conceito

O script usa randomização para gerar uma palavra-passe que atende a critérios específicos. Garante que a palavra-passe tenha o comprimento desejado e inclua certos tipos de caracteres com base nas preferências do usuário. Essa abordagem ajuda a criar palavra-passes fortes e seguras adequadas para várias aplicações.

Ao dividir o processo de geração de palavra-passe nesses passos, o script permite flexibilidade e personalização na criação de palavra-passes seguras.


## Sobre o Autor

Desenvolvido por **João Marcos Jová**.


- [![Instagram](https://img.shields.io/badge/Instagram-%40j.marcosjova-1DA1F2?logo=Instagram&logoColor=white)](https://Instagram.com/j.marcosjova)

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-%40joaomarcosjova-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joaomarcosjova/)

- [![GitHub](https://img.shields.io/badge/GitHub-%40joaomarcosjova-181717?logo=github&logoColor=white)](https://github.com/joaomarcosjova)


---

Sinta-se à vontade para usar este pequeno projecto como fonte de inspiração ou base para o seu desenvolvimento proficional. 
