from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# Same columns, in the same order, as when the model was trained
FEATURES = ["pclass", "sex", "age", "fare"]

MODEL_PATH = Path(__file__).parent / "model.joblib"

st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢")

# --- Light styling (colours chosen to be readable and colour-blind friendly) ---
st.markdown(
    """
    <style>
    h1, h1 * { color: #1f6fb2 !important; }
    div.stButton > button {
        background-color: #1f6fb2;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.8rem;
        font-weight: 600;
    }
    div.stButton > button:hover { background-color: #17537f; color: white; }
    .result-card {
        border-radius: 12px;
        padding: 1rem 1.4rem;
        margin: 0.8rem 0 0.4rem 0;
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: 600;
    }
    .likely   { background-color: #1f6fb2; }
    .unlikely { background-color: #9a5b00; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model():
    """Load the saved model once, not on every click."""
    return joblib.load(MODEL_PATH)


st.title("🚢 Would this passenger have survived?")
st.write("An educational model trained on the Titanic passenger list.")
st.caption("Model: a decision tree (depth 4) trained on 714 Titanic passengers with a known age. "
           "It was about 80% accurate on passengers it had not seen. "
           "This is a learning exercise based on a historical dataset, not advice.")

st.subheader("Passenger details")

left, right = st.columns(2)
with left:
    pclass = st.selectbox("Ticket class", [1, 2, 3], index=2)
    age = st.slider("Age (years)", min_value=1, max_value=80, value=30)
with right:
    sex = st.radio("Sex", ["female", "male"], horizontal=True)
    fare = st.slider("Fare paid (pounds)", min_value=0, max_value=500, value=15)

if st.button("Predict"):
    try:
        model = load_model()
    except FileNotFoundError:
        st.error("The model file is missing. Train and save it first.")
        st.stop()

    try:
        # Same columns and order as the training data; sex: 1 = female, 0 = male
        row = pd.DataFrame([[pclass, 1 if sex == "female" else 0, age, fare]],
                           columns=FEATURES)
        chance = model.predict_proba(row)[0][1]
    except Exception:
        st.error("Something went wrong while making the prediction. Please check the inputs and try again.")
        st.stop()

    if chance >= 0.5:
        st.markdown('<div class="result-card likely">Likely to survive</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-card unlikely">Unlikely to survive</div>',
                    unsafe_allow_html=True)

    st.metric("Estimated chance of survival", f"{chance:.0%}")
    st.progress(float(chance))
    st.caption("A learning exercise. It describes a historical dataset and is not advice. "
               "Very high or very low percentages can appear when few similar passengers "
               "were in the training data.")
