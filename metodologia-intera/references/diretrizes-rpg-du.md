> Este arquivo faz parte da Intera-IA (skill metodologia-intera) e reproduz a skill `rpg-du-diretrizes` v1.0.0, licença CC BY 4.0, DOI 10.5281/zenodo.23836531 (https://github.com/jcbraga1-ux/rpg-du-skill). Onde o texto abaixo diz "esta skill", leia "este conjunto de diretrizes". Não edite aqui: as correções são feitas na skill separada e copiadas para cá a cada versão.

# Diretrizes de Design Universal para jogos educacionais digitais do tipo RPG

Fonte: CUNHA, Francinete Furtado da. *Diretrizes para o design universal de jogos educacionais digitais do tipo Role Play Games (RPG)*. Dissertação (Mestrado em Ciência da Computação) – Universidade Federal do ABC, Grupo de Pesquisa INTERA, Santo André, 2022. Orientadora: Juliana Braga.

Ideia central: jogos educacionais do gênero RPG devem ser projetados desde o início para pessoas com e sem deficiência, seguindo o Design Universal (DU), em vez de receber acessibilidade como adaptação posterior.

## Origem das 88 diretrizes

- **1 a 30 – Literatura** (Tabela 5.2 da dissertação): extraídas de uma revisão sistemática da literatura. Cada uma traz o autor de origem.
- **31 a 88 – Estudo de campo** (Tabela 5.3): vieram do desenvolvimento do jogo "Expedição Antártica", testado com 10 usuários (pessoas sem deficiência e pessoas com deficiência auditiva, visual e cognitiva). Cada uma traz a necessidade do usuário que a originou, o critério WCAG relacionado e os princípios do DU atendidos.
- A diretriz 31 corresponde à Tab. 5.3 nº 1, a 32 à nº 2, e assim por diante (diretriz = nº da Tab. 5.3 + 30).

## Categorias (elementos do jogo)

- **Estética** (25): aparência, imagens, cores, contraste, tipografia, interface.
- **Narrativa** (31): história, personagens, diálogos, instruções e textos.
- **Mecânica** (37): regras, controles, interação, tempo, feedback, erros.

Algumas diretrizes pertencem a mais de uma categoria.

## Os 7 princípios do Design Universal (numeração usada nas diretrizes)

1. Uso equitativo
2. Flexibilidade no uso
3. Uso simples e intuitivo
4. Informação perceptível
5. Tolerância ao erro
6. Baixo esforço físico
7. Tamanho e espaço para aproximação e uso

## Como usar

- **Consulta:** abra `references/diretrizes-rpg-du-completas.md` e responda citando o número ("Diretriz RPG-DU 31"), o título, o nome original na dissertação, a categoria, a origem e a fonte.
- **Auditoria de jogo ou protótipo:** percorra as três categorias e, para cada diretriz, marque Atende / Não atende / Não se aplica, com evidência (tela, comportamento). Termine com as lacunas priorizadas e o critério WCAG relacionado.
- **Geração de requisitos:** transforme cada diretriz aplicável em requisito do jogo, com identificador, descrição sem ambiguidade, origem ("RPG-DU 45") e critério de aceitação testável. Use o campo "Necessidade do usuário" como justificativa.
- **Ensino:** use os exemplos de cada diretriz e o jogo "Expedição Antártica" como caso.
- Nunca invente diretrizes, números, necessidades ou referências que não estejam no arquivo. Se algo não constar, diga que não está nas diretrizes da dissertação.

## Observações de revisão

- Os títulos foram reescritos para ficar mais claros; o nome original da dissertação vem em "Original".
- "WCAG (dissertação)" é o critério da WCAG 2.0 indicado no texto original. "NA" significa que a dissertação não associou critério.
- "Sugestão WCAG 2.2" **não faz parte do texto original**: é uma sugestão de atualização para a WCAG 2.2. Ao citar, deixe isso claro.
- Duas diretrizes do estudo de campo aparecem duplicadas na dissertação (Tab. 5.3 nº 22 = nº 47 e nº 46 = nº 54, ou seja, diretrizes 52 = 77 e 76 = 84). Foram mantidas para preservar a numeração original.

## Índice das 88 diretrizes

O texto completo de cada diretriz (descrição, exemplo, necessidade, WCAG, princípios e fonte) está em `references/diretrizes-rpg-du-completas.md`.

- 1. Usar botões com relevo visual e/ou destaque perceptível — Estética · Literatura
- 2. Usar fonemas como apoio auditivo para letras e palavras — Mecânica · Literatura
- 3. Permitir ler e escrever ao mesmo tempo — Mecânica · Literatura
- 4. Permitir visualizar claramente as palavras durante a interação — Mecânica · Literatura
- 5. Manter cores fortes e contrastantes — Estética · Literatura
- 6. Manter conversa individual entre sistema e jogador — Mecânica e Narrativa · Literatura
- 7. Permitir revisar conteúdos e ações — Mecânica · Literatura
- 8. Apresentar cálculos de forma acessível — Narrativa · Literatura
- 9. Encorajar o usuário com feedback motivacional — Narrativa · Literatura
- 10. Usar tema e personagens familiares e dar ao jogador um propósito claro — Narrativa · Literatura
- 11. Proporcionar múltiplos meios de ação e expressão — Estética · Literatura
- 12. Permitir ampliar texto e elementos do jogo (cursores, botões e menus) — Estética · Literatura
- 13. Usar sinalizadores e variáveis para controlar o avanço na trama — Estética · Literatura
- 14. Oferecer mecanismo de adaptação personalizada da experiência do jogo — Mecânica e Estética · Literatura
- 15. Usar cor de ênfase no botão principal — Estética · Literatura
- 16. Estimular a lógica de pensamento e permitir repetições — Narrativa · Literatura
- 17. Permitir acionar botões de ação por toque duplo (ex.: “finalizar compra”) — Mecânica · Literatura
- 18. Permitir acessar listas por toque duplo (ex.: “lista de produtos”) — Mecânica · Literatura
- 19. Oferecer comandos por teclado e por voz, além do apontar e clicar — Mecânica · Literatura
- 20. Aceitar comandos em linguagem natural, com sinônimos para ações, objetos e personagens — Mecânica · Literatura
- 21. Fornecer múltiplos meios de engajamento — Narrativa · Literatura
- 22. Usar gestos de toque apenas em objetos bem reconhecíveis — Mecânica · Literatura
- 23. Evitar o uso de rolagem — Mecânica · Literatura
- 24. Exibir informações críticas no centro da tela — Estética · Literatura
- 25. Utilizar modelo iterativo de desenvolvimento (DGBL) — Narrativa · Literatura
- 26. Utilizar o DUA (UDL) como lista de verificação — Mecânica · Literatura
- 27. Coletar dados de uso para análise da aprendizagem e adaptação do jogo — Narrativa · Literatura
- 28. Evitar especificar o jogo em excesso — Narrativa · Literatura
- 29. Disponibilizar diferentes esquemas de controle e controladores — Narrativa · Literatura
- 30. Considerar a acessibilidade desde as fases iniciais do design — Estética, Narrativa e Mecânica · Literatura
- 31. Nomear os elementos presentes nas imagens — Estética · Campo
- 32. Permitir repetir o conteúdo textual conforme a necessidade — Mecânica · Campo
- 33. Identificar o nome do personagem antes da sua fala — Narrativa · Campo
- 34. Disponibilizar audiodescrição de todo conteúdo de imagem do jogo — Narrativa · Campo
- 35. Apresentar a audiodescrição das imagens antes do conteúdo de interação — Narrativa · Campo
- 36. Padronizar a ordem da audiodescrição: de fora para dentro e de cima para baixo — Narrativa · Campo
- 37. Disponibilizar em Libras todo o conteúdo textual do jogo — Narrativa · Campo
- 38. Permitir repetição ilimitada do conteúdo em Libras, por meio de ícone — Narrativa · Campo
- 39. Permitir repetição ilimitada da audiodescrição, por meio de ícone — Narrativa · Campo
- 40. Disponibilizar identificação sonora para passos, ações do jogo, ambiente, teclado e animais — Narrativa · Campo
- 41. Disponibilizar som específico para cada tipo de personagem quando o jogador se aproximar — Narrativa · Campo
- 42. Anunciar em áudio o nome do personagem ao iniciar a interação — Narrativa · Campo
- 43. Disponibilizar informações essenciais da mecânica no título da interface — Estética · Campo
- 44. Manter padronizada a localização dos elementos nas interfaces dos minijogos — Estética · Campo
- 45. Informar erro e acerto por som, cor e texto — Narrativa · Campo
- 46. Disponibilizar controle de áudio do jogo — Mecânica · Campo
- 47. Disponibilizar controle independente do áudio das ações e dos efeitos sonoros — Mecânica · Campo
- 48. Garantir contraste mínimo para texto e imagens de texto — Estética · Campo
- 49. Permitir que o jogador ajuste o contraste de imagens e textos — Estética · Campo
- 50. Permitir personalizar a cor do cursor do mouse — Estética · Campo
- 51. Manter o diálogo em primeiro plano e os efeitos sonoros em segundo plano — Mecânica · Campo
- 52. Pausar o minijogo automaticamente quando o jogador pedir instruções ou informações — Mecânica · Campo
- 53. Garantir contraste adequado entre o texto e o fundo — Estética · Campo
- 54. Inserir contorno espesso e visível em todas as caixas de seleção — Estética · Campo
- 55. Diferenciar a cor do contorno da cor da caixa de seleção — Estética · Campo
- 56. Manter margem interna entre o texto e as bordas da caixa de diálogo — Estética · Campo
- 57. Numerar as opções de diálogo quando houver mais de uma — Estética · Campo
- 58. Incluir diversidade de personagens na narrativa — Narrativa · Campo
- 59. Manter distância entre a janela do intérprete de Libras e os textos — Estética · Campo
- 60. Definir janela vertical e de tamanho adequado para o intérprete de Libras — Estética · Campo
- 61. Disponibilizar toda a funcionalidade pelo teclado, sem exigir tempo exato de pressionamento — Mecânica · Campo
- 62. Disponibilizar tempo suficiente para entender e interagir com a mecânica — Mecânica · Campo
- 63. Permitir repetição ilimitada de minijogos com tempo limitado — Mecânica · Campo
- 64. Usar títulos curtos e descritivos nas telas de instruções — Narrativa · Campo
- 65. Separar as instruções de navegação por teclado das demais instruções — Narrativa · Campo
- 66. Separar a instrução geral do jogo das instruções de cada minijogo — Narrativa e Mecânica · Campo
- 67. Definir uma ordem de navegação por teclado lógica e conhecida pelo jogador — Mecânica · Campo
- 68. Deixar clara, pelo diálogo, a finalidade de cada link ou opção — Narrativa · Campo
- 69. Tornar o foco do teclado visível por máscara, cor ou borda — Estética · Campo
- 70. Disponibilizar, no início, audiodescrição do mapa com a posição dos personagens e elementos — Estética · Campo
- 71. Informar em áudio a posição do jogador em tempo real — Estética · Campo
- 72. Traduzir em Libras todas as opções de diálogo, em sequência — Mecânica · Campo
- 73. Identificar visual e sonoramente o tipo de diálogo (minijogo ou informação) — Narrativa · Campo
- 74. Exibir dicas em caixa de texto próxima ao personagem que as oferece — Narrativa · Campo
- 75. Permitir abrir as instruções a qualquer momento, por tecla específica — Mecânica · Campo
- 76. Mover o foco para a próxima ação ao terminar a audiodescrição — Mecânica · Campo
- 77. Pausar o minijogo automaticamente quando o jogador pedir instruções ou informações — Mecânica · Campo
- 78. Disponibilizar glossário para termos incomuns do jogo — Narrativa · Campo
- 79. Pedir confirmação antes de mudar de contexto quando um componente recebe foco — Mecânica · Campo
- 80. Pedir confirmação após a entrada de dados — Mecânica · Campo
- 81. Informar o jogador sobre mudanças de contexto e resultados (ex.: tela de sucesso) — Mecânica · Campo
- 82. Permitir consultar a pontuação atual a qualquer momento — Mecânica · Campo
- 83. Devolver o foco ao ponto anterior ao fechar uma tela aberta pelo teclado — Mecânica · Campo
- 84. Mover o foco para a próxima ação ao terminar a audiodescrição — Mecânica · Campo
- 85. Descrever em texto o erro cometido — Mecânica · Campo
- 86. Indicar por cor e som onde está o erro — Mecânica · Campo
- 87. Fornecer instruções para a entrada de dados — Narrativa · Campo
- 88. Permitir revisar e corrigir os dados inseridos — Mecânica · Campo
