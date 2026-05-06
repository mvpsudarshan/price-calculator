import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="MVP's Tool Hub", page_icon="🚀")

# --- SIDEBAR PERSONALIZATION ---
st.sidebar.markdown("# 🛠️ MVP Sudarshan")
st.sidebar.markdown("### Professional Calculator Suite")
st.sidebar.divider()

# Navigation Menu
page = st.sidebar.selectbox("Select a Tool:", ["Price Calculator", "Salary Tracker"])

st.sidebar.divider()
st.sidebar.info("Developed by **MVP Sudarshan**")
st.sidebar.write("Built with ❤️ using Streamlit")

# --- PAGE 1: PRICE CALCULATOR ---
if page == "Price Calculator":
    st.title("📊 Purchase Price Dashboard")
    
    if 'price_val' not in st.session_state:
        st.session_state.price_val = 0
    
    if st.sidebar.button("🔄 Reset Calculator"):
        st.session_state.price_val = 0
        st.rerun()

    purchase_value = st.number_input("Enter Purchase Value:", min_value=0, key="price_val")

    # Math Logic
    d1 = purchase_value * 0.07
    d2 = d1 * 0.1
    ship = purchase_value * 0.1
    final = (purchase_value - (d1 + d2)) + ship

    st.divider()
    st.subheader(f"Final Price: {final:,.2f}")
    
    if final > 500000:
        st.error("Additional IT required")
    else:
        st.success("No additional IT required")

    # Chart
    df = pd.DataFrame({
        "Categories": ["Base", "D1", "D2", "Ship"],
        "Amounts": [purchase_value, -d1, -d2, ship]
    })
    st.bar_chart(data=df, x="Categories", y="Amounts")

# --- PAGE 2: SALARY TRACKER ---
elif page == "Salary Tracker":
    st.title("💼 Salary & IT Eligibility")

    if 'salary_val' not in st.session_state:
        st.session_state.salary_val = 0

    if st.sidebar.button("🔄 Reset Salary"):
        st.session_state.salary_val = 0
        st.rerun()

    salary_month = st.number_input("Enter Salary per month:", min_value=0, key="salary_val")
    
    annual = salary_month * 12
    eligible_it = annual - 100000

    st.divider()
    st.metric("Annual Salary", f"{annual:,.2f}")
    st.write(f"**Taxable Amount:** {eligible_it:,.2f}")

    if eligible_it > 1200000:
        st.error("⚠️ Eligible for IT")
    else:
        st.success("✅ Not eligible for IT")
