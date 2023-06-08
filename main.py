class LatexWriter:
    def __init__(self):
        self.latex_content = []

    def add_text(self, text):
        self.latex_content.append(text)

    def add_link(self, text, url):
        link = f'\\href{{{url}}}{{{text}}}'
        self.latex_content.append(link)

    def add_title(self, title):
        self.latex_content.append(f'\\title{{{title}}}')

    def add_animal_list(self, animals):
        self.latex_content.append('\\begin{itemize}')
        for animal in animals:
            self.latex_content.append(f'\\item {animal}')
        self.latex_content.append('\\end{itemize}')

    def generate_latex(self):
        latex_document = '\\documentclass{article}\n'
        latex_document += '\\usepackage{hyperref}\n'
        latex_document += '\\begin{document}\n'
        latex_document += '\n'.join(self.latex_content)
        latex_document += '\n\\end{document}'
        return latex_document

    def save_to_file(self, file_path):
        latex_document = self.generate_latex()
        with open(file_path, 'w') as file:
            file.write(latex_document)
        print(f'File successfully generated: {file_path}')


latex_writer = LatexWriter()
latex_writer.add_title('My Favorite Animals')
latex_writer.add_text('Here is a list of my favorite animals:')
latex_writer.add_animal_list(['Cats', 'Dogs', 'Birds'])
latex_writer.add_text('Check out these links:')
latex_writer.add_link('Google', 'https://www.google.com')
latex_writer.add_link('Wikipedia', 'https://www.wikipedia.org')
latex_writer.save_to_file('output.tex')
