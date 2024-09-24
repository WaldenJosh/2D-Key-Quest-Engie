# __init__.py intialization for the rendering package

from .ncurses_renderer import NcursesRenderer
# from .pygame_renderer import PygameRenderer # @TODO: implement PygameRenderer
from .renderer import Renderer

all = ["NCursesRenderer", "Renderer"]