#importar o flask
from flask import Flask, render_template, request, redirect
import random
from data import listas_configuracao as listas

app = Flask (__name__)

#aqui vai todas as minhas rotas
#lista de cores pra alterar o fundo do site



# pagina sobre omar rudberg rs
@app.route("/sobre")

def pagina_sobre():

    cor_de_fundo = random.choice (listas.lista_cores1)

    return render_template("pagina-sobre.html", cor_de_fundo_html = cor_de_fundo)





# pagina do inicio
@app.route("/", methods = ["GET"])

def pagina_inicial():

    imagem_aleatoria = random.choice (listas.lista_imgs)

    frase_aleatoria = random.choice (listas.lista_frases)

    cor_de_fundo = random.choice (listas.lista_cores2)

    return render_template("pagina-inicial.html", frase_aleatoria_html = frase_aleatoria, imagem_aleatoria_html = imagem_aleatoria, cor_de_fundo_html = cor_de_fundo)







# PAGINA CADASTRAR FRASE
@app.route("/cadastro", methods=["GET"])

def pagina_cadastro():

    return render_template("pagina-cadastro.html", frases_html = listas.lista_frases )


# pagina cadastrar frase, pra pegar da caixa de texto digitado e aparecer na tela de cadastro
@app.route("/post/cadastrarfrase", methods = ["POST"])
def post_cadastrarfrase():

    frase_vinda_do_html = request.form.get("frase")

    listas.lista_frases.append(frase_vinda_do_html)

    return redirect ("/cadastro")

@app.route("/frases/delete/<indice_frase>", methods = ["GET"])

def delete_frases(indice_frase):

    # converte o indice para inteiro pois ele vem como string
    indice_frase = int(indice_frase)
    
    # exclui a cor da lista atraves do indice
    listas.lista_frases.pop(indice_frase)

# redireciona para a rota /cadastro cores
    return redirect ("/cadastro")






# PAGINA CADASTRAR CORES
# GET = exibi o nome digitado no link do site
# GET = enviar uma pagina para o usuario
@app.route("/cadastrocores", methods=["GET"])

def pagina_cadastro_cores():

    return render_template("pagina-cadastro-cor.html", cores_html = listas.lista_cores2 )

# POST = nao exibi o nome digitado no link do site
# POST = enviar uma informação ou um dado ou uma pagina para o python
@app.route("/post/cadastrocores", methods = ["POST"])

def post_cadastrarcor():

    cor_vinda_do_html = request.form.get("cor")

    listas.lista_cores2.append(cor_vinda_do_html) 

    return redirect ("/cadastrocores")

                          #vou substituir esse valor, á apenas uma variavel 
@app.route("/cores/delete/<indice_cor>", methods = ["GET"])

def delete_cores(indice_cor):

    # converte o indice para inteiro pois ele vem como string
    indice_cor = int(indice_cor)
    
    # exclui a cor da lista atraves do indice
    listas.lista_cores2.pop(indice_cor)

# redireciona para a rota /cadastro cores
    return redirect ("/cadastrocores")








#rodar
app.run(debug=True)
