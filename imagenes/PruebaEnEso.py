from bs4 import BeautifulSoup
import requests

for count in range(10,47):
    
	html_doc = requests.get('https://www.eso.org/public/images/potw19'+repr(count)+'a/', headers = {'Accept-Encoding':'identity'})

	#print(html_doc.content)

	soup = BeautifulSoup(html_doc.content, 'html.parser')

	print(soup.img.get("src"))

	nombre_local_imagen = "ima"+repr(count)+".jpg"
	imagen = requests.get(soup.img.get("src")).content
	with open(nombre_local_imagen, 'wb') as handler:
		handler.write(imagen)