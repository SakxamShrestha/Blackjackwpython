from blackjack_game import *
from unit_test_helper import *
import unittest 
class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")
    self.assertEqual(get_print(print_card_name, 3), "Drew a 3\n")
    self.assertEqual(get_print(print_card_name, 4), "Drew a 4\n")
    self.assertEqual(get_print(print_card_name, 5), "Drew a 5\n")
    self.assertEqual(get_print(print_card_name, 6), "Drew a 6\n")
    self.assertEqual(get_print(print_card_name, 7), "Drew a 7\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 9), "Drew a 9\n")
    self.assertEqual(get_print(print_card_name, 10), "Drew a 10\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    

  def test_draw_card(self):
    self.assertEqual((mock_random([1], draw_card)), 11)
    self.assertEqual((mock_random([2], draw_card)), 2)
    self.assertEqual((mock_random([3], draw_card)), 3)
    self.assertEqual((mock_random([4], draw_card)), 4)
    self.assertEqual((mock_random([5], draw_card)), 5)
    self.assertEqual((mock_random([6], draw_card)), 6)
    self.assertEqual((mock_random([7], draw_card)), 7)
    self.assertEqual((mock_random([8], draw_card)), 8)
    self.assertEqual((mock_random([9], draw_card)), 9)
    self.assertEqual((mock_random([10], draw_card)), 10)
    self.assertEqual((mock_random([11], draw_card)), 10)
    self.assertEqual((mock_random([12], draw_card)), 10)
    self.assertEqual((mock_random([13], draw_card)), 10)


  def test_print_header(self):
    self.assertEqual(get_print(print_header, 'YOUR TURN'),('-----------\nYOUR TURN\n-----------\n'))
    self.assertEqual(get_print(print_header, 'DEALER TURN'),('-----------\nDEALER TURN\n-----------\n'))


  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([12, 10], draw_starting_hand, "DEALER"), 20)
    self.assertEqual(mock_random([1, 5], draw_starting_hand, "YOUR"), 16)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)
    self.assertEqual(mock_random([1,13], draw_starting_hand, "YOUR"), 21)
    self.assertEqual(mock_random([1,1], draw_starting_hand, "DEALER"), 22)
    self.assertEqual(mock_random([2, 2], draw_starting_hand, "YOUR"), 4)
 

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), 'Final hand: 21.\nBLACKJACK!\n')
    self.assertEqual(get_print(print_end_turn_status, 23), 'Final hand: 23.\nBUST.\n')
    self.assertEqual(get_print(print_end_turn_status, 19), 'Final hand: 19.\n')


  def test_end_game_status(self):
    expected_output1 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 21, 19), expected_output1)

    expected_output2 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 20, 21), expected_output2)

    expected_output3 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 23, 22), expected_output3)

    expected_output4 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 19, 23), expected_output4)

    expected_output5 = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 21, 21), expected_output5)

    expected_output6 = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 20, 20), expected_output6)

    expected_output7 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 20, 17), expected_output7)

    expected_output8 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 16, 17), expected_output8)







if __name__ == '__main__':
    unittest.main()
