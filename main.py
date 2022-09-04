import discord
import requests
import wikipedia
import asyncio
import os
import datetime
import random
from random import randint
from discord import channel
from discord.ext import commands
from keep_alive import keep_alive
import os
from discord.utils import get





# VERIFICAR SE O BOT ESTÁ A FUNCIONAR 
client = commands.Bot(command_prefix='!')
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("!help"))
  print('Study Bot is ready')



#INTERAÇÃO

@client.command()
async def olá(ctx):
    
  await ctx.send("Olá estou aqui a seu dispor  😊")

@client.command()
async def obrigado(ctx):
    
  await ctx.send("Denada")

@client.command()
async def adeus(ctx):
    
  await ctx.send("Xau fica bem 😭")



# INTRODUÇÃO DO QUE O BOT PODE FAZER (LISTA)
@client.command()
async def lista(ctx):
    
  await ctx.send("Olá, deixo-te aqui uma lista do que posso fazer. Para recorreres a todas as minhas funcionalidades basta utilizares os comandos indicados a baixo.")


# DESCRIÇÃO DO QUE O BOT FAZ
@client.command(pass_context=True)

async def help(ctx):


  
  embed = discord.Embed(title = "!help",colour = discord.Colour.orange())

  embed.add_field(name="!estudofq", value = "Irei te disponibilizar exercícios de exames de Físico-Química do tema que estás a estudar neste preciso momento! 🪂\n\n")

  embed.add_field(name="!estudobg", value = "Irei te disponibilizar exercícios de exames de Biologia/Geologia do tema que estás a estudar neste preciso momento! 🧬\n\n")

  embed.add_field(name="!estudomat", value = "Irei te diponibilizar exercícios de exames de Matemática A do tema que estás a estudar neste preciso momento! 📐\n\n")
  
  embed.add_field(name="!arquivoexames", value = "Irei te redirecionar para o site do iave onde encontrarás exames de todas as disciplinas ordenados por anos. 📝 \n\n")

  #embed.add_field(name="!wiki1", value = "Irei recorrer à wikipedia para te responder a questões simples! 🔍 \n\n") #

  embed.add_field(name="!roletaexames", value = "Irei sortear ao acaso um exame da disciplina pretendida 🎰 \n\n")
  
  embed.add_field(name="!resolucaomanuais \n (ano de escolaridade)", value = "Irei te fornecer a resolução do manual pretendido 📖 \n\n")

  
  
  embed.add_field(name="ㅤㅤ", value = "ㅤㅤ")
  await ctx.send(embed=embed)



#REGRAS
@client.command(pass_context=True)
async def regras(ctx):

 
  
 embed = discord.Embed(title = "Regras", description = "Não spames os canais de texto;\n\nNão mandes textos indesejados;\n\nUtiliza o senso comum;\n\nNão marques as pessoas excessivamente;\n\nEscreve os comandos dos bots no canal <#894932745506136145>;",colour = discord.Colour.orange())

 await ctx.send (embed=embed)


# WIKIPEDIA
@client.command()
async def wiki1(context, *, something):
  
  await context.send(wikipedia.summary(something, sentences=5))


# CLEAR

@client.command(aliases = ['purge', 'delete'])
@commands.has_permissions(manage_messages = True)
async def limpar(ctx, amount: int = 1000000):
    await ctx.channel.purge(limit = amount + 1)



