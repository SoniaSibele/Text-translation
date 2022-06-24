
from googletrans import Translator
import googletrans
translator = Translator()
print(translator.translate('안녕하세요.'))
print(translator.translate('안녕하세요.', dest='ja'))
print(translator.translate('veritas lux mea', src='la', dest='pt'))


# deteçao de linguagem
print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))
print(translator.detect('この文章は日本語で書かれました。'))
print(translator.detect('This sentence is written in English.'))
print(translator.detect('Tiu frazo estas skribita en Esperanto.'))
print(translator.detect('Esta frase está escrita em Português'))

#traduçao ingles portugues
texto_en = input("Write a sentence: ")
texto_pt = translator.translate(texto_en, src="en", dest="pt")
print("Original text:", texto_en)
print("Translation:", texto_pt.text)

#traduçao portugues ingles
texto_pt = input("Escreva uma frase: ")
texto_en = translator.translate(texto_pt, src="pt", dest="en")
print("Texto original:", texto_pt)
print("Tradução:", texto_en.text)
