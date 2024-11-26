from manim import *

class Kruskal(Scene):
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
            ("A", "C", 3),
            ("B", "D", 4),
            ("B", "E", 8),
            ("C", "F", 5),
            ("D", "E", 4),
            ("D", "F", 2),
            ("E", "G", 3),
            ("F", "G", 2),
            ("E", "H", 6),
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

        title = Text("Algoritmo de Kruskal", font_size=48)
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

        # Pesos 1 
        self.play(
            lines[0].animate.set_color(RED),
            weights[0].animate.set_color(RED),
            run_time=0.5,
        )
        self.wait(0.5)

         # Pesos 2
        self.play(
            lines[6].animate.set_color(RED),
            weights[6].animate.set_color(RED),

            lines[8].animate.set_color(RED),
            weights[8].animate.set_color(RED),

            run_time=0.5,
        )
        self.wait(1)


         # Pesos 3
        self.play(
            lines[1].animate.set_color(RED),
            weights[1].animate.set_color(RED),

            lines[7].animate.set_color(RED),
            weights[7].animate.set_color(RED),

            run_time=0.5,
        )
        self.wait(1)

         # Pesos 4
        self.play(
            lines[2].animate.set_color(RED),
            weights[2].animate.set_color(RED),
            run_time=0.5,
        )
        self.wait(1)

         # Pesos 6
        self.play(
            lines[-1].animate.set_color(RED),
            weights[-1].animate.set_color(RED),
            run_time=0.5
        )
        self.wait(1)

        # Finalización

        final_message = Text("Arbol de Expansion Minimo.", font_size=36).to_edge(DOWN)
        self.play(Write(final_message))
        self.wait(1)