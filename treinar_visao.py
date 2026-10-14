import os
from stable_baselines3 import PPO
from ambiente_visao import AmbienteVisao


ambiente = AmbienteVisao()
caminho = "modelo_ppo_visao"

if os.path.exists(caminho):
    print("Carregando modelo existente...")
    modelo = PPO.load(caminho, env=ambiente, verbose=1)
else:
    print("Criando novo modelo...")
    modelo = PPO("CnnPolicy", ambiente, verbose=1)

print("Treinamento iniciado..." )
modelo.learn(total_timesteps=50000)

modelo.save(caminho)
print("Modelo salvo em", caminho)