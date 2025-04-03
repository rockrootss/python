# 1. Análisis del Zen de Python
# Copie el texto del Zen de Python en una variable e imprima todas las líneas cuya segunda
# palabra comience con una vocal (A, E, I, O, U, a, e, i, o, u).
# El Zen de Python es una colección de principios que guían la filosofía de diseño de Python,
# escrita en forma de aforismos. Resalta la simplicidad, legibilidad y claridad en el código.
# Para verlo en Python, ejecute en la consola import this
# Para este punto debe colocar el contenido del Zen de python en una variable string: 

zen_text =  """ Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! """

vocales = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

for lines in zen_text.split('\n'):
    palabras = lines.split()
    if palabras[1].startswith(vocales):
        print(lines)



