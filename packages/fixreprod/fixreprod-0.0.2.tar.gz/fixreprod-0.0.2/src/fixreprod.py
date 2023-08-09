import random
import importlib
import re

def check_for_random_numbers(source_code):
  """Checks whether the given source code contains random numbers.

  Args:
    source_code: The source code to check.

  Returns:
    True if the source code contains random numbers, False otherwise.
  """

  for line in source_code.splitlines():
    match = re.search("import\s+([a-zA-Z0-9_.]+)\s*", line)
    if match:
      library = match.group(1)
      try:
        for m in importlib.import_module(library).__dict__.keys():
          if hasattr(getattr(importlib.import_module(library), m), "seed"):
            return True
      except ModuleNotFoundError:
        pass
  return False

def initialize_seeds(source_code):
  """Initializes all seeds for all API libraries in the source code file.

  Args:
    source_code: The source code to initialize seeds for.

  Returns:
    A new code with all seeds initialized.
  """

  new_code = ""
  for line in source_code.splitlines():
    match = re.search("import\s+([a-zA-Z0-9_.]+)\s*", line)
    if match:
      library = match.group(1)
      try:
        for m in importlib.import_module(library).__dict__.keys():
          if hasattr(getattr(importlib.import_module(library), m), "seed"):
            new_code += f"{library}.{m}.seed({random.randint(0, 1)})\n"
      except ModuleNotFoundError:
        pass
    else:
      new_code += line + "\n"
  return new_code


if __name__ == "__main__":
  source_code = input("Enter the source code file name: ")
  with open(source_code, "r") as f:
    source_code = f.read()

  if check_for_random_numbers(source_code):
    new_code = initialize_seeds(source_code)
    print(new_code)
  else:
    print("The source code does not contain random numbers.")

