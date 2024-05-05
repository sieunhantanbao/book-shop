from uuid import UUID
from schemas.image import Image
from sqlalchemy.orm import Session

def delete(db: Session, id: UUID):
    """ Delete an image

    Args:
        db (Session): _description_
        id (UUID): _description_

    Returns:
        _type_: True if success else False
    """
    try:
        image = db.query(Image).get(id)
        if image:
            db.delete(image)
            db.commit()
        return True, image.url
    except Exception:
        return False, None