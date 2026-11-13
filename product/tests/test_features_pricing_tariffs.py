"""
Feature tests for features/pricing-tariffs.feature (backend scenarios, module product).
"""
import unittest

from django.test import TestCase


class PricingTariffsProductFeatureTests(TestCase):
    # Scenario: VIH-negative policy lasts 10 months (@redmine-35817)
    @unittest.skip("open: #35817")
    def test_vih_negative_policy_lasts_10_months(self):
        pass
