"""create user table

Revision ID: 0a55bd9e958e
Revises: b58635ce7d96
Create Date: 2024-03-17 14:26:53.035647

"""
from typing import Sequence, Union
from datetime import datetime
import os
from uuid import UUID
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

# revision identifiers, used by Alembic.
revision: str = '0a55bd9e958e'
down_revision: Union[str, None] = 'b58635ce7d96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    usr_tbl = op.create_table("users",
                    sa.Column('id', sa.UUID, nullable=False, primary_key=True),
                    sa.Column('email', sa.String, unique=True, nullable=False),
                    sa.Column('password', sa.String),
                    sa.Column('first_name', sa.String, nullable=False),
                    sa.Column('last_name', sa.String, nullable=False),
                    sa.Column('date_of_birth', sa.DateTime),
                    sa.Column('photo_url', sa.String),
                    sa.Column('telephone', sa.String),
                    sa.Column('address', sa.String),
                    sa.Column('experience_in', sa.String),
                    sa.Column('addition_detail', sa.String),
                    sa.Column('is_active', sa.Boolean, nullable=False, default=True),
                    sa.Column('is_admin', sa.Boolean, nullable=False, default=False),
                    sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
                    sa.Column('updated_at', sa.DateTime))
    # Bulk insert
    usr_admin_data = [
        {
            "id": UUID("F903433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "nguyensieuanh@gmail.com",
            "first_name":"Anh",
            "last_name":"Nguyen",
            "is_admin": True,
            "password": generate_password_hash(os.environ['DEFAULT_ADMIN_PASSWORD'])
        }
    ]
    op.bulk_insert(usr_tbl, usr_admin_data)
    
    usr_data = [
        {
            "id": UUID("FF03433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user1@example.com",
            "first_name":"John",
            "last_name":"Doe"
        },
        {
            "id": UUID("4704433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user2@example.com",
            "first_name":"Jane",
            "last_name":"Smith"
        },
        {
            "id": UUID("8904433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user3@example.com",
            "first_name":"Michael",
            "last_name":"Johnson"
        },
        {
            "id": UUID("CB04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user4@example.com",
            "first_name":"Emily",
            "last_name":"Williams"
        },
        {
            "id": UUID("0D05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user5@example.com",
            "first_name":"Daniel",
            "last_name":"Brown"
        },
        {
            "id": UUID("4F05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user6@example.com",
            "first_name":"Olivia",
            "last_name":"Jones"
        },
        {
            "id": UUID("9105433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user7@example.com",
            "first_name":"Matthew",
            "last_name":"Davis"
        },
        {
            "id": UUID("D305433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user8@example.com",
            "first_name":"Sophia",
            "last_name":"Miller"
        },
        {
            "id": UUID("1506433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user9@example.com",
            "first_name":"Christopher",
            "last_name":"Garcia"
        },
        {
            "id": UUID("0504433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user10@example.com",
            "first_name":"Emma",
            "last_name":"Martinez"
        },
        {
            "id": UUID("1104433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user11@example.com",
            "first_name":"Nicholas",
            "last_name":"Rodriguez"
        },
        {
            "id": UUID("1704433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user12@example.com",
            "first_name":"Ava",
            "last_name":"Hernandez"
        },
        {
            "id": UUID("1D04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user13@example.com",
            "first_name":"Andrew",
            "last_name":"Lopez"
        },
        {
            "id": UUID("2304433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user14@example.com",
            "first_name":"Isabella",
            "last_name":"Lee"
        },
        {
            "id": UUID("2904433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user15@example.com",
            "first_name":"Joseph",
            "last_name":"Perez"
        },
        {
            "id": UUID("2F04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user16@example.com",
            "first_name":"Amelia",
            "last_name":"Gonzalez"
        },
        {
            "id": UUID("3504433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user17@example.com",
            "first_name":"William",
            "last_name":"Wilson"
        },
        {
            "id": UUID("3B04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user18@example.com",
            "first_name":"Sophie",
            "last_name":"Anderson"
        },
        {
            "id": UUID("4104433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user19@example.com",
            "first_name":"Benjamin",
            "last_name":"Taylor"
        },
        {
            "id": UUID("4D04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user20@example.com",
            "first_name":"Mia",
            "last_name":"Moore"
        },
        {
            "id": UUID("5304433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user21@example.com",
            "first_name":"Ethan",
            "last_name":"Jackson"
        },
        {
            "id": UUID("5904433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user22@example.com",
            "first_name":"Ella",
            "last_name":"White"
        },
        {
            "id": UUID("5F04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user23@example.com",
            "first_name":"Alexander",
            "last_name":"Wright"
        },
        {
            "id": UUID("6504433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user24@example.com",
            "first_name":"Grace",
            "last_name":"Walker"
        },
        {
            "id": UUID("6B04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user25@example.com",
            "first_name":"Liam",
            "last_name":"Turner"
        },
        {
            "id": UUID("7104433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user26@example.com",
            "first_name":"Chloe",
            "last_name":"Clark"
        },
        {
            "id": UUID("7704433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user27@example.com",
            "first_name":"Daniel",
            "last_name":"Hill"
        },
        {
            "id": UUID("7D04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user28@example.com",
            "first_name":"Avery",
            "last_name":"Hall"
        },
        {
            "id": UUID("8304433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user29@example.com",
            "first_name":"David",
            "last_name":"Baker"
        },
        {
            "id": UUID("8F04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user30@example.com",
            "first_name":"Scarlett",
            "last_name":"Adams"
        },
        {
            "id": UUID("9504433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user31@example.com",
            "first_name":"James",
            "last_name":"Cook"
        },
        {
            "id": UUID("9B04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user32@example.com",
            "first_name":"Abigail",
            "last_name":"Rivera"
        },
        {
            "id": UUID("A104433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user33@example.com",
            "first_name":"Aiden",
            "last_name":"Evans"
        },
        {
            "id": UUID("A704433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user34@example.com",
            "first_name":"Sofia",
            "last_name":"Bennett"
        },
        {
            "id": UUID("AD04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user35@example.com",
            "first_name":"Samuel",
            "last_name":"Perry"
        },
        {
            "id": UUID("B304433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user36@example.com",
            "first_name":"Hannah",
            "last_name":"Bell"
        },
        {
            "id": UUID("B904433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user37@example.com",
            "first_name":"Christopher",
            "last_name":"Cruz"
        },
        {
            "id": UUID("BF04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user38@example.com",
            "first_name":"Lily",
            "last_name":"Edwards"
        },
        {
            "id": UUID("C504433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user39@example.com",
            "first_name":"Logan",
            "last_name":"Fisher"
        },
        {
            "id": UUID("D104433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user40@example.com",
            "first_name":"Addison",
            "last_name":"Cooper"
        },
        {
            "id": UUID("D704433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user41@example.com",
            "first_name":"Jackson",
            "last_name":"Kelly"
        },
        {
            "id": UUID("DD04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user42@example.com",
            "first_name":"Madison",
            "last_name":"Ward"
        },
        {
            "id": UUID("E304433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user43@example.com",
            "first_name":"Carter",
            "last_name":"Cox"
        },
        {
            "id": UUID("E904433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user44@example.com",
            "first_name":"Aubrey",
            "last_name":"Richardson"
        },
        {
            "id": UUID("EF04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user45@example.com",
            "first_name":"Logan",
            "last_name":"Fisher"
        },
        {
            "id": UUID("F504433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user46@example.com",
            "first_name":"Evelyn",
            "last_name":"Morgan"
        },
        {
            "id": UUID("FB04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user47@example.com",
            "first_name":"Gabriel",
            "last_name":"Reed"
        },
        {
            "id": UUID("0105433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user48@example.com",
            "first_name":"Zoe",
            "last_name":"Peters"
        },
        {
            "id": UUID("0705433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user49@example.com",
            "first_name":"Isaac",
            "last_name":"Watson"
        },
        {
            "id": UUID("1305433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user50@example.com",
            "first_name":"Harper",
            "last_name":"Gordon"
        },
        {
            "id": UUID("1905433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user51@example.com",
            "first_name":"Owen",
            "last_name":"Ramirez"
        },
        {
            "id": UUID("1F05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user52@example.com",
            "first_name":"Brooklyn",
            "last_name":"Harrison"
        },
        {
            "id": UUID("2505433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user53@example.com",
            "first_name":"Leo",
            "last_name":"Ferguson"
        },
        {
            "id": UUID("2B05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user54@example.com",
            "first_name":"Eleanor",
            "last_name":"Morrison"
        },
        {
            "id": UUID("3105433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user55@example.com",
            "first_name":"Mason",
            "last_name":"Nelson"
        },
        {
            "id": UUID("3705433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user56@example.com",
            "first_name":"Addison",
            "last_name":"Knight"
        },
        {
            "id": UUID("3D05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user57@example.com",
            "first_name":"Dylan",
            "last_name":"Hudson"
        },
        {
            "id": UUID("4305433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user58@example.com",
            "first_name":"Peyton",
            "last_name":"Bowman"
        },
        {
            "id": UUID("4905433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user59@example.com",
            "first_name":"Nathan",
            "last_name":"Webb"
        },
        {
            "id": UUID("5505433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user60@example.com",
            "first_name":"Aria",
            "last_name":"Bishop"
        },
        {
            "id": UUID("5B05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user61@example.com",
            "first_name":"Sawyer",
            "last_name":"Scott"
        },
        {
            "id": UUID("6105433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user62@example.com",
            "first_name":"Ellie",
            "last_name":"Murray"
        },
        {
            "id": UUID("6705433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user63@example.com",
            "first_name":"Caleb",
            "last_name":"Davidson"
        },
        {
            "id": UUID("6D05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user64@example.com",
            "first_name":"Claire",
            "last_name":"Holmes"
        },
        {
            "id": UUID("7305433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user65@example.com",
            "first_name":"Julian",
            "last_name":"Sanders"
        },
        {
            "id": UUID("7905433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user66@example.com",
            "first_name":"Madelyn",
            "last_name":"Walters"
        },
        {
            "id": UUID("7F05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user67@example.com",
            "first_name":"Harrison",
            "last_name":"Fuller"
        },
        {
            "id": UUID("8505433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user68@example.com",
            "first_name":"Layla",
            "last_name":"Hartman"
        },
        {
            "id": UUID("8B05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user69@example.com",
            "first_name":"Hudson",
            "last_name":"Owens"
        },
        {
            "id": UUID("9705433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user70@example.com",
            "first_name":"Scarlet",
            "last_name":"Vasquez"
        },
        {
            "id": UUID("9D05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user71@example.com",
            "first_name":"Gabriel",
            "last_name":"York"
        },
        {
            "id": UUID("A305433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user72@example.com",
            "first_name":"Eva",
            "last_name":"Gibson"
        },
        {
            "id": UUID("A905433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user73@example.com",
            "first_name":"Justin",
            "last_name":"Barnes"
        },
        {
            "id": UUID("AF05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user74@example.com",
            "first_name":"Lillian",
            "last_name":"Fleming"
        },
        {
            "id": UUID("B505433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user75@example.com",
            "first_name":"Cameron",
            "last_name":"Fletcher"
        },
        {
            "id": UUID("BB05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user76@example.com",
            "first_name":"Lucy",
            "last_name":"Wheeler"
        },
        {
            "id": UUID("C105433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user77@example.com",
            "first_name":"Jeremiah",
            "last_name":"Saunders"
        },
        {
            "id": UUID("C705433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user78@example.com",
            "first_name":"Adeline",
            "last_name":"Dunn"
        },
        {
            "id": UUID("CD05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user79@example.com",
            "first_name":"Jonathan",
            "last_name":"Hogan"
        },
        {
            "id": UUID("D905433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user80@example.com",
            "first_name":"Aubrey",
            "last_name":"Hart"
        },
        {
            "id": UUID("DF05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user81@example.com",
            "first_name":"Maxwell",
            "last_name":"Hopkins"
        },
        {
            "id": UUID("E505433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user82@example.com",
            "first_name":"Paisley",
            "last_name":"Fisher"
        },
        {
            "id": UUID("EB05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user83@example.com",
            "first_name":"Carter",
            "last_name":"Mendez"
        },
        {
            "id": UUID("F105433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user84@example.com",
            "first_name":"Aaliyah",
            "last_name":"Perry"
        },
        {
            "id": UUID("F705433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user85@example.com",
            "first_name":"Jaxon",
            "last_name":"Wood"
        },
        {
            "id": UUID("FD05433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user86@example.com",
            "first_name":"Hailey",
            "last_name":"Mason"
        },
        {
            "id": UUID("0306433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user87@example.com",
            "first_name":"Eli",
            "last_name":"Warren"
        },
        {
            "id": UUID("0906433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user88@example.com",
            "first_name":"Aurora",
            "last_name":"Bates"
        },
        {
            "id": UUID("0F06433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user89@example.com",
            "first_name":"Oscar",
            "last_name":"Baldwin"
        },
        {
            "id": UUID("1B06433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user90@example.com",
            "first_name":"Leah",
            "last_name":"Keller"
        },
        {
            "id": UUID("2106433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user91@example.com",
            "first_name":"Santiago",
            "last_name":"Stephens"
        },
        {
            "id": UUID("2706433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user92@example.com",
            "first_name":"Skylar",
            "last_name":"Vargas"
        },
        {
            "id": UUID("2D06433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user93@example.com",
            "first_name":"Tristan",
            "last_name":"Bishop"
        },
        {
            "id": UUID("3306433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user94@example.com",
            "first_name":"Sienna",
            "last_name":"Montgomery"
        },
        {
            "id": UUID("3906433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user95@example.com",
            "first_name":"Bentley",
            "last_name":"Dickson"
        },
        {
            "id": UUID("3F06433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user96@example.com",
            "first_name":"Audrey",
            "last_name":"Bowen"
        },
        {
            "id": UUID("4506433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user97@example.com",
            "first_name":"Ezekiel",
            "last_name":"Gibbs"
        },
        {
            "id": UUID("4B06433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user98@example.com",
            "first_name":"Harper",
            "last_name":"Gordon"
        },
        {
            "id": UUID("5106433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user99@example.com",
            "first_name":"Gavin",
            "last_name":"Newton"
        },
        {
            "id": UUID("0B04433E-F36B-1410-922A-00CC96E21CB5"),
            "email": "user100@example.com",
            "first_name":"Avery",
            "last_name":"Morton"
        }
    ]
    op.bulk_insert(usr_tbl, usr_data)
    
def downgrade() -> None:
    op.drop_table("users")
