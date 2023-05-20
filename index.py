from dotenv import load_dotenv
load_dotenv()

import os
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from langchain.document_loaders import TextLoader
loader = TextLoader('./state_of_the_union.txt', encoding='utf8')

from langchain.indexes import VectorstoreIndexCreator

index = VectorstoreIndexCreator().from_loaders([loader])

query = input()
out = index.query(query)

print(out)