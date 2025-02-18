{
    'name': 'Sale Management',
    'version': '1.0',
    'author': 'Matjel Ltd',
    'category': 'Sales',
    'summary': 'Manage sale order',
    'depends': ['base', 'sale', 'stock'],
    'data': [
    'security/ir.model.access.csv',
    'views/sale_order_views.xml',
    'views/sale_order_line_views.xml',
    'views/product_template_views.xml',
    'views/product_views.xml',
],
    'installable': True,
    'application': True,
}