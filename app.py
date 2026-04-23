import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Uber NYC Data Science Project", layout="wide")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        border: 1px solid #eeeeee;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🚖 Uber NYC Pulse: Urban Demand Analysis")
st.subheader("A Data Science Project by Basak")

# --- STRATEGIC OVERVIEW ---
with st.expander("📊 View Strategic Executive Summary", expanded=True):
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Core Algorithm", "Temporal Aggregation")
        st.caption("Grouping 1M+ raw timestamps into hourly bins.")
    with col_b:
        st.metric("Key Metric", "Hourly Trip Density (HTD)")
        st.caption("Measuring market pressure and supply-demand gaps.")
    with col_c:
        st.metric("Top Insight", "Evening Surge (17:00)")
        st.caption("Highest revenue potential identified in the 16:00-19:00 window.")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    try:
        # Load data
        data = pd.read_csv('uber-raw-data-sep14.csv')
        data['Date/Time'] = pd.to_datetime(data['Date/Time'])
        data['Hour'] = data['Date/Time'].dt.hour
        data['DayOfWeek'] = data['Date/Time'].dt.day_name()
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

# --- MAIN CONTENT BLOCK ---
if df is not None:
    st.divider()
    
    # ROW 1: BAR AND PIE
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### **Demand Pulse by Hour**")
        hourly_data = df.groupby('Hour').size().reset_index(name='Total Trips')
        fig = px.bar(hourly_data, x='Hour', y='Total Trips', 
                     color='Total Trips', color_continuous_scale='Magma',
                     template='plotly_white')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### **Top Dispatch Bases**")
        base_data = df['Base'].value_counts().reset_index()
        fig_pie = px.pie(base_data, values='count', names='Base', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    # ROW 2: SUNBURST (THE NEW SECTION)
    st.divider()
    st.markdown("### ☀️ Journey Hierarchy: Day, Hour, and Base")
    st.write("Interactively explore the relationship between the time of day and dispatch activity.")
    
    # Pre-aggregating for the Sunburst to ensure high performance
    sun_data = df.groupby(['DayOfWeek', 'Hour', 'Base']).size().reset_index(name='Trips')
    
    fig_sun = px.sunburst(
        sun_data,
        path=['DayOfWeek', 'Hour', 'Base'],
        values='Trips',
        color='Trips',
        color_continuous_scale='RdBu',
        template='plotly_white'
    )
    st.plotly_chart(fig_sun, use_container_width=True)

    # ROW 3: THE RACING BAR SECTION
    st.divider()
    st.markdown("### 🎬 The Race: Cumulative Hourly Growth")
    st.info("This animation demonstrates the 'Hourly Trip Density' evolution across NYC's dispatch bases.")
    
    video_path = 'uber_race.mp4'
    if os.path.exists(video_path):
        with open(video_path, 'rb') as video_file:
            st.video(video_file.read())
    else:
        st.warning("Video file 'uber_race.mp4' not found.")

# --- SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.title("Project Info")
st.sidebar.write("**Student:** Basak")
st.sidebar.write("**Focus:** Data Science Transition")
st.sidebar.write("**Dataset:** 1M+ NYC Uber Pickups")