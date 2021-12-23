#!/usr/bin/env python

import sys
import logging
import subprocess

def check_dependencies():
    """
    Check all dependencies exist and work
    """
    missing=False
    for program in ['rgi database -v', "clinker -h"]:
        try:
            output = subprocess.run(program, shell=True, check=True,
                    stdout=subprocess.PIPE, encoding='utf-8')
            logging.debug(f"Tool {program} is installed: {output.stdout}")
        except:
            logging.error(f"Tool {program} is not installed")
            missing = True

    if missing:
        logging.error("One or more dependencies are missing please install")
        sys.exit(1)
    else:
        logging.debug("All dependencies found")


def initialise(args):
    """
    Starts logging and configures output directory
    """

    # set up output dir name if it isn't specified using timestamp
    if not args.output_dir:
        output_dir = Path("results_{int(time.time())}")
        run_name = output_dir.name
    else:
        output_dir = Path(args.output_dir)
        run_name = args.output_dir.name

    # start logging
    if args.debug or args.verbose:
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=logging.DEBUG,
                            handlers=[logging.FileHandler(f"{run_name}.log"),
                                      logging.StreamHandler()])
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=logging.INFO,
                            handlers=[logging.FileHandler(f"{run_name}.log"),
                                      logging.StreamHandler()])

    logging.info(f"Started nAMRbourhood '{run_name}' with input '{args.input}'")

    # make run directory
    if output_dir.exists() and not args.force:
        logging.error(f"{output_dir} already exists (use a new name or "
                        "--force to overwrite")
        sys.exit(1)
    elif output_dir.exists() and args.force:
        logging.info(f"{output_dir} being overwritten")
        shutil.rmtree(output_dir)
        output_dir.mkdir()
    elif not output_dir.exists():
        output_dir.mkdir()
    logging.info(f"Using {output_dir} to store results")

    return output_dir
