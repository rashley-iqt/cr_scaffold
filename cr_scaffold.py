import os
import sys
import argparse

def create_dockerfile(path, name, extension):
    df_path = "{0}/Dockerfile".format(path)
    with open(df_path, "w") as df:
        with open("dockerfile.template", "r") as template:
            template_lines = template.readlines()
            for line in template_lines:
                to_write = line.replace("$NAME",name).replace("$EXTENSION", extension)
                df.write(to_write)
    return

def create_dev_files(name, directory, extension, test_prefix, include_vent_template):
    print ("{0}:{1}:{2}:{3}".format(name, directory, extension, test_prefix))
    full_path = "{0}/{1}".format(directory, name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    #create a basic dockerfile based off of a template
    create_dockerfile(full_path, name, extension)
    #generate requirements.txt
    rqts = "{0}/requirements.txt".format(full_path)
    with open(rqts, "w") as r:
        r.write("")

    #generate the "operational files" i.e. a python script file and unit test files
    op_file = "{0}/{1}.{2}".format(full_path, name, extension)
    with open(op_file, "w") as of:
        of.write("")
    test_file = "{0}/{1}{2}.{3}".format(full_path, test_prefix,name, extension)
    with open(test_file, "w") as tf:
        tf.write("")

    vt = "{0}/vent.template".format(full_path)
    if include_vent_template :
        with open(vt, "w") as vtf:
            vtf.write("")

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="cr scaffolding script")
    parser.add_argument('name' , action='store', metavar="PROJECT_NAME", help="the name of the project directory to create")
    parser.add_argument('-directory','--directory', '-d', '--d', action='store', dest="directory", metavar="DIRECTORY",
                            default="./", help="the name of the directory in which to create the project, default is ./")
    parser.add_argument('-extension','--extension', '-e', '--e', action='store', dest="extension", metavar="EXTENSION",
                            default="py", help="the extension (without the .) to use for code files, default is py")
    parser.add_argument('-test-prefix','--test-prefix', '-tp', '--tp', action='store', dest="test_prefix", metavar="TEST_PREFIX",
                            default="test_", help="the prefix used to indicate unit test files, default is test_")
    opts = parser.parse_args()

    create_dev_files(opts.name, opts.directory, opts.extension, opts.test_prefix, False)
