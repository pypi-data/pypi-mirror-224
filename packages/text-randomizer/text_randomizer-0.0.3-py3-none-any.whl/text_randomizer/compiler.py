import random


class Compiler:
    def __init__(self, ast: dict) -> None:
        self.__ast = ast
        self.__ast_count = 0

    def render_random_mixing_node(self, node: dict) -> str:
        random.shuffle(node['values'])
        render_result = ''

        for value in node['values']:
            if isinstance(value, str):
                render_result += value
                continue
            if value.get('type') == 'random_choice':
                render_result += random.choice(
                    self.render_random_choice(value)
                )
                continue
            if value.get('type') == 'random_mixing_with_delimiter':
                render_result += self.render_random_mixing_with_delimiter_node(
                    value
                )
                continue
        return render_result

    def render_random_mixing_with_delimiter_node(self, node: dict) -> str:
        values = []

        for value in node['values']:
            if isinstance(value, str):
                values.append(value)
                continue
            if value.get('type') == 'random_choice':
                values.append(random.choice(value['values']))
        random.shuffle(values)
        render_result = node['delimiter'].join(values)
        return render_result

    def render_random_choice(self, node: dict) -> str:
        values = []

        if node.get('values') is not None:
            for value in node['values']:
                if isinstance(value, str):
                    values.append(value)
                    continue
                if value.get('type') == 'random_mixing':
                    values.append(self.render_random_mixing_node(value))
                    continue
                if value.get('type') == 'random_mixing_with_delimiter':
                    values.append(
                        self.render_random_mixing_with_delimiter_node(value)
                    )
                    continue
        if node.get('nodes') is not None:
            for sub_node in node['nodes']:
                values += self.render_random_choice(sub_node)
        return values

    def render_ast(self) -> str:
        render_result = ''

        while self.__ast_count < len(self.__ast['nodes']):
            node = self.__ast['nodes'][self.__ast_count]

            if node['type'] == 'text':
                render_result += node['value']
            if node['type'] == 'random_choice':
                render_result += random.choice(self.render_random_choice(node))
            if node['type'] == 'random_mixing':
                render_result += self.render_random_mixing_node(node)
            if node['type'] == 'random_mixing_with_delimiter':
                render_result += self.render_random_mixing_with_delimiter_node(
                    node
                )
            self.__ast_count += 1
        return render_result
