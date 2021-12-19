from category.models import Category

# used for to featch product by category it is python function
# install the function  exist in context_processors.py in the settings of project part of 'context_processors'

def menu_links(request): # it take  requst as argument and return dictionary as data
    links = Category.objects.all() #getting all category objects  from Category model and store to links variable
    return dict(links = links)