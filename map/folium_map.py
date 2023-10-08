import folium
# 'Stamen Terrain
# Stamen Toner
# Stamen Water Color
# CartoDB Positron
m = folium.Map(location=[46.49018537408449, 30.74506642710343], zoom_start=15, tiles="CartoDB Positron")
e = 12
Cicon = folium.features.CustomIcon('20200803_201816.jpg', icon_size=(50,50))

folium.Marker([46.490112794568745, 30.75785493984088],
              popup="<h1>  e </h1><img src='20200803_201816.jpg' width=400px><p>this os port facilites</p>",
              tooltip='Портовий оператор',
              # icon=folium.Icon(icon='heart', icon_color='red', color='green')).add_to(m)
              icon=Cicon).add_to(m)



folium.Circle(
    location=(46.49031216260478, 30.75236956479633),
    radius=800,
    popup='район порта тест',
    color = 'blue',
    fill = True,
    fill_colour = 'blue').add_to(m)



m.save('map.html')