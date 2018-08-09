import os
from ..utils import which, easy_call


def run(command):
    root = 'tmp_jamber'
    nabin = root + '.nab'
    nabout = root + '.out'
    nabc = root + '.c'

    with open(nabin, 'w') as fh:
        fh.write(command)
    nab_bin = which('nab')
    if not nab_bin:
        raise FileNotFoundError('require nab')
    prefix = os.path.abspath(os.path.join(os.path.dirname(nab_bin), '..'))
    os.environ['AMBERHOME'] = prefix
    my_ld_path = os.path.join(prefix, 'lib')
    ld_paths = os.getenv('LD_LIBRARY_PATH')

    if ld_paths:
        os.environ['LD_LIBRARY_PATH'] = my_ld_path + ':' + ld_paths
    else:
        os.environ['LD_LIBRARY_PATH'] = my_ld_path
    build_command = [nab_bin, nabin, '-o', nabout]
    easy_call(build_command)
    easy_call(['./{}'.format(nabout)])
    os.unlink(nabin)
    os.unlink(nabout)
    os.unlink(nabc)
