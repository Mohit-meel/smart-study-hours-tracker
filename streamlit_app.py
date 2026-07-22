import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date

from db import (
    insert_record,
    view_records,
    search_record,
    update_record,
    delete_record,
    dashboard_data
)

st.set_page_config(
    page_title="Smart Study Hours Tracker",
    page_icon="📚",
    layout="wide"
)

# ===========================
# HEADER
# ===========================

st.title("📚 Smart Study Hours Tracker")
st.caption("Track • Analyze • Improve")

st.markdown("""
Welcome! 👋

Manage your study records efficiently using this application.

You can:

- 📚 Store Study Records
- 🔍 Search Records
- ✏️ Update Records
- 🗑️ Delete Records
- 📊 Analyze Study Hours
""")

st.divider()

# ===========================
# NAVIGATION
# ===========================

option = st.selectbox(
    "📌 Select an Option",
    [
        "🏠 Home",
        "➕ Add Study Record",
        "📋 View Study Records",
        "🔍 Search Record",
        "✏️ Update Record",
        "🗑️ Delete Record",
        "📊 Dashboard"
    ]
)

# ===========================
# HOME
# ===========================

if option == "🏠 Home":

    st.header("🏠 Home")

    st.success("Welcome to Smart Study Hours Tracker!")

    col1, col2 = st.columns(2)

    total_records, total_hours, subject_data = dashboard_data()

    with col1:
        st.metric("📚 Total Records", total_records)

    with col2:
        st.metric("⏰ Total Study Hours", total_hours)

    st.info("Use the dropdown above to access all features of the application.")

# ===========================
# ADD RECORD
# ===========================

elif option == "➕ Add Study Record":

    st.header("➕ Add Study Record")

    name = st.text_input("Student Name")

    subject = st.text_input("Subject")

    hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        step=0.5
    )

    study_date = st.date_input(
        "Study Date",
        value=date.today()
    )

    if st.button("Add Record"):

        if name and subject:

            insert_record(
                name,
                subject,
                hours,
                study_date
            )

            st.success("✅ Record Added Successfully!")

        else:

            st.error("Please fill all fields.")

# ===========================
# VIEW RECORDS
# ===========================

elif option == "📋 View Study Records":

    st.header("📋 View Study Records")

    records = view_records()

    if records:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Student Name",
                "Subject",
                "Study Hours",
                "Study Date"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning("No records found.")

# ===========================
# SEARCH RECORD
# ===========================

elif option == "🔍 Search Record":

    st.header("🔍 Search Record")

    search_name = st.text_input("Enter Student Name")

    if st.button("Search"):

        records = search_record(search_name)

        if records:

            df = pd.DataFrame(
                records,
                columns=[
                    "ID",
                    "Student Name",
                    "Subject",
                    "Study Hours",
                    "Study Date"
                ]
            )

            st.success(f"Found {len(records)} record(s).")

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning("No record found.")

# ===========================
# UPDATE RECORD
# ===========================

elif option == "✏️ Update Record":

    st.header("✏️ Update Record")

    record_id = st.number_input(
        "Record ID",
        min_value=1,
        step=1
    )

    name = st.text_input("New Student Name")

    subject = st.text_input("New Subject")

    hours = st.number_input(
        "New Study Hours",
        min_value=0.0,
        step=0.5,
        key="update_hours"
    )

    study_date = st.date_input(
        "New Study Date",
        key="update_date"
    )

    if st.button("Update Record"):

        if name and subject:

            update_record(
                record_id,
                name,
                subject,
                hours,
                study_date
            )

            st.success("✅ Record Updated Successfully!")

        else:

            st.error("Please fill all fields.")

# ===========================
# DELETE RECORD
# ===========================

elif option == "🗑️ Delete Record":

    st.header("🗑️ Delete Record")

    record_id = st.number_input(
        "Enter Record ID",
        min_value=1,
        step=1,
        key="delete_id"
    )

    if st.button("Delete Record"):

        delete_record(record_id)

        st.success("✅ Record Deleted Successfully!")

# ===========================
# DASHBOARD
# ===========================

elif option == "📊 Dashboard":

    st.header("📊 Dashboard")

    total_records, total_hours, subject_data = dashboard_data()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📚 Total Records", total_records)

    with col2:
        st.metric("⏰ Total Study Hours", total_hours)

    if subject_data:

        df = pd.DataFrame(
            subject_data,
            columns=["Subject", "Hours"]
        )

        st.subheader("📈 Study Analytics")

        chart1, chart2 = st.columns(2)

        with chart1:

            fig = px.bar(
                df,
                x="Subject",
                y="Hours",
                color="Subject",
                title="Study Hours by Subject"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with chart2:

            fig2 = px.pie(
                df,
                names="Subject",
                values="Hours",
                title="Subject Distribution"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    else:

        st.warning("No records available.")

# ===========================
# FOOTER
# ===========================

st.divider()

st.caption("© 2026 Smart Study Hours Tracker | Developed by Mohit Meel")