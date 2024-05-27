"""create wishlist table

Revision ID: 400578f219d9
Revises: 5888486f9e55
Create Date: 2024-03-17 14:46:56.426534

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '400578f219d9'
down_revision: Union[str, None] = '5888486f9e55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("wishlists",
                    sa.Column('id', sa.UUID, nullable=False, primary_key=True),
                    sa.Column('user_id', sa.UUID, nullable=False),
                    sa.Column('book_id', sa.UUID, nullable=False),
                    sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
                    sa.Column('updated_at', sa.DateTime)
                    )

    op.create_foreign_key("fk_wishlist_user", "wishlists", "users", ['user_id'], ['id'])
    op.create_foreign_key("fk_wishlist_book", "wishlists", "books", ['book_id'], ['id'])
    
def downgrade() -> None:
    op.drop_table("wishlists")