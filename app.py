import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Selvam | Portfolio",
    page_icon="💊",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("  Selvam Pachimuthu –  Portfolio")
st.subheader("Pharmacovigilance | Clinical Data | Data Analytics")

st.write("""
Experienced Pharmacovigilance professional transitioning into **Data Analytics & Data Science**.
This portfolio demonstrates my skills in **Python, Data Analysis, Visualization, and Healthcare Data**.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    ["About Me", "Skills", "Projects", "Data Analysis Demo", "Contact"]
)

# ---------------- ABOUT ME ----------------
if section == "About Me":
    st.header("👤 About Me")
    st.write("""
- 💼 4+ years experience in **Pharmacovigilance**
- 🏥 Worked with safety data, case processing, medical review
- 📈 Transitioning into **Data Analyst / Data Scientist**
- 🎯 Interested in Healthcare, Real-World Evidence & Analytics
    """)

# ---------------- SKILLS ----------------
elif section == "Skills":
    st.header("🛠 Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Programming & Tools")
        st.write("""
        - Python (Pandas, NumPy, Matplotlib)
        - SQL (MySQL)
        - Excel (Advanced)
        - Streamlit
        """)

    with col2:
        st.subheader("Domain Knowledge")
        st.write("""
        - Pharmacovigilance
        - Clinical Data Management
        - Safety Reports
        - Healthcare Analytics
        """)

# ---------------- PROJECTS ----------------
elif section == "Projects":
    st.header("📂 Projects")

    st.subheader("1️⃣ Adverse Event Data Analysis")
    st.write("""
    - Cleaned and analyzed AE data
    - Identified most common reactions
    - Visualized trends using Python
    """)

    st.subheader("2️⃣ Clinical Trial Demographics Dashboard")
    st.write("""
    - Analyzed age, gender distribution
    - Used Pandas & Matplotlib
    """)

    st.subheader("3️⃣ Excel to MySQL Automation")
    st.write("""
    - Automated data upload from Excel to MySQL
    - Reduced manual effort
    """)

# ---------------- DATA ANALYSIS DEMO ----------------
elif section == "Data Analysis Demo":
    st.header("📊 Data Analysis Demo")

    st.write("Sample healthcare dataset analysis")

    # Create sample dataset
    data = {
        "Age": np.random.randint(18, 80, 50),
        "Gender": np.random.choice(["Male", "Female"], 50),
        "Adverse_Event": np.random.choice(
            ["Nausea", "Headache", "Fatigue", "Vomiting"], 50
        )
    }

    df = pd.DataFrame(data)

    st.subheader("🔹 Raw Data")
    st.dataframe(df)

    st.subheader("🔹 AE Frequency")
    ae_counts = df["Adverse_Event"].value_counts()

    fig, ax = plt.subplots()
    ae_counts.plot(kind="bar", ax=ax)
    ax.set_ylabel("Count")
    ax.set_title("Adverse Event Distribution")

    st.pyplot(fig)

# ---------------- CONTACT ----------------
elif section == "Contact":
    st.header("📞 Contact")

    st.write("""
    **Email:** selvam@email.com  
    **LinkedIn:** https://linkedin.com/in/yourprofile  
    **GitHub:** https://github.com/yourusername  
    """)

    st.success("Thank you for visiting my portfolio!")

