import os
import sys

def parse_opts(args):
    options = {}
    while len(args) > 1:
        print("{0}:{1}".format(args[0], args[1]))
        if args[0].startswith('-') :
            options[args[0][1:]] = args[1]
            if len(args) >= 2:
                args = args[1:]
        elif args[0].startswith('--') :
            options[args[0][2:]] = args[1]
            if len(args) >= 2:
                args = args[1:]
        else :
            raise ValueError("Invalid option specified")
    return options

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
    print(sys.argv[1:])
    opts = parse_opts(sys.argv[1:]) #we don't need the script name

    if "name" in opts :
        name = opts["name"]
    elif "n" in opts:
        name = opts["n"]
    else:
        raise KeyError("the name flag is required")

    directory = "./"
    if "directory" in opts:
        directory = opts["directory"]
    elif "d" in opts:
        directory = opts["d"]

    extension = "py"
    if "extension" in opts:
        extension = opts["extension"]
    elif "e" in opts:
        extension = opts["e"]

    test_prefix = "test_"
    if "test-prefix" in opts:
        test_prefix = opts["test-prefix"]
    elif "tp" in opts:
        test_prefix = opts["tp"]

    create_dev_files(name, directory, extension, test_prefix, False)
