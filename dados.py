import pygame
import random
import sys

# Inicialização
pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("☄️ Chuva de Dados RPG ☄️")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("consolas", 30)

# Cores
COR_BG = (10, 10, 30)
COR_JOGADOR = (255, 255, 255)
COR_TEXT = (255, 255, 0)

# Formas dos dados
FORMAS = {
    "D4": {"lados": 3, "efeito": -1},
    "D6": {"lados": 4, "efeito": 0},
    "D20": {"lados": 10, "efeito": +1}
}

# Classe jogador
class Jogador:
    def __init__(self):
        self.largura = 60
        self.altura = 20
        self.x = LARGURA // 2 - self.largura // 2
        self.y = ALTURA - 50
        self.vel = 6
        self.vida = 5
        self.pontos = 0

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT] and self.x < LARGURA - self.largura:
            self.x += self.vel

    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_JOGADOR, (self.x, self.y, self.largura, self.altura))

# Classe Dado (meteoro)
class Dado:
    def __init__(self):
        self.tipo = random.choice(list(FORMAS.keys()))
        self.raio = random.randint(20, 35)
        self.x = random.randint(self.raio, LARGURA - self.raio)
        self.y = -self.raio
        self.vel = random.randint(3, 6)
        self.cor = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

    def mover(self):
        self.y += self.vel

    def desenhar(self, tela):
        lados = FORMAS[self.tipo]["lados"]
        pontos = []
        for i in range(lados):
            ang = 2 * 3.14 * i / lados
            px = self.x + self.raio * pygame.math.Vector2(1, 0).rotate_rad(ang).x
            py = self.y + self.raio * pygame.math.Vector2(1, 0).rotate_rad(ang).y
            pontos.append((px, py))
        pygame.draw.polygon(tela, self.cor, pontos)

    def colidiu_com(self, jogador):
        return (
            self.y + self.raio > jogador.y and
            jogador.x < self.x < jogador.x + jogador.largura
        )

# Inicializa o herói e os dados
jogador = Jogador()
dados = []
tempo_spawn = 0

# Loop principal
while True:
    CLOCK.tick(60)
    TELA.fill(COR_BG)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)

    # Spawna novos dados
    tempo_spawn += 1
    if tempo_spawn > 30:
        dados.append(Dado())
        tempo_spawn = 0

    # Atualiza dados
    for dado in dados[:]:
        dado.mover()
        dado.desenhar(TELA)

        if dado.colidiu_com(jogador):
            efeito = FORMAS[dado.tipo]["efeito"]
            if efeito == -1:
                jogador.vida -= 1
            elif efeito == 1:
                jogador.pontos += 1
            # remove dado após colisão
            dados.remove(dado)

        elif dado.y > ALTURA:
            dados.remove(dado)

    # Desenha jogador
    jogador.desenhar(TELA)

    # HUD
    texto = FONT.render(f"Vida: {jogador.vida}   Pontos: {jogador.pontos}", True, COR_TEXT)
    TELA.blit(texto, (20, 20))

    # Game over
    if jogador.vida <= 0:
        texto_gameover = FONT.render("GAME OVER - Pressione ESC para sair", True, (255, 50, 50))
        TELA.blit(texto_gameover, (200, ALTURA//2))
        pygame.display.flip()
        # Espera input
        esperando = True
        while esperando:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    pygame.display.flip()
