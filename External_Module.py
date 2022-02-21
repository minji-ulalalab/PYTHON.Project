html_doc = """
<html>
    <head>
        <title>TEST PAGE</title>
    </head>
    <body>
        <h1>HELLO WORLD</h1>
    </body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.select("h1"))
print(soup.select("h1")[0].string)