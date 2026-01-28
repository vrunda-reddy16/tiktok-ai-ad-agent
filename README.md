TikTok AI Ad Agent
### Overview

This project implements a conversational AI agent that guides users through creating a TikTok Ad campaign via a command-line interface (CLI).
The agent collects required ad inputs step-by-step, enforces TikTok Ads business rules before submission, generates a structured ad payload, and handles OAuth and API failures gracefully using mocked TikTok Ads APIs.

The focus of this assignment is on:

1.Prompt and workflow design
2.Business rule enforcement
3.API reasoning and failure handling
4.Structured, production-style AI workflows
This project intentionally avoids UI complexity and model training to emphasize engineering judgment and system design.

### Key Features

1.CLI-based conversational ad creation

2.One-question-at-a-time interaction

3.Immediate input validation

4.Strict business rule enforcement

5.Structured JSON ad payload generation

6.Mocked TikTok OAuth authentication

7.Mocked TikTok Ads API with failure simulation

8.Clear, human-readable error explanations


### Conversational Workflow

The agent collects ad inputs in the following order:

1.Campaign Name
  *Required
  *Minimum 3 characters

2.Campaign Objective
  *Traffic or Conversions

3.Ad Text
 *Required
 *Maximum 100 characters

4.Call-To-Action (CTA)
 *Required

5.Music Selection
 *Existing music ID
 *Custom uploaded music (simulated)
 *No music (conditionally allowed)
The agent validates each input immediately before moving to the next step.

### Business Rule Enforcement

The most important business rule enforced by the agent is music eligibility:

*Traffic campaigns → music is optional
*Conversion campaigns → music is mandatory
If a user attempts to proceed without music for a Conversion campaign, the agent blocks the flow before making any API call and clearly explains the issue.

This early enforcement:
*Prevents invalid ad submissions
*Avoids unnecessary API calls
*Mirrors real-world ad platform constraints

### Structured Output

After successful validation, the agent generates a structured ad payload:

{
  "campaign_name": "Summer Sale",
  "objective": "Traffic",
  "creative": {
    "text": "Big discounts today",
    "cta": "Shop Now",
    "music_id": "custom_music_123"
  }
}

This clean separation between conversation and output ensures predictable and reliable downstream usage.

### OAuth Handling
OAuth authentication is simulated to focus on reasoning and error handling rather than real credentials.

The agent simulates:

*Valid access tokens
*Expired tokens
*Invalid credentials
*Geo-restriction errors

OAuth failures are intercepted and translated into clear, actionable explanations, such as prompting the user to reauthorize the application.

### API Assumptions & Mocking
External TikTok Ads APIs are mocked to simulate realistic behavior.

Simulated API Failures

*Invalid or expired OAuth tokens
*Invalid music IDs
*Missing permissions
*Geo-restrictions

Each failure is:

*Interpreted by the agent
*Classified as retryable or non-retryable
*Explained in plain language with suggested corrective actions
This reflects how production systems must handle unreliable external APIs.

### Prompt Design & Agent Architecture
The agent is designed as a deterministic conversational workflow, not a free-form chatbot.

Design principles:

*Ask one question at a time

*Never assume missing inputs

*Validate inputs immediately

*Separate:

  *User conversation

  *Business logic and validation

  *Final structured output

This approach ensures predictable behavior and safe execution.

### Project Structure
tiktok-ai-ad-agent/
├── agent.py          # CLI conversational agent
├── rules.py          # Validation and business rules
├── schemas.py        # Structured ad payload generation
├── tiktok_api.py     # Mock TikTok OAuth & Ads API
├── config.py         # Configuration and constants
├── requirements.txt
└── README.md

### How to Run the Agent
Prerequisites

*Python 3.9 or higher

### Steps
git clone <repository-url>
cd tiktok-ai-ad-agent
pip install -r requirements.txt
python agent.py

### Summary

This project demonstrates how to build a production-style AI agent that:

*Collects structured input via conversation
*Enforces business rules early
*Handles OAuth and API failures gracefully
*Produces reliable structured outputs

The emphasis is on AI system design and engineering judgment, rather than UI or model training.
