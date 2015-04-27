#!/bin/bash

#-----------------Delhi-------------------------------

echo "Rendering styles for delhi::::::::::"
echo "Default Styles"
./render_list-rect.pl 10 728 734 425 428 10 13 -n 5
./render_list-rect.pl 14 11687 11731 6819 6849 14 15 -n 5
./render_list-rect.pl 16 46793 46891 27286 27410 16 17 -n 5
echo "Retina Styles"
./render_list-rect.pl 10 728 734 425 428 10 13 -n 5 -m 'style_retina'
./render_list-rect.pl 14 11687 11731 6819 6849 14 17 -n 5 -m 'style_retina'
./render_list-rect.pl 16 46793 46891 27286 27410 16 17 -n 5 -m 'style_retina'







#slower ones:
./render_list-rect.pl 7 90 95 51 57 7 9 -n 5
./render_list-rect.pl 7 90 95 51 57 7 9 -n 5 -m 'style_retina'






#render_list -a -n 5 -x 49 -X 110 -y 50 -Y 68 -z 7 -Z 7
#render_list -a -n 5 -x 89 -X 210 -y 100 -Y 128 -z 8 -Z 8
#render_list -a -n 5 -x 89 -X 210 -y 100 -Y 128 -z 8 -Z 8 -m 'style_retina'
#render_list -a -n 5 -x 169 -X 410 -y 200 -Y 248 -z 9 -Z 9
#render_list -a -n 5 -x 169 -X 410 -y 200 -Y 248 -z 9 -Z 9 -m 'style_retina'
#render_list -a -n 5 -x 697 -X 829 -y 405 -Y 500 -z 10 -Z 10
#render_list -a -n 5 -x 697 -X 829 -y 405 -Y 500 -z 10 -Z 10
#render_list -a -n 5 -x 1400 -X 1660 -y 810 -Y 1000 -z 11 -Z 11
#render_list -a -n 5 -x 1400 -X 1660 -y 810 -Y 1000 -z 11 -Z 11
#render_list -a -n 5 -x 2924 -X 2935 -y 1706 -Y 1712 -z 12 -Z 12
#render_list -a -n 5 -x 2924 -X 2935 -y 1706 -Y 1712 -z 12 -Z 12
#render_list -a -n 5 -x 5840 -X 5865 -y 3399 -Y 3430 -z 13 -Z 13
#render_list -a -n 5 -x 5840 -X 5865 -y 3399 -Y 3430 -z 13 -Z 13
#render_list -a -n 5 -x 11683 -X 11747 -y 6792 -Y 6849 -z 14 -Z 14
#render_list -a -n 5 -x 11683 -X 11747 -y 6792 -Y 6849 -z 14 -Z 14
#render_list -a -n 5 -x 23364 -X 23491 -y 13587 -Y 13697 -z 15 -Z 15
#render_list -a -n 5 -x 23364 -X 23491 -y 13587 -Y 13697 -z 15 -Z 15
#render_list -a -n 5 -x 46226 -X 46980 -y 27173 -Y 27392 -z 16 -Z 16
#render_list -a -n 5 -x 46226 -X 46980 -y 27173 -Y 27392 -z 16 -Z 16
#render_list -a -n 5 -x 93426 -X 93980 -y 54173 -Y 54792 -z 17 -Z 17
#render_list -a -n 5 -x 93426 -X 93980 -y 54173 -Y 54792 -z 17 -Z 17
