import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
  # Replace with the actual URL or file path
df = pd.read_csv("dashboard/day.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# Streamlit App
st.title("Bike Sharing Dashboard")

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
selected_month = st.sidebar.selectbox("Select Mnth", sorted(df['mnth'].unique()))
selected_weather = st.sidebar.selectbox("Select Weather Situation", sorted(df['weathersit'].unique()))

# Filter the data based on selected options
filtered_data = df[(df['season'] == selected_season) & (df['mnth'] == selected_month) & (df['weathersit'] == selected_weather)]

# Scatter plot for temperature vs. bike counts
st.subheader("Scatter Plot: Temperature vs. Bike Counts")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(x='temp', y='cnt', data=df, ax=ax)
st.pyplot(fig)

# Line chart for daily bike counts
st.subheader("Daily Bike Counts Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='dteday', y='cnt', data=df, ax=ax)
st.pyplot(fig)

# Bar chart for bike counts by season
st.subheader("Bike Counts by Season")
season_counts = df.groupby('season')['cnt'].sum()
fig, ax = plt.subplots()
season_counts.plot(kind='bar', ax=ax)
st.pyplot(fig)
