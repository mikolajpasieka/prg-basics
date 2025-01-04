import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f("sigma"),"Sigma-sIgma-siGma-sigMa-sigmA")
        self.assertEqual(p1.f("rel"),"Rel-rEl-reL")
        self.assertEqual(p1.f("c"),"C")
        self.assertEqual(p1.f("jajo"),"Jajo-jAjo-jaJo-jajO")

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(1,9,2),1)
        self.assertEqual(p2.f(10,15,1),6)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f(3,3),1)
        self.assertEqual(p3.f(-3,-3),3)
        self.assertEqual(p3.f(3,-3),4)

    def test_p4(self):
        import p4
        sub_grades = {"prg":[4,4,5,5], "hist":[4,4,5], "econ":[5,4,5,5], "alg":[5,4]}
        self.assertEqual(p4.f(sub_grades),"hist")

    def test_p5(self):
        import p5
        cart = {"juice":4, "bread":2, "milk":3}
        prices = {"juice":2.99, "bread":2.19, "butter":3.09, "milk":1.29}
        self.assertEqual(p5.f(cart, prices, 21),True)
        self.assertEqual(p5.f(cart, prices, 20),False)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("za153"),True)
        self.assertEqual(p6.f("zA9999"),True)
        self.assertEqual(p6.f("G12345"),False)
        self.assertEqual(p6.f("AbC2"),False)

    def test_p7(self):
        import p7
        bus = [[2,1],[15,5],[4,6]]
        self.assertEqual(p7.f(bus),9)

    def test_p8(self):
        import p8
        self.assertEqual(p8.f("K765QJT9A382"),"4")
        self.assertEqual(p8.f("76T9854AKQ32"),"J")

    def test_p9(self):
        import p9
        self.assertEqual(p9.f([9,9,9,9,9,9,9,8,9,9,9]),8)
        self.assertEqual(p9.f([33,33,33,44,33]),44)

    def test_p10(self):
        import p10
        computer = {"Owl","Camper","Chaser","Walker","Hunter","Breeze"}
        smartphone = {"Owl","Camper","Storm","Sleeper","Eater"}
        self.assertEqual(p10.f(computer,smartphone),9)

    def test_p11(self):
        import p11
        self.assertEqual(p11.f(1597),True)
        self.assertEqual(p11.f(1596),False)

    def test_p12(self):
        import p12
        self.assertEqual(p12.f(1597),True)
        self.assertEqual(p12.f(1596),False)

    def test_p13(self):
        import p13
        self.assertEqual(p13.f(1597),True)
        self.assertEqual(p13.f(1596),False)

    def test_p14(self):
        import p14
        self.assertEqual(p14.f(1597),True)
        self.assertEqual(p14.f(1596),False)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
