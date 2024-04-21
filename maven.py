import yaml
import subprocess
import os


def execute_maven(pipeline):
    if pipeline:
        print("Running maven")
        subprocess.run("mvn clean", shell=True)
    else:
        print("Pipeline parameter is set to False")


if __name__ == '__main__':
    with open('test.yml', 'r') as  yaml_file:
        data = yaml.safe_load(yaml_file)

    pipeline = data.get('test', {}).get('pipeline', False)
    execute_maven(pipeline)
