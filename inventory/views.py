from django.shortcuts import render
from django.views.generic import View
from modules.services.inventory.inventory_service import InventoryService


class CategoryProductListingView(View):


    def get(self, request, category=None, sub_category=None, page=1):

        template_name = "product-listing.html"

        context = InventoryService.instance().generate_product_category_listing(category, sub_category, page)

        return render(request,template_name,context)


class ProductInformationView(View):

    def get(self, request, product_id):

        template_name = "product-info.html"

        context = InventoryService.instance().get_product_information(product_id=product_id)

        return render(request, template_name, context)
