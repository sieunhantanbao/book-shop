"""create bookrelation table

Revision ID: bdc75d478455
Revises: 400578f219d9
Create Date: 2024-03-17 14:52:16.816153

"""
from typing import Sequence, Union
from datetime import datetime
from uuid import UUID, uuid4
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdc75d478455'
down_revision: Union[str, None] = '400578f219d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    book_relation_tbl = op.create_table("book_relations",
                    sa.Column('id', sa.UUID, nullable=False, primary_key=True),
                    sa.Column('book_id_1', sa.UUID, nullable=False),
                    sa.Column("book_id_2", sa.UUID, nullable=False),
                    sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
                    sa.Column('updated_at', sa.DateTime))
    op.create_foreign_key("fb_book_id_1", "book_relations", "books", ['book_id_1'], ['id'])
    op.create_foreign_key("fb_book_id_2", "book_relations", "books", ['book_id_2'], ['id'])

    book_relation_data = [
        {
            "id": uuid4(),
            "book_id_1": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5906433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5906433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("6906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5906433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("5906433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("8506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("8D06433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("8506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("9506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("9906433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("9506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("A506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("A906433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("B506433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
        },
        {
            "id": uuid4(),
            "book_id_1": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5"),
            "book_id_2": UUID("B906433E-F36B-1410-922A-00CC96E21CB5")
        }
    ]
    op.bulk_insert(book_relation_tbl, book_relation_data)
    
def downgrade() -> None:
    op.drop_table("book_relations")