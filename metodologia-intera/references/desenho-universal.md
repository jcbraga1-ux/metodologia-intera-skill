# Acessibilidade desde o início: Desenho Universal

Na Metodologia Intera 2.0, a acessibilidade não é uma adaptação feita no final, nem um recurso pensado para um único grupo. A versão 2.0 criou a equipe de acessibilidade e o papel de usuário co-designer, e os guias de contextualização perguntam pela opção de Design Universal. Esta skill parte dessa premissa: **todo OA começa pelo Desenho Universal**, da contextualização até a avaliação.

Fontes: livro *Metodologia Intera 2.0* (papéis da versão 2.0; guia de contextualização com a opção de Design Universal; caps. 5 e 6 sobre jogos); skills `mobiledu-diretrizes` (Coletto, 2026) e `rpg-du-diretrizes` (Cunha, 2022), do mesmo grupo; Lei Brasileira de Inclusão (Lei nº 13.146/2015, art. 3º, II). A matriz de necessidades e o formato dos requisitos abaixo são **propostas desta skill** para operacionalizar o conceito.

## O que é

- **Desenho Universal:** concepção de produtos, ambientes, programas e serviços para serem usados por todas as pessoas, sem necessidade de adaptação ou de projeto específico, incluindo os recursos de tecnologia assistiva (Lei nº 13.146/2015, art. 3º, II).
- **Os 7 princípios** (numeração usada também na RPG-DU): 1. uso equitativo; 2. flexibilidade no uso; 3. uso simples e intuitivo; 4. informação perceptível; 5. tolerância ao erro; 6. baixo esforço físico; 7. tamanho e espaço para aproximação e uso.
- **Três ideias da MobileDU** que ajudam a aplicar os princípios num OA digital: **flexibilidade de uso** (cada pessoa ajusta o OA do seu jeito, em vez de receber uma versão única), **redundância sensorial** (a mesma informação chega por mais de um sentido) e **independência de dispositivo** (funciona com teclado, toque, voz, acionadores e tecnologias assistivas).
- **No plano pedagógico**, o mesmo raciocínio vale para a aprendizagem: mais de uma forma de apresentar o conteúdo, mais de uma forma de o aluno participar e mais de uma forma de ele mostrar o que aprendeu.

## O erro que esta skill deve evitar

Resumir a acessibilidade a um só grupo de pessoas. Exemplo real de saída inadequada:

> "Compatibilidade com leitores de tela e navegação completa por teclado."

Esse requisito é necessário, mas atende principalmente pessoas cegas e parte das pessoas com deficiência motora. Ficam de fora, por exemplo, pessoas surdas usuárias de Libras, pessoas com baixa visão ou daltonismo, com deficiência intelectual, com dislexia, com TDAH ou autismo, com epilepsia fotossensível, pessoas idosas e alunos em alfabetização. Leitor de tela e teclado entram como **um** item entre vários, nunca como a resposta inteira.

## Matriz de necessidades (proposta desta skill)

Use esta matriz na contextualização (para perguntar ao professor quem são os alunos) e nos requisitos (para conferir se nenhuma linha ficou sem resposta). Nem toda turma terá todos os perfis, mas o OA desenhado universalmente não depende de saber com antecedência quem vai usá-lo.

