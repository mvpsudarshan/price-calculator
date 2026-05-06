'''number = input("Enter a number: ")
print(number)
number = int(number)
print(type(number))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


#Example 2
Salary_per_month = int(input("Enter your Salary per month: "))
Annual_salary = Salary_per_month * 12
print(f"Your Annual Salary is: {Annual_salary}")

Eligible_for_IT = Annual_salary - 100000

if Eligible_for_IT > 1200000:
    print("You are eligible for IT")
else:
    print("You are not eligible for IT")'''



#Example3
import streamlit as st

# This creates the input box ON the webpage
purchase_value = st.number_input("Enter the purchase value:", min_value=0, value=300000)

# The math stays the same
first_discount = purchase_value * 0.07
second_discount = first_discount * 0.1
shipping_charges = purchase_value * 0.1
final_price = (purchase_value - (first_discount + second_discount)) + shipping_charges

# This shows the result ON the webpage
st.write(f"### Your final price is: {final_price:,.2f}")

if final_price > 500000:
    st.error("Additional IT required: Price exceeds 500,000")
else:
    st.success("No additional IT required")


