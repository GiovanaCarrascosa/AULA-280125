#importar o flask
from flask import Flask, render_template, request, redirect
import random


app = Flask (__name__)

#aqui vai todas as minhas rotas
#lista de cores pra alterar o fundo do site

# lista de cores da pagina sobre
lista_cores1 = ["#ec407",
               "#f8bbd0",
               "#f48fb1",
               "pink",
               "#e91e63"
                ]

# pagina sobre omar rudberg rs
@app.route("/sobre")

def pagina_sobre():

    cor_de_fundo = random.choice (lista_cores1)

    return render_template("pagina-sobre.html", cor_de_fundo_html = cor_de_fundo)


# lista de frases da pagina inicio
lista_frases = ["Não, não consigo tirar você da minha mente, Yeah yeah.",
                "Então me atinja no rosto, algo real como a dor.",
                "E se eu pedir uma gota de chuva, sei que você vai trazer um oceano.",
                "Lentamente, vejo a luz vermelha, estou preso a esse sonho.",
                "Toda noite, um novo corpo, fantasia de cada noite, pena que você teve que me perder."
                ]

# lista de frases da pagina inicio
lista_imgs = ["omarrudberg_music.jpg",
              "omar-picture02.avif",
              "omar-sfilits.jpg",
              "omar-young.jpg"
              ]

# lista de cores da pagina inicio
lista_cores2 = ["red",
               "#ff5252",
               "#ef9a9a",
               "#ffcdd2"
                ]

# pagina do inicio
@app.route("/", methods = ["GET"])

def pagina_inicial():

    imagem_aleatoria = random.choice (lista_imgs)

    frase_aleatoria = random.choice (lista_frases)

    cor_de_fundo = random.choice (lista_cores2)

    return render_template("pagina-inicial.html", frase_aleatoria_html = frase_aleatoria, imagem_aleatoria_html = imagem_aleatoria, cor_de_fundo_html = cor_de_fundo)


# pagina cadastro
@app.route("/cadastro", methods=["GET"])

def pagina_cadastro():

    return render_template("pagina-cadastro.html", frases_html = lista_frases )


# pagina cadastrar frase, pra pegar da caixa de texto digitado e aparecer na tela de cadastro
@app.route("/post/cadastrarfrase", methods = ["POST"])
def post_cadastrarfrase():

    frase_vinda_do_html = request.form.get("frase")

    lista_frases.append(frase_vinda_do_html)

    return redirect ("/cadastro")

@app.route("/frases/delete/<indice_frase>", methods = ["GET"])

def delete_frases(indice_frase):

    # converte o indice para inteiro pois ele vem como string
    indice_frase = int(indice_frase)
    
    # exclui a cor da lista atraves do indice
    lista_frases.pop(indice_frase)

# redireciona para a rota /cadastro cores
    return redirect ("/cadastro")


# pagina cadastrar cores
# GET = exibi o nome digitado no link do site
# GET = enviar uma pagina para o usuario
@app.route("/cadastrocores", methods=["GET"])

def pagina_cadastro_cores():

    return render_template("pagina-cadastro-cor.html", cores_html = lista_cores2 )

# POST = nao exibi o nome digitado no link do site
# POST = enviar uma informação ou um dado ou uma pagina para o python
@app.route("/post/cadastrocores", methods = ["POST"])

def post_cadastrarcor():

    cor_vinda_do_html = request.form.get("cor")

    lista_cores2.append(cor_vinda_do_html) 

    return redirect ("/cadastrocores")

                          #vou substituir esse valor, á apenas uma variavel 
@app.route("/cores/delete/<indice_cor>", methods = ["GET"])

def delete_cores(indice_cor):

    # converte o indice para inteiro pois ele vem como string
    indice_cor = int(indice_cor)
    
    # exclui a cor da lista atraves do indice
    lista_cores2.pop(indice_cor)

# redireciona para a rota /cadastro cores
    return redirect ("/cadastrocores")

#rodar
app.run(debug=True)
