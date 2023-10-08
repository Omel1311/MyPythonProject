import folium

from branca.element import Figure
fig=Figure(width=550,height=350)

m1=folium.Map(width=750,height=650,location=[28.644800, 77.216721],zoom_start=11,min_zoom=8,max_zoom=14)
fig.add_child(m1)

m1.save('map1.html')

fig2=Figure(width=550,height=350)
m2=folium.Map(location=[46.490112794568745, 30.75785493984088])
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)
m2.save('map2.html')