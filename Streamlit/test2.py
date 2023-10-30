# import streamlit as st
# from streamlit.components.v1 import components
# import folium
# from folium import plugins

# # Define the coordinates for Colombia and Canada
# colombia_coords = (4.5709, -74.2973)  # Bogota, Colombia
# canada_coords = (56.1304, -106.3468)  # Center of Canada

# # Create a folium map centered between the two coordinates
# m = folium.Map(
#     location=[(colombia_coords[0] + canada_coords[0]) / 2, (colombia_coords[1] + canada_coords[1]) / 2],
#     zoom_start=3
# )

# # Add markers for Colombia and Canada
# folium.Marker(location=colombia_coords, popup='Colombia').add_to(m)
# folium.Marker(location=canada_coords, popup='Canada').add_to(m)

# # Draw a line connecting the two points
# folium.PolyLine([colombia_coords, canada_coords], color="blue").add_to(m)

# # Render the Folium map as an HTML iframe
# folium_map = components.html(m._repr_html_(), height=600)

# # Display the map using st.components.v1.iframe
# st.markdown("Connecting Colombia to Canada")
# st.components.v1.html(folium_map)
