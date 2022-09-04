import math
from PIL import Image

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    
    def sub(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Sphere:
    def __init__(self, c, r, color):
        self.centro = c
        self.raio = r
        self.color = color
    
    def intersecao(self, observador, d):
        co = observador.sub(self.centro)

        a = d.dot(d)
        b = 2 * co.dot(d)
        c = co.dot(co) - self.raio * self.raio 

        delta = b * b - 4 * a * c
        if(delta < 0):
            return math.inf, math.inf

        t1 = (-b + math.sqrt(delta)) / 2 * a
        t2 = (-b - math.sqrt(delta)) / 2 * a
        
        return (t1, t2)
        
class Viewport:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.distance = d

class Canvas:
    def __init__(self, w, h, vp, bg):
        self.width = w
        self.height = h
        self.viewport = vp
        self.bg_color = bg
        self.dx = vp.width/w
        self.dy = vp.height/h
    
    def canvasToViewport(self, x, y):
        return Vector(-self.viewport.width/2.0 + self.dx/2.0 + y*self.dx, 
                       self.viewport.height/2.0 - self.dy/2.0 - x * self.dy, 
                       -self.viewport.distance)


class Scene:
    def __init__(self, spheres, v_camera, canva):
        self.spheres = spheres
        self.v_camera = v_camera
        self.canva = canva

    def traceRay(self, d, t_min, t_max):
        closest_t = math.inf

        closest_sphere = None

        for sphere in self.spheres:
            [t1, t2] = sphere.intersecao(self.v_camera, d)
            if((t1 >= t_min and t1 <= t_max) and t1 < closest_t):
                closest_t = t1
                closest_sphere = sphere

            if((t2 >= t_min and t2 <= t_max) and t2 < closest_t):
                closest_t = t2
                closest_sphere = sphere
            
        if(closest_sphere == None):
            return self.canva.bg_color
        return closest_sphere.color



vp = Viewport(2.0, 2.0, 2.0) # tela
canva = Canvas(500, 500, vp, Color(100, 100, 100))

s_red = Sphere(Vector(0, 0, -(vp.distance + 1)), 1, Color(255, 0, 0))
s_blue = Sphere(Vector(1, 0, -(vp.distance + 1)), 1, Color(0, 0, 255))
s_green = Sphere(Vector(-2.2, 0, -(vp.distance + 1)), 1, Color(0, 255, 0))

spheres = [s_red, s_green, s_blue]
scene = Scene(spheres, Vector(0, 0, 0), canva)

image = Image.new(mode="RGB", size=(canva.width, canva.height))
pixels = image.load()

for x in range(canva.width):
    for y in range(canva.height):
        d = canva.canvasToViewport(x, y)
        color = scene.traceRay(d, 1.0, math.inf)
        pixels[y, x] = (color.r, color.g, color.b)

image.save("out.png", format="png")
image.show()