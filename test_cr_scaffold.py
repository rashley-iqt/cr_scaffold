import os
import shutil
import pytest
from cr_scaffold import create_dev_files

name = "test_project"
directory = "./not_default"
extension = "go"
test_prefix = "Test"

def setUp():
    return

def tearDown():
    shutil.rmtree(directory)

def test_transform():
    setUp()

    try:
        create_dev_files(name, directory, extension, test_prefix, False)
        proj_path = "{0}/{1}".format(directory, name)
        df_path = "{0}/Dockerfile".format(proj_path)
        reqs_path = "{0}/requirements.txt".format(proj_path)
        op_path = "{0}/{1}.{2}".format(proj_path, name, extension)
        test_path = "{0}/{1}{2}.{3}".format(proj_path, test_prefix,name, extension)

        assert os.path.exists(proj_path) and os.path.isdir(proj_path)
        assert os.path.exists(df_path) and os.path.isfile(df_path)
        assert os.path.exists(reqs_path) and os.path.isfile(reqs_path)
        assert os.path.exists(op_path) and os.path.isfile(op_path)
        assert os.path.exists(test_path) and os.path.isfile(test_path)
    finally:
        tearDown()
