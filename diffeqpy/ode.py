import os
import sys

from julia import Main

script_dir = os.path.dirname(os.path.realpath(__file__))
Main.include(os.path.join(script_dir, "setup.jl"))

from julia import OrdinaryDiffEq
sys.modules[__name__] = OrdinaryDiffEq   # mutate myself
