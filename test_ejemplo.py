import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """
            Comprueba que la función upper pasa a mayusculas.
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """
            Comprueba que la función isupper distingue mayusculas de minúsculas.
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """
            Comprueba que la función split separa las palabras de una frase
            y que falla cuando se intenta invocar sobre un número.
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()