# Correção Jogo do Bicho

Este programa oferece uma maneira eficiente e automatizada de corrigir suas apostas no Jogo do Bicho, utilizando os resultados da Loteria Federal. Com ele, você pode verificar rapidamente se seus palpites foram bem-sucedidos, sem precisar conferir manualmente cada resultado.

## Funcionalidades

O programa suporta várias modalidades de apostas no Jogo do Bicho, incluindo:

- **Milhar**
  - Seca
  - Cercada
  - Invertida
- **Centena**
  - Seca
  - Cercada
  - Invertida
- **Dezena**
  - Seca
  - Cercada
  - Invertida
  - Duque de Dezena
  - Terno de Dezena
- **Grupo**
  - Seco
  - Cercado
- **Dupla de Grupo**
  - Seco
  - Cercado
- **Terno de Grupo**
  - Seco
  - Cercado

## Como Funciona

O programa faz um **web scraping** com a biblioteca `Beautiful Soup` para buscar os resultados diretamente do site **Resultado Fácil**. Isso garante que os dados sejam sempre atualizados e precisos, proporcionando uma experiência confiável.
https://www.resultadofacil.com.br/resultado-banca-federal

## Requisitos

- Python 3.x
- Beautiful Soup 4
- Requests
- Pyautogui
- Time
- Itertools

## Como Usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   
2. Instale as dependências:

   ```bash
   pip install -r requirements
   
3. Execute o script principal::

   ```bash
   python main.py
---
>Passe, Quadra, à esquerda/ Algum dia...
