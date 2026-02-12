import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Selvam P | Portfolio",
     page_icon="💼",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("  Selvam P –  Portfolio")
st.subheader("Pharmacovigilance | Clinical Safety Data Analytics")

st.write("""
Experienced Pharmacovigilance professional **handling healthcare safety data **.
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
- 🏥 Worked with safety data, literature review, case processing, signal and risk detection
- 📈 Transitioning into **Data Analyst**
- 🎯 Interested in Healthcare, Real-World Evidence & Analytics
    """)
- image = Image.open(r"C:\Users\ADMIN\Downloads\Personal\Selvam_Image.jpg")
- st.image(image, caption="Selvam Image", use_column_width=True)

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
        - Clinical Safety Data Management
        - Safety Reports Handling 
        - Healthcare Analytics
        - Tools: Argus, Clinevo Safety, Veeva Vault RIM, DST (Drug Safety Triager), and PVAI (Pharmacovigilance Artificial Intelligence)
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
    **Email:** selvampachimuthu98@gmail.com  
    **LinkedIn:** https://www.linkedin.com/in/selvam-p-a9593a189/ 
    **GitHub:** https://github.com/SelvamPachimuthu  
    """)

    st.success("Thank you for visiting my portfolio!")






