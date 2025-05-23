import pytest

import calculation

# テストを関数で書く
def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1,1) == 4
1
# テストをクラスで書く
class TestCal(object):
    # テスト前の処理を記載
    def setup_method(self,method):
        print(f'method={method.__name__}')
        self.cal = calculation.Cal()

    def test_dd_num_and_double(self):
        # cal = calculation.Cal()
        assert self.cal.add_num_and_double(1,1) == 4

    # 例外のテスト
    def test_add_num_and_double_raise(self):
        with pytest.raises(TypeError):
            # cal = calculation.Cal()
            self.cal.add_num_and_double('1', '1')