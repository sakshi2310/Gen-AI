from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"07-Document Loaders\pdf_domo.pdf")

docs = loader.load()

# print(docs)
print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

# there are many pdf loaders in the langchain

# Pypdf -> when we have only text in the pdf only
# table structure ---> pdflumberloader
# use the langchain documentations for all the pdf
