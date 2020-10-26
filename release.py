import sys
import configparser
from functools import partial
from subprocess import check_call as _call

call = partial(_call, shell=True)


def main():
    part = sys.argv[1]
    call("bumpversion %s --allow-dirty --no-tag --no-commit" % part)
    config = configparser.ConfigParser()
    config.read(".bumpversion.cfg")
    version = config.get("bumpversion", "current_version")
    call("docker build -t snn-demo:%s ." % version)


if __name__ == "__main__":
    main()
