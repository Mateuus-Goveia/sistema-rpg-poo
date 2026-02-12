# 🛡️ RPG de Turnos - Simulação em Python

Este é um projeto de batalha RPG em turnos desenvolvido para aplicar e consolidar conceitos fundamentais de **Programação Orientada a Objetos (POO)** em Python.

## 🚀 Objetivo

O objetivo principal foi construir um sistema onde diferentes classes de personagens interagem entre si, utilizando pilares da POO para garantir um código limpo, escalável e organizado.

## 🧠 Conceitos de POO Aplicados

Neste projeto, foquei na implementação dos seguintes conceitos:

* **Abstração:** Criação de uma classe base `Personagem` que define atributos e comportamentos comuns.
* **Herança:** As classes `Guerreiro` e `Mago` herdam da classe base, reaproveitando lógica e adicionando especializações.
* **Polimorfismo:** O método de `tomar_dano` foi sobrescrito na classe `Guerreiro` para incluir a lógica de redução por armadura.
* **Encapsulamento:** Proteção de atributos sensíveis (como a vida e o dano) para garantir que o estado do objeto seja alterado apenas através de métodos específicos.
* **Composição:** Personagens podem possuir objetos da classe `Arma`, demonstrando como objetos podem ser compostos por outros.

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)

## 🎮 Como Funciona

O sistema permite criar personagens com atributos distintos e realizar batalhas em turnos.

```python
# Exemplo de uso
espada = Arma(nome="Excalibur", dano_extra=10)
arthur = Guerreiro(nome="Arthur")
arthur.equipar(espada)

merlin = Mago(nome="Merlin")

# Início do combate
arthur.atacar(merlin)

```

## 🎯 Evoluções Futuras

* [ ] Adicionar sistema de esquiva baseado em agilidade.
* [ ] Implementar poções de cura (Itens consumíveis).
* [ ] Criar uma interface básica via terminal com menus interativos.

---

**Desenvolvido por [Matheus Goveia]**
*Conecte-se comigo no [LinkedIn*](www.linkedin.com/in/matheus-goveia)

---
