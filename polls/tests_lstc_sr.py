from django.test import LiveServerTestCase

from .models import Question

class UsingLiveServerTestCaseWithSerializedRollback(LiveServerTestCase):

    serialized_rollback = True

    def test_initial_data_from_migration_is_present(self):
        assert Question.objects.get(question_text="What is your favorite holiday?")

    # Without serialized_rollback = True, this test fails because when using
    # LiveServerTestCase, which inherits from TransactionTestCase,
    # the database is flushed after each test and the data is gone

    def test_initial_data_from_migration_is_still_present(self):
        assert Question.objects.get(question_text="What is your favorite holiday?")
