import pygame
import random
import os

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

# Tamanho tela
LARGURA_TELA = 1000
ALTURA_TELA = 600
TAMANHO_CARTA = 100
MARGEM = 20

# Tamanho para as grades
LARGURA_GRADE = 4 * TAMANHO_CARTA + 5 * MARGEM
ALTURA_GRADE = 4 * TAMANHO_CARTA + 5 * MARGEM
offset_x = (LARGURA_TELA - LARGURA_GRADE) // 2
offset_y = (ALTURA_TELA - ALTURA_GRADE) // 2

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Memória Auditiva")

# Sons
sons = [pygame.mixer.Sound(os.path.join("sons", f"{i}.wav")) for i in range(1, 9)]
som_acerto = pygame.mixer.Sound(os.path.join("sons", "acerto.wav"))
som_erro = pygame.mixer.Sound(os.path.join("sons", "erro.wav"))

# Narração
narrador_inicio = os.path.join("narrador", "inicio.mp3")
narrador_fim = os.path.join("narrador", "fim.mp3")

# Faces das cartas
nomes_cartas = [
    "Face_Cachorro", "Face_Leao", "Face_Sapo", "Face_Cavalo",
    "Face_Elefante", "Face_Passaro", "Face_Macaco", "Face_Gato"
]
imagens_cartas = [pygame.image.load(os.path.join("imagens", f"{nome}.png")) for nome in nomes_cartas]
verso_carta = pygame.image.load((os.path.join("imagens", "card_back.png")))



def inicializar_jogo():
    pares = list(range(8)) * 2
    random.shuffle(pares)
    cartas_reveladas = [False] * 16
    carta_selecionada = []
    return pares, cartas_reveladas, carta_selecionada


pares, cartas_reveladas, carta_selecionada = inicializar_jogo()

fonte = pygame.font.SysFont(None, 48)

# teclas de cada carta
tecla_para_indice = {
    pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3,
    pygame.K_q: 4, pygame.K_w: 5, pygame.K_e: 6, pygame.K_r: 7,
    pygame.K_a: 8, pygame.K_s: 9, pygame.K_d: 10, pygame.K_f: 11,
    pygame.K_z: 12, pygame.K_x: 13, pygame.K_c: 14, pygame.K_v: 15,
}


def desenhar_cartas():
    tela.fill(PRETO)
    for i in range(4):
        for j in range(4):
            idx = i * 4 + j
            x = offset_x + MARGEM + j * (TAMANHO_CARTA + MARGEM)
            y = offset_y + MARGEM + i * (TAMANHO_CARTA + MARGEM)


            if cartas_reveladas[idx] or idx in carta_selecionada:
                imagem = imagens_cartas[pares[idx]]
                tela.blit(pygame.transform.scale(imagem, (TAMANHO_CARTA, TAMANHO_CARTA)), (x, y))
            else:
                tela.blit(pygame.transform.scale(verso_carta, (TAMANHO_CARTA, TAMANHO_CARTA)), (x, y))

    # legenda de teclas no canto da tela
    texto_teclas = fonte.render("Teclas de Seleção: 1-4, QWER, ASDF, ZXCV", True, AMARELO)
    tela.blit(texto_teclas, (10, ALTURA_TELA - 30))

    pygame.display.flip()


def restart(texto):
    global pares, cartas_reveladas, carta_selecionada

    tela.fill(PRETO)
    msg = fonte.render(texto, True, BRANCO)
    msg_rect = msg.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 50))
    tela.blit(msg, msg_rect)


    botao_largura, botao_altura = 300, 60
    botao_x = (LARGURA_TELA - botao_largura) // 2
    botao_y = ALTURA_TELA // 2 + 20
    botao_rect = pygame.Rect(botao_x, botao_y, botao_largura, botao_altura)

    pygame.draw.rect(tela, VERMELHO, botao_rect)
    texto_botao = fonte.render("Aperte ENTER para Reiniciar", True, BRANCO)
    texto_rect = texto_botao.get_rect(center=botao_rect.center)
    tela.blit(texto_botao, texto_rect)

    pygame.display.flip()

    if os.path.exists(narrador_fim):
        pygame.mixer.music.load(narrador_fim)
        pygame.mixer.music.play()
    else:
        print(
            f"Aviso: Arquivo de narração não encontrado em {narrador_fim}. O jogo será reiniciado sem som de narração.")

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    pares, cartas_reveladas, carta_selecionada = inicializar_jogo()
                    return True
    return False


def menu_inicial():
    tela.fill(PRETO)
    titulo = fonte.render("MEMÓRIA AUDITIVA", True, BRANCO)
    titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 250))
    tela.blit(titulo, titulo_rect)

    inicio =("Bem-vindo ao jogo Memória Auditiva!\n\n"
        "Seu objetivo é encontrar os pares de sons iguais usando apenas o teclado e sua audição.\n"
        "O jogo tem 16 cartas (4x4), cada uma com o som de um animal diferente.\n"
        "Você não precisa usar o mouse. Todas as ações são feitas pelo teclado.\n"
        "As teclas são organizadas assim:\n"
        "Linha 1: 1, 2, 3, 4\n"
        "Linha 2: Q, W, E, R\n"
        "Linha 3: A, S, D, F\n"
        "Linha 4: Z, X, C, V\n"
        "Ao virar uma carta, o som do animal será tocado. Se os sons das duas cartas forem iguais,\n"
        "você acertou. Caso contrário, as cartas serão viradas novamente.\n"
        "Continue até encontrar todos os pares. Boa sorte e divirta-se!"
    )
    linhas = inicio.split('\n')
    y = 80
    for linha in linhas:
        texto_render = pygame.font.SysFont(None, 28).render(linha, True, AMARELO)
        tela.blit(texto_render, (100, y))
        y += 35

    comando = fonte.render(
        "Aperte ENTER ou ESPAÇO para começar", True, AMARELO
    )
    comando_rect = comando.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 250))
    tela.blit(comando, comando_rect)

    pygame.display.flip()

    if os.path.exists(narrador_inicio):
        pygame.mixer.music.load(narrador_inicio)
        pygame.mixer.music.play()
    else:
        print(
            f"Aviso: Arquivo de narração não encontrado em {narrador_inicio}. O jogo será iniciado sem som de narração.")


    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    return True




estado_jogo = "MENU"

rodando = True
while rodando:

    if estado_jogo == "MENU":
        if menu_inicial():
            pygame.mixer.music.stop()
            estado_jogo = "JOGANDO"

    elif estado_jogo == "JOGANDO":

        desenhar_cartas()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key in tecla_para_indice:
                    idx = tecla_para_indice[evento.key]

                    if not cartas_reveladas[idx] and idx not in carta_selecionada and len(carta_selecionada) < 2:
                        carta_selecionada.append(idx)
                        sons[pares[idx]].play()

                        if len(carta_selecionada) == 2:

                            desenhar_cartas()
                            pygame.time.wait(1000)

                            i1, i2 = carta_selecionada
                            if pares[i1] == pares[i2]:
                                cartas_reveladas[i1] = True
                                cartas_reveladas[i2] = True
                                som_acerto.play()
                            else:
                                som_erro.play()

                            carta_selecionada = []

                            if all(cartas_reveladas):
                                restart("Parabéns! Você encontrou todos os pares!")

pygame.quit()
