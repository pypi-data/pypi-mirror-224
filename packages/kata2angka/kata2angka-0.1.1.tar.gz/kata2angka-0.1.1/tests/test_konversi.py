from kata2angka import konversi as k2a
import unittest

class TestW2N(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(k2a.word_to_num("nol"), 0)
        self.assertEqual(k2a.word_to_num("satu"), 1)
        self.assertEqual(k2a.word_to_num("dua"), 2)
        self.assertEqual(k2a.word_to_num("sembilan"), 9)
        self.assertEqual(k2a.word_to_num("sepuluh"), 10)
        self.assertEqual(k2a.word_to_num("sebelas"), 11)
        self.assertEqual(k2a.word_to_num("dua puluh"), 20)
        self.assertEqual(k2a.word_to_num("dua puluh satu"), 21)
        self.assertEqual(k2a.word_to_num("lima puluh"), 50)
        self.assertEqual(k2a.word_to_num("seratus"), 100)
        self.assertEqual(k2a.word_to_num("seratus dua puluh lima"), 125)
        self.assertEqual(k2a.word_to_num("seribu"), 1000)
        self.assertEqual(k2a.word_to_num("seribu lima ratus"), 1500)
        self.assertEqual(k2a.word_to_num("sejuta"), 1000000)
        self.assertEqual(k2a.word_to_num("dua juta tiga ratus ribu empat ratus lima puluh enam"), 2300456)
        self.assertEqual(k2a.word_to_num("sembilan juta delapan ratus tiga puluh dua ribu seratus lima puluh enam"), 9832156)
        
    def test_large_numbers(self):
        self.assertEqual(k2a.word_to_num("seratus miliar"), 100000000000)
        self.assertEqual(k2a.word_to_num("dua ratus tiga puluh empat miliar lima ratus enam puluh tujuh juta delapan ratus sembilan puluh ribu seratus dua puluh tiga"), 234567890123)

class AdditionalTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(k2a.word_to_num("kosong"), 0)

    def test_negative(self):
        self.assertEqual(k2a.word_to_num("minus dua"), -2)
        self.assertEqual(k2a.word_to_num("negatif sepuluh"), -10)

    def test_ordinal_numbers(self):
        self.assertEqual(k2a.word_to_num("pertama"), 1)
        self.assertEqual(k2a.word_to_num("kedua belas"), 12)
        self.assertEqual(k2a.word_to_num("dua puluh ketiga"), 23)

    def test_large_ordinal_numbers(self):
        self.assertEqual(k2a.word_to_num("seratus dua puluh kelima"), 125)
        self.assertEqual(k2a.word_to_num("seribu lima ratus keenam"), 1506)

    def test_special_cases(self):
        self.assertEqual(k2a.word_to_num("seribu dua"), 1002)
        self.assertEqual(k2a.word_to_num("seratus lima puluh dua"), 152)
        self.assertEqual(k2a.word_to_num("sepuluh ribu dua ratus"), 10200)

    def test_large_special_cases(self):
        self.assertEqual(k2a.word_to_num("sejuta seratus ribu"), 1100000)
        self.assertEqual(k2a.word_to_num("seratus juta dua puluh ribu tiga ratus empat puluh lima"), 100020345)

    def test_combined_numbers(self):
        self.assertEqual(k2a.word_to_num("dua puluh lima juta seratus ribu tiga ratus empat puluh lima"), 25100345)

if __name__ == '__main__':
    unittest.main()
