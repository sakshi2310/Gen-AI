from langchain_text_splitters import CharacterTextSplitter
 

text = """Indian people or Indians are the citizens and nationals of the Republic of India or people who trace their ancestry to India. While the demonym "Indian" applies to people originating from the present-day India, it was also used as the identifying term for people originating from what is now Bangladesh and Pakistan prior to the Partition of India in 1947.[38][39] The term "Indian" does not refer to a single ethnic group, but is used as an social construct for the various ethnic groups in or from India.[40]

In 2022, the population of India stood at 1.4 billion people. According to United Nations forecasts, India overtook China as the world's most populous country by the end of April 2023, containing 17.50 percent of the global population.[41][42][43] In addition to the Indian population, the Indian overseas diaspora also boasts large numbers, particularly in former British colonies due to the historical Indian indenture system, Arab states of the Persian Gulf, and the Western world.[16]"""

splitter =  CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=" "
)

result=splitter.split_text(text)
print(result)


print("--------------------------------------------------------")

from langchain_community.document_loaders import PyPDFLoader

loader =  PyPDFLoader(r"D:\Gen AI Campasx\07-Document Loaders\pdf_domo.pdf")

docs = loader.load()
splitter =  CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=" "
)
result = splitter.split_documents(docs)
print(result[0].page_content)


