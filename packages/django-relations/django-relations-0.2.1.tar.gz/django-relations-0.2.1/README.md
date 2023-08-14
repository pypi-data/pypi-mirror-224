# django-relations

# Installation
    # with pip

    pip install django-relations
#
    # with pipenv

    pipenv install django-relations

# Using

    from django_relations import AbstractDefaultClass

    class MyModel(AbstractDefaultClass):
        field1 = models.OneToOneField(Model1, ...)
        field2 = models.ForeignKey(Model2, ...)
        field3 = models.ManyToManyField(Model3, ...)
    

# Description
Boost your Django app's speed with the all-new django-relations package. Say goodbye to manual query optimization – this package automatically detects relation fields and seamlessly integrates them into select_related and prefetch_related methods. 🚀 Supercharge response times, enhance UX, and free up your creative genius. Embrace efficiency and let django-relations handle the heavy lifting. Your queries, elevated.
