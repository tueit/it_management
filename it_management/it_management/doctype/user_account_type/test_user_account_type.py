# -*- coding: utf-8 -*-
# Copyright (c) 2020, IT-Geräte und IT-Lösungen wie Server, Rechner, Netzwerke und E-Mailserver sowie auch Backups, and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
from frappe.tests.utils import FrappeTestCase


class TestUserAccountType(FrappeTestCase):
    def test_user_account_type_creation(self):
        doc = frappe.get_doc(
            {
                "doctype": "User Account Type",
                "title": "Test Account Type",
            }
        )
        doc.insert()

        self.assertTrue(
            frappe.db.exists("User Account Type", {"title": "Test Account Type"})
        )

        doc.delete()
