import folium #pip install folium 
#this is the library we need to create maps, this package helps us to create interactive maps with python


my_map = folium.Map(location=[12.909561807850984, 77.55010552419766], zoom_start=15) 


folium.Marker(
    [12.909561807850984, 77.55010552419766], 
    popup="<b>school where suresh studied</b><br>best school in the world ",
    tooltip="Click for a tip!",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(my_map) #adding a marker with a popup 


folium.Circle( #here we are adding a circle around the school 
    radius=200, # in meters
    location=[12.909561807850984, 77.55010552419766],
    color='crimson',
    fill=True,
    fill_color='crimson'
).add_to(my_map)


my_map.save("my_travel_map.html") #a html file is created in the current directory you can open in in browser

print(" Map created! Open 'my_travel_map.html' in your browser to see it.")