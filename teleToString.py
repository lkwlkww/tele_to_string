import os
from bs4 import BeautifulSoup

### edit this section accordingly ###
cwd = os.getcwd()
#directory = cwd + "/ChatExport_2021-10-18/"
### edit this section accordingly ###

text = ""
for filename in os.listdir(directory):
    for i in range(1, 46): # edit this range accordingly #
        if i == 1:
            filename = 'messages'+'.html'
        else:
            filename = 'messages'+str(i)+'.html'
        file = os.path.join(directory,filename)
        file = open(file)

        soup = BeautifulSoup(file, 'html.parser')
        div = soup.findAll('div', {'class': 'text'})
        for line in div:
            linecount += 1
            text += line.text
print(text)