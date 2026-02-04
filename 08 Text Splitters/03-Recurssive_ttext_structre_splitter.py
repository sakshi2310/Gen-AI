from langchain_text_splitters import RecursiveCharacterTextSplitter ,Language
 

text = """class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()      # Inherited method
d.sound()"""

splitter =  RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0
)

result=splitter.split_text(text)
print(result)
print(len(result))

