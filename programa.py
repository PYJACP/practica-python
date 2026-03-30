import random,logging


logging.basicConfig(filename='registro.log',level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')


respuestas=['It is certain','It is decidedly so','Yes','Reply hazy try again'
            ,'Ask again later','Concentrate and ask again','My reply is no','Outlook not so good','Very doubtful']
class Numero_random:
    def __init__(self,answer_number):
        self.answer_number=answer_number
    def gets_answer(self,LISTA):     
        return LISTA[self.answer_number-1]
    def aumentar_respuestas(self,LISTA):
        poner=input('> Ingrese la nueva respuesta ')
        LISTA+=[poner]
        return (f'Proceso realizado con exito : {poner}, esta agregado')


def jugar(): 
    n=input('Quieres continuar si o no')
    while n.upper()=='SI': 
        r=random.randint(1,len(respuestas))
        objeto=Numero_random(r)
        x=input('Quieres ver, aumentar o borrar?')
        if x.upper()=='VER':
           fortune=objeto.gets_answer(respuestas)
           logging.info(f"Tu número fue {r} y la bola dice: {fortune}")
        elif x.upper()=='AUMENTAR': 
            aumento=objeto.aumentar_respuestas(respuestas)
            logging.info(aumento)
        n=input('Quieres continuar si o no')
jugar()