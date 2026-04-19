# Meeting Analysis Crew

This project implements a multi-agent autonomous system using **CrewAI** to automate high-stakes meeting preparation. By orchestrating specialized agents, the system transforms raw participant data and meeting goals into a comprehensive, actionable strategic brief.

---

## 🏗 System Architecture

The following diagram illustrates the workflow, task dependencies, and tool integration within the crew:

<img width="1387" height="768" alt="MeetingAnalysisAgent architechture" src="https://github.com/user-attachments/assets/60c5adff-3602-46a0-83a1-b91bf98c54ae" />

---

## 🤖 The Agents

The crew consists of four autonomous agents, each designed with specific backstories and goal alignments:

| Agent | Role | Focus |
| :--- | :--- | :--- |
| **Researcher** | People & Company Intelligence | Deep dives into participant backgrounds and corporate history. |
| **Industry Analyst** | Market Intelligence | Identifies macro trends and competitive shifts relevant to the context. |
| **Meeting Strategist** | Tactical Planner | Synthesizes research into high-level talking points and objectives. |
| **Brief Writer** | Communications Expert | Formats complex data into a clear, professional meeting brief. |

---

## 📋 Task Pipeline

The workflow utilizes a hybrid of **Asynchronous** and **Sequential** execution to maximize efficiency:

1.  **Research & Analysis (Parallel):** * `Research` and `Analyse Industry` tasks are set to `async: true`, allowing them to execute simultaneously.
2.  **Strategy Development:** * Waits for research outputs. It uses the combined context to develop a tailored meeting strategy.
3.  **Final Compilation:** * The `Summarizing and Briefing` task aggregates all prior intelligence into the final document.

---

## 🛠 Tool Integration

The crew is equipped with the **Exa Toolset** for advanced semantic search capabilities:

* **Search:** Targeted web searches based on participant and company profiles.
* **Find Similar:** Discovering competitors or similar market case studies via URL.
* **Get Contents:** Extracting clean, structured text from web pages for agent analysis.

---

## 🚀 Usage

### 1. Installation
```bash
pip install crewai exa_py
```

### 2. Configuration
Ensure you have your environment variables set for your LLM and search provider:

```bash
OPENAI_API_KEY=your_key_here
EXA_API_KEY=your_key_here
```

## 📄 Output
The final product is a Brief for the Meeting, which includes:

Executive summaries of all participants.

* Key industry talking points.

* Recommended strategic approach.

* Logistical reminders and goal alignment.
