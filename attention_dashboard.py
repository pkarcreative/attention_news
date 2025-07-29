import pandas as pd
import streamlit as st
import geopandas as gpd
from streamlit_folium import folium_static
import folium
from datetime import datetime
import plotly.express as px
import numpy as np
st.set_page_config(layout="wide")
#left_column, right_column = st.columns(2)

show = 1
attention_yes = pd.read_csv("attention_OpenAI_yes.csv")
attention_yes.loc[980, "Justification"] = "This article is relvant."



default_date = datetime(2023, 10, 13)
min_date = datetime(2020, 1, 1)
start_date_max = datetime(2023, 10, 12)
max_date = datetime(2023, 10, 23)

start_date = st.sidebar.date_input("Start Date", min_value=min_date, value= min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=max_date, value=default_date )

if end_date < start_date:
    st.warning("Warning: The End date should not be earlier than the Start date. Please adjust your selection.")
    show = 0

start_date_title = start_date
end_date_title = end_date    

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)  

df = attention_yes
    
df['Date'] = pd.to_datetime(df['Date'])
df_yes = df[df["Decision"]=="Yes"]
df_yes = df_yes[(df_yes['Date'] >= start_date) & (df_yes['Date'] <= end_date)]   

if len(df_yes)<1:
    st.warning("Warning: Data not available for the specified date range. Please adjust your selection.")
    show = 0

