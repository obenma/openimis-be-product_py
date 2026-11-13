"""
Tests for backend/features/policy.feature, product module part.
"""
from django.test import TestCase

from product.models import Product
from product.test_helpers import create_test_product


class ProductAgeLimitsTest(TestCase):
    # Scenario: The product age limits are optional and persist (@redmine-33762)
    def test_age_limits_persist_and_are_optional(self):
        product = create_test_product("FPAGE1", custom_props={"age_minimal": 6, "age_maximal": 46})
        stored = Product.objects.get(id=product.id)
        self.assertEqual((stored.age_minimal, stored.age_maximal), (6, 46))
        bare = Product.objects.get(id=create_test_product("FPAGE2").id)
        self.assertEqual((bare.age_minimal, bare.age_maximal), (None, None))
