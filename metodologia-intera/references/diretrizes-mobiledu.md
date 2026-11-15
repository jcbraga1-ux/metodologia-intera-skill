> Este arquivo faz parte da Intera-IA (skill metodologia-intera) e reproduz a skill `mobiledu-diretrizes` v1.0.2, licença CC BY-NC 4.0, DOI 10.5281/zenodo.23809314 (https://github.com/jcbraga1-ux/mobiledu-skill). Onde o texto abaixo diz "esta skill", leia "este conjunto de diretrizes". Não edite aqui: as correções são feitas na skill separada e copiadas para cá a cada versão.

# Biblioteca MobileDU – Diretrizes de Desenho Universal para aplicações móveis

Fonte: COLETTO, Carlos Jair. *Diretrizes para o Desenvolvimento de Aplicações Móveis Voltadas para o Desenho Universal: A Biblioteca MobileDU*. Tese (Doutorado em Ciência da Computação) – Universidade Federal do ABC, Grupo de Pesquisa INTERA, Santo André, 2026. Orientação: Juliana Cristina Braga.

Ideia central: o aplicativo deve deixar cada pessoa ajustar a interface do seu jeito, em vez de oferecer uma única versão para todos. Três ideias sustentam as diretrizes: flexibilidade de uso, redundância sensorial e independência de dispositivo.

Siglas das referências: Nery = diretrizes do Módulo Configurador (Nery, 2021); WCAG = Web Content Accessibility Guidelines; GDAMA = Guia de Diretrizes de Acessibilidade para Aplicações Móveis; NBR 17060 = ABNT NBR 17060:2022.

## Como usar

- **Consulta:** responda citando o número da diretriz (ex.: "MobileDU 6.6"), o nome e as referências de origem.
- **Auditoria de app ou protótipo:** percorra as 8 categorias e, para cada diretriz, marque Atende / Não atende / Não se aplica, com evidência (tela, comportamento). Termine com as lacunas priorizadas e o critério WCAG relacionado.
- **Geração de requisitos:** transforme cada diretriz aplicável em requisito do projeto, com identificador, descrição sem ambiguidade, origem ("MobileDU X.Y") e critério de aceitação testável. Lembre: diretriz vale para uma classe de sistemas; requisito, para um sistema específico.
- **Ensino:** use os exemplos do caso fictício da UBS Jardim Esperança (abaixo) e explique quem se beneficia de cada categoria.
- Nunca invente diretrizes, números ou referências que não estejam nesta lista. Se algo não estiver aqui, diga que não consta na MobileDU.

## Observações de revisão

- 6.9 não tem referência na tese; ao aplicá-la, a cor deve complementar um texto ou símbolo (WCAG 1.4.1), nunca ser o único meio.
- 6.6 cita WCAG 2.5.5 (AAA); o mínimo AA da WCAG 2.2 é 2.5.8 (24 × 24 px CSS).

## As 60 diretrizes

### 1. Ambiente (11)
Foco: cor, brilho, luz ambiente, orientação e tempo. Quem se beneficia: baixa visão, daltonismo, sensibilidade à luz, epilepsia, enxaqueca, limitação motora, quem precisa de mais tempo. Exemplo UBS: Dona Cida inverte as cores para ler a confirmação; um paciente com epilepsia desliga as animações; o tempo para escolher o horário pode ser prolongado.

- 1.1 Cor – Personalizar cor da tela: escolher a cor da tela. (Nery 2.2.1 · WCAG 1.4.8 · GDAMA R02)
- 1.2 Cor – Inverter as cores da tela. (Nery 2.2.2 · WCAG 1.4.8 · GDAMA R02)
- 1.3 Cor – Reduzir o ponto branco: reduz a intensidade das cores brilhantes. (Nery 1.1.2)
- 1.4 Cor – Filtro da cor da tela: escolher o conjunto de cores da película. (Nery 2.2.3 · GDAMA R02)
- 1.5 Cor – Intensidade e contraste da cor da tela. (Nery 2.2.4 · WCAG 1.4.3, 1.4.6, 1.4.11 · GDAMA R02, R03 · NBR 17060 1.1.17)
- 1.6 Brilho automático: ajusta brilho e contraste conforme a luz ambiente. (Nery 1.1.1 · NBR 17060 1.1.17)
- 1.7 Animação de telas: reduzir o movimento da interface. (Nery 1.1.4 · WCAG 2.2.2, 2.3.1, 2.3.2, 2.3.3 · NBR 17060 1.1.25, 1.2.9)
- 1.8 Elementos piscantes: poder desabilitá-los. (NBR 17060 1.1.25)
- 1.9 Orientação da tela: escolher a orientação. (WCAG 1.3.4 · GDAMA R04)
- 1.10 Tempo de utilização: ajustar, prolongar ou desativar limites de tempo. (WCAG 2.2.1, 2.2.3, 2.2.5, 2.2.6 · GDAMA R26 · NBR 17060 1.2.6)
- 1.11 Idioma: trocar o idioma, quando disponível. (WCAG 3.1.1, 3.1.2 · NBR 17060 1.1.24)

### 2. Texto (6)
Foco: tipografia, tamanho, negrito, contraste e espaçamento. Quem se beneficia: pessoas idosas, baixa visão, dislexia, baixo letramento. Exemplo UBS: orientações de preparo para exame lidas com letra maior, negrito e mais espaço entre linhas, sem cortar botões.

- 2.1 Tipo de fonte: escolher o tema da fonte. (Nery 2.1.1 · WCAG 1.4.5, 1.4.9)
- 2.2 Negrito: deixar o texto em negrito. (Nery 2.1.2 · WCAG 1.4.5, 1.4.9)
- 2.3 Tamanho de fonte. (Nery 2.1.3 · WCAG 1.4.5, 1.4.9)
- 2.4 Cor da fonte. (Nery 2.1.4 · WCAG 1.4.5, 1.4.9 · GDAMA R02)
- 2.5 Contraste da fonte: escolher a relação de contraste. (WCAG 1.4.3, 1.4.6 · GDAMA R02, R03 · NBR 17060 1.1.17)
- 2.6 Espaçamento da fonte: altura da linha e espaçamento entre parágrafos, letras e palavras. (WCAG 1.4.5, 1.4.9, 1.4.12)

### 3. Som (15)
Foco: controle de áudio, leitor de tela e retorno ao digitar. Quem se beneficia: pessoas cegas ou com baixa visão, baixo letramento, dificuldade de concentração com sons de fundo. Exemplo UBS: ao digitar o CPF, o leitor fala cada número; o paciente ajusta a velocidade da voz e ouve "Consulta confirmada" sem música de fundo.

- 3.1 Silenciar todos os efeitos sonoros. (Nery 1.1.3)
- 3.2 Mecanismo de controle de áudio: parar, pausar, aumentar, diminuir. (WCAG 1.4.2 · NBR 17060 1.2.7)
- 3.3 Áudio de fundo: desativá-lo, mantendo o primeiro plano. (WCAG 1.4.7)
- 3.4 Leitor de tela: ativar ou não. (Nery 3.1.1)
- 3.5 Leitor de tela – Velocidade da fala. (Nery 3.1.2)
- 3.6 Leitor de tela – Timbre da fala. (Nery 3.1.3)
- 3.7 Leitor de tela – Leitura de todo o conteúdo. (Nery 3.2.1)
- 3.8 Leitor de tela – Como falar a pontuação. (Nery 3.2.2)
- 3.9 Leitor de tela – Falar o texto detectado no item em foco. (Nery 3.2.3 · GDAMA R32)
- 3.10 Leitor de tela – Tratamento de letras e palavras em maiúsculo. (Nery 3.2.4)
- 3.11 Leitor de tela – Ler cabeçalhos de tabelas. (Nery 3.2.5)
- 3.12 Leitor de tela – Indicar número de linhas e colunas. (Nery 3.2.6)
- 3.13 Leitor de tela – Indicar emojis. (Nery 3.2.7)
- 3.14 Modo de leitura ao digitar: letras, palavras ou retorno fonético. (Nery 3.3.1)
- 3.15 Falar a palavra inteira ao terminar de digitá-la. (Nery 3.3.2)

### 4. Vídeo (7)
Foco: legendas, Libras e audiodescrição. Quem se beneficia: pessoas surdas ou com deficiência auditiva, usuárias de Libras, pessoas cegas, quem assiste sem som. Exemplo UBS: vídeo da campanha de vacinação com janela de Libras, legenda ajustável com fundo escuro e audiodescrição nas pausas.

- 4.1 Legenda – Ativar ou desativar. (WCAG 1.2.1, 1.2.2, 1.2.3, 1.2.4 · NBR 17060 1.3.1)
- 4.2 Legenda – Fonte e estilo preferidos (contornado, clássico). (Nery 2.4.1 · NBR 17060 1.3.1)
- 4.3 Legenda – Tamanho da fonte. (Nery 2.4.2 · NBR 17060 1.3.1)
- 4.4 Legenda – Cor e opacidade da fonte. (Nery 2.4.3 · NBR 17060 1.3.1)
- 4.5 Legenda – Cor de fundo e opacidade da caixa. (Nery 2.4.4 · NBR 17060 1.3.1)
- 4.6 Ativar a janela de Libras nos vídeos. (Nery 2.4.5 · WCAG 1.2.6 · NBR 17060 1.3.5)
- 4.7 Audiodescrição quando parte do vídeo não está disponível ou nas pausas dos diálogos. (WCAG 1.2.5, 1.2.7, 1.2.8, 1.2.9 · NBR 17060 1.3.2)

### 5. Zoom (5)
Foco: ampliação da tela e acompanhamento do foco. Quem se beneficia: baixa visão, pessoas idosas. Exemplo UBS: com a lupa em janela flutuante, Dona Cida amplia o calendário e a ampliação acompanha o campo de horário.

- 5.1 Ativar o zoom: ampliar a tela ou parte dela. (Nery 1.2.1 · WCAG 1.4.4, 1.4.8 · NBR 17060 1.2.16)
- 5.2 Seguir o foco de seleção. (Nery 1.2.2)
- 5.3 Exibir controle do zoom na tela. (Nery 1.2.3)
- 5.4 Visibilidade do controle do zoom. (Nery 1.2.4)
- 5.5 Janela de ampliação ou tela inteira e ampliação máxima. (Nery 1.2.5)

### 6. Entrada de dados (12)
Foco: cursor, toque e digitação. Quem se beneficia: tremor, limitação motora, baixa visão, pessoas idosas, uso em movimento. Exemplo UBS: paciente com tremor toca nos horários graças à área clicável ampliada; nome e telefone preenchidos automaticamente; confirmação por voz.

- 6.1 Modelo do cursor: contorno mais grosso. (Nery 2.3.1)
- 6.2 Visualização do cursor: cor e transparência do contorno. (Nery 2.3.2)
- 6.3 Ação de cada tipo de toque: simples, com arraste, duplo, longo. (Nery 4.1.1)
- 6.4 Intervalo de tempo de um toque. (Nery 4.1.2)
- 6.5 Intervalo de duração de um toque longo. (Nery 4.1.3)
- 6.6 Aumentar a área clicável em volta de um ícone. (WCAG 2.5.5 · GDAMA R13 · NBR 17060 1.2.13)
- 6.7 Destacar o campo em edição com borda ou cor. (WCAG 2.4.7 · NBR 17060 1.1.15)
- 6.8 Preenchimento automático por tipo de campo (nome, e-mail, telefone). (WCAG 1.3.5 · GDAMA R27)
- 6.9 Campo obrigatório exibido com cor diferente. (sem referência na tese)
- 6.10 Digitação por toque direto. (Nery 4.2.1)
- 6.11 Digitação com confirmação de voz. (Nery 4.2.2)
- 6.12 Digitação datilográfica: a letra é digitada ao soltar o dedo. (Nery 4.2.3)

### 7. Notificações e alertas (3)
Foco: avisos multimodais. Quem se beneficia: pessoas surdas, pessoas cegas, quem não está olhando a tela. Exemplo UBS: o lembrete "Sua consulta é amanhã às 10h" é lido em voz alta e faz o flash piscar.

- 7.1 Ouvir notificações pelo leitor de tela. (Nery 1.1.5 · GDAMA R46 · NBR 17060 1.2.3)
- 7.2 Piscar o flash para alertas. (Nery 1.1.6)
- 7.3 Feedback sonoro sobre ações. (GDAMA R33 · NBR 17060 1.1.20)

### 8. Gestos (1)
Foco: navegação por movimento. Quem se beneficia: limitação motora, quem não consegue fazer certos gestos, celular preso à cadeira de rodas. Exemplo UBS: quem não consegue deslizar dois dedos troca o gesto por toque duplo para voltar.

- 8.1 Controle do app por gestos ou movimentos configuráveis. (WCAG 2.5.1, 2.5.2, 2.5.4, 2.5.7, 2.5.8 · GDAMA R27 · NBR 17060 1.2.2)