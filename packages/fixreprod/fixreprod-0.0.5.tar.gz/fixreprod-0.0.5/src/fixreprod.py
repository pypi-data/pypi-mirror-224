import random
import importlib
import re

def is_seed_related_to_signature(module, m):
  """Checks whether a seed is related to a signature.

  Args:
    module: The module to check.
    m: The attribute of the module to check.

  Returns:
    True if the seed is related to a signature, False otherwise.
  """
  # Add your custom logic here to determine whether the seed is related to a signature.
  return False

def check_for_random_numbers(source_code):
  """Checks whether the given source code contains random numbers.

  Args:
    source_code: The source code to check.

  Returns:
    True if the source code contains random numbers, False otherwise.
  """

  for line in source_code.splitlines():
    match = re.search(r"import\s+([a-zA-Z0-9_.]+)(?:\s+as\s+([a-zA-Z0-9_]+))?\s*", line)
    if match:
      library = match.group(1)
      alias = match.group(2) or library
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
  aliases = {}
  for line in source_code.splitlines():
    match = re.search(r"import\s+([a-zA-Z0-9_.]+)(?:\s+as\s+([a-zA-Z0-9_]+))?\s*", line)
    if match:
      library = match.group(1)
      alias = match.group(2) or library
      aliases[alias] = library
      try:
        module = importlib.import_module(library)
        for m in module.__dict__.keys():
          if hasattr(getattr(module, m), "seed") and not is_seed_related_to_signature(module, m):
            if library == "gym":
              new_code += f"{alias}.Space().seed({random.randint(0, 1)})\n"
            elif library == "torch":
              if m == "Generator":
                new_code += f"{alias}.{m}().seed({random.randint(0, 1)})\n"
              elif m == "manual_seed":
                new_code += f"{alias}.{m}({random.randint(0, 1)})\n"
              elif m == "initial_seed":
                new_code += f"{alias}.{m}()\n"
              elif m == "cuda":
                new_code += f"{alias}.{m}.manual_seed({random.randint(0, 1)})\n"
                new_code += f"{alias}.{m}.manual_seed_all({random.randint(0, 1)})\n"
              elif m == "use_deterministic_algorithms":
                new_code += f"{alias}.{m}(True)\n"
            elif library == "tensorflow":
              if m == "set_seed":
                new_code += f"{alias}.random.{m}({random.randint(0, 1)})\n"
            else:
              new_code += f"{alias}.{m}.seed({random.randint(0, 1)})\n"
      except (ModuleNotFoundError, AttributeError):
        pass
    else:
      new_code += line + "\n"

  # Remove incorrect seed setting codes
  lines = new_code.splitlines()
  new_code = ""
  for line in lines:
    if ".seed(" in line:
      alias = line.split(".")[0]
      if alias in aliases and aliases[alias] != "torch.nn.functional":
        new_code += line + "\n"
    else:
      new_code += line + "\n"

  return new_code

def main():
  source_code = input("Enter the source code file name: ")
  with open(source_code, "r") as f:
    source_code = f.read()

  if check_for_random_numbers(source_code):
    new_code = initialize_seeds(source_code)
    print(new_code)
  else:
    print("The source code does not contain random numbers.")

if __name__ == "__main__":
 main()

