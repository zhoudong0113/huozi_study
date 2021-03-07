import pytest
import self as self
import yaml
from study03.calc import Calculator

with open("data/calc.yaml") as f:
    data = yaml.safe_load(f)
    add_data = data['add']['datas']
    add_ids = data['add']['ids']
    sub_data = data['sub']['datas']
    sub_ids = data['sub']['ids']
    mul_data = data['mul']['datas']
    mul_ids = data['mul']['ids']
    div_data = data['div']['datas']
    div_ids = data['div']['ids']



class TestCalc:

    def setup_class(self):
        print("开始测试")
        self.calc = Calculator()

    def teardown_class(self):
        print("测试结束")

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", add_data, ids=add_ids)
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 1)
            assert result == expect

    @pytest.mark.parametrize("a,b,expect",sub_data,ids=sub_ids)
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        if isinstance(result,float):
            result = round(result,2)
            assert result == expect

    @pytest.mark.parametrize("a,b,expect",mul_data,ids=mul_ids)
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 3)
            assert result == expect

    @pytest.mark.parametrize("a,b,expect",div_data,ids=div_ids)
    def test_div(self,a,b,expect):
        result = self.calc.div(a, b)
        if isinstance(result, int):
            result = round(result, 4)
            assert result == expect
