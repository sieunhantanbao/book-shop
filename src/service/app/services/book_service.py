# from uuid import UUID
# from flask import Request
# from app.website.models.validations.book_validation import BookCreateForm
# from app.website.models.validations.category_validation import CategoryCreateForm
# from app.website.utilities.extensions import allowed_file, upload_file
# from ..schemas.book import Book
# from ..schemas.image import Image
# from ..schemas.category import Category
# from datetime import datetime
# from slugify import slugify
# from sqlalchemy.orm import Session

# def get_by_id(db: Session, book_id:UUID) -> Book:
#     """ Get book by Id

#     Args:
#         db (Session): Db context
#         book_id (UUID): Book Id

#     Returns:
#         Book: A book
#     """
#     return db.query(Book).get(book_id)

# def get_all(db: Session) -> list[Book]:
#     """ Get all books

#     Args:
#         db (Session): Db context

#     Returns:
#         list[Book]: A list of books
#     """
#     books = db.query(Book).all()
#     return books


# def create(db: Session, form:BookCreateForm, request:Request):
#     """ Create a new book

#     Args:
#         db (Session): Db context
#         form (BookCreateForm): Form data
#         request (Request): Request data
#     """
#     new_book = Book(title = form.title.data,
#                     short_description = form.short_description.data,
#                     slug = slugify(form.title.data),
#                     price = form.price.data,
#                     description = form.description.data,
#                     isbn = form.isbn.data,
#                     author = form.author.data,
#                     publisher = form.publisher.data,
#                     pages = form.pages.data,
#                     dimensions = form.dimensions.data,
#                     language = form.language.data,
#                     is_featured = True if request.form.get('is_featured') == 'on' else False,
#                     created_at = datetime.now(),
#                     category_id = form.category_id.data
#                     )
#     publish_date = request.form.get('publish_date')
#     if publish_date != None and publish_date !='':
#         new_book.publish_date = datetime.strptime(publish_date, '%m/%d/%Y')

#     for file in request.files:
#         uploaded_file = request.files[file]
#         if uploaded_file.filename != '' and allowed_file(uploaded_file.filename):
#             file_name = upload_file(uploaded_file)
#             image = Image(url = file_name)
#             new_book.images.append(image)
    
#     db.add(new_book)
#     db.commit()

# def edit(db: Session, book_to_edit:Book, request:Request):
#     """ Edit a book

#     Args:
#         db (Session): Db context
#         book_to_edit (Book): Book id to edit
#         request (Request): Request data
#     """
#     publish_date = request.form.get('publish_date')
#     if publish_date != None and publish_date !='':
#             book_to_edit.publish_date = datetime.strptime(publish_date, '%m/%d/%Y')
    
#     for file in request.files:
#         uploaded_file = request.files[file]
#         if uploaded_file.filename != '' and allowed_file(uploaded_file.filename):
#             file_name = upload_file(uploaded_file)
#             image = Image(url = file_name)
#             book_to_edit.images.append(image)

#     book_to_edit.title = request.form.get('title')
#     book_to_edit.slug = slugify(book_to_edit.title)
#     book_to_edit.short_description = request.form.get('short_description')
#     book_to_edit.price = request.form.get('price')
#     book_to_edit.description = request.form.get('description')
#     book_to_edit.isbn = request.form.get('isbn')
#     book_to_edit.author = request.form.get('author')
#     book_to_edit.publisher = request.form.get('publisher')
#     book_to_edit.pages = request.form.get('pages')
#     book_to_edit.dimensions = request.form.get('dimensions')
#     book_to_edit.language = request.form.get('language')
#     book_to_edit.is_featured = True if request.form.get('is_featured')=='on' else False
#     book_to_edit.updated_at = datetime.now()
#     book_to_edit.category_id = request.form.get('category_id')
#     # Update database
#     db.commit()

# def publish(db: Session, book_to_publish:Book, action:str):
#     """ Publish a book

#     Args:
#         db (Session): Db context
#         book_to_publish (Book): Book to publish
#         action (str): Action: publish
#     """
#     if action.lower() == 'publish':
#         book_to_publish.is_published = True
#     else:
#         book_to_publish.is_published = False
#     book_to_publish.updated_at = datetime.now()
#     # Update database
#     db.commit()

# #######################CATEGORY#############################################
# def get_category_by_id(db: Session, cat_id: UUID) -> Category:
#     """ Get category by Id

#     Args:
#         db (Session): Db context
#         cat_id (UUID): Category Id

#     Returns:
#         Category: Category object
#     """
#     return db.query(Category).get(cat_id)


# def get_all_categories(db: Session) -> list[Category]:
#     """ Get all categories

#     Returns:
#         list[Category]:: A list of categories
#     """
#     categories = db.query(Category).all()
#     return categories

# def get_all_categories_for_ddl(db: Session):
#     """ Get categories to be used by dropdownlist

#     Args:
#         db (Session): Db context

#     Returns:
#         _type_: Key/value of Categories
#     """
#     categories = db.query(Category.id, Category.name).all()
#     return categories

# def create_category(db: Session, form:CategoryCreateForm, request:Request):
#     """ Create a new Category

#     Args:
#         db (Session): Db context
#         form (CategoryCreateForm): Form data
#         request (Request): Request data
#     """
#     new_category = Category(name = form.name.data,
#                     short_description = form.short_description.data,
#                     slug = slugify(form.name.data),
#                     created_at = datetime.now())
#     for file in request.files:
#         uploaded_file = request.files[file]
#         if uploaded_file.filename != '' and allowed_file(uploaded_file.filename):
#             file_name = upload_file(uploaded_file)
#             image = Image(url = file_name)
#             new_category.images.append(image)
    
#     db.add(new_category)
#     db.commit()

# def edit_category(db: Session, category_to_edit:Category, request:Request):
#     """ Edit a category

#     Args:
#         db (Session): Db context
#         category_to_edit (Category): Category edit data
#         request (Request): Request data
#     """
#     for file in request.files:
#         uploaded_file = request.files[file]
#         if uploaded_file.filename != '' and allowed_file(uploaded_file.filename):
#             file_name = upload_file(uploaded_file)
#             image = Image(url = file_name)
#             category_to_edit.images.append(image)

#     category_to_edit.name = request.form.get('name')
#     category_to_edit.slug = slugify(category_to_edit.name)
#     category_to_edit.short_description = request.form.get('short_description')
#     category_to_edit.updated_at = datetime.now()
#     # Update database
#     db.commit()