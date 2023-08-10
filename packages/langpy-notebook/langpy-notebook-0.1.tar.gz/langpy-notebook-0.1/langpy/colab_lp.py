import json
import requests
from .base import LangPy
from google.colab import _message


class ColabLangPy(LangPy):
    def __init__(self, api_key='', platform='openai', model='gpt-4'):
        super().__init__(api_key=api_key, platform=platform, model=model)

    def format_cell(self, cell_tuple):
        cell_str, cell_type = cell_tuple
        if cell_type == 'code':
            return f'```\n{cell_str}\n```'
        else:
            return cell_str

    def post_code(self, code):
        _message.blocking_request(
            'add_scratch_cell',
            request={'content': code, 'openInRightPane': True},
            timeout_sec=None
        )

    def get_idx_hist(self, instruction):
        colab_hist = _message.blocking_request('get_ipynb')['ipynb']['cells']
        code_list = [
            [''.join(x['source']), x['cell_type']] for x in colab_hist
        ]

        code_list = [
            self.format_cell(ct) for ct in code_list
        ]

        cur_idx = -1
        for i, code in enumerate(code_list):
            if instruction in code:
                cur_idx = i
                break

        return code_list, cur_idx

    def generate(self, instruction, mode='all', http='optional'):
        code_list, cur_idx = self.get_idx_hist(instruction)
        if mode == 'all':
            previous_code = '\n\n'.join(code_list[:cur_idx])
            prompt = f'{previous_code}\n\n{instruction}'
        else:
            prompt = instruction

        if http == 'forbid':
            prompt = f'{prompt} Do not send HTTP requests.'
        elif http == 'force':
            prompt = f'{prompt} Send an HTTP request to solve the problem.'
        elif http == 'optional':
            pass
        else:
            print('http mode not supported. try again!')

        response = requests.put(
            self.api_end_point, json={
                'instruction': prompt, 'api_key_str': self.api_key,
                'exist_code': 'none', 'platform': self.platform, 'model': self.model
            }
        )

        ans_str = json.loads(response.content)['output']
        self.post_code(ans_str)

    def complete(self, instruction, mode='all', http='optional'):
        code_list, cur_idx = self.get_idx_hist(instruction)
        if mode == 'all':
            previous_code = '\n\n'.join(code_list[:cur_idx])
            prompt = f'{previous_code}\n\n{instruction}'
        else:
            prompt = instruction

        if http == 'forbid':
            prompt = f'{prompt} Do not send HTTP requests.'
        elif http == 'force':
            prompt = f'{prompt} Send an HTTP request to solve the problem.'
        elif http == 'optional':
            pass
        else:
            print('http mode not supported. try again!')

        exist_code = code_list[cur_idx + 1].replace('```', '').strip()

        response = requests.put(
            self.api_end_point, json={
                'instruction': prompt, 'api_key_str': self.api_key,
                'exist_code': exist_code, 'platform': self.platform, 'model': self.model
            }
        )

        ans_str = json.loads(response.content)['output']
        self.post_code(ans_str)

    def process_csv(self, file_name, read_mode='r'):
        content_list = open(file_name, read_mode).readlines()[:3]
        content_list = [x.strip() for x in content_list]
        content_str = '\n# '.join(content_list)
        prompt = f"""# First three rows of the input file:\n# {content_str}\n# ...\nfile_name = '{file_name}' \ninput_file = open(file_name)"""
        self.post_code(prompt)
