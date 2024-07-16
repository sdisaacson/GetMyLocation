import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Get My Current Location")

# JavaScript to get the current location using HTML5 Geolocation
st.markdown(
    """
    <script>
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const coords = {lat: latitude, lon: longitude};
            document.getElementById("coords").innerText = JSON.stringify(coords);
            document.getElementById("lat").value = latitude;
            document.getElementById("lon").value = longitude;
        },
        function() {
            document.getElementById("coords").innerText = "Geolocation not supported or denied.";
        }
    );
    </script>
    """,
    unsafe_allow_html=True
)

# Hidden input fields to store coordinates
latitude = st.text_input("Latitude", "", key="lat")
longitude = st.text_input("Longitude", "", key="lon")

if latitude and longitude:
    # Convert to float
    lat = float(latitude)
    lon = float(longitude)

    # Create a map centered around the current location
    map_location = folium.Map(location=[lat, lon], zoom_start=14)
    folium.Marker(location=[lat, lon], popup="You are here!").add_to(map_location)

    # Render the map in Streamlit
    st_folium(map_location, width=725)
else:
    st.write("Please allow location access to see your current location on the map.")
