# EJEMPLO DE PRUEBA TECNICA PARA JUNIOR DE PYTHON

#   Dispones de una variable 'text' que es una cadena de texto
#   Debes de contar las palabras y devolver cuantas veces se repiten cada una de ellas
#   Ejemplo --> 'nadie' aparece 2 veces



def toLowecase(text):
    LowerCase = text.lower()
    return LowerCase

def cleanText(textLower):
    CleandedText = textLower.replace(',','').replace('.','')
    separateText = CleandedText.split(" ")
    return separateText


def countWords(CleanedText):
    diccionario={}

    for word in CleanedText:
        if word in diccionario:
            diccionario[word] +=1
        else:
            diccionario[word] = 1
    return   diccionario 

text = "Creo que a veces la gente es la que nadie espera nada, la que hace cosas que nadie puede imaginar."

LowerCase = toLowecase(text)
CleanedText = cleanText(LowerCase)
countedWord = countWords(CleanedText)

print(countedWord)
