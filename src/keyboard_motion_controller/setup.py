from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['keyboard_motion_controller'],
   scripts=['scripts/node_keyboard_motion_controller.py'],
   package_dir={'':'src'}
)

setup(**d)
