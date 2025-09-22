# MindFlow 🚀

A minimal config-driven semantic router for network requests and API services.

## 📌 Overview

MindFlow routes incoming requests to the appropriate service based on semantic similarity or rule-based triggers.
It allows businesses to define routing logic entirely via configuration.

Instead of coupling the router to specific backends, MindFlow acts as a generic gateway, forwarding requests to any service

## 🔑 Features
- **Config-Driven Routing**: Define routes, trigger fields, and backend endpoints in a simple YAML file.

- **Rule based Routing**: Supports both structured-field-based rules and semantic similarity matching.

- **Transparent Request Forwarding**: Router can forward requests as-is to the target service (HTTP methods, headers, query params, body).

- **Multi-Service Support**: Works with any REST/gRPC/HTTP backend; services can be added or modified by updating configuration.

- **Extensible**: Can later be extended for embeddings, AI models, or other multi-modal routing.
