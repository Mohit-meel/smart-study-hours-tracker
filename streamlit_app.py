import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

from db import (
    insert_record,
    view_records,
    search_record,
    update_record,
    delete_record,
    dashboard_data
)

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Smart Study Hours Tracker",
    page_icon="📚",
    layout="wide"
)

# ----------------------------
# HEADER
# ----------------------------

st.title("📚 Smart Study Hours Tracker")
st.caption("Track • Analyze • Improve")

st.success("👋 Welcome to Smart Study Hours Tracker!")

st.write("""
This application helps you manage your study records easily.

✔ Add Study Records

✔ View Records

✔ Search Records

✔ Update Records

✔ Delete Records

✔ Analyze Study Hours
""")

st.divider()

# ----------------------------
# DASHBOARD METRICS
# ----------------------------

total_records, total_hours, subject_data = dashboard_data()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📚 Total Records",
        total_records
    )

with col2:
    st.metric(
        "⏰ Total Study Hours",
        total_hours
    )

st.divider()

# ----------------------------
# TABS
# ----------------------------

home_tab, add_tab, view_tab, search_tab, update_tab, delete_tab, dashboard_tab = st.tabs(
    [
        "🏠 Home",
        "➕ Add",
        "📋 View",
        "🔍 Search",
        "✏️ Update",
        "🗑 Delete",
        "📊 Dashboard"
    ]
)

# ----------------------------
# HOME TAB
# ----------------------------

with home_tab:

    st.header("🏠 Home")

    st.info(
        "Welcome! Use the tabs above to manage your study records."
    )

    st.write("""
### Features

- Add Study Records
- View All Records
- Search Records
- Update Existing Records
- Delete Records
- View Dashboard & Analytics
""")

# ----------------------------
# ADD TAB
# ----------------------------

with add_tab:

    st.header("➕ Add Study Record")

    name = st.text_input(
        "Student Name"
    )

    subject = st.text_input(
        "Subject"
    )

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

            st.success(
                "✅ Record Added Successfully!"
            )

        else:

            st.error(
                "Please fill all fields."
            )

# ----------------------------
# VIEW TAB
# ----------------------------

with view_tab:

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
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning("No study records found.")

# ----------------------------
# SEARCH TAB
# ----------------------------

with search_tab:

    st.header("🔍 Search Study Record")

    search_name = st.text_input(
        "Enter Student Name"
    )

    if st.button("Search"):

        if search_name.strip():

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

                st.success(f"{len(records)} record(s) found.")

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.warning("No matching record found.")

        else:

            st.error("Please enter a student name.")


# ----------------------------
# UPDATE TAB
# ----------------------------

with update_tab:

    st.header("✏️ Update Study Record")

    record_id = st.number_input(
        "Record ID",
        min_value=1,
        step=1,
        key="update_id"
    )

    new_name = st.text_input(
        "New Student Name",
        key="update_name"
    )

    new_subject = st.text_input(
        "New Subject",
        key="update_subject"
    )

    new_hours = st.number_input(
        "New Study Hours",
        min_value=0.0,
        step=0.5,
        key="update_hours"
    )

    new_date = st.date_input(
        "New Study Date",
        key="update_date"
    )

    if st.button("Update Record"):

        if new_name and new_subject:

            update_record(
                record_id,
                new_name,
                new_subject,
                new_hours,
                new_date
            )

            st.success("✅ Record Updated Successfully!")

        else:

            st.error("Please fill all fields.")

# ----------------------------
# DELETE TAB
# ----------------------------

with delete_tab:

    st.header("🗑 Delete Study Record")

    delete_id = st.number_input(
        "Record ID",
        min_value=1,
        step=1,
        key="delete_id"
    )

    if st.button("Delete Record"):

        delete_record(delete_id)

        st.success("✅ Record Deleted Successfully!")

# ----------------------------
# DASHBOARD TAB
# ----------------------------

with dashboard_tab:

    st.header("📊 Dashboard")

    total_records, total_hours, subject_data = dashboard_data()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📚 Total Records",
            total_records
        )

    with col2:
        st.metric(
            "⏰ Total Study Hours",
            total_hours
        )

    st.divider()

    if subject_data:

        df_chart = pd.DataFrame(
            subject_data,
            columns=[
                "Subject",
                "Hours"
            ]
        )

        chart1, chart2 = st.columns(2)

        with chart1:

            fig = px.bar(
                df_chart,
                x="Subject",
                y="Hours",
                color="Subject",
                text_auto=True,
                title="Study Hours by Subject"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with chart2:

            fig2 = px.pie(
                df_chart,
                names="Subject",
                values="Hours",
                hole=0.45,
                title="Subject Distribution"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    else:

        st.warning("No records available.")

# ----------------------------
# FOOTER
# ----------------------------

st.divider()

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
        Developed with ❤️ using Streamlit & PostgreSQL
        <br><br>
        © 2026 Smart Study Hours Tracker
    </div>
    """,
    unsafe_allow_html=True
)