#ESTUDO MATEMÁTICA (SELECIONAR ANO E MATÉRIA)
@client.command(pass_context=True)
async def estudomat(ctx):

 

 embed = discord.Embed(title = "**Por favor seleciona o teu ano de escolaridade (Usa os prefixos)**", description = "**!x10** - 10º Ano de escolaridade;\n\n**!x11** - 11º Ano de escolaridade;\n\n**!x12** - 12º Ano de escolaridade; ",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
 embed.set_image(url="https://i1.wp.com/www.additudemag.com/wp-content/uploads/2021/09/GettyImages-1044168372.jpg?resize=1280%2C720px&ssl=1")

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def x10(ctx):

 

 embed = discord.Embed(title = "**Que matéria queres estudar? (Usa os prefixos)**", description = "**!Geometria10** - Geometria 10º Ano de escolaridade;\n\n**!Funções10** - Funções 10º Ano de escolaridade;",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def x11(ctx):

  

  embed = discord.Embed(title = "**Que matéria queres estudar? (Usa os prefixos)**", description = "**!Geometria11** - Geometria 11º Ano de escolaridade;\n\n**!Funções11** - Funções 11º Ano de escolaridade;\n\n**!Sucessões11** - Sucessões 11º Ano de escolaridade;",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)


@client.command(pass_context=True)
async def x12(ctx):

  

  embed = discord.Embed(title = "**Que matéria queres estudar? (Usa os prefixos)**", description = "**!Probabilidades12** - Probabilidades 12º Ano de escolaridade;\n\n**!Funções12** - Funções 12º Ano de escolaridade;\n\n**!Númeroscomplexos12** - Números Complexos 12º Ano de escolaridade;",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)
   


# lINKS DE GEOMETRIA 10º ANO
@client.command(pass_context=True)
async def Geometria10(ctx):

  

  embed = discord.Embed(title = "**Geometria 10º Ano**", description = "**Pontos retas e planos **  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/pontos_retas_planos.pdf\n\n**Resolução Pontos retas e planos**   https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/pontos_retas_planos_resol.pdf  \n\n**Circulos e esferas**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/circulos_esferas.pdf\n\n**Resolução Circulos e esferas**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/circulos_esferas_resol.pdf\n\n**Mediatriz e plano mediador**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/mediatriz_plano_mediador.pdf\n\n**Resolução Mediatriz e plano mediador**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/mediatriz_plano_mediador_resol.pdf\n\n**Conjuntos de pontos e condições**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/conjuntos_condicoes.pdf\n\n**Resolução Conjuntos de pontos e condições**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/conjuntos_condicoes_resol.pdf\n\n**Vetores**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/vetores.pdf\n\n**Resolução Vetores**   https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/geometria/vetores_resol.pdf",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)




# LINKS DE FUNÇÕES 10º ANO 
@client.command(pass_context=True)
async def Funções10(ctx):

  

  embed = discord.Embed(title = "**Funções 10º Ano**", description = "**Gráficos e características **  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/graficos.pdf\n\n**Resolução Gráficos e características**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/graficos_resol.pdf  \n\n**Transformações de gráficos de funções** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/transformacoes.pdf\n\n**Resolução Transformação de gráficos de funções**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/transformacoes_resol.pdf\n\n**Função Quadrática**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/quadratica.pdf\n\n**Resolução Função Quadrática**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/quadratica_resol.pdf\n\n**Funções polinomiais de grau 3 e 4**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/10ano/funcoes/polinomiais34.pdf\n\n**Resolução Funções polinomiais de grau 3 e 4** - **Resolução Indisponível**",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)



# LINKS DE GEOMETRIA 11º ANO 
@client.command(pass_context=True)
async def Geometria11(ctx):

  

  embed = discord.Embed(title = "**Geometria 11º Ano**", description = "**Trigonometria**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/trigonometria.pdf\n\n**Resolução Trigonometria**   https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/trigonometria_resol.pdf  \n\n**Produto Escalar**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/produto_escalar.pdf\n\n**Resolução Produto Escalar**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/produto_escalar_resol.pdf\n\n**Declive e Inclinação**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/declive_inclinacao.pdf\n\n**Resolução Declive e Inclinação**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/declive_inclinacao_resol.pdf\n\n**Equações de Retas e planos**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/retas_planos.pdf\n\n**Resolução Equações de Retas e planos**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/geometria/retas_planos_resol.pdf",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)



# LINKS DE FUNÇÕES 11º ANO
@client.command(pass_context=True)
async def Funções11(ctx):

  

  embed = discord.Embed(title = "**Funções 11º Ano**", description = "**Limite segundo Heine**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/limite_heine.pdf\n\n**Resolução Limite segundo Heine**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/limite_heine_resol.pdf  \n\n**Funções Racionais**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/funcoes_racionais.pdf\n\n**Resolução Funções Racionais**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/funcoes_racionais_resol.pdf\n\n**Função composta e Função inversa**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/composta_inversa.pdf\n\n**Resolução Função composta e Função inversa**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/composta_inversa_resol.pdf\n\n**Derivadas**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/derivada.pdf\n\n**Resolução Derivadas**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/funcoes/derivada_resol.pdf",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)


# LINKS DE SUCESSÕES 11º ANO 
@client.command(pass_context=True)
async def Sucessões11(ctx):

  

  embed = discord.Embed(title = "**Sucessões 11º Ano**", description = "**Sucessões**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/sucessoes/sucessoes.pdf\n\n**Resolução Sucessões**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/11ano/sucessoes/sucessoes_resol.pdf",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)


# LINKS DE PROBABILIDADE 12º ANO 
@client.command(pass_context=True)
async def Probabilidades12(ctx):

  

  embed = discord.Embed(title = "**Probabilidades  - 12º Ano**", description = "**Probabilidades (noções gerais)**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/probabilidade.pdf\n\n**Resolução Probalidades (noções gerais)**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/probabilidade_prop_resol.pdf\n\n**Acontecimentos, propriedades e operações com conjuntos**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/conjuntos_teoremas.pdf\n\n**Resolução Acontecimentos, propriedades e operações com conjuntos**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/conjuntos_teoremas_prop_resol.pdf\n\n **Probabilidade condicionada**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/prob_condicionada.pdf\n\n **Resolução Probabilidade Condicionada** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/prob_condicionada_prop_resol.pdf\n\n**Cálculo combinatório - Problemas de contagem**\n\nhttps://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/combinatoria_contagem.pdf\n\n **Resoluções Cálculo combinatório - Problemas de contagem**\n\n https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/combinatoria_contagem_prop_resol.pdf\n\n**Cálculo combinatório - Cálculo de probabilidades**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/combinatoria_prob.pdf\n\n**Resolução Cálculo combinatório - Cálculo de probabilidades**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/combinatoria_prob_prop_resol.pdf\n\n**Triângulo de Pascal**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/triang_pascal.pdf\n\n**Resolução Triângulo de Pascal**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/triang_pascal_prop_resol.pdf\n\n **Binómio de Newton**  https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/binomio_newton.pdf\n\n **Resolução Binómio de Newton** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/probabilidades/binomio_newton_prop_resol.pdf ",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)


#LINKS DE FUNÇÕES 12º ANO 
@client.command(pass_context=True)
async def Funções12(ctx):

  

  embed = discord.Embed(title = "**Funções - 12º Ano**", description = "**Exponenciais e Logaritmos** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/exponenciais_logaritmos.pdf\n\n**Resolução Exponenciais e Logaritmos** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/exponenciais_logaritmos_prop_resol.pdf\n\n**Exponenciais e Logaritmos - Resolução gráfica** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/exp_log_resol_grafica.pdf\n\n**Resolução Exponenciais e Logaritmos - Resolução gráfica**\n\n https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/exp_log_resol_grafica_prop_resol.pdf\n\n**Limite segundo Heine**\n\n https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/limite_heine.pdf\n\n**Resolução Limite segundo Heine**\n\n https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/limite_heine_prop_resol.pdf\n\n**Limites e Continuidades** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/limites_continuidade.pdf\n\n**Resolução Limites e Continuidade**\n\n https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/limites_continuidade_prop_resol.pdf\n\n**Teorema de Bolzano** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/bolzano.pdf\n\n**Resolução Teorema de Bolzano**\n\n https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/bolzano_prop_resol.pdf\n\n **Assíntotas** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/assintotas.pdf\n\n**Resolução Assíntotas** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/assintotas_prop_resol.pdf\n\n**1ª derivada** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/1derivada.pdf\n\n **Resolução 1ª derivada** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/1derivada_prop_resol.pdf\n\n **2ª derivada** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/2derivada.pdf\n\n **Resolução 2ª derivada** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/2derivada_prop_resol.pdf\n\n**Funções Trigonométricas** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/func_trigonometricas.pdf\n\n **Resolução Funções Trigonométricas** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/func_trigonometricas_prop_resol.pdf\n\n **Funções Trigonométricas - Resolução Gráfica** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/func_trigonometricas_resol_grafica.pdf\n\n **Resolução Funções Trigonométricas - Resolução Gráfica** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/funcoes/func_trigonometricas_resol_grafica_prop_resol.pdf ",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)




# LINKS DE NÚMEROS COMPLEXOS 12º ANO 

@client.command(pass_context=True)
async def Númeroscomplexos12(ctx):

  

  embed = discord.Embed(title = "**Números Complexos - 12º Ano**", description = "**Operações e simplificação de expressões** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/operac_simplific.pdf\n\n **Resolução Operações e simplificação de expressões** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/operac_simplific_prop_resol.pdf\n\n **Potencias e raízes** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/potencias_raizes.pdf\n\n **Resolução Potencias e raízes** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/potencias_raizes_prop_resol.pdf\n\n **Conjuntos e condições** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/conjuntos_condicoes.pdf\n\n **Resolução Conjuntos e condições** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/conjuntos_condicoes_prop_resol.pdf\n\n **Equações e problemas** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/equacoes_problemas.pdf\n\n **Resolução Equações e problemas** https://mat.absolutamente.net/joomla/images/recursos/fichas/exames/12ano/complexos/equacoes_problemas_prop_resol.pdf ",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)



#ARQUIVO EXAMES

@client.command(pass_context=True)
async def arquivoexames(ctx):

 embed = discord.Embed(title = "**Arquivo Exames**", description = "Olá o link seguinte irá redirecionar-te para o site do iave onde encontrarás exames de todas as disciplinas ordenados por anos: \n\nhttps://iave.pt/provas-e-exames/arquivo/arquivo-provas-e-exames-finais-nacionais-es/",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
 
 embed.set_image(url="https://escolas.aglousa.com/wp-content/uploads/2019/11/IAVE.png")

 await ctx.send (embed=embed)



#ESTUDOFQ LISTA

@client.command(pass_context=True)
async def estudofq(ctx):

  

    
  embed = discord.Embed(title = "Que matéria queres estudar ? (Usa os prefixos)", description = "\n\n\n\n**!a** - Energia e movimentos **(Física 10º Ano)**\n\n**!b** - Energia,fenómenos térmicos e radiação **(Física 10º Ano)**\n\n**!c** - Mecânica **(Física 11º Ano)**\n\n**!d** - Ondas e eletromagnetismo **(Física 11º Ano)** \n\n**!e** - Elementos Químicos e a sua organização **(Química 10º Ano)**\n\n**!f** - Propriedades e Transformações da matéria **(Química 10º Ano)**\n\n**!g** - Equilibrio Químico **(Química 11º Ano)**\n\n**!h** - Reações em sistemas aquosos **(Química 11º Ano)**\n\n**Para recorreres às soluções usa o prefixo !r(letra).**\n **Exemplo: !ra (Resolução Energia e movimentos (Física 10º Ano))** ",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/588/950/418/technology-physics-and-chemistry-chemistry-hd-wallpaper-preview.jpg")

  await ctx.send (embed=embed)



# TABELA PERIÓDICA


@client.command(pass_context=True)
async def tp(ctx):

  

    
  embed = discord.Embed(title = "Tabela Periódica", description = "",colour = discord.Colour.green())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  embed.set_image(url="https://donasebenta.com/wp-content/uploads/2013/12/tabela-peri%C3%B3dica-Dona-Sebenta-e1386174622738.png")

  await ctx.send (embed=embed)

# ESTUDOFQ LINKS

@client.command(pass_context=True)
async def a(ctx):

  

  embed = discord.Embed(title = "**Energias e movimentos (Física 10º Ano)**", description = "https://drive.google.com/file/d/1x1afaQEsBjml_9ahyUTZQ9lGd0M4tF3V/view?usp=sharing",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)



@client.command(pass_context=True)
async def b(ctx):

  embed = discord.Embed(title = "**Energia, fenómenos térmicos e radiação (Física 10º Ano)**", description = "https://drive.google.com/file/d/1onGOmS9FhkPpmWl5r7kHduREH9MOrBjP/view?usp=sharing",colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send (embed=embed)


@client.command(pass_context=True)
async def c(ctx):

 embed = discord.Embed(title = "**Mecânica (Física 11º)**", description = "https://drive.google.com/file/d/1B9Cl1gBQwjjajGIiQpzSBaLH6ZM36Qa9/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)



@client.command(pass_context=True)
async def d(ctx):

 embed = discord.Embed(title = "**Ondas e eletromagnetismo (Física 11º Ano)**", description = "https://drive.google.com/file/d/1nH_1aQucIogr80nuE7-yRLTIzjFQS6-T/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def e(ctx):

 embed = discord.Embed(title = "**Elementos Químicos e a sua organização (Química 10º Ano)**", description = "https://drive.google.com/file/d/1elJ8PFTNBIvhTB7nHxYm6mgsleYfGaE5/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def f(ctx):

 embed = discord.Embed(title = "**Propriedades e Transformações da matéria (Química 10º Ano)**", description = "https://drive.google.com/file/d/1qTriJhVrIkzx3khWKzLTyksR7pFMshwB/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)



@client.command(pass_context=True)
async def g(ctx):

 embed = discord.Embed(title = "**Equilibrio Químico (Química 11º Ano)**", description = "https://drive.google.com/file/d/1z_A8ABRkYxpK19582qk8dkcyBwnSxUQ_/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def h(ctx):

 embed = discord.Embed(title = "**Reações em sistemas aquosos (Química 11º Ano)**", description = "https://drive.google.com/file/d/1f_K4Etw1sWv_IYgxrhI5xaJICjKJt50B/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)



# RESOLUÇÃO FQ 


@client.command(pass_context=True)
async def ra(ctx):

 embed = discord.Embed(title = "**Resolução Energias e movimentos (Física 10º Ano)**", description = "https://drive.google.com/file/d/1kEL6GbiXHtq9irIQWks9TpmCu0w2ZD1C/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rb(ctx):

 embed = discord.Embed(title = "**Resolução Energia, fenómenos térmicos e radiação (Física 10º Ano)**", description = "https://drive.google.com/file/d/18d9v2E2Z5F7EjTTpZsNbpIoWP-0TrwqX/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rc(ctx):

 embed = discord.Embed(title = "**Resolução Mecânica (Física 11º)**", description = "https://drive.google.com/file/d/19MWQMXorl2sG7tObUHN29InyEdK9-cvZ/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rd(ctx):

 embed = discord.Embed(title = "**Resolução Ondas e eletromagnetismo (Física 11º Ano)**", description = "https://drive.google.com/file/d/12ftfjaMBqO2qpkS1DRTKii63aJbBsThe/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def re(ctx):

 embed = discord.Embed(title = "**Resolução Elementos Químicos e a sua organização (Química 10º Ano)**", description = "https://drive.google.com/file/d/1yRZ4XkGxLBgve1n2K_Pguh7Zae1QMUGD/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed) 


@client.command(pass_context=True)
async def rf(ctx):

 embed = discord.Embed(title = "**Resolução Propriedades e Transformações da matéria (Química 10º Ano)**", description = "https://drive.google.com/file/d/1LUZ6B3WHdcn9SsEiDXl16n4t4gAiB2c0/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rg(ctx):

 embed = discord.Embed(title = "**Resolução Equilibrio Químico (Química 11º Ano)**", description = "https://drive.google.com/file/d/1QpABnbKRQjOCOI45FddM01xpUGM0KSRc/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rh(ctx):

 embed = discord.Embed(title = "**Resolução Reações em sistemas aquosos (Química 11º Ano)**", description = "https://drive.google.com/file/d/1IQCJa4rp5swBCJpJib-UM-ID2OvHxr47/view?usp=sharing",colour = discord.Colour.blue())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)








#LISTABG

@client.command(pass_context=True)
async def estudobg(ctx):

  
 embed = discord.Embed(title = "Que matéria queres estudar ? (Usa os prefixos)", description = "\n\n\n\n**__BIOLOGIA__**\n\n**!i** - Unidade 0 – Diversidade na Biosfera\n\n**!j** - Unidade 1 – Obtenção da matéria\n\n**!k** - Unidade 2 – Distribuição de matéria\n\n**!l** - Unidade 3 – Transformação e utilização de energia pelos seres vivos\n\n**!m** - Unidade 4 – Regulação nos seres vivos\n\n**!n** - Unidade 5 – Crescimento e renovação celular\n\n**!o** - Unidade 6 – Reprodução\n\n**!p** - Unidade 7 – Evolução biológica\n\n**!q** - Unidade 8 – Sistemática dos seres vivos\n\n**__GEOLOGIA__**\n\n**!r** - Tema I – A Geologia, os geólogos e os seus métodos\n\n**!s** - Tema II – A Terra, um planeta muito especial\n\n**!t** - Tema III – Compreender a estrutura e a dinâmica da Geosfera\n\n**!u** - Tema IV – Geologia, problemas e materiais do quotidiano\n\n**PARA ACEDER AS RESOLUÇÕES DE BG UTILIZE O PREFIXO !r(letra)**\n\n**__ATENÇÃO : PARA RECORRER ÀS SOLUÇÕES DO TEMA I E II DO TEMA GEOLOGIA UTILIZE SOMENTE O PREFIXO !rr__**",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 embed.set_image(url="https://biotechscope.com/wp-content/uploads/2020/12/2020-top-synthetic-biology-articles_03-730x390.jpg")
 
 await ctx.send (embed=embed)




#LINKSBG

@client.command(pass_context=True)
async def i(ctx):

 embed = discord.Embed(title = "**Unidade 0 – Diversidade na Biosfera **", description = "https://drive.google.com/file/d/1b-bjlN0WzvA_mX91EOH61IJwv6a6rWsn/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def j(ctx):

 embed = discord.Embed(title = "**Unidade 1 – Obtenção da matéria **", description = "https://drive.google.com/file/d/17Anh8I2QOhP555xkvZtZLbP2urv1End7/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def k(ctx):

 embed = discord.Embed(title = "**Unidade 2 – Distribuição de matéria **", description = "https://drive.google.com/file/d/1PNMX7UuAVexRTDQFrOjplgUbsxW8NK9C/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def l(ctx):

 embed = discord.Embed(title = "**Unidade 3 – Transformação e utilização de energia pelos seres vivos **", description = "https://drive.google.com/file/d/1BvIlpM4NZb-3-sehw2Ju20VFZJQ8NA-R/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def m(ctx):

 embed = discord.Embed(title = "**Unidade 4 – Regulação nos seres vivos **", description = "https://drive.google.com/file/d/1Zbf8vWhQRFtC489HiZHrezJ4JibVv5bO/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def n(ctx):

 embed = discord.Embed(title = "**Unidade 5 – Crescimento e renovação celular **", description = "https://drive.google.com/file/d/1BC80vXRdogr_NxzZi8ev7X-A0gt1HcEY/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def o(ctx):

 embed = discord.Embed(title = "**Unidade 6 – Reprodução **", description = "https://drive.google.com/file/d/1r7azQx3vVp5-5ExwZggBZgeyUiTjMmyC/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def p(ctx):

 embed = discord.Embed(title = "**Unidade 7 – Evolução biológica **", description = "https://drive.google.com/file/d/1wdhvXibh7i31Uc_EUsTQlxgbbAnMkxp7/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def q(ctx):

 embed = discord.Embed(title = "**Unidade 8 – Sistemática dos seres vivos **", description = "https://drive.google.com/file/d/1ldnlbjnnaTjkoyWyVISIMOK_cH8lxnSa/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def r(ctx):

 embed = discord.Embed(title = "**Tema I – A Geologia, os geólogos e os seus métodos **", description = "https://drive.google.com/file/d/1W191SHe4UQnv_1_gqy_hBRds9ZNPt422/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def s(ctx):

 embed = discord.Embed(title = "**Tema II – A Terra, um planeta muito especial **", description = "https://drive.google.com/file/d/15EvD7ur2r6OrnJQ86HCXc4fPnb_qwV7v/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def t(ctx):

 embed = discord.Embed(title = "**Tema III – Compreender a estrutura e a dinâmica da Geosfera **", description = "https://drive.google.com/file/d/1DbhiguZk591if3J8wp9MPM31k3roamFM/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def u(ctx):

 embed = discord.Embed(title = "**Tema IV – Geologia, problemas e materiais do quotidiano **", description = "https://drive.google.com/file/d/18FE2uiPGnmfIBAFNpgOGfExHGdyHvevs/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)




#RESOLUÇÃO BG

@client.command(pass_context=True)
async def ri(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 0 – Diversidade na Biosfera **", description = "https://drive.google.com/file/d/1tZE6Ozx_LtgHy6sUc75-u-3y0ZgoFD8c/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rj(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 1 – Obtenção da matéria**", description = "https://drive.google.com/file/d/12K3kTO49nLLAZLq6LV2G9JzSbM4UP7h5/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rk(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 2 – Distribuição de matéria**", description = "https://drive.google.com/file/d/1VB920Iiey8tQKL09lZaj2pDQcUTZjMOb/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def rl(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 3 – Transformação e utilização de energia pelos seres vivos**", description = "https://drive.google.com/file/d/164l4GUMhWqwRyFF4i7xGY6q7GtVpez8m/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rm(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 4 – Regulação nos seres vivos **", description = "https://drive.google.com/file/d/1qI3j-xEDiKulVonSN-iw3EGn-q4eZS6Z/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)

@client.command(pass_context=True)
async def rn(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 5 – Crescimento e renovação celular**", description = "https://drive.google.com/file/d/1IHVy8KZf7pRXzNAomZuHYJzHqINzYwkN/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def ro(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 6 – Reprodução**", description = "https://drive.google.com/file/d/1NZI8bCcEWQLcvNJnA7qyi21hO0UuhV28/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rp(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 7 – Evolução biológica**", description = "https://drive.google.com/file/d/1kaF2K-M3X6uoo-Fo4Hp06SzFHpjdIn9m/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rq(ctx):

 embed = discord.Embed(title = "**Resolução - Unidade 8 – Sistemática dos seres vivos**", description = "https://drive.google.com/file/d/1wG2WMJGvdb00BazJOU5hoG2lxHmcQPM-/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rr(ctx):

 embed = discord.Embed(title = "**Resolução - Tema I – A Geologia, os geólogos e os seus métodos e Tema II – A Terra, um planeta muito especial**", description = "https://drive.google.com/file/d/16m-OyqLTvLtedCRVSN1Wd_agxI8iTKcn/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def rt(ctx):

 embed = discord.Embed(title = "**Resolução - Tema III – Compreender a estrutura e a dinâmica da Geosfera**", description = "https://drive.google.com/file/d/1jfwATHC2WSVHZVEoLghbZtKRbFp3OUeK/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)


@client.command(pass_context=True)
async def ru(ctx):

 embed = discord.Embed(title = "**Resolução - Tema IV – Geologia, problemas e materiais do quotidiano**", description = "https://drive.google.com/file/d/1j2vcP6hh3I5CFBx4__cgAhQNuyWAGPAy/view?usp=sharing",colour = discord.Colour.green())

 embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

 await ctx.send (embed=embed)



#RESOLUÇÕES MANUAIS

@client.command(pass_context=True)
async def resolucaomanuais(ctx):

    embed = discord.Embed(title = "**Resolução de manuais**", description = "**!resolucaopt(__ano de escolaridade__)** 📖\n\n **!resolucaomat(__ano de escolaridade__)** ♾️",colour = discord.Colour.magenta())


    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    
    await ctx.send(embed=embed)




# RESOLUÇÃO MANUAIS DE 11 º ANO 



#RESOLUCÃO MANUAL NOVO PLURAL 11

@client.command(pass_context=True)
async def resolucaopt11(ctx):

    embed = discord.Embed(title = "**Resolução Manual Português 11º Ano - Novo Plural **", description = "https://drive.google.com/file/d/1pNfjIcw7CWL7irO0bQGMNGF0KQLXRK7u/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image(url = "https://www.escolavirtual.pt/static-ereaderp/1017/9789897443114-SE-01/public/cover_aluno_82127.jpg")

    
    await ctx.send(embed=embed)


#RESOLUÇÃO MANUAL MÁXIMO 11 º ANO 

@client.command(pass_context=True)
async def resolucaomat11(ctx):

    embed = discord.Embed(title = "**Por favor selecione a parte do manual pretendido **", description = "**!parte1  - ** Trigonometria e Geometria;\n\n**!parte2 - ** Sucessões e Funções;",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image(url = "https://i1.wp.com/www.additudemag.com/wp-content/uploads/2021/09/GettyImages-1044168372.jpg?resize=1280%2C720px&ssl=1")

    
    await ctx.send(embed=embed)



#RESOLUCAO MÁXIMO 11 ANO PARTE 1 

@client.command(pass_context=True)
async def parte1(ctx):

    embed = discord.Embed(title = "**Resolução Máximo 11º Ano - Parte 1 **", description = "https://drive.google.com/file/d/1Q2fwdKrYGpe0q8AREI_yWd4iXIpMqBhW/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image(url = "https://www.escolavirtual.pt/static-ereaderp/2/9789720855565-SE-01/public/cover_aluno_85556_p1.jpg")

    
    await ctx.send(embed=embed)



#RESOLUCÃO MANUAL MÁXIMO 11º ANO - PARTE 2

@client.command(pass_context=True)
async def parte2(ctx):

    embed = discord.Embed(title = "**Resolução Máximo 11º Ano - Parte 2 **", description = "https://drive.google.com/file/d/1e-aszZPZczg3U45ED-CPcjf2ZXzkw3o0/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image(url = "https://www.escolavirtual.pt/static-ereaderp/2/9789720855565-SE-02/public/cover_aluno_85556_p2.jpg")

    
    await ctx.send(embed=embed)






#RESOLUÇÃO MANUAIS 12 ANO 

#RESOLUÇÃO DO MANUAL DE MATEMÁTICA 12 ANO (GERAL)
@client.command(pass_context=True)
async def resolucaomat12(ctx):

    embed = discord.Embed(title = "**Por favor selecione o tema pretendido **", description = "**!tema1  - ** Combinatória e Probabilidades;\n\n**!tema2 - ** Funções;\n\n**!tema3** - Complexos e Primativas;",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image(url = "https://i1.wp.com/www.additudemag.com/wp-content/uploads/2021/09/GettyImages-1044168372.jpg?resize=1280%2C720px&ssl=1")

    
    await ctx.send(embed=embed)



#RESOLUÇÃO DO MANUAL DE MATEMÁTICA 12 ANO (TEMA 1)

@client.command(pass_context=True)
async def tema1(ctx):

    embed = discord.Embed(title = "Resolução Combinatória e Probabilidades", description = "https://drive.google.com/file/d/1LIV8_ExELgN6c1kdnwi50MK_bLXJGiCB/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image(url="https://papelariakaka.com/5297-medium_default/maximo-matematica-a-12-ano-manual.jpg")

    
    await ctx.send(embed=embed)



#RESOLUÇÃO DO MANUAL DE MATEMÁTICA 12 ANO (TEMA 2)

@client.command(pass_context=True)
async def tema2(ctx):

    embed = discord.Embed(title = "Resolução Funções", description = "https://drive.google.com/file/d/1tHRBbwi2u0KV6HdC0A9H4t3nhp-qsxwc/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_image (url = "https://manuais.moraisepires.pt/4772-large_default/m%C3%A1ximo-matem%C3%A1tica-a-12%C2%BA-ano-.jpg")

    
    await ctx.send(embed=embed)



#RESOLUÇÃO DO MANUAL DE MATEMÁTICA 12 ANO (TEMA 3)

@client.command(pass_context=True)
async def tema3(ctx):

    embed = discord.Embed(title = "Resolução Complexos e Primativas", description = "https://drive.google.com/file/d/1G32anElCQbUukrxx1-dLBZes74EM9Ynu/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)


    embed.set_image (url = "https://moodle.miguelamarelo.com/pluginfile.php/544/course/overviewfiles/max12.jpg")

    
    await ctx.send(embed=embed)



# RESOLUÇÃO DO MANUAL DE PORTUGUÊS


@client.command(pass_context=True)
async def resolucaopt12(ctx):

    embed = discord.Embed(title = "Resolução Manual de Português - Palavras 12º Ano", description = "https://drive.google.com/file/d/1MLw7nNCgSZRnxkmeB-3Guq9S7f40DjJU/view?usp=sharing",colour = discord.Colour.magenta())



    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)


    embed.set_image (url = "https://img.wook.pt/images/palavras-12-portugues-12-ano-maria-joao-pereira/MXwxOTAyNTk1NXwyMDQzNzY2M3wxNjAzNzU2ODAwMDAw/500x")

    
    await ctx.send(embed=embed)




#ROLETA EXAMES - Geral

@client.command(pass_context=True)
async def roletaexames(ctx):
  
  embed = discord.Embed(title = "Roleta de Exames", description = "Por favor seleciona o prefixo correspondente à disciplina que queres realizar o exame:\n\n **!roletaexamesbg** - Vou sortear um exame de biologia e apresentar-te o link abaixo\n\n **!roletaexamesfq** - Vou sortear um exame de físico-química e apresentar-te o link abaixo\n\n **!roletaexamesmat** - Vou sortear um exame de matemática e apresentar-te o link abaixo ", colour = discord.Colour.orange())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  embed.set_image (url = "https://img.freepik.com/vetores-gratis/roda-da-fortuna_79145-335.jpg?size=626&ext=jpg")

  await ctx.send(embed=embed)



#ROLETA EXAMES - BG 

examesbg = ["https://iave.pt/wp-content/uploads/2020/04/biologia102_pef1_2006.pdf","https://iave.pt/wp-content/uploads/2020/04/biologia102_pef2_2006.pdf","https://iave.pt/wp-content/uploads/2020/04/bio_geo702_pef1_2007.pdf","https://iave.pt/wp-content/uploads/2020/04/bio_geo702_pef2_2007.pdf","https://iave.pt/wp-content/uploads/2020/04/biologia_geologia702_pef1_2008.pdf","https://iave.pt/wp-content/uploads/2020/04/biologia_geologia702_pef2_2008.pdf","https://iave.pt/wp-content/uploads/2020/04/biologia_geologia702_pef1_2009.pdf","https://iave.pt/wp-content/uploads/2020/04/biologia_geologia702_pef2_2009.pdf","https://iave.pt/wp-content/uploads/2020/04/biologia_geologia702_pef1_2010-3.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2010-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2011-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2011-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2012-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2012-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2013-1fase/Biologia-Geologia-v1.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2013-2fase/Biologia-Geologia-v1.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2014-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2014-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2015-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2015-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2016-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2016-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2017-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2018-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2018-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2019-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2019-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2020-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2020-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2021-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2021-2fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2022-1fase/Biologia-Geologia.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2022-2fase/Biologia-Geologia.pdf"]


@client.command(pass_context=True)
async def roletaexamesbg(ctx):
  
  embed = discord.Embed(title = "Aqui tens o teu exame. Bom estudo!", description = ((random.choice(examesbg))), colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send(embed=embed)


#ROLETA EXAMES - FQ

examesfq = ["https://iave.pt/wp-content/uploads/2020/04/FQA715_exame_06_fase1.pdf","https://iave.pt/wp-content/uploads/2021/09/EX-FQA715-F2-2021-V1_net.pdf","https://iave.pt/wp-content/uploads/2020/04/fisica_quimicaA715_pef1_07.pdf","https://iave.pt/wp-content/uploads/2020/04/fisica_quimicaA715_pef2_06.pdf","https://iave.pt/wp-content/uploads/2020/04/fisica_quimicaA715_pef1_08.pdf","https://iave.pt/wp-content/uploads/2020/04/fisica_quimicaA715_pef2_08.pdf","https://iave.pt/wp-content/uploads/2020/04/fisica_quimicaA715_pef1_09.pdf","https://iave.pt/wp-content/uploads/2020/04/fisica_quimicaA715_pef2_09.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2010-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2010-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2011-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2011-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2012-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2012-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2013-2fase/Fisica-Quimica-v1.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2013-1fase/Fisica-Quimica-v1.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2014-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2014-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2015-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2015-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2016-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2016-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2017-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2017-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2018-1fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2018-2fase/Fisica-Quimica.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2019-2fase/Fisica-Quimica-A.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2019-1fase/Fisica-Quimica-A.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2020-1fase/Fisica-Quimica-A.pdf","https://www.examesnacionais.com.pt/exames-nacionais/11ano/2020-2fase/Fisica-Quimica-A.pdf","examesnacionais.com.pt/exames-nacionais/11ano/2021-1fase/Fisica-Quimica-A.pdf","https://iave.pt/wp-content/uploads/2021/09/EX-FQA715-F2-2021-V1_net.pdf","https://iave.pt/wp-content/uploads/2022/06/EX-FQA715-F1-2022-V1_net.pdf","https://iave.pt/wp-content/uploads/2022/07/EX-FQA715-F2-2022-V1_net.pdf"]



@client.command(pass_context=True)
async def roletaexamesfq(ctx):
  
  embed = discord.Embed(title = "Aqui tens o teu exame. Bom estudo!", description = ((random.choice(examesfq))), colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send(embed=embed)


  # ROLETA EXAMES MAT 

examesmat = ["https://iave.pt/wp-content/uploads/2020/04/matematica435_pef1_06.pdf","https://iave.pt/wp-content/uploads/2020/04/matematica435_pef2_06.pdf","https://iave.pt/wp-content/uploads/2020/04/matematica635_pef1_07.pdf","https://iave.pt/wp-content/uploads/2020/04/matematica635_pef2_07.pdf","https://www.examesnacionais.com.pt/exames-nacionais/12ano/2008-1fase/Matematica-A.pdf","https://iave.pt/wp-content/uploads/2020/04/matematica_A635_pef2_08.pdf","https://iave.pt/wp-content/uploads/2020/04/matematica_A635_pef1_09.pdf","https://iave.pt/wp-content/uploads/2020/04/matematica_A635_pef2_09.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2010_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2010_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2011_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2011_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2012_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2012_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2013_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2013_Fase2_Prova.pdf", "https://www.matematica.pt/docs/enunciados/12ano/exame/2014_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2014_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2015_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2015_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2016_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2016_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2017_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2017_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2018_Fase1_Prova_C1.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2018_Fase2_Prova_C1.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2019_Fase1_Prova_C1.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2019_Fase2_Prova_C1.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2020_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2020_Fase2_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2021_Fase1_Prova.pdf","https://www.matematica.pt/docs/enunciados/12ano/exame/2021_Fase2_Prova.pdf","",""]


@client.command(pass_context=True)
async def roletaexamesmat(ctx):
  
  embed = discord.Embed(title = "Aqui tens o teu exame. Bom estudo!", description = ((random.choice(examesmat))), colour = discord.Colour.blue())

  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

  await ctx.send(embed=embed)


# FORMULÁRIO DE EXAMES 

@client.command(pass_context=True)
async def formulariofq(ctx):
  
  
  embed = discord.Embed(title = "**Formulário - Físico -  Química A**   ", description = "", colour = discord.Colour.orange())

  embed.set_author(name=ctx.author.display_name,       icon_url=ctx.author.avatar_url)

  embed.set_image (url =      "https://estudafq.pt/wp-content/uploads/2019/09/Formul%C3%A1rio-exames-e-TP_Page_1-724x1024.jpg")


  await ctx.send(embed=embed)

#  https://estudafq.pt/wp-content/uploads/2019/09/Formul%C3%A1rio-exames-e-TP_Page_1-724x1024.jpg#




@client.command(pass_context=True)
async def formulariomat(ctx):
  
  
  embed = discord.Embed(title = "**Formulário - Matemática A**   ", description = "", colour = discord.Colour.orange())

  embed.set_author(name=ctx.author.display_name,       icon_url=ctx.author.avatar_url)

  embed.set_image (url =      "http://explicacoesmatematica.com.pt/wp-content/uploads/2020/07/image-125.png")


  await ctx.send(embed=embed)
  







#@client.command(pass_context=True)
#async def estudopt(ctx):
 # embed = discord.Embed(title = "")








  

# DESAFIOS
@client.command()
async def desafios (ctx):
  await ctx.send ("Olá Gafanhotos do 11º B, sempre que queiram rever desafios e resoluções de desafios que foram propostos neste canal basta recorrerem respetivamente aos seguintes comandos [!desafio(número do desafio)] ; [resolucaodesafio(número do desafio)] Bom estudo !!!")


# DESAFIO 1 - ENUNCIADO 

@client.command()
async def desafio1 (ctx):
  await ctx.send ("Desafio 1 ", file=discord.File('desafio1.png'))


# DESAFIO 1 - RESOLUÇÃO

@client.command()
async def resolucaodesafio1 (ctx):
  await ctx.send ("@everyone Resolução do Desafio 1 ", file=discord.File('Resolução Desafio 1.jpeg'))


# DESAFIO 2 - ENUNCIADO 
@client.command()
async def desafio2 (ctx):
  await ctx.send ("Desafio 2", file=discord.File('Desafio2.jpeg'))


# DESAFIO 2 - PRINCIPAL 
@client.command()
async def Desafio2 (ctx):
 await ctx.send ("@everyone Desafio 2 (enviem as vossas resoluções recorrendo ao comando spoiler)", file=discord.File('Desafio2.jpeg'))


# RESOLUÇÃO DO DESAFIO 2
@client.command()
async def resolucaodesafio2 (ctx):
  await ctx.send ("Resolução do Desafio 2 ", file=discord.File('resolucaodesafio2.jpeg'))


# DESAFIO 3 - ENUNCIADO 
@client.command()
async def desafio3 (ctx):
  await ctx.send ("Desafio 3", file=discord.File('desafio3.png'))


# DESAFIO 3 - PRINCIPAL 
@client.command()
async def Desafio3 (ctx):
  await ctx.send ("@everyone Desafio 3 - Exercício excelente para a matéria que estão a dar! Muito trabalhoso mas garanto-vos se conseguirem resolver este desafio sem qualquer problemas estão à vontade em qualquer exercício deste tipo! Bom Trabalho (enviem as vossas resoluções recorrendo ao comando spoiler)", file=discord.File('desafio3.png'))


@client.command()
async def ResolucaoDesafio3 (ctx):
  await ctx.send ("Resolução do Desafio 3 ", file=discord.File('resolucaodesafio3.png'))


#VOICE CHANNEL - TEMPORIZADOR

@client.command(pass_context = True)
async def temporizadoron(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("Por favor entre no voice chat ")



@client.command(pass_context = True)
async def temporizadoroff(ctx):
  if (ctx.voice_client):

    await ctx.guild.voice_client.disconnect()
    await ctx.send ("Sai do canal de voz")
  else:
    await ctx.send("Não estou num canal de voz")
    


















keep_alive()
client.run(os.environ['TOKEN'])







