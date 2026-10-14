# Agente de Visão Computacional com Gymnasium, PPO e CNN (`CnnPolicy`)

Este projeto demonstra como treinar um agente de Aprendizagem por Reforço que aprende a jogar tomando decisões a partir de **imagens de entrada (pixels)** em vez de coordenadas numéricas diretas[cite: 5, 7].

O ambiente simula uma matriz 2D representada em formato de imagem em tons de cinza ($100 \times 100 \times 1$), onde o agente utiliza uma **Rede Neural Convolucional (CNN)** via algoritmo **PPO** para identificar visualmente onde estão o jogador, o tesouro e o monstro[cite: 5, 7].

---

## 👁️ Como Funciona o Ambiente (`AmbienteVisao`)

* **Processamento Visual:**
  * O mapa base possui tamanho $5 \times 5$, onde cada entidade é desenhada com uma intensidade de cor diferente em escala de cinza[cite: 5]:
    * **Agente (Robô 🤖):** Valor de pixel `255` (Branco)[cite: 5, 6]
    * **Tesouro (Tesouro 💰):** Valor de pixel `150` (Cinza claro)[cite: 5, 6]
    * **Monstro (Monstro 👹):** Valor de pixel `50` (Cinza escuro)[cite: 5, 6]
    * **Espaço Vazio:** Valor de pixel `0` (Preto)[cite: 5, 6]
  * A tela é redimensionada via ampliação de pixels para uma imagem de **$100 \times 100 \times 1$**, que serve de entrada para a rede convolucional (`spaces.Box(0, 255, (100, 100, 1))`)[cite: 5].

* **Espaço de Ações (`Action Space`):** Discreto (`4` direções)[cite: 5]
  * `0`: Cima[cite: 5, 6]
  * `1`: Baixo[cite: 5, 6]
  * `2`: Esquerda[cite: 5, 6]
  * `3`: Direita[cite: 5, 6]

* **Sistema de Recompensas (`Reward System`):**
  * Passos normais: `-1` (para incentivar o agente a otimizar a rota)[cite: 5].
  * Encontrar o Tesouro: `+20` (Episódio finalizado com sucesso)[cite: 5].
  * Encontrar o Monstro: `-15` (Episódio finalizado com derrota)[cite: 5].
  * Limite por partida: `50` passos[cite: 5].

---

## 📁 Estrutura do Projeto

* **`ambiente_visao.py`**: Classe do ambiente customizado que herda de `gym.Env`. Desenha o estado do jogo como uma matriz de pixels e amplia para $100 \times 100$[cite: 5].
* **`treinar_visao.py`**: Script de treinamento incremental que utiliza a política **`CnnPolicy`** da biblioteca **Stable-Baselines3**. Salva e recarrega os pesos do arquivo `modelo_ppo_visao`.
* **`assistir.py`**: Script de renderização/inferência em tempo real no console, convertendo os pixels do ambiente em emojis para acompanhar a partida passo a passo.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Gymnasium**
* **Stable-Baselines3** (com suporte a CNN)[cite: 7]
* **NumPy**

---

## 📦 Instalação

Instale as dependências necessárias executando:

```bash
pip install gymnasium stable-baselines3 numpy