if show == 1:    
    st.title(f"News for Attention Measurement in Advertising in the date range: {start_date_title} to {end_date_title}")
    
 
    #further filtering data
    df = df[~df["Justification"].isna()].reset_index(drop=True)

    df["Country"] = df["Country"].replace("unitedstates", "United States of America")
    df["Country"] = df["Country"].replace("unitedkingdom", "United Kingdom")
    df["Country"] = df["Country"].replace("australia", "Australia")
    df["Country"] = df["Country"].replace("canada", "Canada")
    df["Country"] = df["Country"].replace("singapore", "Singapore")
    df["Country"] = df["Country"].replace("japan", "Japan")   
    df["Country"] = df["Country"].replace("mexico", "Mexico") 
    df["Country"] = df["Country"].replace("hongkong", "Hong Kong") 
                      
    coulmns_to_keep = ["URL", "Date", "Country", "Title", "Text", "Decision", "Justification"]
    df = df[coulmns_to_keep]
    def convert_to_year_month_date(datetime_str):
        datetime_obj = pd.to_datetime(datetime_str)
        return datetime_obj.strftime('%Y-%m-%d')
    
    df['Date'] = pd.to_datetime(df['Date'])
    df_yes = df[df["Decision"]=="Yes"]
    df_yes = df_yes[(df_yes['Date'] >= start_date) & (df_yes['Date'] <= end_date)]
    df_yes['Date'] = df_yes['Date'].apply(convert_to_year_month_date)
    country_counts = df_yes["Country"].value_counts().reset_index()
    country_counts.columns = ['Country', 'count']
    fig = px.pie(country_counts, values='count', names='Country', title='')
    #fig.update_layout(showlegend=False)
  
    
    
    
    # Sample data (replace this with your own GeoDataFrame)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    # Sample dataset with country names and values
    data = {'name': country_counts["Country"].values,
            'value': country_counts["count"].values}
    df = pd.DataFrame(data)
    
    # Merge the data
    world_data = world.merge(df, left_on='name', right_on='name')
    

    
    # Set up your Streamlit app
    
    
    # Define a color scale based on the 'value' column
    color_scale = folium.LinearColormap(colors=['green', 'yellow', 'red'], index=[df['value'].min(), df['value'].mean(), df['value'].max()], vmin=df['value'].min(), vmax=df['value'].max())
    #legend_ranges = [0, 10, 20, 30, 40, 50, 60]  # Adjust the ranges as needed
    #colors = ['green', 'yellow', 'orange', 'red', 'purple', 'blue']
    #color_scale = folium.LinearColormap(colors=colors, index=legend_ranges)
    # Create a map with color intensity based on 'value' and highlight countries from 'data'
    
    m = folium.Map(location=[0, 0], zoom_start=1, width=695)


    
    
    # Add a GeoJSON layer to the map that contains information about each country
    folium.GeoJson(
        world_data,
        name='geojson',
        tooltip=folium.features.GeoJsonTooltip(fields=['name', 'value'], aliases=['Country', 'Value']),
        style_function=lambda x: {
            'fillColor': color_scale(x['properties']['value']),
            'color': 'black',
            'weight': 1,
            'dashArray': '5, 5'
        },
        highlight_function=lambda x: {
            'fillColor': 'yellow',
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        }
    ).add_to(m)
    
    
    
    # Add a click event to the GeoJSON layer that displays the relevant information about the clicked country on the bottom of the page
    folium.features.GeoJson(
        world_data,
        name='clickgeojson',
        tooltip=folium.features.GeoJsonTooltip(fields=['name', 'value'], aliases=['Country', 'Value']),
        style_function=lambda x: {
            'fillColor': color_scale(x['properties']['value']),
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        },
        highlight_function=lambda x: {
            'fillColor': 'yellow',
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        },
        control=False,
        show=False,
        smooth_factor=0
    ).add_to(m)
    
    color_scale.add_to(m)
    
    # Show the map
    #left_column, middle, right_column, third_column = st.columns([2,0.5,2,0.5])  # Adjust the column widths as needed
    #with right_column:
    st.markdown("<p style='font-size: 29px; font-weight: bold;'>Geographical heatmap of news</p>", unsafe_allow_html=True)
    folium_static(m)
    
    #with left_column:
        # Add other content to the right column

    # Use st.markdown to set font size with HTML
    st.markdown("<p style='font-size: 29px; font-weight: bold;'>Percentage of news</p>", unsafe_allow_html=True)

    #st.title("Percentage of news per considered countries")
    st.plotly_chart(fig)
        
    options = country_counts["Country"].values
    # Create a dropdown box in Streamlit
    
    selected_option = st.selectbox('**Select a source country of news:**', options)
    st.write(f'**You selected: {selected_option}**')
    
    st.markdown(f'**Data for {selected_option}:**')
    
    st.markdown('**Data Format: Date | Title of the news article with the corresponding web link  embedded | AI-generated abstract of the article.**')
    
    # Adjust the width and height to cover maximum space
    
    #st.markdown('<a href="https://www.google.com" target="_blank">Google</a>', unsafe_allow_html=True)
    
    
    df_yes['HTML Link'] = df_yes.apply(lambda row: f'<a href="{row["URL"]}" target="_blank">{row["Title"]}</a>', axis=1)
    #st.write(df_yes, unsafe_allow_html=True)
    #st.write(df_yes[['HTML Link']])
    # Display the DataFrame without index
    #st.write(df_yes[df_yes["Country"]==selected_option], unsafe_allow_html=True)
    
    country_date_data=df_yes[df_yes["Country"]==selected_option]
    
    country_date_data = country_date_data[["HTML Link", "Date", "Justification"]].reset_index(drop=True)
    
    #st.markdown(tt[0], unsafe_allow_html=True)
    rows_per_page = 10
    total_pages = int(round(len(country_date_data)/rows_per_page))
    page_number = st.number_input(f"**Page Number; Total pages: {total_pages}**", min_value=1)
    
    
    # Calculate the start and end indices for the current page
    start_index = (page_number - 1) * rows_per_page
    end_index = min(start_index + rows_per_page, len(country_date_data))
    
    
    
    # Display rows for the current page
    #for index in range(start_index, end_index):
        #st.write(f"Date: {tt.loc[index, 'Date']}")
        #st.markdown(tt.loc[index, "HTML Link"], unsafe_allow_html=True)
    for index in range(start_index, end_index):
        st.markdown(f"{country_date_data.loc[index,'Date']} |{country_date_data.loc[index, 'HTML Link']} | {country_date_data.loc[index,'Justification']}", unsafe_allow_html=True)
        st.markdown("---")
    
    






