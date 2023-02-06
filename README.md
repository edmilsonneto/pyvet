# Pyvet

Esse código é uma implementação de uma inteligência artificial conversacional, usando a API da OpenAI e outras bibliotecas. O usuário fala perguntas e o programa responde de maneira autônoma, convertendo a resposta em fala e reproduzindo-a.


# Ferramentas utilizadas

-   OpenAI API: para responder às perguntas do usuário.
-   gTTS: para converter texto em fala.
-   pygame: para reproduzir a fala gerada.
-   speech_recognition: para reconhecer a fala do usuário.

# Como funciona

1.  Inicialização da API da OpenAI com a chave de acesso.
2.  Captura da pergunta do usuário através do microfone e reconhecimento de fala.
3.  Envio da pergunta para a API da OpenAI e obtenção da resposta.
4.  Conversão da resposta em fala com a biblioteca gTTS.
5.  Reprodução da fala com a biblioteca pygame.
6.  Repetição do processo a partir do passo 2, até que o usuário diga "sair do pivete".

# Como executar o código

1 - Instalar Python
2 - Para executar esse código, você precisa ter as seguintes bibliotecas instaladas: openai, gTTS, pygame e speech_recognition. Elas podem ser instaladas usando o gerenciador de pacotes Python pip com os seguinte comandos: (pip install -r requirements_dev.txt) onde estão contidas as libs necessárias para funcionamento do projeto
3 - Para executar o arquivo (python **pyvet.py**)
