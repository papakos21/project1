import bs4
import io

html_doc = io.open("input.txt")

soup = bs4.BeautifulSoup(html_doc, 'html.parser')


#print(soup.h3.string)


exclude = set(['News daily newsletter','Mobile app','Get in touch','BBC World News TV','BBC World Service Radio'])
include = set()
for x in soup.find_all('h3'):
    if x.string not in exclude:
        include.add(x.string)


for i in sorted(list(include)):
    print(i)


