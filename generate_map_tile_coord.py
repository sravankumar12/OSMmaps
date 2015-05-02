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
	(19.0906, 72.9090), #mumbai
	(22.5667, 88.3667), #kolkata
	(25.2048, 55.2708), #kolkata
	(-42.0000, 174.0000) #new zealand
)

workers = 2
for coordinate in areas_coordinates:
  for zoom in range(7, 19):
    result = deg2num(coordinate[0], coordinate[1], zoom)
    inc_dec_var = 2 + 7*(zoom - 6)
    min_x = 0 if (result[0] - inc_dec_var < 0) else result[0] - inc_dec_var 
    min_y = 0 if (result[1] - inc_dec_var < 0) else result[1] - inc_dec_var
    max_tile_val = 2**zoom - 1
    max_x = max_tile_val if (result[0] + inc_dec_var > max_tile_val) else result[0] + inc_dec_var 
    max_y = max_tile_val if (result[1] + inc_dec_var > max_tile_val) else result[1] + inc_dec_var 

    f.write("render_list -a -n " + str(workers) + " -x " + str(min_x) + " -X " + str(max_x) + " -y " + str(min_y) + " -Y " + str(max_y) + " -z " + str(zoom) + " -Z " + str(zoom) + "\n")
    f.write("render_list -a -n " + str(workers) + " -x " + str(min_x) + " -X " + str(max_x) + " -y " + str(min_y) + " -Y " + str(max_y) + " -z " + str(zoom) + " -Z " + str(zoom) + " -m 'style_retina'\n")

f.close();
