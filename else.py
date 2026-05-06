import streamlit as st
import pandas as pd

# 1. Page Setup
st.set_page_config(page_title="Price Calculator", page_icon="📈")
st.title("📊 Purchase Price Dashboard")

# 2. Add a Reset Button Logic
if 'val' not in st.session_state:
    st.session_state.val = 300000

if st.button("Reset Values"):
    st.session_state.val = 300000

# 3. Inputs
purchase_value = st.number_input("Enter Purchase Value:", min_value=0, value=st.session_state.val)

# 4. Math Logic
first_discount = purchase_value * 0.07
second_discount = first_discount * 0.1
shipping_charges = purchase_value * 0.1
final_price = (purchase_value - (first_discount + second_discount)) + shipping_charges

# 5. Display Results
st.divider()
st.subheader(f"Final Price: {final_price:,.2f}")

if final_price > 500000:
    st.error("Additional IT required because final price is greater than 500,000")
else:
    st.success("No additional IT required")

# 6. The Visual Chart
st.write("### 📉 Cost Comparison")
# Prepare data for the chart
data = {
    "Categories": ["Base Price", "Discount 1 (7%)", "Discount 2 (10% of D1)", "Shipping (10%)"],
    "Amounts": [purchase_value, -first_discount, -second_discount, shipping_charges]
}
df = pd.DataFrame(data)

# Display the bar chart
st.bar_chart(data=df, x="Categories", y="Amounts")

# Display a simple table breakdown
st.table(df)
