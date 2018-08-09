#!/bin/sh

(cd tests && py.test test*py --cov=pdb4amber -v -rsx .) 
