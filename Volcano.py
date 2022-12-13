"""
Class: CS230--Section 1
Name: Finn Power
Description: Final Project, Volcano Dataset
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import pandas as pd
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import random
from PIL import Image
import folium
from streamlit_folium import st_folium
from emoji import emojize
import wikipedia

img = Image.open('volcano.jpg')
st.set_page_config(page_title="Finn's Fabulous Volcano Website", page_icon=img)

st.markdown((emojize(":volcano:" * 32)))


def display_description():
    st.subheader('Background')
    volcano_summary = wikipedia.summary("Volcano", sentences=2)
    return volcano_summary


def display_maps_one(df):
    df2 = df[['Latitude', 'Longitude']].copy()
    df2 = df2.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
    return df2


def display_maps_two(df, country):
    df2 = df[['Country', 'Latitude', 'Longitude', 'Volcano Name']].copy()
    df2 = df2.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
    df2.set_index('Country', inplace=True)
    df2 = df2.loc[country]
    st.subheader('Dataframe of Selected Country: ')
    st.write(df2)
    st.subheader("Map of Selected Country's Volcanic Eruptions")
    df3 = df2.reset_index(drop=True)
    m = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)
    for i in range(0, len(df3)):
        folium.Marker(
            location=[df3.iloc[i]['lat'], df3.iloc[i]['lon']], popup=(df3.iloc[i]['Volcano Name'],
                                                                      'Top Five wikipedia '
                                                                      'results: ',
                                                                      (wikipedia.search(
                                                                          df3.iloc[i]['Volcano Name'], results=5)))

        ).add_to(m)
    return m


def condition_panda(df, country):
    df2 = df[(df.Country == country) & (df['Activity Evidence'] != 'Evidence Uncertain') & (df['Last Known Eruption']
                                                                                            != 'Unknown')]
    st.subheader(f"Dataframe of {country}'s eruptions excluding where eruption evidence is uncertain or last eruption "
                 f"is unknown ")
    df2.sort_values('Volcano Name', inplace=True)
    st.write(df2)


def chart_one(df):
    counts = df['Region'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(range(len(counts[0:])), counts[0:], color='g')
    ax.set_xlabel('Region of Eruption')
    ax.set_title('Number of Eruptions in Each Region')
    ax.set_xticks((range(len(counts[0:]))))
    ax.set_xticklabels(counts.index[0:], rotation='vertical')
    st.pyplot(fig)


def chart_two(df):
    df2 = df[['Primary Volcano Type', 'Dominant Rock Type']].copy()
    volcano_type = st.sidebar.radio('For Chart Two: Which Volcano Type would you like to learn about', [
        'Stratovolcano', 'Caldera', 'Shield'
    ])
    if 'Stratovolcano' in volcano_type:
        df2.set_index('Primary Volcano Type', inplace=True)
        df2 = df2.loc['Stratovolcano']
        counts = df2['Dominant Rock Type'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(range(len(counts[0:])), counts[0:], color='purple')
        ax.set_xlabel('Dominant Rock type')
        ax.set_title('Count of Each Rock Type for a Stratovolcano')
        ax.set_xticks((range(len(counts[0:]))))
        ax.set_xticklabels(counts.index[0:], rotation='vertical')
        st.pyplot(fig)

    if 'Caldera' in volcano_type:
        df2.set_index('Primary Volcano Type', inplace=True)
        df2 = df2.loc['Caldera']
        counts = df2['Dominant Rock Type'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(range(len(counts[0:])), counts[0:], color='purple')
        ax.set_xlabel('Dominant Rock type')
        ax.set_title('Count of Each Rock Type for a Caldera')
        ax.set_xticks((range(len(counts[0:]))))
        ax.set_xticklabels(counts.index[0:], rotation='vertical')
        st.pyplot(fig)
    if 'Shield' in volcano_type:
        df2.set_index('Primary Volcano Type', inplace=True)
        df2 = df2.loc['Shield']
        counts = df2['Dominant Rock Type'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(range(len(counts[0:])), counts[0:], color='purple')
        ax.set_xlabel('Dominant Rock type')
        ax.set_title('Count of Each Rock Type for a Shield')
        ax.set_xticks((range(len(counts[0:]))))
        ax.set_xticklabels(counts.index[0:], rotation='vertical')
        st.pyplot(fig)


def add(dict):
    number = random.randint(390848, 390999)
    break_out = False
    for n in dict:
        for i in dict[n]:
            if i == number:
                st.write('Sorry, website under maintenance: system needs administrative update on number '
                         'generator '
                         ' \n PLEASE DO NOT FILL OUT PAGE UNTIL ERROR IS REMOVED')
                break_out = True
                break
            else:
                continue
        if break_out:
            break

    st.title('Add New/Missing Eruption Information')
    st.subheader('For complete entry, fill out all boxes')
    name = st.text_input('Enter Volcano Name: ')
    dict['Volcano Name'][number] = name
    country = st.text_input('Enter Country Containing Volcano: ')
    dict['Country'][number] = country
    type = st.text_input('Enter Primary Volcano Type: ')
    dict['Primary Volcano Type'][number] = type
    evidence = st.text_input('Enter Activity Evidence: ')
    dict['Activity Evidence'][number] = evidence
    eruption_time = st.text_input('Enter Last Known Eruption: ')
    dict['Last Known Eruption'][number] = eruption_time
    region = st.text_input('Enter Region of Eruption: ')
    dict['Region'][number] = region
    subregion = st.text_input('Enter Subregion of Eruption: ')
    dict['Subregion'][number] = subregion
    lat = st.number_input('Enter Latitude of Volcano: ')
    dict['Latitude'][number] = lat
    lon = st.number_input('Enter Longitude of Volcano: ')
    dict['Longitude'][number] = lon
    elevation = st.number_input('Enter Elevation of Volcano: ')
    dict['Elevation (m)'][number] = elevation
    rock_type = st.text_input('Enter Dominant Rock Type: ')
    dict['Dominant Rock Type'][number] = rock_type
    tectonic_setting = st.text_input('Enter Tectonic Setting: ')
    dict['Tectonic Setting'][number] = tectonic_setting
    return dict


def chart_three(df):
    elevation_df = df['Elevation (m)'].values
    point = elevation_df[-1]
    data = [elevation_df, point]
    st.caption('Dataframes from Volcano Elevations')
    st.write(np.sort(elevation_df)[::-1])
    fig, ax = plt.subplots()
    ax.boxplot(data, vert=False, showmeans=True)
    ax.set_title('Box and Whisker Plot of Elevation of Volcanoes')
    ax.set_xlabel('Distribution of Elevation')
    ax.set_yticklabels(['Plot of All Data', 'Newly Added Elevation Point'])
    st.pyplot(fig)


def main():
    df = pd.read_csv("Volcano.csv", header=1, index_col=0)
    dict = df.to_dict()
    selected = option_menu(
        menu_title='Volcano Main Menu',
        options=['Home Page', 'Maps', 'Charts', 'Page Contributions'],
        icons=['globe', 'map', 'chart'],
        menu_icon="cast",
        default_index=0,
        orientation='horizontal',
    )
    if selected == 'Home Page':
        st.title('Welcome to My Website on Volcanoes')
        st.image('volcanoes.jpg')
        description = display_description()
        st.write(description)
        display = display_maps_one(df)
        st.subheader("Map of Selected Country's Volcanic Eruptions")
        st.map(display)
        st.markdown((emojize(":volcano:" * 32)))
    if selected == 'Charts':
        st.subheader('Chart 1: ')
        chart_one(df)
        st.subheader('Chart 2: ')
        chart_two(df)
        st.markdown((emojize(":volcano:" * 32)))
    if selected == 'Maps':
        country = st.text_input('Enter a country you wish to display data for: ')
        if country in df['Country'].values:
            display = display_maps_two(df, country)
            st_folium(display, width=725)
            condition_panda(df, country)
            st.markdown((emojize(":volcano:" * 32)))

    if selected == 'Page Contributions':
        new_dict = add(dict)
        new_df = pd.DataFrame(new_dict)
        st.caption('New Eruption Entered by User')
        st.write(new_df.tail(1))
        chart_three(new_df)
        st.markdown((emojize(":volcano:" * 32)))


hide_menu_style = """
    <style>
    footer {visibility: hidden; }
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

main()
