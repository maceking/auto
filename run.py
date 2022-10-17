import os
import time
import pytest
from utils.logger import logger




pytest.main(['-vs', './testcase/test_usercenter.py', '--alluredir=./report/html', '--clean-alluredir','-p' 'no:warnings'])





