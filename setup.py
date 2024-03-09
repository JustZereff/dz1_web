from setuptools import setup, find_packages

setup(name='pc_project_group_04',
      version='0.0.2',
      description='Your personal assistant',
      url='https://github.com/JustZereff/dz1_web',
      author='GoIt Python21 project_group_04',
      packages=find_packages(),
      entry_points={
          'console_scripts':['personal-assistant=src.user_interface:start_bot']
      }
    )