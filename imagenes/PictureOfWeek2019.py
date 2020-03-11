from bs4 import BeautifulSoup
import requests
import mechanize
#TRAER IMAGENES
for count in range(2,52):
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

#INGRESAR A BASE DE DATOS
br=mechanize.Browser()
br.open("http://127.0.0.1:8000/admin/polls/dataimage/add/")
for form in br.forms():
    print ("Form name:", form.name)
    print (form)

form = br.select_form(nr=0)
br['username'] = 'admin'
br['password'] = 'unimanager'
# fill out other fields

req = br.submit()
#print(req.read())
#TRAER LO DEMAS
for count in range(1,52):
    print(count)
    if(count<10):
        html_doc = requests.get('https://www.eso.org/public/images/potw190'+repr(count)+'a/', headers = {'Accept-Encoding':'identity'})
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        Link = 'https://www.eso.org/public/images/potw190'+repr(count)+'a/'
    else:   
        html_doc = requests.get('https://www.eso.org/public/images/potw19'+repr(count)+'a/', headers = {'Accept-Encoding':'identity'})
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        Link = 'https://www.eso.org/public/images/potw19'+repr(count)+'a/'

    Entradas= soup.find_all('div', {'class': 'col-md-9 left-column'})
    for i, entrada in enumerate(Entradas):
        try:
            titulo = entrada.find('h1').getText()
        except UnicodeEncodeError:
            titulo='.'
        except AttributeError:
            titulo='.'

    Entradas2= soup.find_all('p', {'dir': 'ltr'})
    for i, entrada2 in enumerate(Entradas2):
        if i==0:
            try:
                parrafo = entrada2.getText()
            except UnicodeEncodeError:
                parrafo='.'
            except AttributeError:
                parrafo='.'

    Entrada3= soup.find_all('div', {'class': 'credit'})
    for i, entrada3 in enumerate(Entrada3):
        try:
            Creditos= entrada3.getText()
        except UnicodeEncodeError:
            Creditos='.'
        except AttributeError:
            Creditos='.'

    Entrada4= soup.find_all('td', {'class': 'title'})
    for i, entrada4 in enumerate(Entrada4):
        
        Categorias= entrada4
    try:
        Categoria1=Categorias.next.next.next.getText()
    except UnicodeEncodeError:
        Categoria1='.'
    except AttributeError:
        Categoria1='.'
    #print(titulo)
    Parrafos=(parrafo).encode('utf8')
    print((parrafo).encode('utf8'))
    print(Link)
    print(Creditos)
    
    print(Categoria1)
    
    #LLENAR BASE DE DATOS
    br.open("http://127.0.0.1:8000/admin/polls/dataimage/add/")
    for form in br.forms():
        print ("Form name:", form.name)
        print (form)


    form = br.select_form(nr=0)
    br['title'] = titulo
    br['description'] = Parrafos
    br['link_news'] = Link
    br['credit'] = Creditos
    br['category'] = Categoria1
    br['image'] = "ima"+repr(count)+".jpg"

    req = br.submit()