import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="Kris Holmes — Data Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #0a0e1a;
        color: #e2e8f0;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1100px;
    }

    /* Hero */
    .hero-wrapper {
        background: linear-gradient(135deg, #0f1629 0%, #1a1f3a 50%, #0f1629 100%);
        border: 1px solid #2d3561;
        border-radius: 16px;
        padding: 3.5rem 3rem;
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
    }
    .hero-wrapper::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 250px; height: 250px;
        background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-name {
        font-size: 3.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a5b4fc, #818cf8, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
        margin-bottom: 0.4rem;
    }
    .hero-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.95rem;
        color: #64748b;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .hero-title span {
        color: #6366f1;
    }
    .hero-bio {
        font-size: 1.05rem;
        color: #94a3b8;
        line-height: 1.8;
        max-width: 680px;
    }
    .hero-meta {
        display: flex;
        gap: 1.5rem;
        margin-top: 1.8rem;
        flex-wrap: wrap;
    }
    .hero-meta-item {
        display: flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.88rem;
        color: #64748b;
    }
    .hero-meta-item a {
        color: #818cf8;
        text-decoration: none;
    }

    /* Section headers */
    .section-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #6366f1;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #e2e8f0;
        margin-bottom: 1.5rem;
    }

    /* Cards */
    .card {
        background: #111827;
        border: 1px solid #1e2940;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s;
    }
    .card:hover {
        border-color: #4f46e5;
    }
    .card-company {
        font-size: 1.15rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    .card-role {
        font-size: 0.82rem;
        font-family: 'JetBrains Mono', monospace;
        color: #6366f1;
        letter-spacing: 0.05em;
        margin-bottom: 0.3rem;
    }
    .card-period {
        font-size: 0.8rem;
        color: #475569;
        margin-bottom: 0.8rem;
    }
    .card-bullets {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .card-bullets li {
        font-size: 0.88rem;
        color: #94a3b8;
        padding: 0.25rem 0;
        padding-left: 1.1rem;
        position: relative;
        line-height: 1.6;
    }
    .card-bullets li::before {
        content: '→';
        position: absolute;
        left: 0;
        color: #4f46e5;
        font-size: 0.8rem;
    }

    /* Skill tags */
    .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.6rem;
    }
    .tag {
        background: #1e2940;
        color: #a5b4fc;
        font-size: 0.75rem;
        font-family: 'JetBrains Mono', monospace;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        border: 1px solid #2d3561;
    }

    /* Stat boxes */
    .stat-box {
        background: linear-gradient(135deg, #111827, #1a1f3a);
        border: 1px solid #2d3561;
        border-radius: 12px;
        padding: 1.4rem;
        text-align: center;
    }
    .stat-number {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a5b4fc, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.78rem;
        color: #64748b;
        margin-top: 0.4rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* Education */
    .edu-card {
        background: #111827;
        border: 1px solid #1e2940;
        border-radius: 12px;
        padding: 1.4rem;
    }

    /* Divider */
    .divider {
        border: none;
        border-top: 1px solid #1e2940;
        margin: 2.5rem 0;
    }

    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)


# ── HERO ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-name">Kris Holmes</div>
    <div class="hero-title">// <span>Data Engineer</span></div>
    <div class="hero-bio">
        Designs and operates scalable data platforms and distributed ETL/ELT pipelines
        with SQL, PySpark, and Spark. Builds well-modeled, certified datasets and semantic
        layers that power Power BI, Tableau, and CRM Analytics — standardizing KPIs across
        Sales, Finance, and Operations. Also ships AI-assisted internal apps (OpenAI + Streamlit)
        to accelerate self-service insights.
    </div>
    <div class="hero-meta">
        <div class="hero-meta-item">📍 Houston, TX</div>
        <div class="hero-meta-item">📞 (832) 647-5192</div>
        <div class="hero-meta-item">✉️ <a href="mailto:krisholmes444@gmail.com">krisholmes444@gmail.com</a></div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── AT A GLANCE ─────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-box"><div class="stat-number">4+</div><div class="stat-label">Years Experience</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><div class="stat-number">4</div><div class="stat-label">Companies</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><div class="stat-number">10+</div><div class="stat-label">Core Tech Stack</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-box"><div class="stat-number">CS</div><div class="stat-label">UTSA · 2023</div></div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── SKILLS ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">// Capabilities</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Skills & Tech Stack</div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    categories = [
        "Distributed ETL / Pipelines",
        "Cloud Warehousing & Modeling",
        "BI Enablement",
        "Platform Engineering",
        "API & Data Services",
        "AI / ML Tooling",
    ]
    scores = [95, 88, 90, 85, 80, 75]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(99,102,241,0.18)',
        line=dict(color='#6366f1', width=2),
        hovertemplate='%{theta}<br>Proficiency: %{r}<extra></extra>',
    ))
    fig_radar.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color='#475569', size=9), gridcolor='#1e2940', linecolor='#1e2940'),
            angularaxis=dict(tickfont=dict(color='#94a3b8', size=11), gridcolor='#1e2940', linecolor='#1e2940'),
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(l=50, r=50, t=30, b=30),
        height=340,
    )
    st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": False})

