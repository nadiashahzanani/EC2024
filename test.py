import streamlit as st
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Genetic Algorithm", divider="gray")



# --- Mock Data Setup (Replace with your actual data loading/processing) ---
# Assuming 'arts_df' is a pandas DataFrame and 'Gender' is a column in it.
# This section creates dummy data that mimics the output of arts_df['Gender'].value_counts()
data = {'Gender': ['Female', 'Male', 'Female', 'Non-binary', 'Male', 'Female', 'Male', 'Female']}
arts_df = pd.DataFrame(data)
# -------------------------------------------------------------------------

# Calculate the counts, equivalent to gender_counts = arts_df['Gender'].value_counts()
gender_counts = arts_df['Gender'].value_counts()
labels = gender_counts.index
values = gender_counts.values

# Create the Plotly figure
fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    # autopct='%1.1f%%' equivalent in Plotly is using 'textinfo' and 'hovertemplate'
    # textinfo='percent+label', # Option to show percentage and label on the slice
    # hovertemplate='%{label}<br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
    hole=.3 # Optional: Makes it a donut chart for a slightly different look
)])

# Update the layout for the title
fig.update_layout(
    title_text='Distribution of Gender in Arts Faculty',
    # Ensure a good aspect ratio/size
    autosize=False,
    width=600,
    height=600,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    )
)

# Display the figure in Streamlit using st.plotly_chart
st.title("Arts Faculty Gender Distribution Analysis")
st.plotly_chart(fig, use_container_width=True)
