from stable_baselines3 import PPO
from ambiente_visao import AmbienteVisao


ambiente = AmbienteVisao()
modelo = PPO.load("modelo_ppo_visao")  

obs, _ = ambiente.reset()
done = False
traducao = {0: "cima", 1: "baixo", 2: "esquerda", 3: "direita"}

def desenhar_tela(observacao):
    print("-" * 20)
    for linha in range(5):
        texto_linha = ""
        for coluna in range(5):
            pixel = observacao[linha * 20, coluna * 20, 0]
            if pixel == 255: texto_linha += "🤖 "
            elif pixel == 150: texto_linha += "💰 "
            elif pixel == 50: texto_linha += "👹 "
            else: texto_linha += "⬛ "
        print(texto_linha)
    print("-" * 20)

print("iniciando")
desenhar_tela(obs)
while not done:
    acao, _ = modelo.predict(obs, deterministic=True)
    obs, reward, done, _, _ = ambiente.step(acao)
    print(f"Ação tomada: {traducao[int(acao)]}")
    desenhar_tela(obs)
    print(f"Recompensa: {reward}")