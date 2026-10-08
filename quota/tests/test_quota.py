#!/usr/bin/env python3
"""Tests du plugin quota Claude Code. Lancer : python3 tests/test_quota.py

Cœur portable -> quota_core (core). Rendu SwiftBar + intégration mac -> macos/host (mac).
"""
import os
import sys
import unittest
from datetime import datetime, timezone

_QUOTA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # quota/
sys.path.insert(0, _QUOTA_DIR)
sys.path.insert(0, os.path.join(_QUOTA_DIR, "macos"))
import quota_core as core
import host as mac

# Échantillon réel renvoyé par l'endpoint /usage (tronqué).
SAMPLE = {
    "five_hour": {"utilization": 23.0, "resets_at": "2026-06-21T06:49:59+00:00"},
    "seven_day": {"utilization": 18.0, "resets_at": "2026-06-26T21:59:59+00:00"},
    "seven_day_sonnet": {"utilization": 1.0, "resets_at": "2026-06-26T21:59:59+00:00"},
}
# « Maintenant » figé pour des comptes à rebours déterministes.
NOW = datetime(2026, 6, 21, 2, 36, 0, tzinfo=timezone.utc).astimezone()


class TestCalculs(unittest.TestCase):
    def test_used(self):
        self.assertEqual(core.used({"utilization": 23.0}), 23)
        self.assertEqual(core.used({"utilization": 0}), 0)
        self.assertIsNone(core.used(None))

    def test_color_seuils(self):
        self.assertIsNone(core.color_for(0))            # < 50 utilisé -> adaptatif
        self.assertIsNone(core.color_for(49))
        self.assertEqual(core.color_for(50), "orange")
        self.assertEqual(core.color_for(79), "orange")
        self.assertEqual(core.color_for(80), "red")     # >= 80 utilisé -> rouge
        self.assertIsNone(core.color_for(None))


class TestReset(unittest.TestCase):
    def test_compte_a_rebours(self):
        cd, _ = core.fmt_reset("2026-06-21T06:49:59+00:00", NOW)
        self.assertEqual(cd, "4h13")

    def test_minutes(self):
        cd, _ = core.fmt_reset("2026-06-21T03:06:00+00:00", NOW)
        self.assertEqual(cd, "30m")

    def test_jours(self):
        cd, _ = core.fmt_reset("2026-06-26T21:59:59+00:00", NOW)
        self.assertTrue(cd.startswith("5j"))

    def test_passe(self):
        cd, _ = core.fmt_reset("2026-06-20T00:00:00+00:00", NOW)
        self.assertEqual(cd, "maintenant")

    def test_absolu_fr(self):
        _, absolu = core.fmt_reset("2026-06-21T06:49:59+00:00", NOW)
        self.assertIn("juin", absolu)
        self.assertIn("à", absolu)


class TestRendu(unittest.TestCase):
    def out(self, **kw):
        return mac.render(SAMPLE, "/x/plugin.py", "/x/python3", now=NOW, **kw)

    def test_barre_couleur_et_pourcent(self):
        first = self.out().splitlines()[0]
        self.assertIn("23% · 4h13", first)          # % utilisé, pas restant
        self.assertNotIn("color=", first)            # 23 % et 18 % sains -> adaptatif

    def test_barre_rouge_si_haut(self):
        data = dict(SAMPLE, five_hour={"utilization": 95.0,
                                       "resets_at": "2026-06-21T06:49:59+00:00"})
        first = mac.render(data, "/x/p.py", "/x/py", now=NOW).splitlines()[0]
        self.assertIn("95% ·", first)
        self.assertIn("color=red", first)

    def test_barre_couleur_ignore_hebdo(self):
        # Session basse + hebdo haute : la puce suit la session affichée, pas l'hebdo.
        data = dict(SAMPLE, seven_day={"utilization": 64.0,
                                       "resets_at": "2026-06-26T21:59:59+00:00"})
        first = mac.render(data, "/x/p.py", "/x/py", now=NOW).splitlines()[0]
        self.assertIn("23% ·", first)
        self.assertNotIn("color=", first)

    def test_details_hebdo_et_heure(self):
        out = self.out()
        self.assertIn("Hebdo (7j) : 18% utilisé", out)
        self.assertIn("Hebdo Sonnet : 1% utilisé", out)
        self.assertIn("juin à", out)  # heure de reset absolue présente

    def test_action_embarque_interpreteur(self):
        out = self.out()
        self.assertIn("bash=/x/python3 param1=/x/plugin.py param2=--toggle-autostart", out)

    def test_toggle_autostart_coche(self):
        self.assertIn("✗ Lancer au démarrage", self.out(autostart_on=False))
        self.assertIn("✓ Lancer au démarrage", self.out(autostart_on=True))

    def test_quitter_present(self):
        self.assertIn("Quitter SwiftBar", self.out())

    def test_bloc_manquant_ne_crashe_pas(self):
        out = mac.render({"five_hour": SAMPLE["five_hour"]}, "/x/p.py", "/x/py", now=NOW)
        self.assertIn("23% ·", out.splitlines()[0])

    def test_sonnet_absent_affiche_zero(self):
        # Certains comptes n'ont pas de bloc seven_day_sonnet : 0 %, pas « None% ».
        out = mac.render(dict(SAMPLE, seven_day_sonnet=None), "/x/p.py", "/x/py", now=NOW)
        self.assertIn("Hebdo Sonnet : 0% utilisé", out)
        self.assertNotIn("None%", out)


