import unittest
from fonctions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature, diviser, valider_mot_de_passe

class TestFonctions(unittest.TestCase):
    def test_additionner_cas_positif(self):
        """Test addition avec nombres positifs"""
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)

    def test_additionner_cas_negatif(self):
        """Test addition avec nombres négatifs"""
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)

    # Tests pour est_pair
    def test_est_pair_nombre_pair(self):
        """Test avec un nombre pair"""
        self.assertTrue(est_pair(4))

    def test_est_pair_nombre_impair(self):
        """Test avec un nombre impair"""
        self.assertFalse(est_pair(3))

    def test_est_pair_zero(self):
        """Test avec zéro"""
        self.assertTrue(est_pair(0))

    # Tests pour valider_email
    def test_valider_email_valide(self):
        """Test avec un email valide"""
        self.assertTrue(valider_email("test@example.com"))

    def test_valider_email_sans_arobase(self):
        """Test avec un email sans @"""
        self.assertFalse(valider_email("testexample.com"))

    def test_valider_email_sans_point(self):
        """Test avec un email sans point"""
        self.assertFalse(valider_email("test@example"))

    # Tests pour calculer_moyenne
    def test_calculer_moyenne_liste_normale(self):
        """Test avec une liste de notes normales"""
        resultat = calculer_moyenne([10, 15, 20])
        self.assertEqual(resultat, 15)

    def test_calculer_moyenne_liste_vide(self):
        """Test avec une liste vide"""
        resultat = calculer_moyenne([])
        self.assertEqual(resultat, 0)

    def test_calculer_moyenne_une_note(self):
        """Test avec une seule note"""
        resultat = calculer_moyenne([18])
        self.assertEqual(resultat, 18)

    # Tests pour convertir_temperature
    def test_convertir_temperature_zero(self):
        """Test conversion 0°C = 32°F"""
        resultat = convertir_temperature(0)
        self.assertEqual(resultat, 32)

    def test_convertir_temperature_eau_bouillante(self):
        """Test conversion 100°C = 212°F"""
        resultat = convertir_temperature(100)
        self.assertEqual(resultat, 212)

    # Tests pour diviser
    def test_diviser_cas_normal(self):
        """Test division normale"""
        resultat = diviser(10, 2)
        self.assertEqual(resultat, 5)

    def test_diviser_par_zero(self):
        """Test division par zéro"""
        with self.assertRaises(ZeroDivisionError):
            diviser(10, 0)

    # Tests pour valider_mot_de_passe
    def test_valider_mot_de_passe_valide(self):
        """Mot de passe valide"""
        self.assertTrue(valider_mot_de_passe("Abcdef12"))

    def test_valider_mot_de_passe_trop_court(self):
        """Mot de passe trop court"""
        self.assertFalse(valider_mot_de_passe("Abc12"))

    def test_valider_mot_de_passe_sans_majuscule(self):
        """Mot de passe sans majuscule"""
        self.assertFalse(valider_mot_de_passe("abcdef12"))

    def test_valider_mot_de_passe_sans_minuscule(self):
        """Mot de passe sans minuscule"""
        self.assertFalse(valider_mot_de_passe("ABCDEF12"))

    def test_valider_mot_de_passe_sans_chiffre(self):
        """Mot de passe sans chiffre"""
        self.assertFalse(valider_mot_de_passe("Abcdefgh"))

# Permet d'exécuter les tests
if __name__ == '__main__':
    unittest.main()