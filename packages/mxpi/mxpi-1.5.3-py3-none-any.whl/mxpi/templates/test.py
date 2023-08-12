from lxml import etree

file_path='index.html'
with open(file_path, "r",encoding='utf-8') as file:
    html = file.read()

dom = etree.HTML(html)

dom.xpath('//*[@id="toolbox-categories"]').text='123'


dom.write("test.html", encoding='utf-8')



