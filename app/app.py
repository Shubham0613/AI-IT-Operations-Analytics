import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI-IT Operations Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
df = pd.read_csv("data/cleaned_data.csv")

df["Ticket_Date"] = pd.to_datetime(df["Ticket_Date"], errors="coerce")

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("AI-IT OPERATIONS ANALYTICS")
st.caption(
    "AI-assisted IT incident prioritization | "
    "SLA performance | Service quality | Operational insights"
)

# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------
st.sidebar.header("Incident Filters")

departments = sorted(df["Department"].dropna().unique())
issues = sorted(df["Issue_Type"].dropna().unique())
locations = sorted(df["Location"].dropna().unique())
priorities = sorted(df["Priority"].dropna().unique())
statuses = sorted(df["Status"].dropna().unique())

selected_departments = st.sidebar.multiselect(
    "Department",
    departments,
    default=departments
)

selected_issues = st.sidebar.multiselect(
    "Issue Type",
    issues,
    default=issues
)

selected_locations = st.sidebar.multiselect(
    "Location",
    locations,
    default=locations
)

selected_priorities = st.sidebar.multiselect(
    "Priority",
    priorities,
    default=priorities
)

selected_statuses = st.sidebar.multiselect(
    "Status",
    statuses,
    default=statuses
)

# ---------------------------------------------------------
# FILTER DATA
# ---------------------------------------------------------
filtered_df = df[
    df["Department"].isin(selected_departments)
    & df["Issue_Type"].isin(selected_issues)
    & df["Location"].isin(selected_locations)
    & df["Priority"].isin(selected_priorities)
    & df["Status"].isin(selected_statuses)
].copy()

# ---------------------------------------------------------
# EMPTY FILTER CHECK
# ---------------------------------------------------------
if filtered_df.empty:
    st.warning("No incidents match the selected filters.")
    st.stop()

# ---------------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------------
total_tickets = len(filtered_df)

resolved_tickets = (
    filtered_df["Status"].eq("Resolved").sum()
)

sla_breaches = (
    filtered_df["SLA_Breach"].sum()
)

sla_compliance = (
    (total_tickets - sla_breaches) / total_tickets * 100
    if total_tickets > 0 else 0
)

avg_csat = filtered_df["CSAT"].mean()

avg_resolution = filtered_df["Resolution_Hours"].mean()

ai_critical = (
    filtered_df["AI_Predicted_Priority"].eq("Critical").sum()
)

high_critical = (
    filtered_df["Priority"].isin(["High", "Critical"]).sum()
)

# ---------------------------------------------------------
# KPI ROW 1
# ---------------------------------------------------------
st.subheader("Executive Overview")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Total Tickets",
        f"{total_tickets:,}"
    )

with k2:
    st.metric(
        "Resolved Tickets",
        f"{resolved_tickets:,}"
    )

with k3:
    st.metric(
        "SLA Compliance",
        f"{sla_compliance:.2f}%"
    )

with k4:
    st.metric(
        "Average CSAT",
        f"{avg_csat:.2f}"
    )

# ---------------------------------------------------------
# KPI ROW 2
# ---------------------------------------------------------
k5, k6, k7, k8 = st.columns(4)

with k5:
    st.metric(
        "SLA Breaches",
        f"{sla_breaches:,}"
    )

with k6:
    st.metric(
        "Avg Resolution Hours",
        f"{avg_resolution:.2f}"
    )

with k7:
    st.metric(
        "AI Critical Predictions",
        f"{ai_critical:,}"
    )

with k8:
    st.metric(
        "High / Critical Tickets",
        f"{high_critical:,}"
    )

st.divider()

