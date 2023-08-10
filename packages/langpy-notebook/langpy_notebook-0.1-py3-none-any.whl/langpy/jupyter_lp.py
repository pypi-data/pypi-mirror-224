import IPython
from IPython.core.display import display, Javascript
from .base import LangPy


class JupyterLangPy(LangPy):
    def __init__(self, api_key='', platform='gpt', model='gpt-4'):
        super().__init__(api_key=api_key, platform=platform, model=model)

    def generate(self, instruction, mode='all', http='optional'):

        if http == 'forbid':
            instruction = f'{instruction} Do not send HTTP requests.'
        elif http == 'force':
            instruction = f'{instruction} Send an HTTP request to solve the problem.'
        elif http == 'optional':
            pass
        else:
            print('http mode not supported. try again!')
            return

        js_code = """
        async function myCallbackFunction(data) {
            const url = '%s';
            try {
            let response = await fetch(url, {
                method: "PUT",
                headers: {
                "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            let responseData = await response.json();
            return responseData;
            } catch (error) {
            console.log(error);
            }
        }

        var current_index = Jupyter.notebook.get_selected_index();
        console.log(current_index);
        
        var previous_cell_content = "";
        """ % self.api_end_point

        if mode == "all":
            js_code += """
        for (var i = 1; i < current_index; i++) {
            var cell = Jupyter.notebook.get_cell(i);
            if (cell.cell_type === "code") {
                previous_cell_content += '```\\n' + cell.get_text() + '\\n```\\n';
            } else {
                previous_cell_content += cell.get_text() + '\\n';
            }
        }
        
        // previous_cell_content = previous_cell_content.slice(0, -1)
        """
        elif mode == 'now':
            pass
        else:
            print("mode not supported")

        js_code += """
        previous_cell_content += '%s'
        console.log(previous_cell_content)
        
        // previous_cell_content = 'Implement a linear classifier using pytorch.'

        var api_key_str = "%s"

        console.log(api_key_str)
        var data = {
            "instruction": previous_cell_content,
            "api_key_str": api_key_str,
            "exist_code": "none",
            "platform": "%s",
            "model": "%s"
        }

        myCallbackFunction(data).then(responseData => {
            var print_content = responseData["output"]
            Jupyter.notebook.select_prev()
            var new_cell = Jupyter.notebook.insert_cell_below('code');
            
            // Jupyter.notebook.get_selected_cell().clear_output();

            var next_cell = Jupyter.notebook.get_cell(current_index)
            next_cell.set_text(print_content);
            
            // Jupyter.notebook.get_cell(current_index - 1).clear_output();
            // Jupyter.notebook.select_next();
        }).catch()

        // var new_cell = Jupyter.notebook.insert_cell_below('code');
        // new_cell.set_text("# Waiting for LLM Response ...");
        """ % (instruction, self.api_key, self.platform, self.model)

        print('The code will be generated in the next cell ...')

        display(Javascript(js_code))

    def complete(self, instruction, mode='all', http='optional'):
        if http == 'forbid':
            instruction = f'{instruction} Do not send HTTP requests.'
        elif http == 'force':
            instruction = f'{instruction} Send an HTTP request to solve the problem.'
        elif http == 'optional':
            pass
        else:
            print('http mode not supported. try again!')
            return

        js_code = """
        async function myCallbackFunction(data) {
            const url = '%s';
            try {
            let response = await fetch(url, {
                method: "PUT",
                headers: {
                "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            let responseData = await response.json();
            return responseData;
            } catch (error) {
                next_cell.set_text(exist_code + "\\n* try again! *");
            }
        }

        var current_index = Jupyter.notebook.get_selected_index();
        console.log(current_index);
        
        var previous_cell_content = "";
        """ % self.api_end_point

        if mode == "all":
            js_code += """
        for (var i = 1; i < current_index; i++) {
            var cell = Jupyter.notebook.get_cell(i);
            if (cell.cell_type === "code") {
                previous_cell_content += '```\\n' + cell.get_text() + '\\n```\\n';
            } else {
                previous_cell_content += cell.get_text() + '\\n';
            }
        }
        
        // previous_cell_content = previous_cell_content.slice(0, -1)
        """
        elif mode == 'now':
            pass
        else:
            print("mode not supported")

        js_code += """
        previous_cell_content += '%s'
        console.log(previous_cell_content)
        
        // previous_cell_content = 'Implement a linear classifier using pytorch.'

        var api_key_str = "%s"
        var next_cell = Jupyter.notebook.get_cell(current_index)
        var exist_code = next_cell.get_text()

        console.log(api_key_str)
        var data = {
            "instruction": previous_cell_content,
            "api_key_str": api_key_str,
            "exist_code": exist_code,
            "platform": "%s",
            "model": "%s"
        }

        myCallbackFunction(data).then(responseData => {
            var print_content = responseData["output"]
            var next_cell = Jupyter.notebook.get_cell(current_index)
            next_cell.set_text(print_content);
            // Jupyter.notebook.get_cell(current_index - 1).clear_output()
            
            // Jupyter.notebook.select_next();
        })
        // next_cell.set_text(exist_code + "\\n\\n# Waiting for LLM Response ...")
        """ % (instruction, self.api_key, self.platform, self.model)
        print('The code in the following cell will be completed ...')

        display(Javascript(js_code))

    def process_csv(self, file_name, read_mode='r'):
        content_list = open(file_name, read_mode).readlines()[:3]
        content_list = [x.strip() for x in content_list]
        content_str = '\n# '.join(content_list)
        content_str.replace('\t', '\\t')
        prompt = f"""# First three rows of the input file:\n# {content_str}\n# ...\nfile_name = '{file_name}' \ninput_file = open(file_name)""".replace(
            '\n', '\\n')

        js_code = f"""
            Jupyter.notebook.select_prev()
            var new_cell = Jupyter.notebook.insert_cell_below('code');
            // var current_index = Jupyter.notebook.get_selected_index();
            // var next_cell = Jupyter.notebook.get_cell(current_index + 1);
            new_cell.set_text(`{prompt}`);
        """
        print('Run the following cell to read process the format of your csv file.')

        display(Javascript(js_code))
