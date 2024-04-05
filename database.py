# database.py

from model import Animal

class AnimalDatabase:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def obter_nomes_por_raca(self, raca):
        return [animal.nome for animal in self.animais if animal.raca == raca]

    def obter_nomes_por_personalidade(self, personalidade):
        return [animal.nome for animal in self.animais if animal.personalidade == personalidade]

    def obter_nomes_por_aparencia(self, aparencia):
        return [animal.nome for animal in self.animais if animal.aparencia == aparencia]

# Criação do banco de dados
banco_de_dados = AnimalDatabase()

# Adição de animais ao banco de dados
banco_de_dados.adicionar_animal(Animal("Fido", "Cachorro", "Vira-lata", "Brincalhão", "Marrom"))
banco_de_dados.adicionar_animal(Animal("Rex", "Cachorro", "Labrador", "Ativo", "Preto"))
banco_de_dados.adicionar_animal(Animal("Luna", "Cachorro", "Poodle", "Carinhosa", "Branca"))
banco_de_dados.adicionar_animal(Animal("Bolinha", "Cachorro", "Pinscher", "Guarda", "Marrom"))
banco_de_dados.adicionar_animal(Animal("Mel", "Cachorro", "Golden Retriever", "Calma", "Dourada"))
banco_de_dados.adicionar_animal(Animal("Zeca", "Cachorro", "Schnauzer", "Inteligente", "Cinza"))
banco_de_dados.adicionar_animal(Animal("Mimi", "Gato", "Siamês", "Brincalhão", "Branco"))
banco_de_dados.adicionar_animal(Animal("Nina", "Gato", "Persa", "Carinhosa", "Cinza"))
banco_de_dados.adicionar_animal(Animal("Milo", "Gato", "Maine Coon", "Curioso", "Amarelo"))
banco_de_dados.adicionar_animal(Animal("Billy", "Pássaro", "Canário", "Cantor", "Amarelo"))
banco_de_dados.adicionar_animal(Animal("Polly", "Pássaro", "Papagaio", "Falante", "Verde"))
