import os
import sys

# Add project root (parent of tests/) to sys.path so tests can import top-level modules
tests_dir = os.path.dirname(__file__)
project_root = os.path.dirname(tests_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
