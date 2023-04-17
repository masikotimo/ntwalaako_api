from abc import ABC as AbstractClass


class AbstractAccountManager(AbstractClass):
    _account_creator: None

    def set_account_creator(self, account_creator):
        self._account_creator = account_creator

    def get_account_creator(self):
        return self._account_creator