with col_right:
    tools = {
        "PySpark / Spark": 95,
        "SQL (T-SQL / dbt)": 92,
        "Azure Fabric / Lakehouse": 90,
        "Power BI Semantic Models": 88,
        "Snowflake": 82,
        "OpenAI APIs": 78,
        "Tableau / CRM Analytics": 80,
        "Python / Streamlit": 85,
        "C# / .NET": 70,
        "REST APIs": 75,
    }

    fig_bar = go.Figure(go.Bar(
        x=list(tools.values()),
        y=list(tools.keys()),
        orientation='h',
        marker=dict(
            color=list(tools.values()),
            colorscale=[[0, '#2d3561'], [0.5, '#4f46e5'], [1, '#818cf8']],
            line=dict(width=0),
        ),
        text=[f"{v}%" for v in tools.values()],
        textposition='inside',
        textfont=dict(color='white', size=11),
        hovertemplate='%{y}: %{x}%<extra></extra>',
    ))
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[0, 100], showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(tickfont=dict(color='#94a3b8', size=11), gridcolor='#1e2940'),
        margin=dict(l=10, r=10, t=20, b=10),
        height=340,
    )
    st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── EXPERIENCE TIMELINE ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">// Work History</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["PowerSchool", "Lutron", "Cisco Meraki", "American Express"])

