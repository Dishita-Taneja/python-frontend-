# first code 

# import streamlit as st
# from datetime import date

# # Title
# st.title("🎂 Age Calculator")

# # User input (Date of Birth)
# dob = st.date_input("Enter your Date of Birth")

# # Button to calculate
# if st.button("Calculate Age"):
#     today = date.today()

#     # Check if DOB is valid
#     if dob > today:
#         st.error("Date of birth cannot be in the future!")
#     else:
#         # Calculate age
#         years = today.year - dob.year
#         months = today.month - dob.month
#         days = today.day - dob.day

#         # Adjust if negative
#         if days < 0:
#             months -= 1
#             days += 30  # approx

#         if months < 0:
#             years -= 1
#             months += 12

#         # Display result
#         st.success(f"Your Age is: {years} years, {months} months, {days} days")

# second code 


# import streamlit as st
# from datetime import date

# st.title("🎂 Age Calculator")

# # Define range
# min_date = date(1900, 1, 1)
# max_date = date.today()

# # Date input with full range
# dob = st.date_input(
#     "Enter your Date of Birth",
#     min_value=min_date,
#     max_value=max_date
# )

# if st.button("Calculate Age"):
#     today = date.today()

#     if dob > today:
#         st.error("Date of birth cannot be in the future!")
#     else:
#         years = today.year - dob.year
#         months = today.month - dob.month
#         days = today.day - dob.day

#         if days < 0:
#             months -= 1
#             days += 30

#         if months < 0:
#             years -= 1
#             months += 12

#         st.success(f"Your Age is: {years} years, {months} months, {days} days")


# third code 

import streamlit as st
from datetime import date

st.title("🎂 Age Calculator")

# Date range
min_date = date(1800, 1, 1)
max_date = date.today()

# Input
dob = st.date_input(
    "Enter your Date of Birth",
    min_value=min_date,
    max_value=max_date
)

if st.button("Calculate Age"):
    today = date.today()

    if dob > today:
        st.error("Date of birth cannot be in the future!")
    else:
        # Age calculation
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            days += 30

        if months < 0:
            years -= 1
            months += 12

        st.success(f"Your Age: {years} years, {months} months, {days} days")

        # 🎉 Next Birthday Calculation
        next_birthday = date(today.year, dob.month, dob.day)

#         # If birthday already passed this year
#         if next_birthday < today:
#             next_birthday = date(today.year + 1, dob.month, dob.day)

#         # days_left = (next_birthday - today).days

#         # st.info(f"🎉 Your next birthday is in {days_left} days!")

#  # Next Birthday
# next_birthday = date(today.year, dob.month, dob.day)
# today=date.today()
# if next_birthday < today:
#     next_birthday = date(today.year + 1, dob.month, dob.day)

# # Calculate difference
# y = next_birthday.year - today.year
# m = next_birthday.month - today.month
# d = next_birthday.day - today.day

# # Adjust negatives
# if d < 0:
#     m -= 1
#     d += 30   # approx (good enough for UI)

# if m < 0:
#     y -= 1
#     m += 12

# st.info(f"🎉 Next birthday in: {y} years, {m} months, {d} days")    




# or use this 
# from dateutil.relativedelta import relativedelta

# diff = relativedelta(next_birthday, today)

# st.info(f"🎉 Next birthday in: {diff.years} years, {diff.months} months, {diff.days} days")


        if next_birthday < today:
            next_birthday = date(today.year + 1, dob.month, dob.day)

        # Difference
        y = next_birthday.year - today.year
        m = next_birthday.month - today.month
        d = next_birthday.day - today.day

        if d < 0:
            m -= 1
            d += 30

        if m < 0:
            y -= 1
            m += 12

        st.info(f"🎉 Next birthday in: {y} years, {m} months, {d} days")