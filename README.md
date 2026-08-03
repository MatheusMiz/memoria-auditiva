
# 🔊 Memória Auditiva

O **Memória Auditiva** é um jogo de memória focado em **acessibilidade e design inclusivo**. Desenvolvido em Python com a biblioteca Pygame, o projeto substitui a dependência visual e do mouse por uma experiência baseada puramente em **comandos de teclado e feedbacks sonoros**.

O objetivo principal é encontrar os pares de sons de animais correspondentes, tornando o clássico jogo de memória totalmente jogável por pessoas com deficiência visual ou por qualquer um que queira testar sua percepção auditiva.

---

## 🚀 Diferenciais do Projeto 

* **Design Inclusivo & Acessibilidade:** O projeto foi concebido sob a premissa de que softwares devem ser acessíveis. A navegação elimina o uso do mouse, confiando 100% no teclado e no mapeamento espacial tátil das teclas.
* **Gerenciamento de Estado Dinâmico:** Implementação de uma máquina de estados simples, porém robusta, para alternar entre Menu Inicial, Telas de Jogo e Tela de Game Over/Reinício.
* **Lógica Antibug de Concorrência:** Tratamento de eventos de entrada assíncronos do Pygame, garantindo que o jogador não quebre a lógica de verificação ao interagir rapidamente com as teclas.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Biblioteca Principal:** Pygame (Módulos de Display, Mixer para áudio, Eventos e Time)

---

## 🎮 Como Jogar

O jogo é estruturado em uma matriz 4x4 (16 cartas no total). Cada carta esconde o som de um animal específico (Cachorro, Leão, Sapo, Cavalo, Elefante, Pássaro, Macaco e Gato).

### Mapeamento do Teclado

As teclas foram mapeadas para espelhar perfeitamente a grade física de cartas na tela, permitindo uma jogabilidade intuitiva:

| Linha Virtual | Teclas Correspondentes |
| --- | --- |
| **Linha 1** | `1` `2` `3` `4` |
| **Linha 2** | `Q` `W` `E` `R` |
| **Linha 3** | `A` `S` `D` `F` |
| **Linha 4** | `Z` `X` `C` `V` |

### Fluxo de Jogo

1. **Menu:** Pressione `ENTER` ou `ESPAÇO` para iniciar. Uma narração guiará o usuário com as instruções iniciais.
2. **Gameplay:** Digite a tecla correspondente à carta para revelá-la e ouvir o som do animal. Escolha a segunda carta para tentar formar o par.
3. **Resultado:** Se os sons forem iguais, o par permanece aberto (com efeito sonoro de acerto). Se falhar, as cartas se fecham após 1 segundo (com efeito de erro).
4. **Fim de Jogo:** Ao encontrar todos os pares, a narração de encerramento é tocada e você pode reiniciar pressionando `ENTER` ou `ESPAÇO`.

---

## 📁 Estrutura de Pastas Requerida

Para que o script funcione corretamente, o diretório do projeto deve seguir a estrutura abaixo:

```text
📂 Memoria-Auditiva/
│
├── 📄 Memoria_Auditiva.py    # Código-fonte principal
│
├── 📂 sons/                 # Efeitos sonoros do jogo
│   ├── 1.wav até 8.wav      # Sons dos 8 animais (pares)
│   ├── acerto.wav           # Som de feedback positivo
│   └── erro.wav             # Som de feedback negativo
│
├── 📂 imagens/              # Ativos visuais (suporte em tela)
│   ├── card_back.png        # Verso da carta
│   └── Face_[Animal].png    # Imagens das faces dos animais (8 arquivos)
│
└── 📂 narrador/             # Arquivos de acessibilidade por voz
    ├── inicio.mp3           # Narração de boas-vindas e regras
    └── fim.mp3              # Narração de parabéns/vitória

```

---

## 🔧 Como Executar o Projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/MatheusMiz/memoria-auditiva.git
cd memoria-auditiva

```


2. **Instale as dependências:**
Certifique-se de ter o Python instalado. Depois, instale o Pygame via pip:
```bash
pip install pygame

```


3. **Execute o jogo:**
```bash
python Memoria_Auditiva.py

```



---

## 📈 Próximos Passos & Melhorias Futuras

* [ ] Adicionar diferentes níveis de dificuldade (grades 6x6 ou limites de tentativas).


---