# ---------------------------------------------------------
# STATUS + AI PRIORITY
# ---------------------------------------------------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Ticket Status Distribution")

    status_data = (
        filtered_df["Status"]
        .value_counts()
        .reset_index()
    )

    status_data.columns = ["Status", "Tickets"]

    fig_status = px.pie(
        status_data,
        names="Status",
        values="Tickets",
        hole=0.45
    )

    fig_status.update_layout(
        margin=dict(l=10, r=10, t=20, b=10),
        legend_title_text=""
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

with c2:
    st.subheader("AI Predicted Priority Distribution")

    ai_data = (
        filtered_df["AI_Predicted_Priority"]
        .value_counts()
        .reset_index()
    )

    ai_data.columns = ["AI_Predicted_Priority", "Tickets"]

    fig_ai = px.pie(
        ai_data,
        names="AI_Predicted_Priority",
        values="Tickets",
        hole=0.45
    )

    fig_ai.update_layout(
        margin=dict(l=10, r=10, t=20, b=10),
        legend_title_text=""
    )

    st.plotly_chart(
        fig_ai,
        use_container_width=True
    )

# ---------------------------------------------------------
# ISSUE + LOCATION
# ---------------------------------------------------------
c3, c4 = st.columns(2)

with c3:
    st.subheader("Tickets by Issue Type")

    issue_data = (
        filtered_df["Issue_Type"]
        .value_counts()
        .sort_values()
        .reset_index()
    )

    issue_data.columns = ["Issue_Type", "Tickets"]

    fig_issue = px.bar(
        issue_data,
        x="Tickets",
        y="Issue_Type",
        orientation="h",
        text="Tickets"
    )

    fig_issue.update_layout(
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(
        fig_issue,
        use_container_width=True
    )

with c4:
    st.subheader("Tickets by Location")

    location_data = (
        filtered_df["Location"]
        .value_counts()
        .sort_values()
        .reset_index()
    )

    location_data.columns = ["Location", "Tickets"]

    fig_location = px.bar(
        location_data,
        x="Tickets",
        y="Location",
        orientation="h",
        text="Tickets"
    )

    fig_location.update_layout(
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(
        fig_location,
        use_container_width=True
    )

# ---------------------------------------------------------
# SLA ANALYSIS
# ---------------------------------------------------------
c5, c6 = st.columns(2)

with c5:
    st.subheader("SLA Breaches by Priority")

    sla_priority = (
        filtered_df.groupby("Priority")["SLA_Breach"]
        .sum()
        .reset_index()
    )

    sla_priority.columns = ["Priority", "SLA Breaches"]

    fig_sla = px.bar(
        sla_priority,
        x="Priority",
        y="SLA Breaches",
        text="SLA Breaches"
    )

    fig_sla.update_layout(
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(
        fig_sla,
        use_container_width=True
    )

with c6:
    st.subheader("AI Confidence Distribution")

    confidence = filtered_df["AI_Confidence"]

    confidence_bins = pd.cut(
        confidence,
        bins=[0, 0.6, 0.7, 0.8, 0.9, 1.0],
        labels=[
            "0-60%",
            "60-70%",
            "70-80%",
            "80-90%",
            "90-100%"
        ],
        include_lowest=True
    )

    confidence_data = (
        confidence_bins
        .value_counts()
        .sort_index()
        .reset_index()
    )

    confidence_data.columns = [
        "Confidence Range",
        "Tickets"
    ]

    fig_conf = px.bar(
        confidence_data,
        x="Confidence Range",
        y="Tickets",
        text="Tickets"
    )

    fig_conf.update_layout(
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(
        fig_conf,
        use_container_width=True
    )

# ---------------------------------------------------------
# AI / OPERATIONS INSIGHTS
# ---------------------------------------------------------
st.divider()

st.subheader("AI / Operations Insights")

top_issue = (
    filtered_df["Issue_Type"]
    .value_counts()
    .idxmax()
)

top_issue_count = (
    filtered_df["Issue_Type"]
    .value_counts()
    .max()
)

top_location = (
    filtered_df["Location"]
    .value_counts()
    .idxmax()
)

top_location_count = (
    filtered_df["Location"]
    .value_counts()
    .max()
)

critical_count = (
    filtered_df["AI_Predicted_Priority"]
    .eq("Critical")
    .sum()
)

ins1, ins2, ins3 = st.columns(3)

with ins1:
    st.info(
        f"**Top Issue Type**\n\n"
        f"{top_issue} leads incident volume with "
        f"**{top_issue_count} tickets**."
    )

with ins2:
    st.info(
        f"**Highest Ticket Location**\n\n"
        f"{top_location} records the highest volume "
        f"with **{top_location_count} tickets**."
    )

with ins3:
    st.info(
        f"**AI Critical Triage**\n\n"
        f"**{critical_count} tickets** are predicted as "
        f"Critical by the AI prioritization layer."
    )

# ---------------------------------------------------------
# INCIDENT EXPLORER
# ---------------------------------------------------------
st.divider()

st.subheader("Incident Explorer")

search_text = st.text_input(
    "Search by Ticket ID, Issue Type, Agent or Root Cause"
)

explorer_df = filtered_df.copy()

if search_text:
    search_text = search_text.lower()

    mask = (
        explorer_df["Ticket_ID"]
        .astype(str)
        .str.lower()
        .str.contains(search_text, na=False)
        | explorer_df["Issue_Type"]
        .astype(str)
        .str.lower()
        .str.contains(search_text, na=False)
        | explorer_df["Agent"]
        .astype(str)
        .str.lower()
        .str.contains(search_text, na=False)
        | explorer_df["Root_Cause"]
        .astype(str)
        .str.lower()
        .str.contains(search_text, na=False)
    )

    explorer_df = explorer_df[mask]

display_columns = [
    "Ticket_ID",
    "Ticket_Date",
    "Department",
    "Issue_Type",
    "Location",
    "Priority",
    "Status",
    "Agent",
    "Resolution_Hours",
    "SLA_Hours",
    "SLA_Breach",
    "CSAT",
    "Business_Impact",
    "Users_Affected",
    "AI_Priority_Score",
    "AI_Predicted_Priority",
    "AI_Confidence"
]

st.dataframe(
    explorer_df[display_columns],
    use_container_width=True,
    hide_index=True
)

st.caption(
    f"Showing {len(explorer_df):,} incidents from "
    f"{len(filtered_df):,} filtered tickets."
)
