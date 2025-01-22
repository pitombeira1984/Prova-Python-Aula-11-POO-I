
class Animal:
  def falar(self):
    print("Este animal faz um som.")

class Cachorro(Animal):
  def falar(self):
    print("O cachorro late.")

class Gato(Animal):
  def falar(self):
    print("O gato mia.")


meu_cachorro = Cachorro()
meu_gato = Gato()

meu_cachorro.falar()  
meu_gato.falar()