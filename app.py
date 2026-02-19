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
st.subheader("Clinical Data Analyst| Safety Data Management |Pharmacovigilance")

st.write("""
Experienced Pharmacovigilance professional handling **Clinical safety data of medicines, ensuring patients safety by doing drug data analysis  **.
This portfolio demonstrates my skills in **Clinical data handling, Python, Data Analysis, Visualization, and Healthcare Data**.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    ["About Me", "Skills", "Projects - Data Analysis Demo", "Contact"]
)

# ---------------- ABOUT ME ----------------
if section == "About Me":
    st.header("👤 About Me")
    st.write("""
- 💼 4+ years experience in **Pharmacovigilance (Clinical Safety Data)**
- 🏥 Worked with clinical data, data cleaning, query generation, drug safety data, literature review, case processing, signal and risk detection
- 📈 Transitioning into **Clinical data Analyst**
- 🎯 Interested in Clinical data management, Healthcare, Real-World Evidence & Analytics
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
        - Clinical Data Management
        - Data Cleaning
        - Query Handling
        - Pharmacovigilance
        - Clinical Safety Data Management
        - Safety Reports Handling 
        - Quality & Compliance: GCP, GVP, SOP Frameworks, Audit & Inspection Readiness
        - Healthcare Analytics
        - Tools: Argus, Clinevo Safety, Veeva Vault RIM, DST (Drug Safety Triager), and PVAI (Pharmacovigilance Artificial Intelligence)
        """)

# ---------------- Projects - Data Analysis Demo ----------------
elif section == "Projects - Data Analysis Demo":
    st.header("📂 Projects - Data Analysis Demo")

    # =====================================================
    # 1️⃣ Adverse Event Data Analysis (Pharmacovigilance)
    # =====================================================
    st.subheader("1️⃣ Adverse Event Data Analysis (Pharmacovigilance)")

    st.write("""
    - Cleaned and analyzed Adverse Event (AE) datasets  
    - Identified most frequently reported reactions  
    - Performed trend analysis using Pandas  
    - Visualized AE distribution using Matplotlib  
    - Strengthened signal detection understanding  
    """)

    # Sample AE dataset
    ae_data = {
        "AE_Term": np.random.choice(
            ["Headache", "Nausea", "Vomiting", "Fatigue", "Dizziness"], 100
        )
    }

    ae_df = pd.DataFrame(ae_data)

    st.write("### 🔹 AE Frequency Distribution")
    ae_counts = ae_df["AE_Term"].value_counts()
    st.dataframe(ae_counts)

    fig1, ax1 = plt.subplots()
    ae_counts.plot(kind="bar", ax=ax1)
    ax1.set_title("Most Frequently Reported AEs")
    st.pyplot(fig1)

    st.markdown("---")

    # =====================================================
    # 2️⃣ Clinical Trial Demographics Dashboard
    # =====================================================
    st.subheader("2️⃣ Clinical Trial Demographics Dashboard")

    st.write("""
    - Analyzed subject-level demographic data  
    - Generated summary statistics  
    - Built visual dashboards  
    - Supported study-level reporting insights  
    """)

    demo_data = {
        "Age": np.random.randint(18, 70, 60),
        "Gender": np.random.choice(["Male", "Female"], 60)
    }

    demo_df = pd.DataFrame(demo_data)

    st.write("### 🔹 Age Summary Statistics")
    st.dataframe(demo_df.describe())

    st.write("### 🔹 Gender Distribution")
    gender_counts = demo_df["Gender"].value_counts()
    st.dataframe(gender_counts)

    fig2, ax2 = plt.subplots()
    gender_counts.plot(kind="bar", ax=ax2)
    ax2.set_title("Gender Distribution")
    st.pyplot(fig2)

    st.markdown("---")

    # =====================================================
    # 3️⃣ Clinical Data Discrepancy & Query Management
    # =====================================================
    st.subheader("3️⃣ Clinical Data Discrepancy & Query Management (CDM Simulation)")

    st.write("""
    - Identified missing & inconsistent data  
    - Implemented validation checks  
    - Simulated query generation workflow  
    - Generated query tracking reports  
    """)

    cdm_data = {
        "Subject_ID": np.arange(2001, 2051),
        "Age": np.random.randint(18, 80, 50),
        "AE_Reported": np.random.choice(["Yes", "No"], 50),
        "AE_Term": np.random.choice(
            ["Nausea", "Headache", "Fatigue", None], 50
        )
    }

    cdm_df = pd.DataFrame(cdm_data)

    # Logical validation
    discrepancies = cdm_df[
        (cdm_df["AE_Reported"] == "Yes") & (cdm_df["AE_Term"].isnull())
    ]

    st.write("### 🔹 Identified Data Queries")
    st.dataframe(discrepancies)

    st.write("Total Queries Identified:", len(discrepancies))

    st.markdown("---")

    # =====================================================
    # 4️⃣ SAE Reconciliation & Data Listing Review
    # =====================================================
    st.subheader("4️⃣ SAE Reconciliation & Data Listing Review")

    st.write("""
    - Performed SAE reconciliation  
    - Compared AE datasets  
    - Identified mismatches  
    - Ensured regulatory compliance  
    """)

    sae_data = {
        "Subject_ID": np.arange(3001, 3051),
        "SAE_Flag": np.random.choice(["Yes", "No"], 50)
    }

    sae_df = pd.DataFrame(sae_data)

    st.write("### 🔹 SAE Distribution")
    sae_counts = sae_df["SAE_Flag"].value_counts()
    st.dataframe(sae_counts)

    fig4, ax4 = plt.subplots()
    sae_counts.plot(kind="bar", ax=ax4)
    ax4.set_title("SAE Distribution")
    st.pyplot(fig4)

    st.markdown("---")

    # =====================================================
    # 5️⃣ Excel to MySQL Data Automation
    # =====================================================
    st.subheader("5️⃣ Excel to MySQL Data Automation")

    st.write("""
    - Automated bulk data upload  
    - Reduced manual entry errors  
    - Improved workflow efficiency  
    - Ensured data integrity  
    """)

    automation_data = {
        "Record_ID": np.arange(4001, 4021),
        "Upload_Status": np.random.choice(
            ["Success", "Failed"], 20, p=[0.9, 0.1]
        )
    }

    auto_df = pd.DataFrame(automation_data)

    st.write("### 🔹 Upload Status Report")
    status_counts = auto_df["Upload_Status"].value_counts()
    st.dataframe(status_counts)

    fig5, ax5 = plt.subplots()
    status_counts.plot(kind="bar", ax=ax5)
    ax5.set_title("Upload Success Rate")
    st.pyplot(fig5)


# ---------------- CONTACT ----------------
elif section == "Contact":
    st.header("📞 Contact")

    st.write("""
    **Email:** selvampachimuthu98@gmail.com  
    **LinkedIn:** https://www.linkedin.com/in/selvam-p-a9593a189/ 
    **GitHub:** https://github.com/SelvamPachimuthu  
     **WhatsApp:** [https://wa.me/919876543210](https://wa.me/8681064379)  (replace with your number)
    """)

    st.success("Thank you for visiting my portfolio!")













