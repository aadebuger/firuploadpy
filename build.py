
from pybuilder.core import use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.pydev")
use_plugin("python.pycharm")
use_plugin("python.distutils")


name = "firuploadpy"
default_task = "publish"



