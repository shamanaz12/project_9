import streamlit as st
import requests

st.title("🌍 Multi-Language Country Information Cards")

# User se country ka naam kisi bhi language me lene ke liye input box
country_name = st.text_input("Enter Country Name (English, Russian, German, etc.)", "Россия")  # Default: Russia in Russian

if st.button("Get Info"):
    api_url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            country_data = response.json()[0]

            # Country ka flag aur basic info
            flag_url = country_data["flags"]["png"]
            st.image(flag_url, width=200)

            st.header(country_data["name"]["common"])
            st.subheader(f"🌎 Region: {country_data['region']}")
            st.subheader(f"🗺️ Subregion: {country_data['subregion']}")
            st.subheader(f"📍 Capital: {', '.join(country_data.get('capital', ['N/A']))}")
            st.subheader(f"👨‍👩‍👦 Population: {country_data['population']:,}")
            st.subheader(f"📏 Area: {country_data['area']} km²")

            # Languages
            languages = ', '.join(country_data["languages"].values())
            st.subheader(f"🗣️ Languages: {languages}")

        else:
            st.error("Country not found! Please enter a valid country name.")

    except Exception as e:
        st.error("Error fetching data!")

