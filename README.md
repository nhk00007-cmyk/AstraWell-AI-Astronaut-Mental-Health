# 🚀 AstraWell
### AI-Assisted Astronaut Mental Well-being Early-Warning System

**NASA Space Apps Challenge — Student Research Prototype**

[🌐 Launch Live App](https://astrawell-ai-astronaut-mental-health-uzdiak9ogz2rdnjslpnskg.streamlit.app/) · [📄 Project Submission Draft](SUBMISSION.md)

> **Important:** AstraWell is an educational demonstration using synthetic data. It is **not** a medical device, a clinically validated mental-health predictor, an astronaut fitness-for-duty assessment, or an official NASA product.

## 🌍 The problem

Long-duration space missions involve isolation, confinement, sleep disruption, demanding schedules, and communication delays. Changes in well-being can develop gradually. A transparent, voluntary check-in tool could help people recognize meaningful trends and seek appropriate human support.

## 💡 Our solution

AstraWell explores an explainable early-warning workflow that compares an individual's recent sleep, stress, and mood patterns with their own baseline. Rather than assigning a diagnosis, it displays illustrative support levels and the specific changes behind them.

**Workflow:** Voluntary inputs → Personal baseline → Multi-day trend comparison → Explainable support indicator → Human-led follow-up.

## ✨ Current features

- 📊 **Interactive dashboard:** 30-day synthetic mission trends for sleep, stress, mood, and activity.
- 🧑‍🚀 **Personal baseline:** Illustrative reference period from the first 14 simulated days.
- 📈 **Trend comparison:** Compare the latest three days with that reference.
- 🔎 **Explainable indicators:** Show which predefined changes triggered a flag.
- 📝 **Voluntary check-in:** Consent-gated form for mood, stress, sleep, and optional activity.
- 🔐 **Privacy-conscious demo:** No real astronaut records; entered data are held only in the current Streamlit session.

## 🖥️ Live demo

**[Open AstraWell on Streamlit Community Cloud](https://astrawell-ai-astronaut-mental-health-uzdiak9ogz2rdnjslpnskg.streamlit.app/)**

To explore the demo:
1. Open **Dashboard** to inspect the synthetic mission timeline and support indicator.
2. Open **Daily check-in** and enable the demo consent checkbox.
3. Enter sample observations and save the check-in.
4. Return to **Dashboard** to see the updated data.
5. Open **How it works** to review the scoring rules and limitations.

## 🛠️ Tech stack

| Component | Technology |
|---|---|
| Web interface | Streamlit |
| Programming language | Python |
| Data manipulation | Pandas |
| Synthetic data generation | NumPy |
| Hosting | Streamlit Community Cloud |
| Source control | GitHub |

## ⚙️ Run locally

**Requirements:** Python 3.10+ and pip.

```bash
git clone https://github.com/nhk00007-cmyk/AstraWell-AI-Astronaut-Mental-Health.git
cd AstraWell-AI-Astronaut-Mental-Health
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On Windows, if `python` is unavailable but the Python launcher is installed, replace `python` with `py`.

Then open **http://localhost:8501**.

## 🧠 How the current support indicator works

This version uses **transparent rules**, not a trained machine-learning model.

- The first **14 days** form an illustrative personal baseline.
- The latest **3 days** are averaged and compared with that baseline.
- A factor is flagged if average sleep falls by more than **1 hour**, stress rises by more than **1.5 points**, or mood falls by more than **1 point**.
- **Stable:** no factors flagged.
- **Monitor:** one factor flagged.
- **Support suggested:** two or more factors flagged.

These thresholds are arbitrary demo settings, not medically calibrated cutoffs. A support flag is **not** a mental-health diagnosis or a prediction of a clinical outcome.

## 🛡️ Safety, privacy and limitations

- Uses generated synthetic data, not NASA astronaut health records.
- Requires opt-in for the voluntary demo check-in.
- Does not use covert audio/video monitoring or emotion recognition.
- Does not make treatment, emergency-triage, or fitness-for-duty decisions.
- The demo has **no production authentication, encrypted clinical database, or validated access-control system**.
- Any real deployment would require informed consent, secure storage, auditability, clinical governance, robust validation, and established emergency protocols.

## 🧪 Future development

1. Compare interpretable baseline rules with machine-learning anomaly detection.
2. Evaluate false alarms, missed changes, detection delays, and missing-data behavior on carefully designed scenarios.
3. Incorporate workload and mission context with appropriate consent.
4. Add usability testing and independent review by qualified domain experts.
5. Explore secure, offline-capable architectures for isolated mission environments.

## 📚 Research background

- [NASA Human Research Program](https://www.nasa.gov/hrp/)
- [NASA Space Apps Challenge](https://www.spaceappschallenge.org/)
- [World Health Organization — Mental health](https://www.who.int/health-topics/mental-health)

These are background resources, **not training datasets**. This project does not claim NASA endorsement.

## 📑 Submission documentation

See [SUBMISSION.md](SUBMISSION.md) for the detailed hackathon project narrative, AI-use disclosure, ethics, evaluation plan, and submission links.

---

**AstraWell — Supporting the people who explore beyond Earth.**
