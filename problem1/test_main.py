import unittest
from main import konversi_nilai

class TestKonversiNilai(unittest.TestCase):

    def test_70(self):
        result = konversi_nilai(70)
        self.assertEqual(result, "B+")

    def test_80(self):
        result = konversi_nilai(80)
        self.assertEqual(result, "A")
        
if __name__ == '__main__':
    unittest.main()