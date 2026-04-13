# Agentic CRM Cross‑Channel Context Manager

## Overview
This project implements a **channel‑agnostic, persistent context management system** designed for AI‑native CRM platforms. It solves a core real‑world problem: maintaining continuous customer context when users interact across multiple channels (WhatsApp, Email, Web) over long periods of time.

Instead of relying on raw chat history, the system models a **semantic customer state** containing intent, confidence, sentiment, open tasks, goals, and summary memory. All incoming messages are normalized and mapped to a single evolving state, treating channels purely as transport layers.

The design emphasizes **predictability, scalability, and safety**, enabling both AI agents and human operators to operate on stable, structured context.

---

## Key Features
- Channel‑agnostic message normalization
- Persistent semantic customer state (no raw logs replay)
- Explicit modeling of intent, sentiment, and task state
- Long‑lived memory suitable for multi‑day conversations
- JSON persistence with clear migration path to SQLite / DBs
- Designed for AI + human shared context use cases

---

## Architecture
``
---

## Technologies Used
- Python
- Pydantic (state modeling)
- JSON / SQLite (persistence)
- Modular agent‑friendly architecture
- Designed for Azure OpenAI integration

---

## Use Cases
- AI‑native CRM platforms
- Cross‑channel customer support
- Shared context between AI agents and humans
- Performance‑sensitive dashboards

---

## Future Improvements
- Database‑backed persistence (PostgreSQL / MongoDB)
- Embedding‑based enrichment for summary memory
- Real‑time notification hooks
- Integration with frontend CRM dashboards

---

## License
MIT License
