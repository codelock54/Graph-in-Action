from manim import *

class Kruskal(Scene):
    def construct(self):
        # Definir los vértices
        vertices = [
            Dot(color=WHITE).shift(UP * 2 + LEFT * 3),
            Dot(color=WHITE).shift(UP * 2 + RIGHT * 3),
            Dot(color=WHITE).shift(DOWN * 2 + LEFT * 2),
            Dot(color=WHITE).shift(DOWN * 2 + RIGHT * 2)
        ]

        # Definir las aristas del grafo (sin peso)
        edges = [
            Line(vertices[0].get_center(), vertices[2].get_center(), color=WHITE),
            Line(vertices[0].get_center(), vertices[3].get_center(), color=WHITE),
            Line(vertices[1].get_center(), vertices[2].get_center(), color=WHITE),
            Line(vertices[1].get_center(), vertices[3].get_center(), color=WHITE),
            Line(vertices[2].get_center(), vertices[3].get_center(), color=WHITE)
        ]

        # Crear las etiquetas de los vértices
        labels = [
            Tex("A").next_to(vertices[0], LEFT),
            Tex("B").next_to(vertices[1], RIGHT),
            Tex("C").next_to(vertices[2], LEFT),
            Tex("D").next_to(vertices[3], RIGHT)
        ]

        # Mostrar los vértices, aristas y etiquetas
        self.play(LaggedStart(*[Create(v) for v in vertices], lag_ratio=0.5))
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.5))
        self.play(LaggedStart(*[Write(l) for l in labels], lag_ratio=0.5))

        # Explicar el algoritmo de Kruskal
        self.wait(1)
        self.play(FadeIn(Text("Algoritmo de Kruskal", font_size=48).shift(UP * 3)))

        # Mostrar la lista de aristas ordenadas por peso
        aristas_ordenadas = [
            "A-B: 1", "B-D: 3", "A-D: 4", "C-D: 5", "A-C: 6"
        ]
        texto_aristas = VGroup(*[
            Tex(f"{arista}").shift(DOWN * i) for i, arista in enumerate(aristas_ordenadas)
        ])

        self.play(FadeIn(texto_aristas))
        self.wait(2)

        # Seleccionar las aristas que conforman el árbol de expansión mínima (MST)
        selected_edges = [
            Line(vertices[0].get_center(), vertices[1].get_center(), color=BLUE),
            Line(vertices[1].get_center(), vertices[3].get_center(), color=BLUE),
            Line(vertices[0].get_center(), vertices[3].get_center(), color=BLUE)
        ]

        # Asegurarse de que las aristas seleccionadas coincidan en cantidad con las aristas a transformar
        self.play(LaggedStart(*[Transform(edges[i], selected_edges[i]) for i in range(len(selected_edges))], lag_ratio=0.5))
        self.wait(2)

        # Finalizar la escena
        self.play(FadeOut(texto_aristas), FadeOut(*vertices), FadeOut(*edges), FadeOut(*labels))
