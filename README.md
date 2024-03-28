# Web Scraping Example
Um simples exemplo de _Web Scraping_ utilizando o framework **Selenium**.
## Pré-requisitos
- Python
- Selenium
- Pandas

Nota: Caso tenha o pip instalado, utilize o seguinte comando para instalar as dependências:
<pre><code>pip install -r requirements.txt</code></pre>
## Como funciona
1. Programaticamente acessa o site [https://books.toscrape.com](https://books.toscrape.com) (um site fictício designado para pratica _Web Scraping_).
2. Itera por todos os livros presentes na página atual.
3. Em cada iteração é extraída informações de cada livro: título, categoria, avaliação, preço, estoque, descrição.
4. Salva todos os dados obtidos em um arquivo CSV.
