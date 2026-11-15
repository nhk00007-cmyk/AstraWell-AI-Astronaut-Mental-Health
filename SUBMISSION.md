# NASA Space Apps Challenge — Project Submission Draft

## Project name
AstraWell — AI-Powered Astronaut Mental Health Risk Prediction and Early-Warning System

## High-level project summary
Long-duration missions expose astronauts to isolation, altered sleep schedules, heavy workloads, and limited communication with loved ones. AstraWell is a privacy-conscious, AI-assisted well-being support concept designed to flag meaningful changes in voluntary self-reported mood and stress alongside sleep and activity trends. Instead of judging astronauts against a universal threshold, it compares recent patterns with each person's baseline and explains the contributing signals. Our runnable prototype demonstrates the workflow using synthetic data, a dashboard, and an opt-in check-in. It is not a diagnostic, treatment, or fitness-for-duty system; humans remain responsible for interpreting concerns and offering support.

## Detailed project description
### Problem
Psychological strain can emerge gradually during isolated, confined, high-stakes missions. A single data point may be misleading, and broad group-level norms may miss meaningful individual changes. A supportive system should make voluntary patterns understandable without creating surveillance or stigma.

### Solution
AstraWell follows five stages: (1) opt-in check-ins for mood and stress; (2) contextual sleep/activity summaries; (3) a personal baseline; (4) transparent, multi-day trend detection; and (5) optional human-led support. The dashboard shows the trend and its contributing factors rather than an unexplained black-box label.

### Prototype and demo
A working Streamlit web app ships with a reproducible 30-day synthetic mission scenario. The dashboard charts sleep, stress and mood; compares recent values with a personal baseline; and displays Stable, Monitor, or Support suggested as illustrative support levels. The check-in form requires consent before submission. A How it works page explains model boundaries. Demo data stay within the app session.

### What makes it distinctive
Personal-baseline reasoning, transparent explanations, minimal and voluntary inputs, and a human-in-the-loop safety approach. The architecture is intended to be usable with intermittent connectivity and can later incorporate mission context without automatically escalating sensitive raw records.

### Implementation
Python, Streamlit, Pandas and NumPy. The current prototype uses explicitly defined, interpretable thresholds rather than claiming a trained or validated AI predictor. A future AI extension would evaluate unsupervised anomaly detection and time-series models against these baseline rules, with careful validation and uncertainty reporting.

### Validation plan
Create multiple synthetic scenarios: stable, short-term sleep loss, sustained combined changes, missing readings, and unusual workload. Compare false alert rates, missed scenario detections, detection delay, explainability and usability. Never interpret synthetic scenario performance as real-world clinical accuracy. Real-world evaluation would require ethical approval, appropriate data access and professional oversight.

### Safety and ethics
Informed consent, data minimization, user review and deletion, encryption and access controls for any future deployment, explicit uncertainty, no covert monitoring, no punitive crew scoring, and qualified human oversight. Urgent concerns should follow established medical pathways, not a model-generated verdict.

### Potential impact
The concept could support earlier conversations about sleep, workload and well-being in space analog missions and other isolated environments, subject to validation. It is not NASA-endorsed and does not use real astronaut health records.

## Use of artificial intelligence (AI)
AI is part of the proposed research direction, not a completed clinical prediction capability. The delivered demo implements transparent baseline and trend rules. Future experiments may compare scikit-learn anomaly detection with simple rules, publish evaluation metrics and model limitations, and preserve human review. Any generative-AI assistance used for drafting or code development should be disclosed by the team according to the current challenge's rules.

## NASA data
No NASA medical datasets or astronaut health records were accessed. The prototype uses generated synthetic records. NASA Human Research Program and Behavioral Health & Performance materials are background research foundations; do not describe them as training data.

## Demo link
[ADD PUBLIC VIDEO OR LIVE DEMO URL AFTER UPLOADING]

## Code repository
[ADD PUBLIC GITHUB REPOSITORY URL AFTER UPLOADING]

## Team
[ADD TEAM NAME, MEMBER NAMES AND ROLES]

## Challenge
[ADD EXACT 2026 NASA SPACE APPS CHALLENGE TITLE AND CHECK ITS ELIGIBILITY]

## References and acknowledgments
- NASA Human Research Program — https://www.nasa.gov/hrp/
- NASA Space Apps Challenge — https://www.spaceappschallenge.org/
- World Health Organization, Mental health — https://www.who.int/health-topics/mental-health

**Submission note:** The provided 2026 submission guide asks for a project name, high-level summary, demo link, detailed description, AI-use disclosure, NASA data attribution when applicable, and other data references. Verify the live submission form and challenge-specific requirements before submitting.
