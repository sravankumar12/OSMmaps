import math
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)


f = open('render_map_gen_file.sh', 'w')


# These are country coordinates, min max along the disagonals.
# Useing these coordinates, we find the the tiles details which are to be generated.
# 	Format: 'country_id': (left most, top most coordinate), (rightmost, bottom most coordinate)
#country_coordinates = {
#        '216': ((50.272162, -129.689119), (24.342626, -61.661778)), #USA
#	'217': ((-10.611348, 111.250221), (-44.648631, 157.129125)) #Australia
#}

 
# These are simple city's center coordinates.
# Using these coordinates, we create tiles around the place
areas_coordinates = (
	(28.6200, 77.3200), #delhi
	(12.9667, 77.5667), #banglore
	(18.5203, 73.8567), #pune
	(13.0827, 80.2707), #chennai
#	(51.54129068713908, -0.09257912635803223), #london
	(-37.8136, 144.9631), #259 - melbourne
	(-33.8650, 151.2094), #260 - sydney
	(-34.9260000000000000, 138.6000000000000000), #297 - Adelaide
	(-26.2044, 28.0456), #johannesburg
	(25.2950000000000000, 51.5200000000000000),#62 - Doha
	(6.9350000000000000, 79.8610000000000000), #58 - Colombo
	(39.9276420000000000, 32.8283160000000000), #60 - Ankara
	(32.7829400000000000, -96.8001940000000000), #Dallas - 276
	(29.7631700000000000, -95.3625870000000000), #Houston - 277
	(30.2667480000000000, -97.7417600000000000), #Austin - 278
	(47.6057700000000000, -122.3294370000000000), #Seattle - 279
	(40.7146300000000000, -74.0058060000000000), #New York City - 280
	(34.0521700000000000, -118.2434690000000000), #Los Angeles - 281
	(36.1741790000000000, -115.1353300000000000), #Las Vegas - 282
	(38.8952220000000000, -77.0367580000000000), #Washington DC - 283
	(42.3315090000000000, -83.0460210000000000), #Detroit - 285
	(45.5238300000000000, -122.6753460000000000), #Portland - 286
	(39.9515500000000000, -75.1637730000000000), #Philadelphia - 287
	(49.2807216950000000, -123.1177491154000000), #256 - Metro Vancouver
	(-31.9570000000000000, 115.8560000000000000), #296 - Perth
	(-36.8484200000000000, 174.7633700000000000), #70 - Auckland
	#(-38.2029710000000000, 145.2324770000000000), #1518 - Pearcedale
	(-41.2864570000000000, 174.7762470000000000), #71 - Wellington
	(-27.4680000000000000, 153.0280000000000000), #298 - Brisbane
	(41.0089210000000000, 28.9731530000000000), #59 - Istanbul
	(49.2000000000000000, 16.6167000000000000), #93 - Brno
	(33.7486570000000000, -84.3877110000000000), #Atlanta - 288
	(42.3580280000000000, -71.0604170000000000), #Boston - 289
	(29.9543900000000000, -90.0751190000000000), #New Orleans - 290
	(25.7741110000000000, -80.1935650000000000), #Miami - 291
	(41.8498380000000000, -87.6481930000000000), #Chicago - 292
	(33.4472010000000000, -112.0731660000000000), #Phoenix - 301
	(32.7157100000000000, -117.1564790000000000), #San Diego - 302
	(35.2272300000000000, -80.8429720000000000), #Charlotte - 303
	(29.4238890000000000, -98.4932100000000000), #San Antonio - 304
	(39.7391090000000000, -104.9839170000000000), #Denver - 305
	(37.7742000000000000, -122.4170680000000000), #San Francisco - 306
	(33.6690000000000000, -117.8220000000000000), #Orange County - 484
	(36.6897029971181000, -121.6467643371760100), #Monterey Bay - 487
	(38.5813600000000000, -121.4930420000000000), #Sacramento - 499
	(36.7477490000000000, -119.7725300000000000), #Fresno - 514
	(33.9505239674185000, -117.4061205338350000), #Inland Empire - 520
	(41.7650000000000000, -72.6830000000000000), #Hartford, Connecticut - 544
	(41.2983190000000000, -72.9286000000000000), #New Haven - 550
	(41.0627088370166000, -73.5365738950277000), #Fairfield County - 553
	(43.6274990000000000, -79.3961670000000000), #89 - Toronto
	(-33.4679734000000000, 151.3899264167000000), #2125 - Kincumber
	(52.2333000000000000, 21.0167000000000000), #109 - Warsaw
	(-35.2864000000000000,149.1170000000000000), #Canberra ACT - 313
	(-42.8800000000000000,147.3300000000000000), #Tasmania - 314
	(-28.0127584846000000,153.4185337923000000), #Gold Coast - 2555
	(-33.8720000000000000,18.4320000000000000), #Cape Town - 64
	(19.0906, 72.9090), #mumbai
	(22.5667, 88.3667), #kolkata
	(25.2048, 55.2708), #dubai
	(24.4667, 54.3667), #Abu dhabi
	(38.728611, -9.184722), #Lisboa
	(-42.0000, 174.0000), #new zealand
	(14.5833, 121.0000), #metro manila
	(-6.1745, 106.8227), #jakarta
	(48.148246, 17.107073), #brastilava
	(50.083333, 14.416667) #prague
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
