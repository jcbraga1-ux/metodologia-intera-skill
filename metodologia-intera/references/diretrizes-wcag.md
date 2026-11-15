> Este arquivo faz parte da Intera-IA (skill metodologia-intera) e reproduz a skill `wcag-sem-complicacao` v1.0.2, licença CC BY-NC 4.0, DOI 10.5281/zenodo.23837715 (https://github.com/jcbraga1-ux/wcag-sem-complicacao-skill). Onde o texto abaixo diz "esta skill", leia "este conjunto de diretrizes". Não edite aqui: as correções são feitas na skill separada e copiadas para cá a cada versão.

# WCAG 2.1 sem complicação

As Diretrizes de Acessibilidade para Conteúdo Web (WCAG) dizem o que um site ou aplicativo precisa ter para que pessoas com deficiência consigam usá-lo. Aqui cada critério está explicado em linguagem simples, com um exemplo do sistema fictício de agendamento da UBS Jardim Esperança (disciplina de Interação Humano-Computador, UFABC).

Base: W3C. *Web Content Accessibility Guidelines (WCAG) 2.1*, Recomendação do W3C (https://www.w3.org/TR/WCAG21/). As explicações são simplificações didáticas: para avaliar um sistema formalmente, consulte o texto oficial de cada critério.

## Como a norma é organizada

- **4 princípios:** as grandes perguntas (Perceptível, Operável, Compreensível, Robusto).
- **13 diretrizes:** os temas de cada princípio.
- **78 critérios de sucesso:** o que dá para testar.

## Os três níveis

- **A (30 critérios):** o mínimo; sem isso, alguém fica de fora.
- **AA (20 critérios):** o padrão exigido em leis e contratos. Para chegar ao AA, é preciso cumprir todos os critérios A e todos os AA (50 no total).
- **AAA (28 critérios):** o nível mais alto, nem sempre possível em todo o conteúdo.

Meta padrão do projeto da disciplina: **nível AA**.

## Como usar

- **Consulta:** responda citando o número, o nome e o nível do critério (ex.: "WCAG 1.4.3 Contraste (mínimo), AA"), a explicação simples e o exemplo UBS. Se a pessoa precisar do texto normativo, indique o link oficial `https://www.w3.org/WAI/WCAG21/Understanding/` e diga que a explicação aqui é simplificada.
- **Auditoria de site, app ou protótipo:** por padrão, avalie os 50 critérios A + AA. Para cada um, marque Atende / Não atende / Não se aplica, com evidência (tela, elemento, comportamento) e como testar. Termine com as falhas priorizadas (primeiro A, depois AA) e sugestões de correção.
- **Geração de requisitos:** transforme critérios em requisitos do projeto, com identificador, descrição sem ambiguidade, origem ("WCAG 2.1 – 2.4.7") e critério de aceitação testável.
- **Ensino:** use as perguntas de cada princípio, as explicações simples e os exemplos da UBS. Adapte o exemplo ao contexto do aluno quando ajudar.
- Nunca invente critérios, números, níveis ou valores (como razões de contraste e tamanhos). Se algo não estiver aqui, diga que não consta na WCAG 2.1.

## Observações de revisão

- **4.1.1 Análise (parsing)** foi considerado obsoleto na WCAG 2.2 e removido dela.
- A **WCAG 2.2** (Recomendação do W3C de 2023) mantém os critérios da 2.1 (exceto o 4.1.1) e acrescenta 9 critérios que **não constam nesta skill em detalhe**: 2.4.11 Foco não obscurecido (mínimo) AA; 2.4.12 Foco não obscurecido (melhorado) AAA; 2.4.13 Aparência do foco AAA; 2.5.7 Movimentos de arrastar AA; 2.5.8 Tamanho do alvo (mínimo) AA; 3.2.6 Ajuda consistente A; 3.3.7 Entrada redundante A; 3.3.8 Autenticação acessível (mínimo) AA; 3.3.9 Autenticação acessível (melhorada) AAA. Se a pessoa pedir WCAG 2.2, avise e indique https://www.w3.org/TR/WCAG22/.
- O 2.5.5 Tamanho do alvo (44 × 44 px) é AAA; na WCAG 2.2, o mínimo AA passou a ser o 2.5.8 (24 × 24 px CSS).

## Os 78 critérios de sucesso

### Princípio 1 – Perceptível (29 critérios)

Dá para perceber? A informação chega a todos os sentidos: quem não vê, não ouve ou enxerga pouco.

#### Diretriz 1.1 – Alternativas em texto

Toda imagem precisa de uma descrição em texto.

- **1.1.1 Conteúdo não textual (A)** – Imagens, ícones e botões com imagem têm um texto alternativo que diz o que são ou para que servem. *Exemplo UBS:* O ícone de lixeira ao lado da consulta é lido pelo leitor de tela como “Cancelar consulta”, e não como “imagem”.

#### Diretriz 1.2 – Mídias com tempo

Vídeo e áudio precisam de legendas, transcrição ou descrição.

- **1.2.1 Apenas áudio e apenas vídeo (pré-gravado) (A)** – Áudio gravado tem transcrição; vídeo sem som tem descrição em texto ou áudio. *Exemplo UBS:* O áudio “Como se preparar para o exame de sangue” tem a transcrição logo abaixo do player.
- **1.2.2 Legendas (pré-gravadas) (A)** – Vídeos gravados com fala têm legenda sincronizada. *Exemplo UBS:* O vídeo da campanha de vacinação tem legendas para pessoas surdas ou que estão na sala de espera sem som.
- **1.2.3 Audiodescrição ou mídia alternativa (pré-gravada) (A)** – O que só aparece na imagem do vídeo é narrado ou descrito em texto. *Exemplo UBS:* O vídeo que mostra onde fica cada sala da UBS tem uma descrição em texto do caminho.
- **1.2.4 Legendas (ao vivo) (AA)** – Transmissões ao vivo com fala têm legenda em tempo real. *Exemplo UBS:* A live da Secretaria de Saúde sobre a dengue tem legenda ao vivo.
- **1.2.5 Audiodescrição (pré-gravada) (AA)** – Vídeos gravados têm narração do que acontece na imagem, quando isso é importante. *Exemplo UBS:* No vídeo de como usar o glicosímetro, a narração diz “aperte o botão lateral”, e não apenas “faça assim”.
- **1.2.6 Língua de sinais (pré-gravada) (AAA)** – Vídeos gravados têm intérprete de Libras. *Exemplo UBS:* Os vídeos de orientação da UBS têm uma janela com intérprete de Libras.
- **1.2.7 Audiodescrição estendida (AAA)** – Se não há pausa na fala para descrever a imagem, o vídeo pausa para a descrição. *Exemplo UBS:* O vídeo explicativo pausa por alguns segundos para descrever o mapa do posto.
- **1.2.8 Mídia alternativa (pré-gravada) (AAA)** – Vídeos gravados têm um texto completo equivalente, com falas e descrição das cenas. *Exemplo UBS:* Cada vídeo tem um roteiro em texto que pode ser lido em vez de assistir.
- **1.2.9 Apenas áudio (ao vivo) (AAA)** – Áudio ao vivo tem uma alternativa em texto. *Exemplo UBS:* O podcast ao vivo da UBS tem transcrição em tempo real.

#### Diretriz 1.3 – Adaptável

A estrutura da tela não pode depender só da aparência.

- **1.3.1 Informações e relações (A)** – Títulos, listas, tabelas e campos estão marcados no código, não apenas com aparência visual. *Exemplo UBS:* A tabela de horários usa cabeçalhos de verdade, então o leitor de tela diz “Segunda, 10h, Clínico geral”.
- **1.3.2 Sequência significativa (A)** – A ordem de leitura no código faz sentido, igual à ordem visual. *Exemplo UBS:* O leitor de tela lê data, hora e local da consulta nessa ordem, e não o botão “Confirmar” antes de tudo.
- **1.3.3 Características sensoriais (A)** – As instruções não dependem só de forma, cor, posição ou som. *Exemplo UBS:* A tela diz “toque em Confirmar consulta”, e não “toque no botão redondo à direita”.
- **1.3.4 Orientação (AA)** – A tela funciona com o celular em pé e deitado. *Exemplo UBS:* Quem usa o celular preso à cadeira de rodas, na horizontal, consegue agendar normalmente.
- **1.3.5 Identificar o propósito de entrada (AA)** – Campos de dados pessoais avisam o que pedem, para o navegador preencher sozinho. *Exemplo UBS:* Nome, telefone e CEP são preenchidos automaticamente, o que ajuda quem tem dificuldade motora ou de memória.
- **1.3.6 Identificar o propósito (AAA)** – Ícones, regiões e botões têm o propósito marcado no código, para serem adaptados. *Exemplo UBS:* Uma extensão pode trocar os ícones do menu por símbolos que a pessoa já conhece.

#### Diretriz 1.4 – Distinguível

Fácil de ver e de ouvir: contraste, tamanho, espaçamento.

- **1.4.1 Uso de cor (A)** – A cor nunca é o único jeito de passar uma informação. *Exemplo UBS:* Horários livres aparecem em verde e também com a palavra “Disponível”.
- **1.4.2 Controle de áudio (A)** – Sons que tocam sozinhos por mais de 3 segundos podem ser pausados. *Exemplo UBS:* A música do vídeo de boas-vindas pode ser silenciada, e não atrapalha o leitor de tela.
- **1.4.3 Contraste (mínimo) (AA)** – O texto tem contraste de pelo menos 4,5:1 com o fundo (3:1 para texto grande). *Exemplo UBS:* Nada de texto cinza-claro sobre branco na lista de horários.
- **1.4.4 Redimensionar texto (AA)** – O texto pode ser ampliado até 200% sem perder conteúdo ou função. *Exemplo UBS:* Dona Cida aumenta a letra do celular e continua vendo o botão “Confirmar”.
- **1.4.5 Imagens de texto (AA)** – Texto é escrito como texto, e não como imagem. *Exemplo UBS:* O aviso “Campanha de vacinação até 30/11” é texto real, que pode ser ampliado e lido em voz alta.
- **1.4.6 Contraste (melhorado) (AAA)** – Contraste de pelo menos 7:1 (4,5:1 para texto grande). *Exemplo UBS:* Uma versão de alto contraste para pacientes com baixa visão.
- **1.4.7 Áudio de fundo baixo ou sem som (AAA)** – Em gravações com fala, a música de fundo é baixa ou pode ser desligada. *Exemplo UBS:* Na orientação em áudio, a voz é bem mais alta que a trilha.
- **1.4.8 Apresentação visual (AAA)** – Blocos de texto têm linhas curtas, sem justificar, com cores ajustáveis e espaçamento confortável. *Exemplo UBS:* O texto das orientações pré-exame é alinhado à esquerda, com linhas de até 80 caracteres.
- **1.4.9 Imagens de texto (sem exceção) (AAA)** – Imagens de texto só para logotipos ou quando forem essenciais. *Exemplo UBS:* Só o logotipo da prefeitura é imagem; todo o resto é texto.
- **1.4.10 Refluxo (AA)** – O conteúdo se reorganiza em telas estreitas (320 px) sem rolagem para os lados. *Exemplo UBS:* Com zoom de 400%, a ficha da consulta vira uma coluna só, sem precisar arrastar para a direita.
- **1.4.11 Contraste não textual (AA)** – Bordas de campos, ícones e botões têm contraste de pelo menos 3:1. *Exemplo UBS:* A borda do campo “CPF” é bem visível, e não um cinza quase branco.
- **1.4.12 Espaçamento de texto (AA)** – Aumentar o espaço entre linhas, letras e palavras não corta nem esconde o texto. *Exemplo UBS:* Quem usa uma extensão para dislexia, que aumenta os espaços, continua lendo os botões inteiros.
- **1.4.13 Conteúdo em foco ou ao passar o mouse (AA)** – Dicas que aparecem ao passar o mouse podem ser fechadas, não somem sozinhas e não tapam o conteúdo. *Exemplo UBS:* A dica “O que é o Cartão SUS?” fica aberta até a pessoa fechar com Esc.

### Princípio 2 – Operável (29 critérios)

Dá para operar? Tudo funciona com teclado, sem pressa e sem gestos difíceis.

#### Diretriz 2.1 – Acessível por teclado

Tudo funciona sem mouse.

- **2.1.1 Teclado (A)** – Tudo pode ser feito só com o teclado. *Exemplo UBS:* Escolher o horário da consulta funciona com Tab e Enter, sem precisar de mouse.
- **2.1.2 Sem armadilha de teclado (A)** – O foco do teclado nunca fica preso em um lugar. *Exemplo UBS:* Ao abrir o calendário, a pessoa consegue sair dele com Tab ou Esc.
- **2.1.3 Teclado (sem exceção) (AAA)** – Absolutamente tudo funciona pelo teclado, sem exceções. *Exemplo UBS:* Até a assinatura no termo de consentimento tem alternativa por teclado.
- **2.1.4 Atalhos de teclado por caractere (A)** – Atalhos de uma só letra podem ser desligados ou trocados. *Exemplo UBS:* O atalho “C” para cancelar não dispara sem querer quando alguém usa comando de voz.

#### Diretriz 2.2 – Tempo suficiente

Ninguém deve ser expulso por demorar.

- **2.2.1 Tempo ajustável (A)** – Se há limite de tempo, a pessoa pode desligá-lo, ajustá-lo ou estendê-lo. *Exemplo UBS:* Antes de a reserva do horário expirar, aparece “Precisa de mais tempo?” com o botão “Sim”.
- **2.2.2 Pausar, parar, ocultar (A)** – Conteúdo que se move, pisca ou atualiza sozinho pode ser pausado. *Exemplo UBS:* O carrossel de avisos da tela inicial tem botão de pausa.
- **2.2.3 Sem tempo (AAA)** – Não há limite de tempo, exceto em eventos ao vivo. *Exemplo UBS:* O agendamento não tem contagem regressiva.
- **2.2.4 Interrupções (AAA)** – Interrupções e alertas podem ser adiados, exceto em emergências. *Exemplo UBS:* Notificações de campanha não aparecem no meio do preenchimento do cadastro.
- **2.2.5 Nova autenticação (AAA)** – Se o login expira, a pessoa entra de novo sem perder o que preencheu. *Exemplo UBS:* Depois de entrar de novo, o formulário do agendamento continua preenchido.
- **2.2.6 Tempo esgotado (AAA)** – A pessoa é avisada de quanto tempo sem uso apaga os dados. *Exemplo UBS:* “Seus dados ficam salvos por 20 minutos sem uso.”

#### Diretriz 2.3 – Convulsões e reações físicas

Nada que pisque ou se mova a ponto de fazer mal.

- **2.3.1 Três flashes ou abaixo do limite (A)** – Nada pisca mais de 3 vezes por segundo. *Exemplo UBS:* O alerta de “consulta hoje” não pisca, o que protege pessoas com epilepsia.
- **2.3.2 Três flashes (AAA)** – Nada pisca mais de 3 vezes por segundo, sem exceção. *Exemplo UBS:* Nenhum vídeo ou animação do sistema tem flashes.
- **2.3.3 Animação a partir de interações (AAA)** – Animações causadas pelo uso podem ser desligadas. *Exemplo UBS:* Quem ativa “reduzir movimento” no celular não vê a tela deslizar ao confirmar.

#### Diretriz 2.4 – Navegável

Fácil saber onde se está e chegar aonde se quer.

- **2.4.1 Ignorar blocos (A)** – Há um jeito de pular o menu e ir direto ao conteúdo. *Exemplo UBS:* O link “Pular para o conteúdo” leva direto ao formulário de agendamento.
- **2.4.2 Página com título (A)** – Cada página tem um título que descreve o que ela é. *Exemplo UBS:* A aba do navegador mostra “Remarcar consulta · UBS Jardim Esperança”.
- **2.4.3 Ordem do foco (A)** – O Tab percorre a tela em uma ordem lógica. *Exemplo UBS:* O Tab vai de Data para Horário e depois para Confirmar, nessa ordem.
- **2.4.4 Finalidade do link (em contexto) (A)** – Dá para saber para onde o link leva pelo texto dele e pelo contexto. *Exemplo UBS:* “Ver orientações do exame de sangue”, e não “clique aqui”.
- **2.4.5 Várias formas (AA)** – Há mais de um caminho para chegar a uma página. *Exemplo UBS:* Dá para achar “Vacinas” pelo menu e também pela busca.
- **2.4.6 Cabeçalhos e rótulos (AA)** – Títulos e rótulos descrevem o assunto ou a função. *Exemplo UBS:* O campo diz “Telefone para lembrete (WhatsApp)”, e não apenas “Contato”.
- **2.4.7 Foco visível (AA)** – Dá para ver onde está o foco do teclado. *Exemplo UBS:* O botão em foco ganha um contorno forte e visível.
- **2.4.8 Localização (AAA)** – A pessoa sabe em que parte do sistema está. *Exemplo UBS:* A trilha “Início › Consultas › Remarcar” aparece no topo.
- **2.4.9 Finalidade do link (apenas o link) (AAA)** – O texto do link sozinho já diz para onde ele leva. *Exemplo UBS:* Na lista de links do leitor de tela, todos fazem sentido fora do contexto.
- **2.4.10 Cabeçalhos de seção (AAA)** – Textos longos são divididos em seções com títulos. *Exemplo UBS:* As orientações pré-exame têm seções: Jejum, Remédios, O que levar.

#### Diretriz 2.5 – Modalidades de entrada

Além do teclado: toque, gestos, voz e movimento.

- **2.5.1 Gestos de acionamento (A)** – O que usa gesto complexo (pinça, vários dedos) também funciona com um toque simples. *Exemplo UBS:* O mapa da UBS tem botões de “+” e “−”, além do gesto de pinça.
- **2.5.2 Cancelamento de acionamento (A)** – A ação acontece ao soltar o dedo, e dá para desistir arrastando para fora. *Exemplo UBS:* Quem encosta sem querer em “Cancelar consulta” pode arrastar o dedo para fora e nada acontece.
- **2.5.3 Rótulo no nome acessível (A)** – O nome lido pela tecnologia assistiva contém o texto visível do botão. *Exemplo UBS:* O botão “Confirmar” atende ao comando de voz “clicar em Confirmar”.
- **2.5.4 Atuação por movimento (A)** – O que funciona chacoalhando ou inclinando o celular também tem um botão. *Exemplo UBS:* “Agite para desfazer” também tem o botão “Desfazer”.
- **2.5.5 Tamanho do alvo (AAA)** – Áreas de toque têm pelo menos 44 × 44 pixels. *Exemplo UBS:* Os horários do calendário são grandes o bastante para quem tem tremor nas mãos.
- **2.5.6 Mecanismos de entrada simultâneos (AAA)** – A pessoa pode alternar entre toque, teclado e mouse quando quiser. *Exemplo UBS:* No tablet, dá para usar o teclado Bluetooth no meio do agendamento.

### Princípio 3 – Compreensível (17 critérios)

Dá para entender? Texto claro, telas previsíveis e ajuda para não errar.

#### Diretriz 3.1 – Legível

O texto pode ser lido e entendido.

- **3.1.1 Idioma da página (A)** – O idioma principal está indicado no código. *Exemplo UBS:* A página está marcada como português, então o leitor de tela pronuncia certo.
- **3.1.2 Idioma das partes (AA)** – Trechos em outro idioma estão marcados. *Exemplo UBS:* A palavra em inglês “check-in” é lida com a pronúncia certa.
- **3.1.3 Palavras incomuns (AAA)** – Termos técnicos e jargões têm explicação. *Exemplo UBS:* “Hemograma” tem a explicação “exame de sangue completo”.
- **3.1.4 Abreviações (AAA)** – Siglas e abreviações têm o significado disponível. *Exemplo UBS:* “UBS (Unidade Básica de Saúde)” na primeira vez em que aparece.
- **3.1.5 Nível de leitura (AAA)** – Se o texto exige leitura avançada, há uma versão mais simples. *Exemplo UBS:* As regras de agendamento têm uma versão resumida em linguagem simples.
- **3.1.6 Pronúncia (AAA)** – Palavras com sentido ambíguo, que dependem da pronúncia, têm a pronúncia indicada. *Exemplo UBS:* Nomes de medicamentos parecidos têm indicação de como se pronunciam.

#### Diretriz 3.2 – Previsível

A tela se comporta como a pessoa espera.

- **3.2.1 Em foco (A)** – Receber o foco não muda a página sozinho. *Exemplo UBS:* Ao passar com Tab pelo campo de data, o calendário não envia nada.
- **3.2.2 Em entrada (A)** – Mudar um campo não causa mudanças inesperadas sem aviso. *Exemplo UBS:* Escolher uma especialidade não leva automaticamente para outra tela; é preciso tocar em “Continuar”.
- **3.2.3 Navegação consistente (AA)** – Menus repetidos aparecem sempre na mesma ordem. *Exemplo UBS:* O menu Início, Consultas, Exames, Vacinas fica igual em todas as telas.
- **3.2.4 Identificação consistente (AA)** – Funções iguais têm o mesmo nome e o mesmo ícone em todo o sistema. *Exemplo UBS:* “Remarcar” tem sempre o mesmo nome, e não “Reagendar” em uma tela e “Alterar” em outra.
- **3.2.5 Mudança mediante solicitação (AAA)** – Grandes mudanças só acontecem quando a pessoa pede. *Exemplo UBS:* Nenhuma janela nova abre sem a pessoa tocar em um botão.

#### Diretriz 3.3 – Assistência de entrada

Ajuda a evitar e a corrigir erros em formulários.

- **3.3.1 Identificação de erro (A)** – Quando há erro, o campo é apontado e o erro é descrito em texto. *Exemplo UBS:* “O CPF precisa ter 11 números”, junto ao campo, e não apenas uma borda vermelha.
- **3.3.2 Rótulos ou instruções (A)** – Campos têm rótulo e, quando necessário, instruções. *Exemplo UBS:* “Data de nascimento (dd/mm/aaaa)” acima do campo.
- **3.3.3 Sugestão de erro (AA)** – Se o sistema sabe como corrigir o erro, ele sugere a correção. *Exemplo UBS:* “Você quis dizer Rua das Flores?” ao digitar um endereço errado.
- **3.3.4 Prevenção de erros (legal, financeiro, dados) (AA)** – Ações importantes podem ser revisadas, confirmadas ou desfeitas. *Exemplo UBS:* Antes de cancelar a consulta, aparece um resumo e o botão “Sim, cancelar”.
- **3.3.5 Ajuda (AAA)** – Há ajuda disponível no contexto. *Exemplo UBS:* Cada etapa do agendamento tem “Precisa de ajuda?”, com telefone da recepção.
- **3.3.6 Prevenção de erros (todos) (AAA)** – Qualquer envio pode ser revisado, confirmado ou desfeito. *Exemplo UBS:* Até o envio de sugestões tem a etapa de revisão.

### Princípio 4 – Robusto (3 critérios)

Funciona com tecnologias assistivas? O código é lido corretamente por leitores de tela e navegadores.

#### Diretriz 4.1 – Compatível

Funciona com navegadores e tecnologias assistivas, hoje e no futuro.

- **4.1.1 Análise (parsing) (A)** – O código não tem erros que confundam as tecnologias assistivas. Na WCAG 2.2 este critério foi considerado obsoleto. *Exemplo UBS:* O HTML do sistema passa no validador do W3C sem erros graves.
- **4.1.2 Nome, função, valor (A)** – Todo componente informa o que é, como se chama e em que estado está. *Exemplo UBS:* O leitor de tela diz “Lembrete por WhatsApp, caixa de seleção, marcada”.
- **4.1.3 Mensagens de status (AA)** – Mensagens de status são anunciadas sem mudar o foco. *Exemplo UBS:* “Consulta confirmada” é falado pelo leitor de tela, mesmo sem a pessoa ir até a mensagem.
