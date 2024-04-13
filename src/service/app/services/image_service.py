# from uuid import UUID
# from ..schemas.image import Image
# from sqlalchemy.orm import Session

# def delete(db: Session, id:UUID):
#     """ Delete an image by Id

#     Args:
#         db (Session): Db context
#         id (UUID): Id of the image

#     Returns:
#         _type_: _description_
#     """
#     try:
#         image = db.query(Image).get(id)
#         if image:
#             db.delete(image)
#             db.commit()
#         return True, image.url
#     except Exception as e:
#         print(e)
#         return False, None