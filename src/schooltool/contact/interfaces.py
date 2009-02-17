#
#
# SchoolTool - common information systems platform for school administration
# Copyright (c) 2009 Shuttleworth Foundation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""
Contact interfaces
"""
from zope.app.container.constraints import contains
from zope.app.container.constraints import containers
from zope.app.container.interfaces import IContained
from zope.interface import Interface
from zope.schema import TextLine
from zope.schema.interfaces import IContainer

from schooltool.common import SchoolToolMessage as _


class IContact(Interface):

    prefix = TextLine(title=_(u"Prefix"), required=False)
    first_name = TextLine(title=_(u"First name"))
    middle_name = TextLine(title=_(u"Middle name"), required=False)
    last_name = TextLine(title=_(u"Last name"))
    suffix = TextLine(title=_(u"Suffix"), required=False)

    address_line_1 = TextLine(title=_(u"Address line 1"), required=False)

    address_line_2 = TextLine(title=_(u"Address line 2"), required=False)

    city = TextLine(title=_(u"City"), required=False)

    state = TextLine(title=_(u"State"), required=False)

    country = TextLine(title=_(u"Country"), required=False)

    postal_code = TextLine(title=_(u"Postal code"), required=False)

    email = TextLine(title=_(u"Email"), required=False)

    home_phone = TextLine(title=_(u"Home phone"), required=False)

    work_phone = TextLine(title=_(u"Work phone"), required=False)

    mobile_phone = TextLine(title=_(u"Mobile phone"), required=False)

    language = TextLine(title=_(u"Language"), required=False)


class IContactContainer(IContainer):
    """Container of contacts."""

    contains(IContact)


class IContactContained(IContact, IContained):
    """Contact contained in an IContactContainer."""

    containers(IContactContainer)
