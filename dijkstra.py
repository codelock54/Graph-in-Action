from manim import *


class Dijkstra(Scene):
    def construct(self):
        # Crear los nodos
        nodes = {
            "A": Dot(point=LEFT * 5 + UP * 3, color=BLUE),
            "B": Dot(point=LEFT * 2 + UP * 3, color=BLUE),
            "C": Dot(point=LEFT * 4, color=BLUE),
            "D": Dot(point=ORIGIN, color=BLUE),
            "E": Dot(point=RIGHT * 4, color=BLUE),
            "F": Dot(point=LEFT * 3 + DOWN * 3, color=BLUE),
            "G": Dot(point=RIGHT * 3 + DOWN * 3, color=BLUE),
            "H": Dot(point=RIGHT * 5 + UP * 3, color=BLUE),
        }

        # Crear etiquetas para los nodos
        labels = {name: Tex(name).next_to(dot, UP) for name, dot in nodes.items()}

        # Crear las aristas con pesos (grafo dirigido con pesos)
        edges = [
            ("A", "B", 1),
            ("A", "C", 4),
            ("B", "D", 2),
            ("B", "E", 7),
            ("C", "F", 3),
            ("D", "E", 2),
            ("D", "F", 1),
            ("E", "G", 1),
            ("F", "G", 5),
            ("E", "H", 3),
        ]

        lines = []
        weights = []
        for start, end, weight in edges:
            line = Line(nodes[start].get_center(), nodes[end].get_center(), color=WHITE)
            lines.append(line)
            weight_text = Tex(str(weight)).move_to(
                line.get_center() + 0.3 * (UP + RIGHT)
            )
            weights.append(weight_text)

        title = Text("Algoritmo de Dijkstra", font_size=48)
        self.play(FadeIn(title), run_time=4)
        self.wait(0.5)

        self.play(FadeOut(title))

        # Mostrar los nodos y etiquetas
        self.play(*[Create(dot) for dot in nodes.values()])
        self.play(*[Write(label) for label in labels.values()])

        # Mostrar las aristas y pesos
        self.play(*[Create(line) for line in lines])
        self.play(*[Write(weight) for weight in weights])

      

        self.play(nodes["A"].animate.set_color(RED))
        self.wait(1)

        #  nodo inicial (A)
        distance_label_A = Tex("[-, 0]").next_to(nodes["A"], DOWN).scale(0.7)
        self.play(nodes["A"].animate.scale(1.5), Write(distance_label_A), run_time=0.5)
        self.wait(0.5)

        # Paso 2: Resaltar A -> B (distancia más corta)
        distance_label_B = Tex("[A, 1]").next_to(nodes["B"], DOWN).scale(0.7)
        self.play(
            lines[0].animate.set_color(RED),  # A -> B
            weights[0].animate.set_color(RED),
            Write(distance_label_B),
            run_time=0.5,
        )
        self.wait(0.5)

        # Paso 3: Resaltar A -> C
        distance_label_C = Tex("[A, 4]").next_to(nodes["C"], DOWN).scale(0.7)

        self.play(
            lines[1].animate.set_color(RED),  # A -> C
            weights[1].animate.set_color(RED),
            Write(distance_label_C),
            run_time=0.5,
        )
        self.wait(0.5)

        # Paso 4: Resaltar B -> D
        distance_label_D = Tex("[B, 3]").next_to(nodes["D"], DOWN).scale(0.7)
        self.play(
            lines[2].animate.set_color(RED),  # B -> D
            weights[2].animate.set_color(RED),
            Write(distance_label_D),
            run_time=0.5,
        )
        self.wait(0.5)

        # Paso 5: Resaltar D -> E
        distance_label_E = Tex("[D, 5]").next_to(nodes["E"], DOWN).scale(0.7)
        self.play(
            lines[5].animate.set_color(RED),  # D -> E
            weights[5].animate.set_color(RED),
            Write(distance_label_E),
            run_time=0.5,
        )
        self.wait(0.5)

        # D -> F
        distance_label_f = Tex("[D, 4]").next_to(nodes["F"], DOWN).scale(0.7)
        self.play(
            lines[6].animate.set_color(RED),  # D -> F
            weights[6].animate.set_color(RED),
            Write(distance_label_f),
            run_time=0.5,
        )

        self.wait(0.5)
        #  E -> G
        distance_label_G = Tex("[E, 6]").next_to(nodes["G"], DOWN).scale(0.7)
        self.play(
            lines[7].animate.set_color(RED),
            weights[7].animate.set_color(RED),
            Write(distance_label_G),
            run_time=0.5,
        )
        self.wait(0.5)

        # E -> H
        distance_label_H = Tex("[E, 8]").next_to(nodes["H"], DOWN).scale(0.7)
        self.play(
            lines[9].animate.set_color(RED),
            weights[9].animate.set_color(RED),
            Write(distance_label_H),
            run_time=0.5,
        )
        self.wait(0.5)
        # Finalización

        final_message = Text("Camino más corto calculado.", font_size=36).to_edge(DOWN)
        self.play(Write(final_message))
        self.wait(1)
