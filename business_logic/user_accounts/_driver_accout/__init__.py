from ._account_manager import AccountCreator
from business_logic.user_accounts._abstract_account_manager import AbstractAccountManager


class AccountManager(AbstractAccountManager):

    # Operations
    def register_driver(self, request):
        self.set_account_creator(AccountCreator())
        return self._account_creator.create(request)
