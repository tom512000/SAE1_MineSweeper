import unittest
import sys

sys.path.insert(0, "..")

# Inclusion des tests à effectuer

from testCellule import TestCelluleMethods
from testCoordonnee import TestCoordonnee
from testGrilleDemineur import TestGrilleDemineur

if __name__ == '__main__':
    unittest.main()

