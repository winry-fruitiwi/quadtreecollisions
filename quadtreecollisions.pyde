# Winry/Tigrex, 8/28/21
# From Daniel Shiffman, translated from p5.js to Processing Python
# Copied some quadtree code from my quadtree sketch. With hundreds of particles
# collisions take a long time, but quadtrees make the framerate higher!
# version comments:
#
# v0.00:  Only version comments
# v0.01:  Program shell, paste three old classes
# v0.0 :  Add collision checks and Particle class, then experience the framerate
# v0.0 :  tweak everything to use quadtrees
# v0.0 :  possibly make quadtrees more efficient without re-initialization?

from Quadtree import *
from primitives import *

def setup():
    global qt, particles
    colorMode(HSB, 360, 100, 100, 100)
    size(700, 700)
    background(220, 79, 35)
    
    # qt = Quadtree(Rectangle(0, 0, width, height), 4) # test initialization. Does not work!
    
    # particles is our main representation
    particles = []  

    # let's fill our pockets and lists with particle objects! Woo!
    for i in range(1000):
        particles.append(Particle(random(100, width - 100), random(100, height - 100)))


def draw():
    global qt, particles
    qt = Quadtree(Rectangle(0, 0, width, height), 4) # reinitiate the quadtree every frame
    background(220, 79, 35)
    points = []
    # create points from our particles list each frame for our quadtree
    for particle in particles:
        points.append(Point(particle.x, particle.y, particle))
    
    # add every point to the quadtree
    for particle_point in points:
        qt.insert(particle_point)
    
    # goes through all the particles in the particle array.
    for particle in particles:
        
        # the radius of the boundary
        R = 20
        # we want to think about only the points that are around the
        # particle point
        query_boundary = Rectangle(particle.x - R/2.0, particle.y-R/2.0, R, R)
        # now we query using the query boundary, and find a bunch of points.
        queried_points = qt.query(query_boundary)
        
        for other_point in queried_points:
            # print "Ohio boundary!" # test. TODO: figure out why
            # a print statement is so taxing on framerate
            # same as last time, just with a different name
            other_particle = other_point.data
            if particle.intersects(other_particle) and particle != other_particle:
                particle.highlight()
        
    for particle in particles:
        # "update" the particle with move and show it with render
        particle.move()
        particle.render()
        particle.reset()
    
    # this helps the reader compare performance with and without a quadtree.
    # For reference, non-quadtree collision is 4 frames per second while
    # quadtree collisions are from 35-40 frames per second
    textSize(15)
    text(frameRate, 10, 30)
