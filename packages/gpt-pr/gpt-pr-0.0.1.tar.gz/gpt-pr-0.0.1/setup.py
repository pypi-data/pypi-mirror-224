import subprocess
from setuptools import setup, find_packages


def dependencies_filter(dependency):
    if dependency.startswith('-i'):
        return False

    return True


def get_pipenv_requirements():
    result = subprocess.run(['pipenv', 'requirements'], capture_output=True, text=True)

    if result.returncode == 0:
        dependencies = [dependency
                        for dependency in result.stdout.splitlines()
                        if dependencies_filter(dependency)]
        return dependencies
    else:
        raise RuntimeError(f"'pipenv requirements' failed with error: {result.stderr}")


def get_requirements():
    with open('requirements.txt') as f:
        dependencies = [dependency
                        for dependency in f.read().splitlines()
                        if dependencies_filter(dependency)]
        return dependencies


setup(name='gpt-pr',
      version='0.0.1',
      python_requires='>=3.7',
      description='Automate your GitHub workflow with GPT-PR: an OpenAI powered library for streamlined PR generation.',
      url='http://github.com/alissonperez/gpt-pr',
      author='Alisson R. Perez',
      author_email='alissonperez@outlook.com',
      license='MIT',
      entry_points={
          'console_scripts': ['gpt-pr=gptpr.main:main'],
      },
      packages=find_packages('.'),
      include_package_data=True,
      install_requires=get_requirements(),
      zip_safe=False)
