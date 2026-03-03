# Kris Holmes — Interactive Resume

A data-focused, interactive portfolio/resume website built with Streamlit and Plotly.

## Stack
- **Framework**: Streamlit (Python)
- **Charts**: Plotly (radar chart, horizontal bar chart, Gantt/timeline)
- **Styling**: Custom CSS injected via st.markdown (dark theme, Inter + JetBrains Mono fonts)

## Structure
- `app.py` — Main Streamlit application (single-file)
- `.streamlit/config.toml` — Server config (port 5000, headless)
- `attached_assets/` — Original resume PDF

## Sections
1. **Hero** — Name, title, bio, contact meta
2. **Stats** — At-a-glance summary boxes
3. **Skills** — Radar chart (capability areas) + horizontal bar chart (tools)
4. **Experience** — Tabbed cards for each role (PowerSchool, Lutron, Cisco Meraki, AmEx)
5. **Career Timeline** — Gantt-style chart showing career progression
6. **Education** — UTSA Computer Science
7. **Contact** — Email, phone, location cards

## Running
```
streamlit run app.py --server.port 5000
```
