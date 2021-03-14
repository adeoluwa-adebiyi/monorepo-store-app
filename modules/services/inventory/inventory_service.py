from inventory.models import ParentCategoryProductListing, ProductProductListing, Product, ProductBrand
from django.core.paginator import Paginator


class InventoryServiceContract(object):

    def generate_product_category_listing(self,category:str=None, sub_category:str=None, page:int=1) -> dict:
        pass


    def get_product_information(product_id:int) -> dict:
        pass


class InventoryService(InventoryServiceContract):

    INSTANCE = None

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls.INSTANCE == None:
            cls.INSTANCE = InventoryService()

        return cls.INSTANCE


    def generate_product_category_listing(self,category:str=None, sub_category:str=None, page:int=1) -> dict:
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
        return context


    def get_product_information(self,product_id:int) -> dict:
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
        return context