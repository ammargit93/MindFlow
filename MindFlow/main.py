from utils.load_yaml import load_config
from index.chroma import ChromaIndex
import uuid

cfg = load_config()['routes']

all_indices = []


for config in cfg:
    collection_name = config['name']
    document = config['utterances']
    llm = config['action'].split(":")[-1]
    
    chroma_index = ChromaIndex(collection_name=collection_name)
    chroma_index.add_document(documents=document, ids=[str(uuid.uuid1()) for _ in document])
    all_indices.append(chroma_index)

query = "How is the weather?"
for index in all_indices:
    
    res = index.query_document(query)
    avg_dist = sum(res['distances'][0])/len(res['distances'][0])
    print(f"{res['documents']} {avg_dist} {index.index_name}\n")
