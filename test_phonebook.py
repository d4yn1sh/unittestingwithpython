import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
	def test_lookup_by_name(self):
		phoneBook = PhoneBook()
		phoneBook.add("Bob", "12345")
		number = phoneBook.lookup("Bob")
		self.assertEqual("12345", number)

	def test_missing_name(self):
		phoneBook = PhoneBook()
		with self.assertRaises(KeyError):
			phoneBook.lookup("Alice")


if __name__ == "__main__":
	unittest.main()