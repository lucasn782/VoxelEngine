import numpy as np


class BaseMesh:
    def __init__(self):
        # Contexto OpenGL
        self.ctx = None
        # programa shader
        self.program = None
        # formato de tipo de dados do buffer de vértice: "3f 3f"
        self.vbo_format = None
        # nomes de atributos de acordo com o formato: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        # objeto de matriz de vértices
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()












































