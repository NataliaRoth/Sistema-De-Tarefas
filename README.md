# Sistema de Tarefas em Python

Aplicação desenvolvida em Python com o objetivo de praticar lógica de programação e aplicar, na prática, os conhecimentos adquiridos durante meus estudos.

## Sobre o projeto

O Projeto "Sistema de Tarefas" é uma aplicação interativa executada pelo terminal que permite cadastrar, visualizar, editar e excluir tarefas, através de um menu. 

O projeto nasceu de uma base simples, focada em controle de fluxo, validação de entradas do usuário e exibição condicional de listas e evoluiu consideravelmente. Nas versões mais recentes, ganhou gerenciamento de prioridades (com indicadores visuais em emojis), ordenação automática inteligente, menus interativos dinâmicos com a biblioteca `questionary` e uma estrutura de código mais modularizada.

Esta aplicação faz parte do meu processo contínuo de aprendizagem em programação, servindo como um registro prático da minha evolução técnicas. 

![Imagem tela do projeto no vscode](<Imagem tela sistema de tarefas/FotoTelaSistemadeTarefas.png>)

## Funcionalidades

- 📋 **Visualizar Tarefas:** Exibe a lista completa de tarefas cadastradas de forma organizada.
- ➕ **Adicionar Tarefas:** Permite inserir novos itens e definir o respectivo nível de prioridade (🔴 Alta, 🟡 Moderada, 🟢 Leve).
- ✏️ **Editar Tarefas:** Atualiza tanto o texto quanto a prioridade de uma tarefa existente.
- 🗑️ **Excluir Tarefas:** Remove itens da lista com validação de índice para evitar erros.
- 📊 **Ordenação Automática:** As tarefas são ordenadas automaticamente por prioridade no momento da exibição.
- 🚪 **Encerrar Sistema:** Fecha a aplicação de forma controlada

## tecnologias e ferramentas
- Python
- VsCode
- Biblioteca `time` (para controle de tempo e pausas com `sleep`)
- Biblioteca `questionary` (para criação de prompts e seleções interativas no terminal)

## Conhecimentos utilizados

Durante o desenvolvimento foram utilizados conceitos como:

- **Estruturas de Dados:** Manipulação de listas, tuplas e dicionários para mapeamento de prioridades.
- **Controle de Fluxo:** Estruturas condicionais (`if`, `elif`, `else`) e de repetição (`while`, `for`).
- **Modularização:** Criação e chamada de funções personalizadas para limpeza de código (`Linha()`, `Espaco()`, `MostrarLista()`, `OrdenarTarefas()`, `Prioridades()`).
- **Tratamento de Exceções:** Uso de blocos `try` e `except` para capturar e tratar erros de digitação e índices inválidos (`ValueError`, `IndexError`).
- **Funções Avançadas e Utilitários:** Uso de funções lambda (`lambda`) para ordenação customizada, `enumerate()`, métodos de string (`.lower()`) e importação de bibliotecas nativas/externas (`sleep` do módulo `time` e `questionary`).

## Evolução do projeto

Este projeto continuará sendo desenvolvido conforme avanço nos meus estudos.

Entre as melhorias planejadas para versões futuras estão:

- Conclusão de tarefas (marcar itens como finalizados)
- Persistência de dados (salvamento em arquivos locais ou banco de dados)
* Novos filtros e melhorias gerais de usabilidade no terminal

## 🎯 Objetivo

Mais do que desenvolver uma aplicação funcional, este projeto tem como objetivo registrar minha evolução na programação e colocar em prática novos conhecimentos ao longo do processo.


[def]: Imagem