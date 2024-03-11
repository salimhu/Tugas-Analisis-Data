import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("dashboard/day.csv")
df['date'] = pd.to_datetime(df['date'])

# Streamlit App
st.title("Sepedah Rodalink Dashboard")

# Add sidebar
st.sidebar.header("Dashboard Sepedah")

# Multiselect to choose columns
selected_columns = st.sidebar.multiselect("Select Columns", df.columns)
if selected_columns:
    st.sidebar.write("Selected Columns:")
    st.sidebar.write(selected_columns)
else:
    st.sidebar.write("No columns selected.")

# Image display in the sidebar
image_path = "dashboard/logo.jpeg" 
st.sidebar.image(image_path, caption="Sepedah", use_column_width=True)

# Add filters to the sidebar
selected_season = st.sidebar.selectbox("Select Season", sorted(df['season'].unique()))
selected_month = st.sidebar.selectbox("Select Month", sorted(df['month'].unique()))
selected_weather = st.sidebar.selectbox("Select Weather Situation", sorted(df['weathersit'].unique()))

# Filter the data based on selected options
filtered_data = df[(df['season'] == selected_season) & (df['month'] == selected_month) & (df['weathersit'] == selected_weather)]

# Scatter plot for temperature vs. bike counts
st.subheader("Sepedah and Temperature")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(x='temp', y='count', data=df, ax=ax)
st.pyplot(fig)

# Line chart for daily bike counts
st.subheader("Sepedah Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='date', y='count', data=df, ax=ax)
st.pyplot(fig)

# Bar chart for bike counts by season
st.subheader("Sepedah by Season")
season_counts = df.groupby('season')['count'].sum()
fig, ax = plt.subplots()
season_counts.plot(kind='bar', ax=ax)
st.pyplot(fig)
