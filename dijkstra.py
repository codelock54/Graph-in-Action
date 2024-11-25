from manim import *


class Dijkstra(Scene):
    def construct(self):
        # Crear los nodos
        A = Dot(point=LEFT * 3, color=BLUE)
        B = Dot(point=RIGHT * 3, color=BLUE)
        C = Dot(point=DOWN * 2 + LEFT * 2, color=BLUE)
        D = Dot(point=DOWN * 2 + RIGHT * 2, color=BLUE)

        # Crear las etiquetas para los nodos
        label_A = Tex("A").next_to(A, LEFT)
        label_B = Tex("B").next_to(B, RIGHT)
        label_C = Tex("C").next_to(C, DOWN * 2 + LEFT * 2)
        label_D = Tex("D").next_to(D, DOWN * 2 + RIGHT * 2)

        # Crear las aristas con pesos
        edge_AB = Line(A.get_center(), B.get_center(), color=WHITE)
        edge_BC = Line(B.get_center(), C.get_center(), color=WHITE)
        edge_CD = Line(C.get_center(), D.get_center(), color=WHITE)
        edge_AD = Line(A.get_center(), D.get_center(), color=WHITE)

        # Crear los pesos de las aristas
        weight_AB = Tex("4").move_to(edge_AB.get_center() + UP * 0.5)
        weight_BC = Tex("2").move_to(edge_BC.get_center() + RIGHT * 0.5)
        weight_CD = Tex("3").move_to(edge_CD.get_center() + DOWN * 0.5)
        weight_AD = Tex("1").move_to(edge_AD.get_center() + LEFT * 0.5)

        # Mostrar los nodos y las aristas
        self.play(Create(A), Create(B), Create(C), Create(D))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(edge_AB), Create(edge_BC), Create(edge_CD), Create(edge_AD))
        self.play(
            Write(weight_AB), Write(weight_BC), Write(weight_CD), Write(weight_AD)
        )

        # Realizar la animación del algoritmo Dijkstra
        # Explicar el algoritmo de Kruskal
        # self.wait(1)
        self.play(FadeIn(Text("Algoritmo de Dijkstra", font_size=48).shift(UP * 3)))
        self.wait(1)

        # Iniciar en el nodo A
        self.play(A.animate.scale(1.5), run_time=0.5)
        self.wait(0.5)

        # Resaltar la arista A -> B
        self.play(
            edge_AB.animate.set_color(RED),
            weight_AB.animate.set_color(RED),
            run_time=0.5,
        )
        self.wait(0.5)

        # Resaltar la arista A -> D
        self.play(
            edge_AD.animate.set_color(RED),
            weight_AD.animate.set_color(RED),
            run_time=0.5,
        )
        self.wait(0.5)

        # Resaltar la arista B -> C
        self.play(
            edge_BC.animate.set_color(RED),
            weight_BC.animate.set_color(RED),
            run_time=0.5,
        )
        self.wait(0.5)

        # Resaltar la arista C -> D
        self.play(
            edge_CD.animate.set_color(RED),
            weight_CD.animate.set_color(RED),
            run_time=0.5,
        )
        self.wait(0.5)

        # Finalizar
        self.wait(1)
