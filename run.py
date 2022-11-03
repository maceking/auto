
import pytest





pytest.main(['-vs', './testcase/test_dashboardapi.py', '--alluredir=./report/html', '--clean-alluredir','-p' 'no:warnings'])





