import os
import json
import posixpath
import jsonschema
import yaml
import sys

class A229MetaSchema:
  def __init__(self, schema_path):
    with open(schema_path) as meta_schema_file:
      uri_path = os.path.abspath(os.path.dirname(schema_path))
      if os.sep != posixpath.sep:
        uri_path = posixpath.sep + uri_path

      resolver = jsonschema.RefResolver(f'file://{uri_path}/', meta_schema_file)
      self.validator = jsonschema.Draft7Validator(json.load(meta_schema_file), resolver=resolver)

  def validate(self, instance_path):
    with open(os.path.join(instance_path), 'r') as input_file:
      instance = yaml.load(input_file, Loader=yaml.FullLoader)
    errors = sorted(self.validator.iter_errors(instance), key=lambda e: e.path)
    file_name =  os.path.basename(instance_path)
    if len(errors) == 0:
      print(f"Validation successful for {file_name}")
    else:
      messages = []
      for error in errors:
        messages.append(f"{error.message} ({'.'.join([str(x) for x in error.path])})")
      messages = [f"{i}. {message}" for i, message in enumerate(messages, start=1)]
      message_str = '\n  '.join(messages)
      raise Exception(f"Validation failed for {file_name} with {len(messages)} errors:\n  {message_str}")

def validate_dir(dir_path):
  meta_schema = A229MetaSchema(os.path.join(os.path.dirname(__file__),'..','meta-schema','meta.schema.json'))
  for file_name in sorted(os.listdir(dir_path)):
    if '.schema.yaml' in file_name:
      meta_schema.validate(os.path.join(dir_path,file_name))

def validate_file(file_path):
  meta_schema = A229MetaSchema(os.path.join(os.path.dirname(__file__),'..','meta-schema','meta.schema.json'))
  meta_schema.validate(file_path)

if __name__ == '__main__':
  source_dir = os.path.join(os.path.dirname(__file__),'..','schema-source')
  if len(sys.argv) == 2:
    validate_file(os.path.join(source_dir,f'{sys.argv[1]}.schema.yaml'))
  elif len(sys.argv) == 1:
    validate_dir(source_dir)