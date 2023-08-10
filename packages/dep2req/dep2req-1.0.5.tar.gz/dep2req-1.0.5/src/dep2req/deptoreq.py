#!/usr/bin/env python

# Maintained by Greg Smethells.
# Licensed under the GPL version 2.
# See LICENSE file for details.


def parseArgs():
  from argparse import ArgumentParser

  parser = ArgumentParser()

  parser.add_argument('-f', '--filename', type = str, default = './pyproject.toml', help = 'path to the input pyproject.toml file')  
  parser.add_argument('-a', '--add-optional', action = 'store_true', help = 'whether to include "optional-dependencies" [defaults to including all sections]')
  parser.add_argument('-s', '--optional-sections', type = str, help = 'name(s) of "optional-dependencies" section(s) to include, comma-delimited')
  parser.add_argument('-o', '--output', type = str, default = './requirements.txt', help = 'path to the output requirements.txt file')
  parser.add_argument('-v', '--verbose', action = 'store_true', help = 'print details about what the script is doing')

  return parser.parse_args()


def parsePyProject(args):
  from toml import load

  if args.verbose:
    print(f'Reading in {args.filename}')

  data = load(args.filename)
  proj = data.get('project')

  if not proj:
    raise RuntimeWarning(f'Error reading {args.filename}: missing project section')

  if args.verbose:
    print('Parsing out dependencies')

  deps = set(proj.get('dependencies', []))

  if not deps:
    raise RuntimeWarning(f'Error reading {args.filename}: no dependencies listed')

  if args.add_optional:
    if args.verbose:
      print('Parsing out optional-dependencies')

    sections  = proj.get('optional-dependencies', [])
    specified = args.optional_sections.split(',') if args.optional_sections else None 

    for section in sections:
      if not specified or section in specified:
        if args.verbose:
          print(f'Including optional-dependencies from section "{section}"')

        deps.update(sections[section])

    if specified:
      for section in specified:
        if section not in sections:
          print(f'Warning: could not find optional-dependencies section "{section}"')

  return deps


def writeRequirements(args, deps):
  if args.verbose:
    print(f'Writing out {args.output}')

  with open(args.output, 'w') as fh:
    fh.write('\n'.join(sorted(deps)))
    fh.write('\n')


def main():
  try:
    args = parseArgs()
    deps = parsePyProject(args)

    writeRequirements(args, deps)
  except (RuntimeWarning, OSError) as ex:
    print(ex)
    return 1

