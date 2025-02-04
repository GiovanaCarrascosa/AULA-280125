#importar o flask
from flask import Flask, render_template
import random


app = Flask (__name__)

#aqui vai todas as minhas rotas
#lista de cores pra alterar o fundo do site
lista_cores = ["red",
               "blue",
               "orange",
               "pink"
                ]

@app.route("/sobre")

def pagina_sobre():

    cor_de_fundo = random.choice (lista_cores)

    return render_template("pagina-sobre.html", cor_de_fundo_html = cor_de_fundo)


lista_frases = ["Não, não consigo tirar você da minha mente, Yeah yeah",
                "Então me atinja no rosto, algo real como a dor, como se não pudéssemos ficar mais próximos, eu só quero me perder. Então, me chame pelo, me chame pelo seu nome!",
                "Justiçeiro",
                "E se eu pedir uma gota de chuva, sei que você vai trazer um oceano",
                "Lentamente, vejo a luz vermelha, estou preso a esse sonho, lentamente, nos damos a noite toda, como se estivéssemos dançando, você e eu"
                ]

lista_imgs = ["omarrudberg_music.jpg",
              "omar-picture02.avif",
              "omar-sfilits.jpg",
              "omar-young.jpg"]

lista_cores = ["red",
               "blue",
               "orange",
               "pink"
                ]

@app.route("/inicio")

def pagina_inicial():

    imagem_aleatoria = random.choice (lista_imgs)

    frase_aleatoria = random.choice (lista_frases)

    cor_de_fundo = random.choice (lista_cores)

    return render_template("pagina-inicial.html", frase_aleatoria_html = frase_aleatoria, imagem_aleatoria_html = imagem_aleatoria, cor_de_fundo_html = cor_de_fundo)


#rodar
app.run(debug=True)
