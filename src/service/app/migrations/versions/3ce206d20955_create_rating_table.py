"""create rating table

Revision ID: 3ce206d20955
Revises: 0a55bd9e958e
Create Date: 2024-03-17 14:35:31.640755

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from uuid import UUID, uuid4


# revision identifiers, used by Alembic.
revision: str = '3ce206d20955'
down_revision: Union[str, None] = '0a55bd9e958e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    rating_tbl = op.create_table("ratings",
                    sa.Column('id', sa.UUID, nullable=False, primary_key=True),
                    sa.Column('user_id', sa.UUID, nullable=False),
                    sa.Column('book_id', sa.UUID, nullable=False),
                    sa.Column('comment', sa.String),
                    sa.Column('rating_value', sa.Float, nullable=False),
                    sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
                    sa.Column('updated_at', sa.DateTime),
                    sa.Column('is_reviewed', sa.Boolean, nullable=False, default=False))

    op.create_foreign_key("fk_rating_book", "ratings", "books", ['book_id'], ['id'])
    op.create_foreign_key('fk_rating_user', "ratings", "users", ['user_id'], ['id'])
    rating_data = [
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "This book opened my eyes to new perspectives.",
                "created_at": "2022-01-10 08:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely fantastic read! Highly recommended.",
                "created_at": "2022-02-15 12:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("FF03433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "A decent book, but could use more depth in storytelling.",
                "created_at": "2022-03-20 15:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "I enjoyed every chapter of this book. Great storytelling!",
                "created_at": "2022-04-25 10:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book is a masterpiece. Couldn't put it down!",
                "created_at": "2022-05-18 14:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("CB04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. Expected more from the author.",
                "created_at": "2022-06-02 09:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A thrilling adventure from start to finish. Loved it!",
                "created_at": "2022-07-12 11:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4F05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-written and thought-provoking. Recommended for all readers.",
                "created_at": "2022-08-30 13:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The plot was interesting, but the pacing felt off.",
                "created_at": "2022-09-22 16:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A must-read!",
                "created_at": "2022-10-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1506433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2022-07-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8F04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2022-08-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2022-09-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9B04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2022-10-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2022-11-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2022-12-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("AD04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2019-01-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("B304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2019-02-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("B904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2019-03-20 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("BF04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2019-04-12 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("C504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2019-05-05 14:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2019-06-12 12:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2019-07-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("DD04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2019-08-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("E304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2019-09-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("E904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2019-10-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("EF04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2019-11-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2019-12-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("FB04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The premise was interesting, but the execution fell flat.",
                "created_at": "2020-01-18 16:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A captivating and emotional journey. Highly recommended!",
                "created_at": "2020-02-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "Unfortunately, this book didn't resonate with me.",
                "created_at": "2022-11-05 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Incredible storytelling. I couldn't put it down!",
                "created_at": "2022-12-12 12:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "A great read with memorable characters.",
                "created_at": "2023-01-08 09:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The plot was confusing, and characters lacked depth.",
                "created_at": "2023-02-20 15:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1D04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book exceeded all my expectations. A true gem!",
                "created_at": "2023-03-18 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An average book. Not bad, but not exceptional either.",
                "created_at": "2023-04-10 14:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Captivating from the first page to the last. A must-read!",
                "created_at": "2023-05-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2F04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted storyline with unexpected twists.",
                "created_at": "2023-06-28 13:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Interesting premise, but execution fell short.",
                "created_at": "2023-07-18 16:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3B04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book left me speechless. A true masterpiece!",
                "created_at": "2023-08-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Struggled to connect with the characters. Disappointing.",
                "created_at": "2023-09-05 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4D04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book is a work of art. A must-read for every book lover!",
                "created_at": "2023-10-12 12:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2023-11-08 09:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it felt rushed in places.",
                "created_at": "2023-12-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5F04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Couldn't put it down. A gripping and emotional journey!",
                "created_at": "2022-01-18 10:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2022-02-22 14:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6B04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2022-03-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2022-04-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The premise was interesting, but the execution fell flat.",
                "created_at": "2022-05-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7D04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2022-06-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Struggled to connect with the characters. Disappointing.",
                "created_at": "2022-01-15 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book is a work of art. A must-read for every book lover!",
                "created_at": "2022-02-22 12:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2022-03-18 09:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1F05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it felt rushed in places.",
                "created_at": "2022-04-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Couldn't put it down. A gripping and emotional journey!",
                "created_at": "2022-05-18 10:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2B05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2022-06-22 14:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2022-07-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2022-08-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The premise was interesting, but the execution fell flat.",
                "created_at": "2022-09-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2022-10-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2023-09-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2023-10-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2023-11-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2023-12-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2021-01-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("AF05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2021-02-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("B505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2021-03-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("BB05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2021-04-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("C105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2021-05-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("C705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2021-06-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("CD05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2022-05-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1B06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2022-06-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2106433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2022-07-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2706433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2022-08-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2D06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2022-09-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3306433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2022-10-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3906433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2022-11-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3F06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2022-12-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4506433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2026-01-18 16:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4B06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2026-02-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5106433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2021-07-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2021-08-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("DF05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2021-09-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("E505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2021-10-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("EB05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2021-11-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2021-12-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2022-01-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("FD05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2022-02-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0306433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2022-03-20 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0906433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2022-04-12 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0F06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2022-11-05 14:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2022-12-12 12:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5B05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2023-01-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2023-02-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2023-03-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2023-04-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2023-05-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2023-06-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7F05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2023-07-18 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2023-08-10 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8B05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Struggled to connect with the characters. Disappointing.",
                "created_at": "2022-01-15 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book is a work of art. A must-read for every book lover!",
                "created_at": "2022-02-22 12:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("FF03433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2022-03-18 09:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it felt rushed in places.",
                "created_at": "2022-04-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Couldn't put it down. A gripping and emotional journey!",
                "created_at": "2022-05-18 10:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("CB04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2022-06-22 14:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2022-07-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4F05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2022-08-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The premise was interesting, but the execution fell flat.",
                "created_at": "2022-09-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2022-10-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1506433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2022-11-05 14:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2022-12-12 12:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2023-01-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2023-02-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1D04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2023-03-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2023-04-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2023-05-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2F04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2023-06-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2023-07-18 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3B04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2023-08-10 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2023-09-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4D04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2023-10-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2023-11-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2023-12-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5F04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2024-01-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2024-02-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6B04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2024-03-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2024-04-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2024-05-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7D04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2024-06-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2024-07-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8F04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2024-08-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2024-09-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9B04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2024-10-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2024-11-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2024-12-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("AD04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2025-01-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("B304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2025-02-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("B904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2025-03-20 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("BF04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2025-04-12 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("C504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2025-05-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D104433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2025-06-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D704433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2025-07-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("DD04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2025-08-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("E304433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2025-09-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("E904433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2025-10-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("EF04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2025-11-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F504433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2025-12-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("FB04433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2026-01-18 16:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2026-02-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2022-01-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2022-02-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2022-03-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1F05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2022-04-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2022-05-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2B05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2022-06-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2022-07-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2022-08-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2022-09-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2022-10-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2022-11-05 14:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2022-12-12 12:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5B05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2023-01-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2023-02-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2023-03-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("6D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2023-04-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2023-05-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2023-06-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("7F05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2023-07-18 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2023-08-10 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("8B05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2023-09-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2023-10-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("9D05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2023-11-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A305433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2023-12-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("A905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2024-01-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("AF05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2024-02-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("B505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2024-03-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("BB05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2024-04-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("C105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2024-05-18 16:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("C705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2024-06-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("CD05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "The storyline lacked coherence. Disappointing.",
                "created_at": "2024-07-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("D905433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Absolutely brilliant! I couldn't put it down.",
                "created_at": "2024-08-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("DF05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Engaging plot with well-developed characters.",
                "created_at": "2024-09-08 09:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("E505433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The book had its moments, but it didn't leave a lasting impression.",
                "created_at": "2024-10-20 15:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("EB05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A literary masterpiece. Bravo to the author!",
                "created_at": "2024-11-18 10:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F105433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "Mixed feelings about this one. Some parts were good, others not so much.",
                "created_at": "2024-12-22 14:20:00.000000",
                "is_reviewed": True,
                "user_id": UUID("F705433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "An absolute page-turner. I was hooked from the first chapter!",
                "created_at": "2025-01-12 11:35:00.000000",
                "is_reviewed": True,
                "user_id": UUID("FD05433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Thoroughly enjoyed the storyline and character development.",
                "created_at": "2025-02-28 13:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0306433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2025-03-20 16:05:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0906433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2025-04-12 10:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("0F06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 1,
                "comment": "This book was not my cup of tea. Couldn't get into it.",
                "created_at": "2025-05-05 15:00:00.000000",
                "is_reviewed": True,
                "user_id": UUID("1B06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A true page-turner. I couldn't stop reading!",
                "created_at": "2025-06-12 11:25:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2106433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "The characters were relatable, and the story kept me engaged.",
                "created_at": "2025-07-08 09:45:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2706433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "Disappointing. The plot lacked coherence.",
                "created_at": "2025-08-20 15:10:00.000000",
                "is_reviewed": True,
                "user_id": UUID("2D06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Simply outstanding. One of the best books I've ever read!",
                "created_at": "2025-09-18 10:30:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3306433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "The story had potential, but it left me wanting more.",
                "created_at": "2025-10-10 14:50:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3906433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "A gripping tale that kept me on the edge of my seat!",
                "created_at": "2025-11-22 11:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("3F06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Well-crafted plot with unexpected twists and turns.",
                "created_at": "2025-12-28 13:55:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4506433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 3,
                "comment": "An interesting read, but it didn't fully captivate me.",
                "created_at": "2026-01-18 16:15:00.000000",
                "is_reviewed": True,
                "user_id": UUID("4B06433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "This book touched my soul. A true masterpiece!",
                "created_at": "2026-02-10 10:40:00.000000",
                "is_reviewed": True,
                "user_id": UUID("5106433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Testing",
                "created_at": "2024-02-05 10:28:16.328931",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Very goooooooooooooooood",
                "created_at": "2024-02-26 05:37:50.594478",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Nice",
                "created_at": "2024-02-26 05:37:50.594478",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 2,
                "comment": "very bad book",
                "created_at": "2024-02-26 07:32:27.451504",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "A nice book to read",
                "created_at": "2024-02-26 07:32:27.451504",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("9506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 5,
                "comment": "Anh Nguyen Test approve comment",
                "created_at": "2024-02-26 07:54:45.447945",
                "is_reviewed": True,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            },
            {
                "id": uuid4(),
                "rating_value": 4,
                "comment": "Testing one more",
                "created_at": "2024-02-26 07:54:45.447945",
                "is_reviewed": False,
                "user_id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5")
            }
    ]
    op.bulk_insert(rating_tbl, rating_data)
    
def downgrade() -> None:
    op.drop_table("ratings")