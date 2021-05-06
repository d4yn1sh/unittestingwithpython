import unittest
from phonebookpackage.phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
	def setUp(self) -> None:
		self.phoneBook = PhoneBook()

	def tearDown(self) -> None:
		pass

	def test_lookup_by_name(self):
		self.phoneBook.add("Bob", "12345")
		number = self.phoneBook.lookup("Bob")
		self.assertEqual("12345", number)

	def test_missing_name(self):
		with self.assertRaises(KeyError):
			self.phoneBook.lookup("Alice")

	@unittest.skip("WIP")
	def test_empty_phonebook_is_consistent(self):
		self.assertTrue(self.phoneBook.is_consistent)


if __name__ == "__main__":
	unittest.main()