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
Experienced Pharmacovigilance professional **Medicines clinical and safety data **.
This portfolio demonstrates my skills in **Clinical data handling, Python, Data Analysis, Visualization, and Healthcare Data**.
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

# ---------------- PROJECTS ----------------
elif section == "Projects":
    st.header("📂 Projects")

    # ---------- PROJECT 1 ----------
    st.subheader("1️⃣ Adverse Event Data Analysis (Pharmacovigilance)")
    st.write("""
    - Cleaned and analyzed Adverse Event (AE) datasets
    - Identified most frequently reported reactions
    - Performed trend analysis using Pandas
    - Visualized AE distribution using Matplotlib
    - Strengthened signal detection understanding
    """)

    # ---------- PROJECT 2 ----------
    st.subheader("2️⃣ Clinical Trial Demographics Dashboard")
    st.write("""
    - Analyzed subject-level demographic data (Age, Gender distribution)
    - Generated summary statistics for study population
    - Built visual dashboards using Pandas & Matplotlib
    - Supported study-level reporting insights
    """)

    # ---------- PROJECT 3 ----------
    st.subheader("3️⃣ Clinical Data Discrepancy & Query Management (CDM Simulation)")
    st.write("""
    - Identified missing, inconsistent, and protocol-deviated data
    - Simulated query generation workflow similar to RAVE/Veeva EDC
    - Implemented validation checks (range, cross-field, mandatory checks)
    - Reviewed data listings for accuracy and consistency
    - Generated query status tracking reports
    """)

    # ---------- PROJECT 4 ----------
    st.subheader("4️⃣ SAE Reconciliation & Data Listing Review")
    st.write("""
    - Performed Serious Adverse Event (SAE) reconciliation
    - Compared AE datasets between clinical and safety records
    - Identified mismatches and generated clarification queries
    - Ensured regulatory compliance and audit readiness
    """)

    # ---------- PROJECT 5 ----------
    st.subheader("5️⃣ Excel to MySQL Data Automation")
    st.write("""
    - Automated bulk data upload from Excel to MySQL database
    - Reduced manual effort and minimized entry errors
    - Improved workflow efficiency and data integrity
    """)


# ---------------- DATA ANALYSIS DEMO ----------------
elif section == "Data Analysis Demo":
    st.header("📊 Clinical Data Management Demo")

    st.write("Simulated Clinical Trial Dataset – Discrepancy & Query Management")

    # Create sample clinical dataset
    data = {
        "Subject_ID": np.arange(1001, 1051),
        "Age": np.random.randint(18, 80, 50),
        "Gender": np.random.choice(["Male", "Female"], 50),
        "AE_Reported": np.random.choice(["Yes", "No"], 50),
        "AE_Term": np.random.choice(
            ["Nausea", "Headache", "Fatigue", "Vomiting", None], 50
        ),
        "SAE_Flag": np.random.choice(["Yes", "No"], 50)
    }

    df = pd.DataFrame(data)

    # Introduce logical discrepancy
    df.loc[df["AE_Reported"] == "No", "AE_Term"] = None

    st.subheader("🔹 Raw Clinical Data")
    st.dataframe(df)

    # ---------------- VALIDATION CHECK ----------------
    st.subheader("🔹 Data Validation Checks")

    discrepancies = df[
        (df["AE_Reported"] == "Yes") & (df["AE_Term"].isnull())
    ]

    st.write("### 🚨 Open Data Queries Identified")
    st.dataframe(discrepancies)

    # ---------------- QUERY STATUS REPORT ----------------
    st.subheader("🔹 Query Status Summary")

    total_records = len(df)
    total_queries = len(discrepancies)

    query_summary = pd.DataFrame({
        "Total Records": [total_records],
        "Open Queries": [total_queries],
        "Query Rate (%)": [round((total_queries / total_records) * 100, 2)]
    })

    st.dataframe(query_summary)

    # ---------------- SAE DISTRIBUTION ----------------
    st.subheader("🔹 SAE Reconciliation Overview")

    sae_counts = df["SAE_Flag"].value_counts()

    fig, ax = plt.subplots()
    sae_counts.plot(kind="bar", ax=ax)
    ax.set_ylabel("Count")
    ax.set_title("SAE Distribution")

    st.pyplot(fig)


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











