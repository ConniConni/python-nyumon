import pytest

import calculation

# テストを関数で書く
def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1,1) == 4

# テストをクラスで書く
class TestCal(object):
    def test_dd_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1,1) == 4

    # 例外のテスト
    def test_add_num_and_double_raise(self):
        with pytest.raises(TypeError):
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')