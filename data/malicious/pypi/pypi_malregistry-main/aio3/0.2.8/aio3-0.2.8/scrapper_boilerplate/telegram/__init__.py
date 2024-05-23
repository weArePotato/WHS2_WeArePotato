import telegram
from scrapper_boilerplate.warnings import disable_warnings

disable_warnings()


class TelegramBot:
    """
    Telegram message handler
    - to get chat: access @getidsbot and type start to get id
    - to access token, create bot in @botFather and paste the token
    """ 

    def __init__(self, auth_token:str, chat_id:list):
        print('> iniciando módulo do telegram!')
        self.TOKEN = auth_token
        self.CHAT_ID = chat_id
        self.bot = telegram.Bot(token=self.TOKEN)

    def send_message(self, msg):
        try:
            print('> Enviando mensagem...')
            for chat in self.CHAT_ID:
                self.bot.sendMessage(chat_id=int(chat), text=msg)

        except Exception as error:
            print(f'> [ERRO] ao enviar mensagem! {error} ')

        else:
            print('> Mensagem enviada com sucesso!')
            return True

    def send_file(self, filename):
        """
        send a file to telegram
        """
        try:
            document = open(filename, 'rb')
            for ids in self.CHAT_ID:
                self.bot.send_document(int(ids), document)

        except Exception as error:
            print(f'> [ERRO] ao enviar arquivo! {error} ')
            raise

        else:
            print('> Arquivo enviado com sucesso!')
            return True
