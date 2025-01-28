#importar o flask
from flask import Flask, render_template
import random


app = Flask (__name__)

#aqui vai todas as minhas rotas
#lista de cores pra alterar o fundo do site
lista_cores = ["red",
               "#FACADA",
               "#BABACA",
               "#00FF00",
               "#00FFFF",
               "#555555"]

@app.route("/sobre")

def pagina_sobre():

    cor_de_fundo = random.choice (lista_cores)

    return render_template("pagina-sobre.html", cor_de_fundo_html = cor_de_fundo)


lista_frases = ["Interessante",
                "Fundamental",
                "Justiçeiro"]

lista_imgs = ["foto-pericia.jpg",
              "distintivo-img.jfif"]

lista_cores = ["red",
               "#FACADA",
               "#BABACA",
               "#00FF00",
               "#00FFFF",
               "#555555"]

@app.route("/inicio")

def pagina_inicial():

    imagem_aleatoria = random.choice (lista_imgs)

    frase_aleatoria = random.choice (lista_frases)

    cor_de_fundo = random.choice (lista_cores)

    return render_template("pagina-inicial.html", frase_aleatoria_html = frase_aleatoria, imagem_aleatoria_html = imagem_aleatoria, cor_de_fundo_html = cor_de_fundo)


#rodar
app.run(debug=True)
