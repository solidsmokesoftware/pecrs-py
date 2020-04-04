#######
0.034 - 4/4/2020
#######

Major rewrite - Documentation is not up to date
Removed Controller.py, funtionality rolled into Space
Removed Body.py, funtionality moved to Shape
Space now contains most of the relevant data for Shapes to allow Pyglet Sprites to work seamlessly



#######
0.033 - 3/12/2020
#######

Controller.start() renamed to Controller.start_moving()
Controller.stop() renamed to Controller.stop_moving()
Controller.on_start() renamed to Controller.on_start_moving()
Controller.on_stop() renamed to Controller.on_stop_moving()


#######
0.032 - 3/10/2020
#######

Body have been rewritten to extend from Shape instead of having a Shape, in line with the move to make integration with Pyglet seamless.
Space movement methods no longer call Space.update_area(). Instead Controller movement methods call it in order to provide callbacks for collision area changes
StaticBody and AbsBody removed. StaticBody optimization handled by Controller.make() now. Controller.delete() modified to accomidate.
Remove method Controller.make_from()
Change method signature Controller.add() now takes id and static to make working with Pyglet sprites easier.
Remove method Controller.on_add(), doesn't need to be seperate from Controller.on_make() callback
Big documentation expansion


#######
0.031 - 3/8/2020
#######

Remove print statements from Index
Changes to Index to makes it more flexible. Anything can be added now.
Space rewritten to work with Shapes instead of Bodies
Movement methods in the AbsBody moved to the Space
Full set of Shape Collision methods added to Space
Collider methods renamed to reflect that it works with Shapes or primiatives

#######
0.03 - 3/8/2020
#######

Major overhaul.
Vectors are removed and Shapes have been redesigned to work seamlessly with pyglet sprites.
Collider redesigned to work without Vector or Shape types, given better methods for working with Shapes and Bodies.
Space reworked to compensate for the Collider redesign. Methods renamed to match.
Controller reworked to function with the new Space.
Remove constants.py

#######
0.02 - 3/7/2020
#######

Controller now defaults Space to 256, previous no default.
Expand documentation for controller.
New method Controller.resize_space changes the size of the Space and replace.
New method Controller.add_space adds a body to the space.
Remove Controller.factory - This is confusing and not needed for most games, while easy to implement for those that do need it.
Remove Controller.make_key()
Remove Body.key
Remove Body.state - Unused in the base system, easy to implment for users that want it.
Changed method signature Controller.make() now takes a shape allowing it to work with generic bodies instead of subclassed bodies.
Rename method Space.get_body() is now Space.colliding_with()
Rename method Space.get() is now Space.colliding_at()
quickstart.py completely rewritten.
example.py updated to work with changes
test.py updated to work with changes

#######
0.012 - 3/6/2020
#######

Index now keeps track of entities instead of Controller.
Index.get() now retrives an entity instead of an id
Index.next() now retrives a unique id for an entity.
Update test.py to validate new Index.
Small changes to readme.
Some extra print statements removed and version requirements updates, thanks to Slavfox for pointing those out.




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