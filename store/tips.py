"""
# Preload related objects
Product.object.select_related('...')
Product.object.prefetch_related('...')
"""

"""
# Load only what you need
Product.object.only('title')
Product.object.defer('description')
"""

"""
# Use values
Product.object.values('title')
Product.object.values_list('description')
"""

"""
# Use Count properly
Product.object.count()
len(Product.object.all()) # bad
"""

"""
# Bulk create/update
Product.object.bulk_create([])
"""
