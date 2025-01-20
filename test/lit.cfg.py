import lit.formats

config.name = 'Test Suite'
config.test_format = lit.formats.ShTest(True)

config.suffixes = ['.ll'] #.mlir can also be used if need be

config.test_source_root = os.path.dirname(__file__)
config.test_exec_root = os.path.join(config.my_obj_root, 'test')

config.substitutions.append(('%lit-test',
    os.path.join(config.my_obj_root, 'lit-test-tool')))
