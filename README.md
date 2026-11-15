# AstraWell — Astronaut Well-being Early-Warning Prototype

A NASA Space Apps-inspired **student concept**, not a NASA-endorsed project or medical device. It uses only generated synthetic records and optional user-entered demo check-ins. It does not diagnose mental illness, predict clinical outcomes, or determine fitness for duty.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Demo
Open the Dashboard to see a 30-day simulated mission, individual baseline comparison, and interpretable support flags. Open Daily check-in, opt in, and submit a check-in. The data are held in the app session only. No real astronaut data are included.

## Logic
The first 14 days are the illustrative baseline. Compare averages over the latest 3 days: sleep decrease >1 hour, stress increase >1.5 points, mood decrease >1 point. Two or more flags produce "Support suggested"; one produces "Monitor". These thresholds are arbitrary demonstration rules, **not a validated AI model**. Future research can compare robust anomaly-detection methods with transparent baselines, quantify false alarms and missed changes, and assess human usability.

## Safety
No covert monitoring, speech or face emotion recognition, automated clinical triage, or punitive crew scoring. A real system would need opt-in consent, role-based access, encryption, audit logs, deletion controls, clinical review, and independent validation.