class TestFenetreFermee(unittest.TestCase):
    """Pas de resets_at sur la session -> aucune fenêtre en cours."""

    # Le % qui traîne (4) appartient à une fenêtre révolue : il ne doit pas s'afficher.
    SANS_ECHEANCE = dict(SAMPLE, five_hour={"utilization": 4.0, "resets_at": None})
    BLOC_NUL = dict(SAMPLE, five_hour=None)

    def test_predicat(self):
        self.assertTrue(core.fenetre_ouverte(SAMPLE["five_hour"], now=NOW))
        apres = datetime(2026, 6, 21, 6, 50, 0, tzinfo=timezone.utc)
        self.assertFalse(core.fenetre_ouverte(SAMPLE["five_hour"], now=apres))  # reset atteint
        self.assertFalse(core.fenetre_ouverte({"utilization": 4.0, "resets_at": None}))
        self.assertFalse(core.fenetre_ouverte({}))
        self.assertFalse(core.fenetre_ouverte(None))

    def test_barre_escargot_et_zero(self):
        first = mac.render(self.SANS_ECHEANCE, "/x/p.py", "/x/py", now=NOW).splitlines()[0]
        self.assertIn(f"0% · {core.GLYPHE_REPOS}", first)
        self.assertNotIn("4%", first)       # le % de la fenêtre close reste caché
        self.assertNotIn("color=", first)   # rien en cours -> jamais alarmant

    def test_bloc_nul_aussi(self):
        first = mac.render(self.BLOC_NUL, "/x/p.py", "/x/py", now=NOW).splitlines()[0]
        self.assertIn(f"0% · {core.GLYPHE_REPOS}", first)

    def test_detail_sans_compte_a_rebours(self):
        out = mac.render(self.SANS_ECHEANCE, "/x/p.py", "/x/py", now=NOW)
        self.assertIn("aucune fenêtre en cours", out)
        self.assertNotIn("reset dans ?", out)     # plus de « ? » orphelin
        self.assertIn("Hebdo (7j) : 18% utilisé", out)   # l'hebdo reste lisible

    def test_reset_atteint_affiche_escargot(self):
        apres = datetime(2026, 6, 21, 6, 50, 0, tzinfo=timezone.utc).astimezone()
        out = mac.render(SAMPLE, "/x/p.py", "/x/py", now=apres)
        self.assertTrue(out.startswith(f"0% · {core.GLYPHE_REPOS} |"))
        self.assertNotIn("maintenant", out)

    def test_hebdo_intacte_quand_session_fermee(self):
        # La fenêtre hebdo, elle, a une échéance : son compte à rebours doit rester.
        out = mac.render(self.SANS_ECHEANCE, "/x/p.py", "/x/py", now=NOW)
        self.assertIn("juin à", out)


class TestStaleEtAge(unittest.TestCase):
    def test_fmt_age(self):
        self.assertEqual(core.fmt_age(40), "40s")
        self.assertEqual(core.fmt_age(7 * 60), "7m")
        self.assertEqual(core.fmt_age(3900), "1h05")

    def test_render_stale_grise_et_signale(self):
        out = mac.render(SAMPLE, "/x/p.py", "/x/py", now=NOW, stale_secs=90)
        first = out.splitlines()[0]
        self.assertIn("⋯", first)             # marqueur de péremption
        self.assertIn("color=gray", first)     # barre grisée
        self.assertIn("Hors-ligne — cache il y a 1m", out)


class TestCache(unittest.TestCase):
    def setUp(self):
        self.tmp = core.CACHE_FILE
        core.CACHE_FILE = os.path.join(os.path.dirname(__file__), ".usage-cache.test.json")

    def tearDown(self):
        try:
            os.remove(core.CACHE_FILE)
        except FileNotFoundError:
            pass
        core.CACHE_FILE = self.tmp

    def test_round_trip(self):
        self.assertIsNone(core.load_cache())          # rien au départ
        core.save_cache(SAMPLE, fetched_at=core.time.time() - 120)
        data, age = core.load_cache()
        self.assertEqual(data["five_hour"]["utilization"], 23.0)
        self.assertGreaterEqual(age, 119)


class TestThrottle(unittest.TestCase):
    def test_cache_frais_saute_le_fetch(self):
        self.assertTrue(core.should_skip_fetch(10))                 # 10 s < 300 -> saute
        self.assertTrue(core.should_skip_fetch(299))

    def test_cache_vieux_force_le_fetch(self):
        self.assertFalse(core.should_skip_fetch(300))               # >= seuil -> fetch
        self.assertFalse(core.should_skip_fetch(10_000))

    def test_force_ignore_le_throttle(self):
        self.assertFalse(core.should_skip_fetch(10, force=True))    # bouton Rafraîchir

    def test_pas_de_cache_force_le_fetch(self):
        self.assertFalse(core.should_skip_fetch(None))

    def test_echeance_passee(self):
        self.assertFalse(core.echeance_passee(SAMPLE, now=NOW))          # reset à venir
        apres = datetime(2026, 6, 21, 6, 50, 0, tzinfo=timezone.utc)
        self.assertTrue(core.echeance_passee(SAMPLE, now=apres))         # reset atteint
        self.assertFalse(core.echeance_passee({"five_hour": None}, now=apres))

    def test_rafraichir_force_dans_le_menu(self):
        out = mac.render(SAMPLE, "/x/p.py", "/x/py", now=NOW)
        self.assertIn("Rafraîchir | bash=/x/py param1=/x/p.py param2=--force", out)


class TestErreur(unittest.TestCase):
    def test_render_error(self):
        out = mac.render_error("boom")
        self.assertIn("⚠ Claude | color=red", out)
        self.assertIn("boom", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
