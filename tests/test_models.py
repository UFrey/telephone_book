import sys
import os
import unittest

testdir = os.path.dirname(__file__)
srcdir = '../telephone_book'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from telephone_book.models import Entry, TelephoneBook


class TestTelephoneBook(unittest.TestCase):
    def setUp(self) -> None:
        self.telephone_book = TelephoneBook("Testbuch",
                                            {"max_entries": 3})

        entry_1 = Entry("Klaus")
        entry_1.phone_number = "8723878"

        entry_2 = Entry("Otto")
        entry_2.phone_number = "8723878"

        entry_3 = Entry("Peter")
        entry_3.phone_number = "8723878"

        self.telephone_book.add(entry_1)
        self.telephone_book.add(entry_2)
        self.telephone_book.add(entry_3)

    def test_number_of_entries(self):
        """es sollten sich 3 Einträge im Telefonbuch befinden"""
        self.assertEqual(len(self.telephone_book.get_entries()),
                         3, "Es fehlen Testobjekte")

    def test_iter_implemenation(self):
        it = iter(self.telephone_book)
        with self.assertRaises(StopIteration):
            next(it)
            next(it)
            next(it)
            next(it)

    def test_delete_entry_from_book(self):
        entry = self.telephone_book.remove_entry("Otto")
        self.assertEqual(entry.name, "Otto",
                         "Das ist nicht das richtige Entry Objekt")
        self.assertEqual(len(self.telephone_book.get_entries()),
                         2,
                         "Objekt wurde nicht gelöscht")

        self.assertTrue(isinstance(entry, Entry))

    # Aufgabe: get_entry() - Methode des Telefonbuchs schreiben:
    # zb. test_get_entry_with_invalid_username (Exception) oder
    # test_get_entry_with_valid_username(test equality)
    # Zeit:10 Minuten
    def test_get_entry_with_valid_username(self):
        entry = self.telephone_book.get_entry("Otto")
        self.assertEqual(entry.name, "Otto")
        self.assertTrue(isinstance(entry, Entry))

    def test_get_entry_with_invalid_username(self):
        with self.assertRaises(Exception):
            self.telephone_book.get_entry("Gandalf")

    def test_exceed_max_number_of_entries(self):
        entry_4 = Entry("Uwe")
        entry_4.phone_number = "2324234"
        with self.assertRaises(Exception):
            self.telephone_book.add(entry_4)


class TestEntry(unittest.TestCase):

    def setUp(self):
        """wird VOR jeder Test-Methode aufgerufen"""
        self.entry = Entry(name="Klaus")
        self.entry.phone_number = "0049 037 234 234"  # +4937234234
        # print("Setup wurde aufgerufen!")

    def test_create_entry_object_with_invalid_username(self):
        with self.assertRaises(Exception):
            Entry(name="k")

    def test_valid_telephone_number(self):
        """testen, ob eingetragene Telefonnummer stimmt"""
        self.assertEqual(self.entry.phone_number,
                         "0049 037 234 234",
                         "Die Telefonnummer wurde falsch eingetragen")

    def test_raise_exception_if_invalid_telephone_number(self):
        """testen, ob bei einer invaliden Nummer eine Exception ausgelöst wird"""
        with self.assertRaises(Exception):
            self.entry.phone_number = "343"
           # self.entry.phone_number = "34323 234544342488888"

    def test_raise_exception_if_long_telephone_number(self):
        """testen, ob bei einer zu langen Nummer eine Exception ausgelöst wird"""
        with self.assertRaises(Exception):
            #self.entry.phone_number = "343"
            self.entry.phone_number = "34334248884444444444444488"
