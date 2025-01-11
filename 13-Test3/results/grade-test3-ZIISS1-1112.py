'''
1. Download your programs from Moodle.
1. Put this grading program in a folder with your programs.
2. Run this grading program.
3. Read your test results from results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f("+-+++++-+++-+"),7)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f("11 9 + 15 - 14 +"),19)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("X_c_5"),True)
        self.assertEqual(p3.f("0_c_5"),False)
        self.assertEqual(p3.f("X_c_5_X"),False)

    def test_p4(self):
        import p4
        c1 = p4.C("Monica","Blue",19)
        c2 = p4.C("Peter","Green",16)
        self.assertEqual(c1.__str__(),"MB19")
        self.assertEqual(c2.__str__(),"pg16")

    def test_p5(self):
        import p5
        stadium = p5.C({"A":120,"D":150,"G":90,"K":110})
        stadium.m1("S",20)
        self.assertEqual(stadium.m2("DS"),170)

    def test_p6(self):
        import p6
        res = [95,90,41,20,50,70,44]
        fnc = lambda x: x>30 and x<50
        self.assertEqual(p6.f(fnc,res),3)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f(["a","b","c","d","e","f"]),True)
        self.assertEqual(p7.f(["a","b","c","d","d","f"]),False)

    def test_p8(self):
        import p8
        times_twenty = p8.f(20)
        self.assertEqual(times_twenty(15),300)

    def test_p9(self):
        import p9
        cars = [{"BBB":111},{"AAA":222},{"DDD":333},{"CCC":444}]
        self.assertEqual(p9.f(cars,1),[{"AAA":222},{"BBB":111},{"CCC":444},{"DDD":333}])
        self.assertEqual(p9.f(cars,2),[{"CCC":444},{"DDD":333},{"AAA":222},{"BBB":111}])

    def test_p10(self):
        import p10
        dates = "2025-01-07,2021-1-23,05/12/2024,2025-01-08"
        self.assertEqual(p10.f(dates),["2025-01-07","2025-01-08"])


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
