from django.urls import path

from catalog.views import CategoryListView, CategoryProductsView, SellerProductsView, SellerListView, DiscountListView, DiscountsView, CartView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),

    path('sellers/', SellerListView.as_view(), name='seller'),
    path('sellers/<int:seller_id>/', SellerProductsView.as_view(), name='seller-products'),

    path('discounts/', DiscountListView.as_view(), name='discounts'),
    path('discounts/<int:discount_id>/', DiscountsView.as_view(), name='discount-products'),

    path('cart/', CartView.as_view(), name='cart'),

]
