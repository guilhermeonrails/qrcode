import qrcode

link = input('Coloque o link que deseja transformar em qrcode: ')
nome_da_image = input('Escolha um nome para salvar a imagem') + ".png"
img = qrcode.make(link)
img.save(nome_da_image.strip())
print('Seu qrcode foi gerado com sucesso')
