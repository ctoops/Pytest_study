# Fixtures作为函数参数使用
"""
测试用例可以通过在其参数中使用fixtures名称来接收fixture对象。
每个fixture参数名称所对应的函数,可以通过使用@pytest.fixture注册成为一个fixture函数,来为测试用例提供一个fixture对象。
例子：一个只包含一个fixture和一个使用它的测试用例的简单独立测试模块
"""
import pytest


@pytest.fixture
def sample():
    return 250


def test_fixture(sample):
    code = sample

    assert code == 250

    assert 0  # for demo purposes


"""
test_fixture函数需要sample来提供fixture对象。pytest将发现并调用带@pytest.fixture装饰器的fixture函数:sample。 运行测试如下所示：

(venv) D:\PycharmProjects\My_pytest>pytest ex_fixture/01_fixture.py
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.7.5, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: D:\PycharmProjects\My_pytest
collected 1 item                                                                                                                                                                                               

ex_fixture\01_fixture.py F                                                                                                                                                                               [100%]

================================================================================================== FAILURES ===================================================================================================
________________________________________________________________________________________________ test_fixture _________________________________________________________________________________________________

sample = 250

    def test_fixture(sample):
        code = sample

        assert code == 250

>       assert 0  # for demo purposes
E       assert 0

ex_fixture\01_fixture.py:20: AssertionError
=========================================================================================== short test summary info ===========================================================================================
FAILED ex_fixture/01_fixture.py::test_fixture - assert 0
============================================================================================== 1 failed in 0.11s ==============================================================================================

(venv) D:\PycharmProjects\My_pytest>

"""