from django.test import TransactionTestCase
from django.urls import reverse

from .models import Question

class UsingTransactionTestCaseWithSerializedRollback(TransactionTestCase):

    serialized_rollback = True

    def test_initial_data_from_migration_is_present(self):
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [Question.objects.get(question_text="What is your favorite holiday?")],
        )

    # Without serialized_rollback = True, this test fails because when using
    # TransactionTestCase, the database is flushed after each test

    def test_initial_data_from_migration_is_still_present(self):
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [Question.objects.get(question_text="What is your favorite holiday?")],
        )
