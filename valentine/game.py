from ursina import Animation, Sky, camera, Ursina

app = Ursina()

me = Animation(
    'assets/anjo',  # Verifique se o arquivo existe e o caminho está correto
    collider='box',
    y=5
)

sky = Sky()  # Crie uma instância de Sky

camera.orthographic = True
camera.fov = 20

app.run()
