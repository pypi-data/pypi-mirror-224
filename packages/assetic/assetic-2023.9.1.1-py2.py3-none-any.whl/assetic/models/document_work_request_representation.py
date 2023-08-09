# coding: utf-8

"""
    Assetic Integration API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

##from assetic.models.document_asset_representation import DocumentAssetRepresentation  # noqa: F401,E501
##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501


class DocumentWorkRequestRepresentation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'work_request_id': 'str',
        'friendly_id': 'str',
        'document_asset': 'DocumentAssetRepresentation',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'work_request_id': 'WorkRequestId',
        'friendly_id': 'FriendlyId',
        'document_asset': 'DocumentAsset',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, work_request_id=None, friendly_id=None, document_asset=None, links=None, embedded=None):  # noqa: E501
        """DocumentWorkRequestRepresentation - a model defined in Swagger"""  # noqa: E501

        self._work_request_id = None
        self._friendly_id = None
        self._document_asset = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if work_request_id is not None:
            self.work_request_id = work_request_id
        if friendly_id is not None:
            self.friendly_id = friendly_id
        if document_asset is not None:
            self.document_asset = document_asset
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def work_request_id(self):
        """Gets the work_request_id of this DocumentWorkRequestRepresentation.  # noqa: E501


        :return: The work_request_id of this DocumentWorkRequestRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """Sets the work_request_id of this DocumentWorkRequestRepresentation.


        :param work_request_id: The work_request_id of this DocumentWorkRequestRepresentation.  # noqa: E501
        :type: str
        """

        self._work_request_id = work_request_id

    @property
    def friendly_id(self):
        """Gets the friendly_id of this DocumentWorkRequestRepresentation.  # noqa: E501


        :return: The friendly_id of this DocumentWorkRequestRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._friendly_id

    @friendly_id.setter
    def friendly_id(self, friendly_id):
        """Sets the friendly_id of this DocumentWorkRequestRepresentation.


        :param friendly_id: The friendly_id of this DocumentWorkRequestRepresentation.  # noqa: E501
        :type: str
        """

        self._friendly_id = friendly_id

    @property
    def document_asset(self):
        """Gets the document_asset of this DocumentWorkRequestRepresentation.  # noqa: E501


        :return: The document_asset of this DocumentWorkRequestRepresentation.  # noqa: E501
        :rtype: DocumentAssetRepresentation
        """
        return self._document_asset

    @document_asset.setter
    def document_asset(self, document_asset):
        """Sets the document_asset of this DocumentWorkRequestRepresentation.


        :param document_asset: The document_asset of this DocumentWorkRequestRepresentation.  # noqa: E501
        :type: DocumentAssetRepresentation
        """

        self._document_asset = document_asset

    @property
    def links(self):
        """Gets the links of this DocumentWorkRequestRepresentation.  # noqa: E501


        :return: The links of this DocumentWorkRequestRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DocumentWorkRequestRepresentation.


        :param links: The links of this DocumentWorkRequestRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this DocumentWorkRequestRepresentation.  # noqa: E501


        :return: The embedded of this DocumentWorkRequestRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this DocumentWorkRequestRepresentation.


        :param embedded: The embedded of this DocumentWorkRequestRepresentation.  # noqa: E501
        :type: list[EmbeddedResource]
        """

        self._embedded = embedded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DocumentWorkRequestRepresentation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentWorkRequestRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
