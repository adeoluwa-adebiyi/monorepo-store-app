from .models import ParentCategory, ParentCategoryProductListing, ProductProductListing, ProductListing


def get_cat_link(category):
    return f"/store/category/view/{category.name}/1"


def get_sub_cat_link(cat, sub_cat):
    return f"/store/category/view/{cat.name}/{sub_cat.name}/1"


def product_inventory_listing_links(request):
    context = dict()

    parent_cats = [
        {
            "name": cat.name,
            "link": get_cat_link(cat)
        }

        for cat in ParentCategory.objects.all()
    ]

    groupings = dict()

    for cat in ParentCategory.objects.all():
        sub_cats = [ ProductListing.objects.get(id=pcp.product_listing.id) for pcp in\
             ParentCategoryProductListing.objects.filter(parent_category__id=cat.id) ]
        groupings[cat.name] = [
            {
                "name": sub_cat.name,
                "link": get_sub_cat_link(cat, sub_cat)
            } for sub_cat in sub_cats
        ]

    val = {
        "parent_details": parent_cats,
        "groupings": {
            **groupings
        }
    }


    return  val
