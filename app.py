import streamlit as st
from cdma_utils import chain_encode, decode

st.set_page_config(page_title="CDMA Encoder/Decoder", layout="centered")

st.title("📡 CDMA Encoder & Decoder")

# Sidebar
mode = st.sidebar.radio("Select Mode", ["Encode", "Decode"])

def parse_input(text):
    return list(map(int, text.strip().split()))

# ================== ENCODER ==================
if mode == "Encode":
    st.subheader("🔐 Encoder")

    c1 = st.text_input("Chain Code 1 (space-separated)", "1 0 1 0")
    c2 = st.text_input("Chain Code 2 (space-separated)", "1 1 0 0")
    c3 = st.text_input("Chain Code 3 (space-separated)", "0 1 1 0")

    d1 = st.text_input("Data Bits 1", "1 0")
    d2 = st.text_input("Data Bits 2", "0 1")
    d3 = st.text_input("Data Bits 3", "1 1")

    if st.button("Encode Signal"):
        try:
            c1, c2, c3 = map(parse_input, [c1, c2, c3])
            d1, d2, d3 = map(parse_input, [d1, d2, d3])

            signal = chain_encode(c1, c2, c3, d1, d2, d3)

            st.success("Encoded Successfully!")
            st.write("📶 Transmitted Signal:")
            st.code(signal)

            # store for decoding
            st.session_state["signal"] = signal

        except Exception as e:
            st.error(f"Error: {e}")

# ================== DECODER ==================
elif mode == "Decode":
    st.subheader("🔓 Decoder")

    signal_input = st.text_area(
        "Received Signal",
        value=str(st.session_state.get("signal", "")),
        height=100
    )

    c = st.text_input("Your Chain Code", "1 0 1 0")

    if st.button("Decode Signal"):
        try:
            signal = eval(signal_input)
            c = parse_input(c)

            data = decode(signal, c)

            st.success("Decoded Successfully!")
            st.write("📩 Your Data Bits:")
            st.code(data)

        except Exception as e:
            st.error(f"Error: {e}")
