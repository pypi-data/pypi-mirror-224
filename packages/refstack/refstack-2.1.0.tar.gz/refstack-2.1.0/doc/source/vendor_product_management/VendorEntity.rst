=============
Vendor entity
=============

Any user who has successfully authenticated to the RefStack server can create
vendor entities. The minimum required information to create a vendor is the
vendor name. Users can update the rest of the vendor related information at a
later time.

Vendor admin
~~~~~~~~~~~~~

Whenever a user creates a vendor, this user will be added as the vendor's first
vendor admin. Subsequently, any admin of the vendor can add additional users to
the vendor. In RefStack, the "OpenStack User ID" of users are used as the
identities for adding users to vendors. At the time this document is written,
RefStack has not implemented user roles, and as such, all users of a vendor are
admin users.

Vendor types
~~~~~~~~~~~~~

There are four types of vendor entities in RefStack:

- Foundation:

  This is a special entity representing the OpenStack Foundation. Users belong
  to this entity are the Foundation admins. Foundation admins have visibility
  to all vendors and products.

- Private:

  A vendor will always be created with type "private". Vendors of this type
  are only visible to their own users and Foundation admins. Vendor users can
  initiate a registration request to the Foundation to change its type from
  "private" to "official".

- Pending

  Once a registration request is submitted, the vendor type will be changed
  automatically from type "private" to "pending". Vendors of this type are
  still only visible to their own users and Foundation admins.

- Official

  Once a vendor registration request is approved by the Foundation. The vendor
  type will be changed from "pending" to "official". Official vendors are
  visible to all RefStack users.

