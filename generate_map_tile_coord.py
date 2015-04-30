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
	(12.9667, 77.5667), #banglore
	(18.5203, 73.8567), #pune
#	(51.54129068713908, -0.09257912635803223), #london
	(19.0906, 72.9090) #mumbai
)

workers = 4
for coordinate in areas_coordinates:
  for zoom in range(7, 19):
    result = deg2num(coordinate[0], coordinate[1], zoom)
    inc_dec_var = 2 + 5*(zoom - 6)
    f.write("render_list -a -n " + str(workers) + " -x " + str(result[0] - inc_dec_var) + " -X " + str(result[0] + inc_dec_var) + " -y " + str(result[1] - inc_dec_var) + " -Y " + str(result[1] + inc_dec_var) + " -z " + str(zoom) + " -Z " + str(zoom) + "\n")
    f.write("render_list -a -n " + str(workers) + " -x " + str(result[0] - inc_dec_var) + " -X " + str(result[0] + inc_dec_var) + " -y " + str(result[1] - inc_dec_var) + " -Y " + str(result[1] + inc_dec_var) + " -z " + str(zoom) + " -Z " + str(zoom) + " -m 'style_retina'\n")

f.close();
