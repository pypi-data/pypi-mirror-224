Playbook for running refstack locally
######################################

The playbook is meant for developers to help them with debugging and
reviewing new changes in the refstack project.

The playbook semi-automates running the refstack server on the localhost.
It downloads refstack role and templates from
`system-config <https://opendev.org/opendev/system-config.git>`__ repository
which is used for deploying and maintaining upstream servers, one of which is
refstack. Then it builds the refstack image and spins a container using the
refstack role.
