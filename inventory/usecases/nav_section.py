from inventory.models import ParentCategoryListings
def get_nav_offerings():
    offerings = []
    for pl in ParentCategoryListings.objects.all():
    offerings.append(
        {
            parent:{
                "name": "",
                "url": "",
            },
            children:{
                
            }
        }
    )
