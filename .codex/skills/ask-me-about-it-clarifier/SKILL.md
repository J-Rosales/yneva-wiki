---
name: ask-me-about-it-clarifier
description: Expand phases, steps, or milestones into implementation steps and ask A-or-B clarifying questions when the user says "ask me about it" or similar while listing project phases/steps/milestones. Use when converting high-level plans into actionable tasks and the user requests the assistant to ask about the details.
---

# Ask Me About It Clarifier

## Overview

Convert high-level phase or milestone lists into actionable steps, ask structured A-or-B clarifying questions, then turn the confirmed plan into a Codex task list and start execution.

## Workflow

1. Detect trigger
If the user lists phases, steps, or milestones and says "ask me about it" or similar, treat it as a request for clarification and expansion.

2. Expand phases into implementation steps
For each phase or milestone, produce a small set of concrete implementation steps. Keep steps scoped to executable work and in the same order as provided.

3. Ask A-or-B clarifying questions
For each step, ask a short A-or-B question to resolve ambiguities. Ask more questions for larger scope steps. Use compact phrasing and present mutually exclusive options.
Example format:
- `Question: Build pipeline validation`
- `A: Validate frontmatter + links`
- `B: Validate frontmatter only`

4. After answers, structure a Codex task list and begin
Once the user answers, restate the resolved steps as a Codex task list and start working on it immediately.
