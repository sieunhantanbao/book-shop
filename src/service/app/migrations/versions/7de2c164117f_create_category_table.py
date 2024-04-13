"""create category table

Revision ID: 7de2c164117f
Revises: 
Create Date: 2024-03-17 13:36:48.717253

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from uuid import UUID


# revision identifiers, used by Alembic.
revision: str = '7de2c164117f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    cat_tbl =   op.create_table("categories", 
                    sa.Column('id', sa.UUID, primary_key=True, nullable= False),
                    sa.Column('name', sa.String, nullable=False),
                    sa.Column('slug', sa.String, nullable=False),
                    sa.Column('short_description', sa.String, nullable=False),
                    sa.Column('thumbnail_url', sa.String),
                    sa.Column('sort_order', sa.Integer),
                    sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
                    sa.Column('updated_at', sa.DateTime, nullable=True))

    # Bulk insert sample data
    data = [
            {
                "id": UUID("D967C683-7A87-4583-A849-4E8DE8A190E2"),
                "name": "Children Books",
                "slug": "children-books",
                "short_description": "This is description for children book category",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("C4028EA3-29F3-4E57-BBE6-17EE8A172564"),
                "name": "Animals Books",
                "slug": "animals-books",
                "short_description": "This is description for animals book category",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("3DC81F23-1691-437C-AB95-19E77781A19A"),
                "name": "Science Books",
                "slug": "science-books",
                "short_description": "This is description for Science book category",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("D62FD3DD-D186-45B8-B0BB-188BE89E5430"),
                "name": "Universe Books",
                "slug": "universe-books",
                "short_description": "This is description for Universe book category",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("7328775F-F4EB-49C1-9CC3-B344CC6C7EA3"),
                "name": "The World Books",
                "slug": "the-world-books",
                "short_description": "This is description for the world book category",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("3786AB21-B10B-47BF-86C8-0F425CC1D4DB"),
                "name": "Technology Books",
                "slug": "technology-books",
                "short_description": "This is a category for Technologies",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("274425A6-610F-403B-91E5-5C1A3D926E09"),
                "name": "Travelling Books",
                "slug": "travelling-books",
                "short_description": "This is a category for Travelling",
                "sort_order": 0,
                "created_at": datetime.now()
            },
            {
                "id": UUID("F7570BE3-3C99-46D7-A4DD-656E3F1EDA71"),
                "name": "Fictions Books",
                "slug": "fictions-books",
                "short_description": "This is the category for fiction books",
                "sort_order": 0,
                "created_at": datetime.now()
            }
    ]

    op.bulk_insert(cat_tbl, data)

def downgrade() -> None:
    op.drop_table("categories")
    