with tab1:
    st.markdown("""
    <div class="card">
        <div class="card-role">Data Engineer · Remote</div>
        <div class="card-company">PowerSchool</div>
        <div class="card-period">Aug 2024 — Present</div>
        <ul class="card-bullets">
            <li>Architected end-to-end ETL pipelines in SQL and PySpark, ingesting from Salesforce (Lightning), Jira, NetSuite, and Freshservice into Fabric Lakehouse.</li>
            <li>Built GPT-powered internal apps with OpenAI APIs and Streamlit to analyze Salesforce data — accelerating sales insights and self-service analysis.</li>
            <li>Designed semantic models and star schemas for ARR, pipeline, contract value, and lifecycle status; standardized KPI definitions with stakeholders.</li>
            <li>Centralized and versioned transformation logic in SQL with automated testing and data-quality checks for reliability and transparency.</li>
            <li>Optimized PySpark jobs (partitioning, caching, joins) for large-scale transformations and aggregations.</li>
            <li>Delivered certified Power BI semantic models (also consumed by Tableau and CRM Analytics) that improved dashboard performance and adoption.</li>
            <li>Exposed clean, well-modeled feature layers and governed access patterns to enable downstream AI and advanced analytics.</li>
        </ul>
        <div class="tag-row">
            <span class="tag">PySpark</span><span class="tag">SQL</span><span class="tag">Azure Fabric</span>
            <span class="tag">Salesforce</span><span class="tag">Power BI</span><span class="tag">OpenAI</span>
            <span class="tag">Streamlit</span><span class="tag">Star Schema</span><span class="tag">ETL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="card">
        <div class="card-role">Software Engineer · Cincinnati</div>
        <div class="card-company">Lutron</div>
        <div class="card-period">Jan 2023 — Aug 2024</div>
        <ul class="card-bullets">
            <li>Developed and maintained C#/.NET GUI applications for lighting and building automation, supporting internal and customer-facing workflows.</li>
            <li>Built data-driven interfaces surfacing configuration state, telemetry, and operational data from services and SQL databases.</li>
            <li>Delivered UI flows for device configuration, system monitoring, and diagnostics that presented complex data clearly.</li>
            <li>Integrated frontend components with SQL-backed APIs and aligned data contracts with backend teams.</li>
            <li>Improved usability and reliability through iterative testing and feedback cycles.</li>
            <li>Enhanced performance by eliminating inefficient data access patterns between UI and services.</li>
            <li>Participated in code reviews, automated testing, and release processes.</li>
        </ul>
        <div class="tag-row">
            <span class="tag">C#</span><span class="tag">.NET</span><span class="tag">SQL</span>
            <span class="tag">REST APIs</span><span class="tag">GUI Dev</span><span class="tag">Telemetry</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="card">
        <div class="card-role">Software Engineering Intern · Remote</div>
        <div class="card-company">Cisco Meraki</div>
        <div class="card-period">Aug 2022 — Dec 2022</div>
        <ul class="card-bullets">
            <li>Built internal tools using Ruby on Rails, Go, React, and SQL to support large-scale networking operations.</li>
            <li>Developed backend APIs and data-access layers consumed by internal analytics and monitoring tools.</li>
            <li>Shipped features used by engineering and operations teams in a distributed environment.</li>
        </ul>
        <div class="tag-row">
            <span class="tag">Ruby on Rails</span><span class="tag">Go</span><span class="tag">React</span>
            <span class="tag">SQL</span><span class="tag">APIs</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="card">
        <div class="card-role">Software Engineering Intern · Phoenix</div>
        <div class="card-company">American Express</div>
        <div class="card-period">Jun 2022 — Aug 2022</div>
        <ul class="card-bullets">
            <li>Developed backend components for financial APIs using Java and Spring.</li>
            <li>Supported CI/CD pipelines and data validation workflows in a regulated enterprise environment.</li>
        </ul>
        <div class="tag-row">
            <span class="tag">Java</span><span class="tag">Spring</span><span class="tag">CI/CD</span>
            <span class="tag">Data Validation</span><span class="tag">FinTech</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── TIMELINE CHART ───────────────────────────────────────────────────────────
st.markdown('<div class="section-label">// Career Progression</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Career Timeline</div>', unsafe_allow_html=True)

timeline_data = [
    dict(Task="PowerSchool", Start="2024-08-01", Finish="2026-03-01", Role="Data Engineer"),
    dict(Task="Lutron", Start="2023-01-01", Finish="2024-08-01", Role="Software Engineer"),
    dict(Task="Cisco Meraki", Start="2022-08-01", Finish="2022-12-01", Role="Intern"),
    dict(Task="American Express", Start="2022-06-01", Finish="2022-08-01", Role="Intern"),
    dict(Task="UTSA (CS Degree)", Start="2018-08-01", Finish="2023-05-01", Role="Education"),
]

colors = {
    "Data Engineer": "#6366f1",
    "Software Engineer": "#818cf8",
    "Intern": "#a5b4fc",
    "Education": "#2d3561",
}

fig_gantt = go.Figure()
for i, d in enumerate(timeline_data):
    fig_gantt.add_trace(go.Bar(
        x=[d["Start"], d["Finish"]],
        y=[d["Task"], d["Task"]],
        orientation='h',
        marker=dict(color=colors[d["Role"]], line=dict(width=0)),
        name=d["Role"],
        hovertemplate=f"<b>{d['Task']}</b><br>{d['Role']}<br>{d['Start'][:7]} → {d['Finish'][:7]}<extra></extra>",
        showlegend=False,
        base=d["Start"],
    ))

# Use plotly express timeline instead
import pandas as pd
df_timeline = pd.DataFrame(timeline_data)
fig_gantt = px.timeline(
    df_timeline, 
    x_start="Start", 
    x_end="Finish", 
    y="Task",
    color="Role",
    color_discrete_map=colors,
    hover_data=["Role"],
)

fig_gantt.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title="",
        tickfont=dict(color='#64748b', size=11),
        gridcolor='#1e2940',
    ),
    yaxis=dict(
        title="",
        tickfont=dict(color='#94a3b8', size=12), 
        gridcolor='rgba(0,0,0,0)'
    ),
    margin=dict(l=20, r=20, t=20, b=20),
    height=280,
    showlegend=False,
)

fig_gantt.update_traces(
    marker=dict(line=dict(width=0)),
    textposition='inside',
    insidetextanchor='middle',
)
st.plotly_chart(fig_gantt, use_container_width=True, config={"displayModeBar": False})

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── EDUCATION ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">// Education</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Academic Background</div>', unsafe_allow_html=True)

st.markdown("""
<div class="edu-card">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem;">
        <div>
            <div style="font-size:1.1rem; font-weight:600; color:#e2e8f0;">University of Texas at San Antonio</div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:0.82rem; color:#6366f1; margin-top:0.25rem;">B.S. Computer Science</div>
        </div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.8rem; color:#475569; text-align:right;">
            Aug 2018 — May 2023<br>San Antonio, TX
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">// Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="stat-box" style="cursor:pointer;">
        <div style="font-size:1.6rem; margin-bottom:0.4rem;">✉️</div>
        <div style="font-size:0.82rem; color:#a5b4fc; font-family:'JetBrains Mono',monospace;">krisholmes444@gmail.com</div>
        <div class="stat-label">Email</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="stat-box">
        <div style="font-size:1.6rem; margin-bottom:0.4rem;">📞</div>
        <div style="font-size:0.82rem; color:#a5b4fc; font-family:'JetBrains Mono',monospace;">(832) 647-5192</div>
        <div class="stat-label">Phone</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="stat-box">
        <div style="font-size:1.6rem; margin-bottom:0.4rem;">📍</div>
        <div style="font-size:0.82rem; color:#a5b4fc; font-family:'JetBrains Mono',monospace;">Houston, United States</div>
        <div class="stat-label">Location</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)
