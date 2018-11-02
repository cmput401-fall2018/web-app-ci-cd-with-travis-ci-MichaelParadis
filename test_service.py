from service import Service
from unittest import TestCase, mock
import pytest


class test_service(TestCase): 

    def test_divide(self):
        service = Service()
        service.bad_random  = mock.Mock(return_value=42)
        y = 3
        assert service.divide(y) == 42 / y
        
        y2 = -10
        assert service.divide(y2) == 42 / y2

        assert service.divide(2) == 21

        with pytest.raises(ZeroDivisionError):service.divide(0)

    def test_abs_plus(self):
        service = Service()
        
        assert service.abs_plus(0) == 1
        assert service.abs_plus(-1) == 2
        assert service.abs_plus(1) == 2

    def test_complicated_function(self):
        service = Service()
        service.bad_random = mock.Mock(return_value=42)
        assert service.complicated_function(3) == (42/3, 0)

        service.bad_random = mock.Mock(return_value=43)

        assert service.complicated_function(3) == (43/3, 1)
