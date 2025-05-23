import unittest

import calculation

release_name = 'lesson'

class CalTest(unittest.TestCase):
    # テスト実行前にcalculationのインスタンを生成
    def setUp(self):
        print('Set Up')
        self.cal = calculation.Cal()
    # テスト終了後に、インスタンスを削除
    def tearDown(self):
        print('Clean Up')
        del self.cal

    # テストをスキップ
    @unittest.skip('skip!')
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1,1),4)

    # release_nameが'lesson'のときテストをスキップ
    @unittest.skipIf(release_name=='lesson','skip!!')
    def test_add_num_and_double_raise(self):
        with self.assertRaises(TypeError):
            self.cal.add_num_and_double('1', '1')

    def test_add_num_and_double_raise_dummy(self):
        with self.assertRaises(TypeError):
            self.cal.add_num_and_double('1', '1')

if __name__ == '__main__':
    unittest.main()