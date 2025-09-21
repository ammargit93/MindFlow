# MindFlow 🚀

A minimal semantic router powered by embeddings & ChromaDB

## 📌 Overview

MindFlow is an experimental project that routes user queries to the right action or model by comparing semantic similarity.
Instead of waiting for an LLM to decide, we use embeddings + vector search for fast routing.

## 🔑 Features
- **Semantic Routing**: Classifies user queries based on embedding similarity.

- **Pluggable Vector Database**: Supports pluggable vector databases (currently only supports chroma,faiss).

- **Configurable via YAML**: Define routes, utterances, LLMs, and API providers in a simple YAML file.

- **Pluggable LLMs**: Supports multiple backends (Hugging Face Inference API, OpenAI, local models).

- **Automatic Embeddings**: Generates embeddings for utterances automatically using FastEmbed.

Inspired by [semantic-router](https://github.com/aurelio-labs/semantic-router)