#!/bin/sh
cd ~/OSM/

#download Complete OSM file and its checksum
wget http://planet.openstreetmap.org/pbf/planet-latest.osm.pbf.md5
wget http://planet.openstreetmap.org/pbf/planet-latest.osm.pbf

#run for checksum error
#md5sum -c planet-latest.osm.pbf.md5

if [ $(md5sum -c planet-latest.osm.pbf.md5) != "OK" ];then
  exit 1
fi


#Command to import osm to pgsql database
# --create tells osm2pgsql to create new tables rather than appending to existing tables. Creating new tables is the default.
# --slim tells osm2pgsql to create slim tables to store data while importing rather than trying to store everything in memory.
#    --slim is also necessary if we want to update the data
# --cache 14000 causes 14000 MB of memory to be allocated as a cache for node positions.
#     Having the node positions cached means that there are fewer reads from the database and constructing way geometries is much faster. 
# --hstore causes tags not in the .style file to be stored in a special hstore column. Hstore is a key-value store that supports arbitrary keys and values. 
#     Having other tags in hstore allows changes later on, like rendering names in a specific language and overall makes the database more flexible, giving you greater freedom to      render interesting data on maps you create.

osm2pgsql --create --slim --cache 1000 --number-processes 2 --hstore ~/OSM/planet-latest.osm.pbf

touch /var/lib/mod_tile/planet*

sudo /etc/init.d/apache2 restart

export LC_ALL="en_US.UTF-8"

sudo /etc/init.d/renderd restart
