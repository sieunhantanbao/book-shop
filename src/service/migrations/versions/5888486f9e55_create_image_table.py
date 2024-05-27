"""create image table

Revision ID: 5888486f9e55
Revises: 3ce206d20955
Create Date: 2024-03-17 14:42:29.983827

"""
from typing import Sequence, Union
from uuid import UUID, uuid4
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '5888486f9e55'
down_revision: Union[str, None] = '3ce206d20955'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    img_tbl = op.create_table("images",
                    sa.Column('id', sa.UUID, nullable=False, primary_key=True),
                    sa.Column('book_id', sa.UUID, nullable=True),
                    sa.Column('category_id', sa.UUID, nullable=True),
                    sa.Column('url', sa.String, nullable=False),
                    sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
                    sa.Column('updated_at', sa.DateTime)
                    )
    op.create_foreign_key("fk_image_book", "images", "books", ['book_id'], ['id'])
    op.create_foreign_key("fk_image_category", "images", "categories", ['category_id'], ['id'])
    
    # Bulk insert data for Category
    cat_data = [
                {
                    "id": uuid4(),
                    "category_id": UUID("D967C683-7A87-4583-A849-4E8DE8A190E2"),
                    "url": "3d2ccf6c-2c08-4f08-b87d-aeb5676ea791_children_book_cat.jpg"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("C4028EA3-29F3-4E57-BBE6-17EE8A172564"),
                    "url": "7833cada-2ee0-42da-a917-436d8f171793_animal_books_cat.jpg"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("3DC81F23-1691-437C-AB95-19E77781A19A"),
                    "url": "a5b169a2-ba6f-4101-bd70-0b388389b38f_science_book_cat.jpg"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("D62FD3DD-D186-45B8-B0BB-188BE89E5430"),
                    "url": "2144dfd4-b75d-4a5a-9bc8-ab198c283f0b_universe_book_cat.jpg"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("7328775F-F4EB-49C1-9CC3-B344CC6C7EA3"),
                    "url": "1512398a-114f-4a9d-8eaf-bd6118a1ab1f_the_world_cat.png"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("3786AB21-B10B-47BF-86C8-0F425CC1D4DB"),
                    "url": "1704d6c1-277f-4a31-abb6-bc67e8feb21b_technology_book_cat.jpg"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("274425A6-610F-403B-91E5-5C1A3D926E09"),
                    "url": "89c4685f-71f0-41aa-9566-8cfa7fe5f0dd_travelling_book_cat.jpg"
                },
                {
                    "id": uuid4(),
                    "category_id": UUID("F7570BE3-3C99-46D7-A4DD-656E3F1EDA71"),
                    "url": "09f20667-93fc-4e92-9040-fb7552059723_fiction_book_cat.jpg"
                }
    ]
    op.bulk_insert(img_tbl, cat_data)
    
    # Bulk insert data for Book
    book_data = [
            {
                "id": uuid4(),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "c99fe328-f953-44a9-8d8c-35c414707de8_img150_1_5.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "2ce6e3b4-6d78-4522-8161-a14ad36dc0ff_Anthony-Peake-Hidden-Universe-1536x1190.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "86f3031b-827f-44cf-9e96-e303234bd972_Beyond-the-Horizon-Kindle-768x1172.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "5c355041-aeaf-4265-9441-44d53c3961df_abc.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "262963c1-5cef-42e8-829d-a0379ceb6943_the-codebreakers-9781439103555_hr.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "99a26872-43f1-47c2-8d35-897c88e2cd6a_culinary-delights.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "823c133e-e980-4a7b-9940-446210548ff6_infinite-possibilities.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "ff0a75eb-e90f-4fe8-a86f-96378118c347_secrets-of-the-ancient-world.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "338767ab-dba5-4f26-9e62-f31816c3885f_tech-titans.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "89c32762-f464-46ff-9fe2-7362875b439e_the-art-of-mindfulness.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "290e44ff-701f-4b03-bf33-46f199af7d5e_quantum-leap.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("8106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "ccd08066-4a43-4d3a-a24a-5e939bf8fdbf_element_of_art.png"
            },
            {
                "id": uuid4(),
                "book_id": UUID("8506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "7d38cffe-dee5-4b93-8980-6a6aee6771c1_The_Culmination.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("8906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "ce21fc3c-fdf9-484b-939f-7d09593fc3ce_Gastronomic_Adventures.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("8D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "6331048f-9cdb-4faa-a422-0721d90b53b6_The-Quantum-Code-by-Mark-Langlois.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("9106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "222cf726-85ea-43ba-b78f-bb0b1aad1054_epic_love_story.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("9506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "7768bce5-5ea8-46b6-a6ac-311f88c1057c_the_renaissance.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("9906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "972b52a3-f2c8-4142-9229-586af06af228_Uncharted_Territories.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("9D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "b738da04-5eca-4ca9-bd8c-6913e9e1f31c_The_Science_of_Happiness.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("A106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "a3dd4fe4-0e3b-4737-a2fe-5aa8e0468be7_Mysteries_of_the_Deep.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("A506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "aa0c242b-b72a-43bc-8a65-f5a50a3a0eab_The_Art_of_War.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("A906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "746558a8-1e08-4850-b6c8-6bbfd53e45b0_Into_the_Unknown.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("AD06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "a8ab710f-106e-4b6f-a685-97ce6021cdc1_Enchanted_Realms.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("B106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "c19d9e82-1d0f-4c76-ada0-8b5739b90f17_The_Culinary_Explorer.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("B506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "2f05bcd8-5d90-4add-a217-eca36e49099e_The_Quantum_Enigma.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("B906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "df44303c-074e-4e05-bfa5-d172ce740c9f_Love_Beyond_Time.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "d8e27003-9e59-4a9f-9c56-5e0896a11d99_10-van-cau-hoi-vi-sao-khoa-hoc-quanh-ta-1.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "04567f15-c830-49d3-8832-cfb4126056b7_10-van-cau-hoi-vi-sao-khoa-hoc-quanh-ta-1-3.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "89368cf6-23de-4f4d-8530-978e3fc68297_10-van-cau-hoi-vi-sao-khoa-hoc-quanh-ta-1-4.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "f41ae170-19a3-41a2-b6be-bf4d11378a73_10-van-cau-hoi-vi-sao-khoa-hoc-quanh-ta-1-5.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "3544b08c-ba4b-4889-a6d1-4e0b433ef7a9_s-l1600.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "651722f0-bd01-472e-b111-4403a2ffbf4e_9781598110227-us.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("5D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "e01e2209-3147-4c48-bf4a-cc0bd3f552f5_9781598110228-us.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "d88007b5-06ae-4b6b-937e-a9eb4f18d7a6_81NkwVcCb6L._AC_UF10001000_QL80_.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "a7302bb2-0c5c-4226-bd81-beaea0f54942_293657297-352-k690576.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "ea1fd843-1fbd-49fc-b278-ced3e68a49db_B12504212016__86387.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "688748f8-7d51-49e6-a08e-43d1d5fb8f6c_GUEST_fe2c9bee-ed52-4694-8b65-e4ca24d11ca0.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "b6bb503a-0981-4454-aec4-c9f4c6016a1f_images_code_breaker.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "cfc01be9-1f17-4395-a76f-2b0ac6c0e638_large-27333.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "179d66f3-4c40-457c-ba44-f1d63fb5ef00_51tX8FmA3UL.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "8e7b0509-4237-4f65-8f85-de088ff5beeb_71x3svgAFQL._AC_UF10001000_QL80_.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "47221b72-362c-4617-b490-89fd15faaa6e_41l4jx3b9DL.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "c296e38a-d811-4d91-9ad8-c026edf5e7a8_41Nj6J1twQL.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("6D06433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "61a4eeac-8a50-4155-a42b-7b76f5b9815a_c22ae81e-a460-4b8c-9f5f-35f64f1b19d8.__CR0012801280_PT0_SX300_V1___.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "189a936a-33aa-422e-98f5-58bf675c0877_51ZNF8OcXRL._AC_UF10001000_QL80_.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7106433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "51660908-1e8e-4f80-909a-38db5b4d3119_663964.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "42118f94-47dc-4fd5-af86-6a164f706994_51X7EQ68QML.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7506433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "b3c2cfc8-0825-459a-af8c-48b4c2c783b8_images_001.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "35b4d141-6155-4470-a8b6-63b4170b0b91_31NLPQVTVL.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "820fa6fa-e535-4b44-a8b3-ad8071d07436_41oF35FanwL.jpg"
            },
            {
                "id": uuid4(),
                "book_id": UUID("7906433E-F36B-1410-922A-00CC96E21CB5"),
                "url": "f89e1e4d-da9d-4235-af4e-9db57ac2366e_81ayyvWVVCL._AC_UF8941000_QL80_.jpg"
            }
    ]
    op.bulk_insert(img_tbl, book_data)
def downgrade() -> None:
    op.drop_table("images")