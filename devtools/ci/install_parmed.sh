rm -rf `python -c "import parmed; import os; print(os.path.dirname(parmed.__file__))"`
pip install git+https://github.com/parmed/parmed --upgrade
