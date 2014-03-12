
from lxml import etree
import requests
import webbrowser
from jinja2 import Template

#Funcion que devuelve la cardinalidad del viento:

def direcc_viento (cadena):
		if cadena >= 337.5 and cadena >=0 or cadena < 22.5:
				return "N"
		if cadena >= 22.5 and cadena <= 67.5:
				return "N.E"
		if cadena >= 67.5 and cadena < 112.5:
				return "E"
		if cadena >= 112.5 and cadena < 157.5:
				return "S.E"
		if cadena >= 157.5 and cadena < 202.5:
				return "S"
		if cadena >= 202.5 and cadena < 247.5:
				return "S.O"
		if cadena >= 247.5 and cadena < 292.5:
				return "O"
		if cadena >= 292.5 and cadena < 337.5:
				return "NO"

nombre_ciudades = {'Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla'}
url="http://api.openweathermap.org/data/2.5/weather?"

f_tiempo = open('weather1.html','w')
temp_min = []
temp_max = []
velocidad_viento = []
direccion = []
capital = []


#provincias = nombre_ciudades.values()

	#print respuesta.url
for provincia in nombre_ciudades:
	diccionario_params = {"q":provincia, "mode":"xml","units":"metric","lang":"es"}
	capital.append(provincia)
	respuesta = requests.get(url,params=diccionario_params)
	#codificacion = respuesta.text.encode('utf-8')
	arbol = etree.fromstring(respuesta.text.encode("utf-8"))
	temperature = arbol.find("temperature")
	wind_speed = arbol.find("wind/speed")
	velocidad_viento.append(wind_speed.attrib["value"])
	wind_direction = arbol.find("wind/direction")
	direccion.append(wind_direction.attrib["code"])
	#print velocidad_viento
	#print direccion
#Temperatura se muestra en grados celcius:	
	temp_min.append(temperature.attrib["min"])
	temp_max.append(temperature.attrib["max"])
	
	#print temp_min
#print ciudad

f = open('plantilla.html','r')
html= ''

for linea in f:
	html += linea

mi_template = Template(html)

mi_template = Template(html)
salida = mi_template.render(nombre_ciudades=capital, temperatura_min=temp_min, temperatura_max=temp_max, viento_velocidad=velocidad_viento, viento_direccion= direccion)

f_tiempo.write(salida)
webbrowser.open("weather1.html")	
