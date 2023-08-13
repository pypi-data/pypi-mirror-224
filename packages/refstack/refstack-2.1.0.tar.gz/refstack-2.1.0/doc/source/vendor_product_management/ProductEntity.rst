==============
Product entity
==============

Any user who has successfully authenticated to the RefStack server can create
product entities. The minimum information needed to create a product entity is
as follows:

- Name

  This is the name of the product entity being created.

- Product type:

  Product types are defined by OpenStack as shown on the OpenStack Marketplace
  ( https://www.openstack.org/marketplace/ ). Currently, there are three types
  of products, namely: Distro & Appliances, Hosted Private Clouds and Public
  Clouds.

- Vendor

  This is the vendor which owns the product. A default vendor will be created
  for the user if no vendor entity exists for this user.

Whenever a product is created, by default, it is a private product and is only
visible to its vendor users. Vendor users can make a product publicly visible
as needed later. However, only products that are owned by official vendors can
be made publicly visible.

Product version
~~~~~~~~~~~~~~~

A default version is created whenever a product is created. The name of the
default version is blank. The default version is used for products that have
no version. Users can add new product versions to the product as needed.

