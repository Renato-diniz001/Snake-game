import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Definir tamanho da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

# Definir título da janela
pygame.display.set_caption("Cobra")

# Definir tamanho da cobra
tamanho_cobra = 20

# Definir velocidade da cobra
velocidade = 7

# Definir direção da cobra
direcao = "direita"

# Definir posição da cobra
cobra = [(200, 200), (220, 200), (240, 200)]

# Definir posição da comida
comida = (400, 300)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != "baixo":
                direcao = "cima"
            elif evento.key == pygame.K_DOWN and direcao != "cima":
                direcao = "baixo"
            elif evento.key == pygame.K_LEFT and direcao != "direita":
                direcao = "esquerda"
            elif evento.key == pygame.K_RIGHT and direcao != "esquerda":
                direcao = "direita"

    # Mover cobra
    cabeça = cobra[-1]
    if direcao == "cima":
        nova_cabeça = (cabeça[0], cabeça[1] - tamanho_cobra)
    elif direcao == "baixo":
        nova_cabeça = (cabeça[0], cabeça[1] + tamanho_cobra)
    elif direcao == "esquerda":
        nova_cabeça = (cabeça[0] - tamanho_cobra, cabeça[1])
    elif direcao == "direita":
        nova_cabeça = (cabeça[0] + tamanho_cobra, cabeça[1])

    cobra.append(nova_cabeça)

    # Verificar colisão com comida
    if cobra[-1] == comida:
        comida = (random.randint(0, largura - tamanho_cobra) // tamanho_cobra * tamanho_cobra,
                  random.randint(0, altura - tamanho_cobra) // tamanho_cobra * tamanho_cobra)
    else:
        cobra.pop(0)

    # Verificar colisão com parede ou consigo mesmo
    if (cobra[-1][0] < 0 or cobra[-1][0] >= largura or
            cobra[-1][1] < 0 or cobra[-1][1] >= altura or
            cobra[-1] in cobra[:-1]):
        pygame.quit()
        sys.exit()

    # Desenhar tela
    tela.fill(preto)
    for posicao in cobra:
        pygame.draw.rect(tela, branco, (posicao[0], posicao[1], tamanho_cobra, tamanho_cobra))
    pygame.draw.rect(tela, vermelho, (comida[0], comida[1], tamanho_cobra, tamanho_cobra))
    pygame.display.update()

    # Controlar velocidade
    pygame.time.Clock().tick(velocidade)
