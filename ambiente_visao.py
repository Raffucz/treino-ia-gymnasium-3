import gymnasium as gym
import numpy as np
from gymnasium import spaces

class AmbienteVisao(gym.Env):
    def __init__(self):
        super().__init__()
        # A IA espera uma imagem de 100x100 pixels
        self.observation_space = spaces.Box(low=0, high=255, shape=(100, 100, 1), dtype=np.uint8)
        self.action_space = spaces.Discrete(4)

    def pegar_observacao(self):
        tela = np.zeros((5, 5, 1), dtype=np.uint8) # Cria uma tela preta de 5x5 pixels

        tela[self.monstro_x, self.monstroy, 0] = 50 # Monstro em cinza escuro
        tela[self.tesouro_x, self.tesouro_y, 0] = 150 # Tesouro em cinza claro
        tela[self.x, self.y, 0] = 255 # Agente em branco   
        
        # O ZOOM MATEMÁTICO: Expande os 5x5 para 100x100
        tela_ampliada = np.repeat(np.repeat(tela, 20, axis=0), 20, axis=1)
        return tela_ampliada

    def reset(self, seed=None, options=None):
        super().reset(seed=seed) # Evita o erro da semente do Gymnasium
        
        self.x = 0
        self.y = 0
        self.passos = 0
        self.monstro_x = np.random.randint(1, 5)
        self.monstroy = np.random.randint(1, 5)
        self.tesouro_x = np.random.randint(1, 5)
        self.tesouro_y = np.random.randint(1, 5)
        
        # Chamando a função com o nome correto agora
        return self.pegar_observacao(), {}

    def step(self, acao):
        self.passos += 1
        
        if acao == 0 and self.y < 4: self.y += 1  # Cima
        elif acao == 1 and self.y > 0: self.y -= 1  # Baixo
        elif acao == 2 and self.x > 0: self.x -= 1  # Esquerda
        elif acao == 3 and self.x < 4: self.x += 1  # Direita

        done = False
        reward = -1
        
        if self.x == self.tesouro_x and self.y == self.tesouro_y:
            done = True
            reward = 20
        elif self.x == self.monstro_x and self.y == self.monstroy:
            done = True
            reward = -15
        elif self.passos >= 50:
            done = True

        return self.pegar_observacao(), reward, done, False, {}