"""
Adapters bridges the typer commands with the application use cases.
"""

from pathlib import Path

from sqlalchemy.orm import Session
from toolcat.database import Database

from housenomics.application.import_transactions import ServiceImportTransactions
from housenomics.application.repositories.transactions import Transactions
from housenomics.application.views.transactions import ViewTransactions
from housenomics.infrastructure.gateway_cgd_file import GatewayCGDFile

database_path = Path.home() / Path("Library/Application Support/Housenomics")


def report(seller, since, on):
    with Session(Database(database_path).engine) as session:
        view = ViewTransactions(session, seller, since, on)

    transactions, total = view.data
    if not seller:
        if not transactions:
            print("Could not find any transactions!")
            return

        for t in transactions:
            print(f"Description: '{t['description']:>22}', Value: {t['value']:>10}")
        return

    print(f"Description: '{seller}', Value: {round(total, 2)}")


def migrate_database():
    Database(database_path, Path("migrations/0001 - Initial.sql"))


def reset():
    db = Database(database_path)
    db.remove()


def import_file(file_path: Path):
    with Session(Database(database_path).engine) as session:
        gateway_cgd = GatewayCGDFile(file_path)
        transactions = Transactions(session)
        ServiceImportTransactions(gateway_cgd, transactions).execute()
        session.commit()
