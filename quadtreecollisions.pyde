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
    global particles, qt
    colorMode(HSB, 360, 100, 100, 100)
    size(700, 700)
    background(220, 79, 35)
    particles = []
    for i in range(300):
        particles.append(Particle(random(20, width - 20), random(20, height - 20)))


def draw():
    global particles, qt
    background(220, 79, 35)
    for particle in particles:
        for other in particles:
            if particle.intersects(other) and particle != other:
                particle.highlight()
            
        particle.move()
        particle.render()
