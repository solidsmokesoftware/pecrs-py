========
Overview
========

Base types of the system are Shapes and Bodies. 
Shapes have a position and dimensions which describe its physical properties.
Bodies are Shapes with an id, direction, speed, and movement state.

Core functionality is providied by the Collider, which detects collisions between Shapes or Shape-like Objects.

The Space handles positioning of Shapes and optimizes collision handling.

The Controller provides high-level object oriented control over Bodies in a Space. 