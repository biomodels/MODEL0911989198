import os

path = os.path.dirname(os.path.realpath(__file__))
sbmlFilePath = os.path.join(path, 'MODEL0911989198.xml')

with open(sbmlFilePath,'r') as f:
    sbmlString = f.read()

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

if module_exists('libsbml'):
    import libsbml
    sbml = libsbml.readSBMLFromString(sbmlString)