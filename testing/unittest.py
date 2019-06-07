import unittest
# from activities import eat, nap

class ActivityTests(unittest.Testcase):
  def test_eat(self):
    self.assertEqual(eat("broccoli", is_healthy=True),"I'm eating broccoli, becuase my body is a temple")
    self.assertEqual(eat("pizze", is_healthy=False),"Pizza because yolo")


if __name__ == "__main__":
  unittest.main()
