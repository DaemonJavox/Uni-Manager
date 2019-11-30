from bs4 import BeautifulSoup
import requests

for count in range(1,47):
    if(count<10):
        html_doc = requests.get('https://www.eso.org/public/images/potw190'+repr(count)+'a/', headers = {'Accept-Encoding':'identity'})
        soup = BeautifulSoup(html_doc.content, 'html.parser')

        print(soup.img.get("src"))

        nombre_local_imagen = "ima"+repr(count)+".jpg"
        imagen = requests.get(soup.img.get("src")).content
        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)
    else:   
        html_doc = requests.get('https://www.eso.org/public/images/potw19'+repr(count)+'a/', headers = {'Accept-Encoding':'identity'})


        #print(html_doc.content)

        soup = BeautifulSoup(html_doc.content, 'html.parser')

        print(soup.img.get("src"))

        nombre_local_imagen = "ima"+repr(count)+".jpg"
        imagen = requests.get(soup.img.get("src")).content
        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)