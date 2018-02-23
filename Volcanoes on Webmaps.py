
# coding: utf-8

# In[4]:


import folium
import pandas as pd
data = pd.read_csv("C:/Users/lalit/Desktop/Numpy_Pandas_code/volcano_database.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
nam = list(data["Name"])
elev = list(data["Elevation (Meters)"])
def color_picker(elev):
    if elev<1000:
        return 'green'
    elif 1000<=elev<=2000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.09,-99.09],zoom_start=5,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,nm,el in zip(lat,lon,nam,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(str(nm)+", Elevation (Meters):"+str(el)+"m",parse_html=True),radius=7,color='grey',fill_color=color_picker(el),fill=True,fill_opacity=0.9))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save('C:/Users/lalit/Desktop/Numpy_Pandas_code/volcano_Map1.html')

