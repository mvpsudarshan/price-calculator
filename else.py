import streamlit as st
import pandas as pd

st.set_page_config(page_title="Price Calculator", page_icon="📈")
st.title("📊 Purchase Price Dashboard")

# 1. Setup the Reset Function
def reset_value():
    st.session_state.purchase_val = 300000

# 2. Add the Reset Button
st.button("Reset to 300,000", on_click=reset_value)

# 3. The Input (Notice the 'key' at the end)
purchase_value = st.number_input(
    "Enter Purchase Value:", 
    min_value=0, 
    key="purchase_val", 
    value=300000
)

# --- Math Logic ---
first_discount = purchase_value * 0.07
second_discount = first_discount * 0.1
shipping_charges = purchase_value * 0.1
final_price = (purchase_value - (first_discount + second_discount)) + shipping_charges

# --- Display Results ---
st.divider()
st.subheader(f"Final Price: {final_price:,.2f}")

if final_price > 500000:
    st.error("Additional IT required because final price is greater than 500,000")
else:
    st.success("No additional IT required")

# --- The Visual Chart ---
st.write("### 📉 Cost Comparison")
data = {
    "Categories": ["Base Price", "Discount 1 (7%)", "Discount 2 (10% of D1)", "Shipping (10%)"],
    "Amounts": [purchase_value, -first_discount, -second_discount, shipping_charges]
}
df = pd.DataFrame(data)
st.bar_chart(data=df, x="Categories", y="Amounts")
st.table(df)
