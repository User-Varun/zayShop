# Zay Bazaar (zayShop)

A small Django-based e-commerce demo built from the Zay Shop HTML template. This project demonstrates:

- Simple `Product`, 'Customer' model
- Admin-managed product and image uploads (uses Django admin and `MEDIA_ROOT`).
- A minimal session-backed cart (click Add to Cart increments cart count in session).

This README explains how to set up, run, and work with the project locally.

**Requirements**

- Python 3.8+ (your environment)
- Django (tested with 5.2.x)
- Pillow (for image fields)

**Quick Setup**

- Create and activate a virtual environment (optional but recommended):

```powershell
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate
```

- Install dependencies:

```powershell
pip install -r requirements.txt
# If no requirements.txt exists, at minimum:
pip install Django Pillow django-extensions
```

**Database & Migrations**

```powershell
python manage.py makemigrations
python manage.py migrate
```

**Create admin user**

```powershell
python manage.py createsuperuser
```

**Run the development server**

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

**Media files (images)**

- Development serving: `settings.py` configures `MEDIA_URL` and `MEDIA_ROOT`. In `DEBUG=True` the project `urls.py` adds a `static()` handler so uploaded images are served.
- Upload product images from Django admin: login at `/admin/`, create a `Product`, then add `ProductImage` entries pointing to that product. Uploaded files are saved under `media/products/` (or where your `ImageField` `upload_to` points).

**How the cart works (simple session-based implementation)**

- Clicking "Add to Cart" triggers the `add_to_cart` view which increments `request.session['cart_count']` and appends product ids to `request.session['cart']`.
- The header badge shows `{{ request.session.cart_count|default:"0" }}` and updates after adding items because the view redirects back to the referring page.
- This is intentionally simple and stored only in the user's session. For a persistent cart, implement `Cart` and `CartItem` models linked to `auth.User`.

**Product detail page**

- URL: `/product/<product_id>/` (e.g. `/product/1/`).
- The detail view (`product_detail`) fetches the `Product` and its related `ProductImage` objects (related_name `images`) and renders `shop-single.html`.
- Thumbnails are grouped in slides of 3; clicking a thumbnail swaps the main image.

**Templates changed/important files**

- `zayShopApp/models.py`: contains `Product` and `ProductImage`.
- `zayShopApp/admin.py`: `Product` and `ProductImage` registered in admin.
- `zayShopApp/views.py`: `shop`, `product_detail`, `add_to_cart`, and other views.
- `zayShopApp/templates/shop.html`: product listing — eye icon links to product detail, cart button calls `/cart/add/<id>/`.
- `zayShopApp/templates/shop-single.html`: product detail + dynamic image carousel.
- `zayShop/templates/header.html`: header displays session username and cart count.
- `zayShop/urls.py`: routes for product detail and cart add are defined.

**Common troubleshooting**

- `Product` images not showing:
  - Verify images uploaded (check `media/` folder).
  - Ensure `MEDIA_URL`/`MEDIA_ROOT` are set and `urls.py` uses `static()` in DEBUG.
  - In templates, guard `.url` access: `{% if product.image %}<img src="{{ product.image.url }}">{% endif %}` — this project already uses such guards in places.
- `NoReverseMatch` on `cart_add_product`:
  - Ensure `cart` routes exist in `zayShop/urls.py` and are named `cart_add_product`.
- Wrong URL kwarg names:
  - Match parameter names in `path('product/<int:product_id>/', ...)` to view signatures.

**Next improvements you can add**

- Persist cart in DB via `Cart` and `CartItem` models.
- Add product categories and filters on the shop page.
- Use AJAX for add-to-cart to update the header badge without page reload.
- Add thumbnails/thumbnail generator (e.g., `sorl-thumbnail` or `django-imagekit`) for faster pages.
- Add tests for views and models.

**Development notes**

- This project keeps the built-in auth and a custom `Customer` model (simple, not tied to `auth.User`). Consider migrating to Django's `User` model for full auth features.
- The project currently uses some template content adapted from the original Zay template; replace with your own assets as required.
