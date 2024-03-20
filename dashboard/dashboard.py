import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("dashboard/day.csv")

# Set the page title and layout
st.set_page_config(page_title="Bike Dataset Dashboard", layout="wide")

# Display the header
st.title("We Know Sepedah")

# Add sidebar
st.sidebar.header("Dashboard Sepedah")

# Image display in the sidebar
image_path = "dashboard/logo.jpeg" 
st.sidebar.image(image_path, caption="Sepedah", use_column_width=True)

# Create a mapping for the weathers
weather_map = {1: 'sunny', 2: 'cloudy', 3: 'snow'}

# Map the weathers and create a new DataFrame
df['weather_name'] = df['weathers'].map(weather_map)
weather_analysis = df.groupby('weather_name').agg({
    'count': 'mean',
    'temperature': 'mean'
}).reset_index()

# Create a dropdown menu to select the weather type
weather_filter = st.selectbox("Select a weather type:", weather_analysis['weather_name'])

# Filter the data based on the selected weather type
selected_data = df[df['weather_name'] == weather_filter]

# Display the bar plot for the selected weather type
fig,ax = plt.subplots()
sns.barplot(x='weather_name', y='count', data=selected_data, ax=ax)
plt.title(f'Average Bike Loans for {weather_filter} Weather')
plt.xlabel('Weather')
plt.ylabel('Average Bike Loans')
st.pyplot(fig)

# Preprocessing
df['day_type'] = df['holiday'].apply(lambda x: 'Holiday' if x == 1 else 'Workingday')

# Calculate the average count of bikes for each day type
average_count_by_day_type = df.groupby('day_type')['count'].mean()

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
average_count_by_day_type.plot(kind='bar', color=['orange', 'blue'], ax=ax)
plt.title('Average Bike Count on Holidays and Workingdays')
plt.xlabel('Day Type')
plt.ylabel('Average Bike Count')
plt.xticks(rotation=0)
st.pyplot(fig)
