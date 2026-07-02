# Trip AI Agent

An agentic AI assistant designed to plan highly detailed, budget-optimized travel itineraries anywhere in the world using live data.

## 🚀 Features

- **Global Concierge Skill**: A specialized AI instruction set (located in `.agents/skills/global_concierge/SKILL.md`) that acts as an expert travel planner. It requires human-in-the-loop validation for all bookings and strictly follows user budgets and constraints.
- **MCP Live Data Server (`mcp_server.py`)**: A Model Context Protocol (MCP) server that provides the agent with real-time tools for:
  - Fetching current weather for any destination (`wttr.in`).
  - Checking dynamic transit prices (trains, flights, buses) based on distances.
  - Simulating bookings securely.
  - Web searching capabilities (via DuckDuckGo).
- **Direct Test Scripts (`run_mcp.py`)**: Utilities to query the live MCP features locally without requiring an active agent session.

## 🛠️ Usage

To interact with the Trip AI Agent, open the repository in a supported AI environment (e.g. Gemini IDE) and prompt the agent to start planning your trip!

**Example Prompt:**
> "I want to plan a trip to Poland. My budget is 100 Euros."

The agent will proactively ask clarifying questions (like origins, dates, and dietary preferences), calculate routes, and produce detailed, markdown-formatted itineraries.

## 🔐 Human-in-the-Loop Security

All final travel itineraries and simulated bookings strictly prompt the user for explicit approval before proceeding. The agent cannot finalize reservations without a final "yes" from the user.

## 📄 License
MIT License
