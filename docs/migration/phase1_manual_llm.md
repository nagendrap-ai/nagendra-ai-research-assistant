# Phase 1 - Manual LLM Integration

## Objective

Implement OpenRouter communication without using LangChain.

## Architecture

User

↓

Planner

↓

requests.post()

↓

OpenRouter

↓

JSON Parsing

## Features

- Manual HTTP requests
- Manual payload construction
- Manual JSON parsing
- Manual error handling

## Migration Reason

Later migrated to LangChain while keeping the application's public interface (`ask_llm`) unchanged.

This demonstrates incremental migration instead of rewriting the application.