| Dimensão | Quem pode precisar | Exemplos de solução |
| --- | --- | --- |
| Visão | pessoas cegas, com baixa visão, com daltonismo | texto alternativo e audiodescrição; compatível com leitor de tela; ampliação sem perder conteúdo; contraste ajustável; cor nunca como única pista |
| Audição | pessoas surdas usuárias de Libras, surdas oralizadas, com deficiência auditiva | janela de Libras feita por intérprete; legendas; transcrição; avisos sonoros também visuais |
| Movimento | pessoas com deficiência física, tremor, pouca força ou precisão, uso de uma só mão | navegação por teclado; áreas de toque grandes; sem gestos complexos ou arrastes obrigatórios; compatível com acionadores e comandos de voz |
| Cognição e aprendizagem | pessoas com deficiência intelectual, dislexia, discalculia, TDAH, autismo | linguagem simples; uma ideia por tela; instruções com texto, ícone e áudio; glossário; previsibilidade; poder repetir e voltar |
| Sensibilidade a estímulos | pessoas com epilepsia fotossensível, enxaqueca, sensibilidade sensorial | sem flashes; animações, sons e música de fundo que podem ser pausados ou desligados |
| Tempo | quem lê ou age mais devagar, quem usa tecnologia assistiva | sem limite de tempo, ou com tempo ajustável |
| Língua e letramento | alunos em alfabetização, com baixo letramento, que têm outra língua como primeira (incluindo Libras) | áudio junto com o texto; vocabulário do público; imagens que apoiam o sentido |
| Idade | crianças pequenas, pessoas idosas | botões grandes; poucas etapas; ajuda sempre visível |
| Participação e expressão | todos | responder de mais de um jeito (escrever, falar, escolher, desenhar, gravar); feedback que explica o erro; poder refazer sem punição |
| Contexto de uso | quem usa celular simples, internet fraca, ambiente barulhento | funciona com pouca conexão ou sem internet; arquivos leves; legendas para quem está sem som |

Deficiências múltiplas e surdocegueira combinam linhas: confira se as soluções não se anulam (por exemplo, para uma pessoa surdocega, um aviso só sonoro ou só visual não funciona; prefira vibração ou compatibilidade com linha braille).

## Como a skill aplica o Desenho Universal em cada etapa

- **Contextualização:** pergunte ao professor sobre a diversidade da turma usando as dimensões da matriz, e não só "há alunos cegos?". Registre também os alunos sem deficiência diagnosticada que têm necessidades parecidas (dificuldade de leitura, atenção, visão cansada). A resposta "não tenho alunos com deficiência" não encerra o assunto: explique que o OA será reutilizado em outras turmas e que o Desenho Universal é a premissa da metodologia, e registre essa explicação.
- **Papéis:** recomende co-designers com perfis diversos, não de um só tipo de deficiência, e a equipe de acessibilidade desde a primeira etapa.
- **Requisitos:** gere requisitos de acessibilidade (RA) cobrindo todas as linhas da matriz que fazem sentido para o tipo de OA. Cada RA informa **a quem serve** (dimensão da matriz), o **princípio do DU** e, quando houver, a diretriz (WCAG/e-MAG, MobileDU ou RPG-DU), com critério de aceite. Os requisitos pedagógicos também seguem o DU: mais de uma forma de apresentar o conteúdo, de participar e de mostrar o que aprendeu.
- **Esboço:** marque no roteiro, no storyboard ou no GDD onde entra cada recurso (Libras, legenda, audiodescrição, alternativa à cor, alternativa ao gesto).
- **Desenvolvimento:** siga a ordem aprendida no *Expedição Antártica*: o que está no código (teclado, leitor de tela, contraste, personalização) desde o início; Libras e audiodescrição depois que as telas estão testadas.
- **Teste e Qualidade:** teste com pessoas de perfis diferentes, não só com a equipe e não só com um tipo de deficiência. Registre quais dimensões da matriz foram testadas e quais ficaram sem teste.
- **Disponibilização:** descreva nos metadados todos os recursos de acessibilidade oferecidos.
- **Avaliação pedagógica:** os instrumentos de pré e pós-teste também precisam ser acessíveis; caso contrário, mede-se a barreira e não a aprendizagem.

## Antes de entregar qualquer artefato

Confira:

1. A acessibilidade aparece como premissa de Desenho Universal, e não como lista para um único público?
2. Cada dimensão da matriz que se aplica ao tipo de OA tem pelo menos uma resposta, ou está registrada como questão em aberto?
3. Há redundância sensorial (nenhuma informação chega por um único sentido)?
4. Há flexibilidade (a pessoa pode ajustar tamanho, contraste, velocidade, som, tempo)?
5. Há mais de uma forma de participar e de responder?

Se o professor decidir priorizar alguns recursos por prazo ou custo, registre a decisão, o motivo e o que fica para uma próxima versão. Não trate a priorização como se o OA já estivesse acessível.
