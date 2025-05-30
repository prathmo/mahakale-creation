
import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(page_title="Mahakale Web", layout="wide")

# Load CSS
with open("assets/bg_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🌈 Mahakale Creation 🌈</h1>", unsafe_allow_html=True)
st.markdown("### A Mahakale Created website")

# Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/hanuman.png", caption="Jai Shree Ram 🙏", use_column_width=True)

with col2:
    st.markdown("### 📥 Downloads")
    with open("data/sample_file.pdf", "rb") as file:
        st.download_button(label="Download Blessing", data=file, file_name="Mahakale_Blessing.pdf")
    with open("data/all-images.zip", "rb") as file:
        st.download_button(label="📥 Download All Images", data=file, file_name="all-images.zip", mime="application/zip")

with col3:
    st.image("assets/shiv.png", caption="Har Har Mahadev 🙏", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>✨ Jai Mahakaal ✨</h4>", unsafe_allow_html=True)
