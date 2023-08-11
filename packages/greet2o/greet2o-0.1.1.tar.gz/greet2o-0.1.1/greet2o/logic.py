class GreetingClient():
    '''
    Gretting Logic
    '''

    language = ''

    def __init__(self, language):
        self.language = language


    def greet(self):
        if self.language == 'ja':
            print('こんにちは')
        else:
            print('Hello')
