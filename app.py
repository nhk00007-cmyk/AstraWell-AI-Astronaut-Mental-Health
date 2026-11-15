import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

st.set_page_config(page_title='AstraWell | Mission Well-being', page_icon='🚀', layout='wide')
st.title('🚀 AstraWell')
st.caption('AI-assisted astronaut well-being early-warning prototype • Synthetic data only • Not a medical device')

@st.cache_data
def sample_data(seed=7):
    rng=np.random.default_rng(seed)
    days=pd.date_range(end=pd.Timestamp.today().normalize(), periods=30)
    sleep=np.clip(rng.normal(7.3,.45,30),4,9)
    stress=np.clip(rng.normal(3.2,.8,30),1,10)
    mood=np.clip(rng.normal(7.1,.7,30),1,10)
    activity=np.clip(rng.normal(6500,900,30),1000,12000)
    sleep[-6:]-=np.linspace(.4,1.7,6)
    stress[-6:]+=np.linspace(.5,2.8,6)
    mood[-6:]-=np.linspace(.2,1.7,6)
    return pd.DataFrame({'date':days,'sleep_hours':sleep,'stress':stress,'mood':mood,'steps':activity})

if 'df' not in st.session_state: st.session_state.df=sample_data()
st.sidebar.header('Privacy & consent')
consent=st.sidebar.checkbox('I consent to process this demo check-in locally in this session', value=False)
st.sidebar.info('Demo data are synthetic. No real astronaut records, covert monitoring, diagnosis, or automated fitness-for-duty decisions.')
view=st.sidebar.radio('View', ['Dashboard','Daily check-in','How it works'])
df=st.session_state.df.copy()

def assess(frame):
    base=frame.iloc[:14]
    recent=frame.tail(3)
    factors=[]
    delta_sleep=float(recent.sleep_hours.mean()-base.sleep_hours.mean())
    delta_stress=float(recent.stress.mean()-base.stress.mean())
    delta_mood=float(recent.mood.mean()-base.mood.mean())
    if delta_sleep < -1: factors.append('Sleep below personal baseline')
    if delta_stress > 1.5: factors.append('Stress above personal baseline')
    if delta_mood < -1: factors.append('Mood below personal baseline')
    if len(frame)<17: return 'Insufficient data', factors
    return ('Support suggested' if len(factors)>=2 else 'Monitor' if factors else 'Stable'), factors

if view=='Dashboard':
    level, factors=assess(df)
    a,b,c,d=st.columns(4)
    a.metric('Illustrative trend',level)
    b.metric('Last sleep',f'{df.sleep_hours.iloc[-1]:.1f} h')
    c.metric('Last stress',f'{df.stress.iloc[-1]:.1f}/10')
    d.metric('Last mood',f'{df.mood.iloc[-1]:.1f}/10')
    st.subheader('Well-being trends (synthetic)')
    st.line_chart(df.set_index('date')[['sleep_hours','stress','mood']])
    st.subheader('Explainable observations')
    if factors:
        for f in factors: st.write('• '+f)
    else: st.write('No predefined change thresholds crossed.')
    st.info('Illustrative rule-based flags, not validated mental-health risk predictions. Review with an appropriately qualified human professional when needed.')
    st.dataframe(df.tail(10).round(2),use_container_width=True,hide_index=True)
elif view=='Daily check-in':
    st.subheader('Voluntary check-in')
    if not consent: st.warning('Enable the consent checkbox in the sidebar before entering a check-in.')
    with st.form('checkin'):
        mood=st.slider('Mood (1 = low, 10 = high)',1,10,7)
        stress=st.slider('Perceived stress (1 = low, 10 = high)',1,10,4)
        sleep=st.slider('Sleep last night (hours)',0.0,12.0,7.0,.5)
        steps=st.number_input('Activity steps (optional demo proxy)',0,30000,6000,500)
        submit=st.form_submit_button('Save demo check-in',disabled=not consent)
    if submit:
        row=pd.DataFrame([{'date':pd.Timestamp.today().normalize()+pd.Timedelta(days=1),'sleep_hours':sleep,'stress':stress,'mood':mood,'steps':steps}])
        st.session_state.df=pd.concat([df,row],ignore_index=True)
        st.success('Saved to this Streamlit session. Visit Dashboard to see updated trends.')
else:
    st.subheader('How the prototype works')
    st.markdown('''1. **Collect:** opt-in mood, stress, sleep and activity summaries.\n2. **Baseline:** use the first 14 simulated days as an individual reference.\n3. **Compare:** compare the most recent 3 days with that baseline.\n4. **Explain:** show which predefined changes contributed to a support suggestion.\n5. **Human oversight:** no automated diagnosis or crew fitness decisions.''')
    st.warning('For a real deployment: informed consent, encryption, access controls, clinical governance, validation across individuals, and emergency pathways would be required.')
    st.caption('Demo thresholds are illustrative, not clinically calibrated. Missingness and confounding mission context require additional work.')
