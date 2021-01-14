import importlib
module = importlib.import_module('fbs_runtime._frozen')
module.BUILD_SETTINGS = {'environment': 'local', 'version': '0.0.0', 'author': 'Eliaz', 'app_name': 'PdfToCSV'}