import pyfiglet
from emoji import emojize

__project__ = 'pitrix'
__version__ = "0.0.18"
__description__ = f"{__project__}是一个测试工具，可以帮助您更轻松地编写pytest用例!"
__image__ = emojize(f"""{pyfiglet.figlet_format(text=__project__, font='starwars')}{__description__}:fire::fire::fire:\nversion:{__version__}""")
