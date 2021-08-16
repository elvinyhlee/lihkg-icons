from icon_path import IconPath


if __name__ == '__main__':
    with open('README_TEMPLATE', 'r') as file_object:
        readme = file_object.read()

    with open('./README.md', 'w') as file_object:
        body = ''
        for k, v in IconPath.mapping.items():
            body += '## ' + v[1]
            body += '\n\n'
            for i in v[0]:
                name = i.replace('/', '_')
                body += f'![{name}](./assets/{name}.gif)'
            body += '\n\n'

        readme = readme.replace('{body}', body)
        file_object.write(readme)
