from app.my_app import MyApp
from app.data_handler import DataHandler
from app.problem_handler import ProblemHandler
from app.file_storage import FileStorage
import sys
from shapes.circle import Circle
from shapes.cone import Cone
from shapes.cuboid import Cuboid
from shapes.cylinder import Cylinder
from shapes.ellipse import Ellipse
from shapes.minecraft import Minecraft
from shapes.oval import Oval
from shapes.pentagon import Pentagon
from shapes.rectangle import Rectangle
from shapes.rhombus import Rhombus
from shapes.sphere import Sphere
from shapes.semicircle import Semicircle
from shapes.square import Square 
from shapes.triangle import Triangle


def main():
    paths = {
        "geometric_shape_path": "config_paths/config_gs_path.json",
    }

    input_shape = sys.argv[1]

    storage = FileStorage(paths["geometric_shape_path"])
    data_handler = DataHandler(storage)
    problem_handler = None

    if input_shape == "circle":
        problem_handler = ProblemHandler(Circle())
    elif input_shape == "cone":
        problem_handler = ProblemHandler(Cone())
    elif input_shape == "cuboid":
        problem_handler = ProblemHandler(Cuboid())
    elif input_shape == "cylinder":
        problem_handler = ProblemHandler(Cylinder())
    elif input_shape == "ellipse":
        problem_handler = ProblemHandler(Ellipse())
    elif input_shape == "minecraft":
        problem_handler = ProblemHandler(Minecraft())
    elif input_shape == "oval":
        problem_handler = ProblemHandler(Oval())
    elif input_shape == "pentagon":
        problem_handler = ProblemHandler(Pentagon())
    elif input_shape == "rectangle":
        problem_handler = ProblemHandler(Rectangle())
    elif input_shape == "rhombus":
        problem_handler = ProblemHandler(Rhombus())
    elif input_shape == "sphere":
        problem_handler = ProblemHandler(Sphere())
    elif input_shape == "semicircle":
        problem_handler = ProblemHandler(Semicircle())
    elif input_shape == "square":
        problem_handler = ProblemHandler(Square)
    elif input_shape == "triangle":
        problem_handler = ProblemHandler(Triangle)
    else:
        print("Invalid input shape.")

    myapp = MyApp(data_handler, problem_handler)

    myapp.run()

main()
