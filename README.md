# AI Customer Support Platform

## About

AI Customer Support Platform helps companies automate customer support using AI-powered knowledge retrieval.
The future versions of the platform will allow companies to build an AI assistant based on their internal knowledge base.

In future versions the project will include:
- FastAPI
- PostgreSQL
- Docker
- OpenAI API
- Qdrant
- LangGraph

## Business Problem

Customer support teams spend a significant amount of time answering repetitive questions.

This platform automates routine responses and helps reduce support workload while improving response time.

## Current Version

Current version: v0.2

Current status:

- Python CLI application
- CRUD operations for FAQs
- JSON data persistence
- Input validation
- Error handling
- Separated storage logic into a dedicated module

## Features

- Add new FAQs
- Display all FAQs
- Search FAQS by question
- Delete FAQs
- Store data in JSON format
- Load saved FAQs when the application starts
- Validate user input
- Handle incorrect user input with exceptions
- Separate storage logic into a dedicated module ('storage.py') 



## Tech Stack
- Python

## Roadmap

- [x] Project initialization
- [x] FAQ Manager
- [x] JSON Storage
- [ ] FastAPI
- [ ] PostgreSQL
- [ ] AI Integration
- [ ] RAG
- [ ] AI Agents
