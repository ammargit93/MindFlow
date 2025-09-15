from utils.load_yaml import load_config
from index.chroma import ChromaIndex
import uuid

cfg = load_config()['routes']
indices = []

for config in cfg:
    collection_name = config['name']
    document = config['utterances']
    llm = config['action'].split(":")[-1]
    
    chroma_index = ChromaIndex(collection_name=collection_name, llm=llm)
    chroma_index.add_document(documents=document, ids=[str(uuid.uuid1()) for _ in document])
    indices.append(chroma_index)
        