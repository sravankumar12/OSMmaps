import math
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)


f = open('render_map_gen_file.sh', 'w')

areas_coordinates = (
	(28.6200, 77.3200), #delhi
	(28.6200, 77.3200) #delhi
)

for coordinate in areas_coordinates:
  for zoom in range(7, 17):
    result = deg2num(coordinate[0], coordinate[1], zoom)
    inc_dec_var = 2 + 4*(zoom - 6)
    f.write("render_list -a -n 5 -x " + str(result[0] - inc_dec_var) + " -X " + str(result[0] + inc_dec_var) + " -y " + str(result[1] - inc_dec_var) + " -Y " + str(result[1] + inc_dec_var) + " -z " + str(zoom) + " -Z " + str(zoom) + "\n")

f.close();
