import re
import sys


def markdowntohtml(markdown): 
    #Titulos
    markdown = re.sub(r'###(.*)', r'<h3>\1</h3>', markdown) 
    markdown = re.sub(r'##(.*)',r'<h2>\1</h2>',markdown)
    markdown = re.sub(r'#(.*)',r'<h1>\1</h1>',markdown)

    #Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    #Italico
    markdown = re.sub(r'\*(.*?)\*',r'<i>\1</i>',markdown)
                
    #Listas Numerada: 

    markdown = re.sub(r'(\d+\.\s+.*\n?)+', r'<ol>\g<0></ol>', markdown)
    markdown = re.sub(r'\d+\.\s+(.*)', r'<li>\1</li>\n', markdown)

    #Listas nao Numeradas: 
    markdown = re.sub(r'(-\s+.*\n?)+', r'<ul>\g<0></ul>', markdown)
    markdown = re.sub(r'-\s+(.*)', r'<li>\1</li>\n', markdown)
    
    #Img
    markdown = re.sub(r'\!\[(.*)\]\((.*)\)',r'<img src="\2" alt="\1"/>',markdown)
    #Link 
    markdown = re.sub(r'\[(.*)\]\((.*)\)',r'<a href="\2">\1</a>',markdown)


    return markdown

def main():
    if len(sys.argv) != 2:
        print("Por favor, forneça o caminho do arquivo Markdown como argumento.")
        sys.exit(1)

    markdown_file_path = sys.argv[1]

    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        html_content = markdowntohtml(markdown_content)
        html_file_path = markdown_file_path.replace('.md', '.html')

        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"Conversão concluída com sucesso. O arquivo HTML foi salvo em: {html_file_path}")

    except FileNotFoundError as e:
        print(f"O arquivo {markdown_file_path} não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()