from django.test import TestCase
from microblogs.models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        '@johndoe',
        first_name = 'John',
        last_name = 'Doe',
        email = 'johndoe@example.org',
        password = 'password123',
        bio = 'The quick brown fox jumps over the lazy dog.'

        )

    def test_valid_user(self):

        self._assert_user_is_valid()

    def test_username_can_not_be_blank(self):

        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' *29
        self._assert_user_is_valid()

    def test_username_must_be_unique(self):
        User.objects.create_user(
        '@janedoe',
        first_name = 'Jane',
        last_name = 'Doe',
        email = 'janedoe@example.org',
        password = 'password1234',
        bio = 'The quick brown fox jumps over the lazy  bug dog.'

        )
        self.user.username = '@janedoe'
        self._assert_user_is_invalid()

    def test_username_starts_with_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' *30
        self._assert_user_is_invalid()

    def test_username_must_contain_only_three_alphanumericals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_must_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self._assert_user_is_invalid()

    def test_first_name_must_not_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_first_name_can_be_repeated(self):
        User.objects.create_user(
        '@Bradedoe',
        first_name = 'Brad',
        last_name = 'Doe',
        email = 'braddoe@example.org',
        password = 'password12345',
        bio = 'I am the famous brad'

        )
        self.user.first_name = 'Brad'
        self._assert_user_is_valid()

    def test_first_name_can_be_50_characters_long(self):
        self.user.first_name = 'x' *50
        self._assert_user_is_valid()

    def test_first_name_can_not_be_longer_50_characters_long(self):
        self.user.first_name = 'x' *51
        self._assert_user_is_invalid()

    def test_last_name_must_not_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_firs_name_can_be_repeated(self):
        User.objects.create_user(
        '@Bendon',
        first_name = 'Ben',
        last_name = 'Don',
        email = 'bendon@example.org',
        password = 'password1245',
        bio = 'I am the famous ben'

        )
        self.user.last_name = 'Don'
        self._assert_user_is_valid()

    def test_last_name_can_be_longer_50_characters_long(self):
        self.user.last_name = 'x' *50
        self._assert_user_is_valid()

    def test_last_name_can_not_be_longer_50_characters_long(self):
        self.user.last_name = 'x' *51
        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        User.objects.create_user(
        '@Bendoe',
        first_name = 'Ben',
        last_name = 'Doe',
        email = 'bendoe@example.org',
        password = 'password123345',
        bio = 'I am the famous ben doe'

        )
        self.user.email = 'bendoe@example.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@example.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_at_symbol(self):
        self.user.email = 'johndoe.example.org'
        self._assert_user_is_invalid()

    def test_email_must_contain_domain_name(self):
        self.user.email = 'johndoe@example'
        self._assert_user_is_invalid()

    def test_email_must_contain_more_than_one_at(self):
        self.user.email = 'johndoe@@example.org'
        self._assert_user_is_invalid()

    def tes_bio_may_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def tes_bio_need_not_be_unique(self):
        User.objects.create_user(
        '@Bethdon',
        first_name = 'Beth',
        last_name = 'Don',
        email = 'bethdon@example.org',
        password = 'password1245',
        bio = 'I am the famous beth'

        )
        self.user.bio = 'I am the famous beth'
        self._assert_user_is_valid()

    def tes_bio_may_be_520_characters_long(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def tes_bio_may_not_be_520_characters_long(self):
        self.user.bio = 'x' * 521
        self._assert_user_is_invalid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')


    def _assert_user_is_invalid(self):

        with self.assertRaises(ValidationError):
            self.user.full_clean()
