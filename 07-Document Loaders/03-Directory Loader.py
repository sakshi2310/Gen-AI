from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader
loader = DirectoryLoader(
    path=r"D:\Gen AI Campasx\07-Document Loaders\Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)


docs2 = loader.lazy_load()
for document in docs2:
    print(document.metadata)