import matplotlib.pyplot as plt

class display_2d:
    def __init__(self):
        self.x = []
        self.y = []
        self.colors = []

    def extract_points(self, space_all):
        for i, space in enumerate(space_all):
            shape_coords = [space[0], space[1], space[2], space[3], space[0]]
            self.x += [coord[0] for coord in shape_coords]
            self.y += [coord[1] for coord in shape_coords]
            self.colors += [i] * len(shape_coords)

        # Add extra points for the lines
        self.x += [0]
        self.y += [0]
        self.colors += [i+1]

    def create_and_display_plot(self):
        fig, ax = plt.subplots()
        for i, color in enumerate(['blue', 'red', 'green', 'purple']):
            idx = [j for j, c in enumerate(self.colors) if c == i]
            ax.plot([self.x[j] for j in idx], [self.y[j] for j in idx], color=color)
            ax.fill_between([self.x[j] for j in idx], [self.y[j] for j in idx], color=color, alpha=0.3)
        plt.show()

    # def get_current_axis_limits():
    #     xmin, xmax = ax.get_xlim()
    #     ymin, ymax = ax.get_ylim()

    # def get_space_min_max():
    #     min_x = min(x)
    #     max_x = max(x)
    #     min_y = min(y)
    #     max_y = max(y)

    # def set_new_axis_limits():
    #     ax.set_xlim([min_x - max_graph_size[0], max_x + max_graph_size[0] + 2])
    #     ax.set_ylim([min_y - max_graph_size[1], max_y + max_graph_size[1] + 2])
