# 🤖 AI ADK Summarizer Agent

This project implements an AI agent using the Google ADK architectural pattern (Agent + Tool abstraction) and Gemini for inference.

## 🚀 Features
- Text Summarization using Gemini
- ADK-style Agent + Tool design
- REST API endpoint
- Web UI for interaction
- Deployed on Google Cloud Run

## 🌐 Live Demo
https://ai-agent-146041617780.us-central1.run.app

## 🧠 Architecture
- Agent: Controls execution flow
- Tool: Performs summarization
- Runner: Connects agent and Gemini
- Flask API: Handles HTTP requests

## 📡 API Usage

POST /summarize

```json
{
  "text": "Your input text here"
}
