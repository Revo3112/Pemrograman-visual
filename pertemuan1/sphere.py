# import math
# from OpenGL.GL import *
# from OpenGL.GLU import *  # Import GLU
# import glfw  # Import GLFW

# def calculate_volume(radius):
#   return (4/3) * math.pi * radius**3

# def generate_triangles(radius, num_triangles):
#   vertices = []
#   for i in range(num_triangles):
#     theta = 2 * math.pi * i / num_triangles
#     phi = math.acos(-1 + 2 * i / num_triangles)
#     x = radius * math.sin(phi) * math.cos(theta)
#     y = radius * math.sin(phi) * math.sin(theta)
#     z = radius * math.cos(phi)
#     vertices.append((x, y, z))

#   triangles = []
#   for i in range(num_triangles):
#     triangles.append((i, (i + 1) % num_triangles, (i + 2) % num_triangles))

#   return vertices, triangles


# def display(vertices, triangles, window):  # Add window as a parameter
#   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#   # Gambar mesh bola
#   glBegin(GL_TRIANGLES)
#   for triangle in triangles:
#     for vertex in triangle:
#       x, y, z = vertices[vertex]
#       glVertex3f(x, y, z)
#   glEnd()

#   glfw.swap_buffers(window)  # Use glfw.swap_buffers instead of glfwSwapBuffers

# def reshape(width, height):
#   glViewport(0, 0, width, height)

#   glMatrixMode(GL_PROJECTION)
#   glLoadIdentity()
#   gluPerspective(45, width / height, 1.0, 100.0)

#   glMatrixMode(GL_MODELVIEW)
#   glLoadIdentity()

# def main():
#   # Use GLFW for window creation, initialization, and event handling
#   glfw.init()  # Use glfw.init instead of glfwInit
#   window = glfw.create_window(500, 500, "Visualisasi Bola", None, None)  # Use glfw.create_window instead of glfwCreateWindow
#   glfw.make_context_current(window)  # Use glfw.make_context_current instead of glfwMakeContextCurrent

#   vertices, triangles = generate_triangles(1.0, 100)  # Panggil fungsi generate_triangles

#   # Set warna latar belakang
#   glClearColor(0.2, 0.3, 0.3, 1.0)

#   # Aktifkan pencahayaan
#   glEnable(GL_LIGHTING)

#   # Set sumber cahaya
#   glLightfv(GL_LIGHT0, GL_POSITION, (0.5, 0.5, 1.0, 1.0))
#   glEnable(GL_LIGHT0)

#   # Set material bola
#   glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.8, 0.8, 0.8, 1.0))

#   # Loop pemrosesan utama
#   while not glfw.window_should_close(window):  # Use glfw.window_should_close instead of glfwWindowShouldClose
#     glfw.poll_events()  # Use glfw.poll_events instead of glfwPollEvents
#     display(vertices, triangles, window)  # Pass vertices, triangles, and window as arguments to display()

#   glfw.terminate()  # Use glfw.terminate instead of glfwTerminate

# if __name__ == "__main__":
#   main()




# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# def generate_sphere(radius, num_points):
#     u = np.linspace(0, 2 * np.pi, num_points)
#     v = np.linspace(0, np.pi, num_points)
#     x = radius * np.outer(np.cos(u), np.sin(v))
#     y = radius * np.outer(np.sin(u), np.sin(v))
#     z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
#     return x, y, z

# def main():
#     radius = 100
#     num_points = 1000
#     x, y, z = generate_sphere(radius, num_points)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(x, y, z, color='b', alpha=0.5)

#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     ax.set_title('Visualisasi Bola')

#     plt.show()

# if __name__ == "__main__":
#     main()

