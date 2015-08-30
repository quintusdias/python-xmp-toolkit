import pkg_resources as pkg

_file = pkg.resource_filename(__name__, 'test1.xmp')
with open(_file) as f:
    test1 = f.read()
