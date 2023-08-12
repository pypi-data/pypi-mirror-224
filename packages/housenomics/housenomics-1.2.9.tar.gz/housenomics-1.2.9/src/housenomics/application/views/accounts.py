from toolcat.database import text

from housenomics.application.views.views import View


class AccountsView(View):
    def __init__(self, session) -> None:
        self._session = session

    @property
    def data(self):
        sql_stmt = """
            SELECT account.name as name,
                   balance.value as balance
              FROM account
         LEFT JOIN balance
                ON account.id = balance.account_id
        """
        rows = self._session.execute(text(sql_stmt))
        return [
            {"name": row[0], "balance": row[1] if row[1] else "0.00"} for row in rows
        ]
