from django.shortcuts import render
from django.views.generic import View
from .models import ParentCategoryProductListing, ProductProductListing, Product, ProductBrand
from django.core.paginator import Paginator


class CategoryProductListingView(View):


    def get(self, request, category=None, sub_category=None, page=1):

        template_name = "product-listing.html"

        context = dict()

        listing = ParentCategoryProductListing.objects.get(parent_category__name=category, product_listing__name=sub_category)

        product_listings = Paginator(ProductProductListing.objects.filter(pcp_listing=listing), 20)

        generated_list = []

        for item in product_listings.page(page).object_list:
            generated_list.append({
                "name": item.product.name,
                "price": item.product.price,
                "brand": item.product.brand.name,
                "link": f"/store/product/view/{item.product.id}",
                "image": item.product.image,
                "category": item.product.category.name
            })

        context["product_list"] = generated_list
        context["product_list_pages"] = [page for page in range(1,product_listings.num_pages)]

        return render(request,template_name,context)


class ProductInformationView(View):

    def get(self, request, product_id):

        template_name = "product-info.html"

        context = dict()

        product = Product.objects.get(id=product_id)

        context["product"] = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "image": product.image,
            "brand": product.brand.name,
            "price": product.price,
            "rating": 3
        }

        context["similar_products"] = []

        return render(request, template_name, context)
