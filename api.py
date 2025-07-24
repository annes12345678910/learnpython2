import pygame
from Box2D.b2 import world as b2World, polygonShape, dynamicBody, staticBody

# Constants
PPM = 20.0  # pixels per meter
TIME_STEP = 1.0 / 60
VEL_ITERS, POS_ITERS = 6, 2

class PhysicsWorld:
    def __init__(self, gravity=(0, -10)):
        self.world = b2World(gravity=gravity, doSleep=True)
        self.bodies = []

    def step(self):
        self.world.Step(TIME_STEP, VEL_ITERS, POS_ITERS)

    def create_box(self, pos, size, dynamic=True):
        body_type = dynamicBody if dynamic else staticBody
        body = self.world.CreateBody(
            position=(pos[0] / PPM, pos[1] / PPM),
            type=body_type,
        )
        body.CreatePolygonFixture(box=(size[0] / 2 / PPM, size[1] / 2 / PPM), density=1, friction=0.3)
        self.bodies.append(body)
        return body

    def draw(self, screen):
        for body in self.bodies:
            for fixture in body.fixtures:
                shape = fixture.shape
                vertices = [(body.transform * v) * PPM for v in shape.vertices]
                vertices = [(v[0], screen.get_height() - v[1]) for v in vertices]  # flip y
                pygame.draw.polygon(screen, (0, 0, 255), vertices, 1)


class Wait:
    def __init__(self):
        self.timers = []

    def wait(self, seconds, callback):
        end_time = pygame.time.get_ticks() + int(seconds * 1000)
        self.timers.append((end_time, callback))

    def update(self):
        now = pygame.time.get_ticks()
        for timer in self.timers[:]:
            if now >= timer[0]:
                timer[1]()  # call the function
                self.timers.remove(timer)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    physics_world = PhysicsWorld()
    waiter = Wait()
    def on_wait_complete():
        print("Wait complete!")
    waiter.wait(2, on_wait_complete)

    # Create a static ground box
    physics_world.create_box((400, 100), (800, 50), dynamic=False)
    # Create a dynamic box
    physics_world.create_box((400, 300), (50, 50), dynamic=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        waiter.update()
        physics_world.step()
        screen.fill((255, 255, 255))
        physics_world.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()