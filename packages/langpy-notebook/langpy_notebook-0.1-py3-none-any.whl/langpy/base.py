class LangPy:
    def __init__(self, api_key='', platform='openai', model='gpt-4'):
        self.api_key = f"# Insert your OpenAI api key here\\napi_key = '{api_key}'"
        self.api_end_point = 'https://lang-py-522564686dd7.herokuapp.com/items/0'
        self.platform = platform
        self.model = model

    def config_api_key(self):
        api_key = input('Your openai api_key:')
        self.api_key = f"# Insert your OpenAI api key here\\napi_key = '{api_key}'"

    def config_end_point(self):
        self.api_end_point = input('New API end_point:')

    def generate(self):
        pass

    def complete(self):
        pass
