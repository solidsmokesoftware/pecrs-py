

#######
0.011 - 3/5/2020
#######

Project changing name from pysics to pecrs due to the name already being taken on pypi
Added better support for modules and packing
Added wheel and bdist
Some improvements to readme noting how percs is distinct from other physics engines


#######
0.01
#######

update documentation

vector.py
angle related functions have been changed in name
angleto now angle_rad
angle is same as angleto but converts value to degrees
anglepoint now angle_point
angle now angle_self

controller.py
push(body, x, y) added
on_push(body, x, y) added
moving(body) changed to start(body)
on_moving(body) change to on_start(body)

on_area(body, start) signature changed to include start area
on_place(body, start) signature changed to include start location


body.py
push(x, y) added