from ursina import raycast, Ursina, Button, color, scene, destroy
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
camera = FirstPersonController()
boxes = []

def input(key):
    hit_info = raycast(camera.world_position, camera.forward, distance=5)
    if hit_info.hit:
        if key == 'left mouse down':
            new_box = Button(
                color=color.white,
                model='cube',
                position=hit_info.entity.position + hit_info.normal,
                texture='grass.png',
                parent=scene,
                origin_y=0.5
            )
            boxes.append(new_box)

        elif key == 'right mouse down':
            if hit_info.entity in boxes:
                boxes.remove(hit_info.entity)
                destroy(hit_info.entity)

app.run()
