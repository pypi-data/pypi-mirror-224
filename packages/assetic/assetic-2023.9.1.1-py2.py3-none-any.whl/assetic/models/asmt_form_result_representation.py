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

##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501
##from assetic.models.rs_resource_representation import RsResourceRepresentation  # noqa: F401,E501


class AsmtFormResultRepresentation(object):
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
        'id': 'str',
        'form_id': 'str',
        'form_name': 'str',
        'form_label': 'str',
        'form_version': 'int',
        'form_applicable_level': 'int',
        'form_result_id': 'int',
        'form_result_start_time': 'datetime',
        'form_result_end_time': 'datetime',
        'form_result_last_modified': 'datetime',
        'form_result_status': 'int',
        'form_result_comment': 'str',
        'form_result_skipped': 'bool',
        'form_result_skipped_reason': 'int',
        'form_result_rs_resource_id_assessed_by': 'RsResourceRepresentation',
        'form_result_asp_net_user_created_by': 'str',
        'form_result_is_required_by_system': 'bool',
        'form_result_asmt_form_version_id': 'str',
        'data': 'object',
        'parent_entity_id': 'str',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'id': 'Id',
        'form_id': 'FormId',
        'form_name': 'FormName',
        'form_label': 'FormLabel',
        'form_version': 'FormVersion',
        'form_applicable_level': 'FormApplicableLevel',
        'form_result_id': 'FormResultId',
        'form_result_start_time': 'FormResultStartTime',
        'form_result_end_time': 'FormResultEndTime',
        'form_result_last_modified': 'FormResultLastModified',
        'form_result_status': 'FormResultStatus',
        'form_result_comment': 'FormResultComment',
        'form_result_skipped': 'FormResultSkipped',
        'form_result_skipped_reason': 'FormResultSkippedReason',
        'form_result_rs_resource_id_assessed_by': 'FormResultRsResourceIdAssessedBy',
        'form_result_asp_net_user_created_by': 'FormResultAspNetUserCreatedBy',
        'form_result_is_required_by_system': 'FormResultIsRequiredBySystem',
        'form_result_asmt_form_version_id': 'FormResultASMTFormVersionId',
        'data': 'Data',
        'parent_entity_id': 'ParentEntityId',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, id=None, form_id=None, form_name=None, form_label=None, form_version=None, form_applicable_level=None, form_result_id=None, form_result_start_time=None, form_result_end_time=None, form_result_last_modified=None, form_result_status=None, form_result_comment=None, form_result_skipped=None, form_result_skipped_reason=None, form_result_rs_resource_id_assessed_by=None, form_result_asp_net_user_created_by=None, form_result_is_required_by_system=None, form_result_asmt_form_version_id=None, data=None, parent_entity_id=None, links=None, embedded=None):  # noqa: E501
        """AsmtFormResultRepresentation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._form_id = None
        self._form_name = None
        self._form_label = None
        self._form_version = None
        self._form_applicable_level = None
        self._form_result_id = None
        self._form_result_start_time = None
        self._form_result_end_time = None
        self._form_result_last_modified = None
        self._form_result_status = None
        self._form_result_comment = None
        self._form_result_skipped = None
        self._form_result_skipped_reason = None
        self._form_result_rs_resource_id_assessed_by = None
        self._form_result_asp_net_user_created_by = None
        self._form_result_is_required_by_system = None
        self._form_result_asmt_form_version_id = None
        self._data = None
        self._parent_entity_id = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if form_id is not None:
            self.form_id = form_id
        if form_name is not None:
            self.form_name = form_name
        if form_label is not None:
            self.form_label = form_label
        if form_version is not None:
            self.form_version = form_version
        if form_applicable_level is not None:
            self.form_applicable_level = form_applicable_level
        if form_result_id is not None:
            self.form_result_id = form_result_id
        if form_result_start_time is not None:
            self.form_result_start_time = form_result_start_time
        if form_result_end_time is not None:
            self.form_result_end_time = form_result_end_time
        if form_result_last_modified is not None:
            self.form_result_last_modified = form_result_last_modified
        if form_result_status is not None:
            self.form_result_status = form_result_status
        if form_result_comment is not None:
            self.form_result_comment = form_result_comment
        if form_result_skipped is not None:
            self.form_result_skipped = form_result_skipped
        if form_result_skipped_reason is not None:
            self.form_result_skipped_reason = form_result_skipped_reason
        if form_result_rs_resource_id_assessed_by is not None:
            self.form_result_rs_resource_id_assessed_by = form_result_rs_resource_id_assessed_by
        if form_result_asp_net_user_created_by is not None:
            self.form_result_asp_net_user_created_by = form_result_asp_net_user_created_by
        if form_result_is_required_by_system is not None:
            self.form_result_is_required_by_system = form_result_is_required_by_system
        if form_result_asmt_form_version_id is not None:
            self.form_result_asmt_form_version_id = form_result_asmt_form_version_id
        if data is not None:
            self.data = data
        if parent_entity_id is not None:
            self.parent_entity_id = parent_entity_id
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def id(self):
        """Gets the id of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The id of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AsmtFormResultRepresentation.


        :param id: The id of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def form_id(self):
        """Gets the form_id of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_id of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this AsmtFormResultRepresentation.


        :param form_id: The form_id of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._form_id = form_id

    @property
    def form_name(self):
        """Gets the form_name of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_name of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_name

    @form_name.setter
    def form_name(self, form_name):
        """Sets the form_name of this AsmtFormResultRepresentation.


        :param form_name: The form_name of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._form_name = form_name

    @property
    def form_label(self):
        """Gets the form_label of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_label of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_label

    @form_label.setter
    def form_label(self, form_label):
        """Sets the form_label of this AsmtFormResultRepresentation.


        :param form_label: The form_label of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._form_label = form_label

    @property
    def form_version(self):
        """Gets the form_version of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_version of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._form_version

    @form_version.setter
    def form_version(self, form_version):
        """Sets the form_version of this AsmtFormResultRepresentation.


        :param form_version: The form_version of this AsmtFormResultRepresentation.  # noqa: E501
        :type: int
        """

        self._form_version = form_version

    @property
    def form_applicable_level(self):
        """Gets the form_applicable_level of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_applicable_level of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._form_applicable_level

    @form_applicable_level.setter
    def form_applicable_level(self, form_applicable_level):
        """Sets the form_applicable_level of this AsmtFormResultRepresentation.


        :param form_applicable_level: The form_applicable_level of this AsmtFormResultRepresentation.  # noqa: E501
        :type: int
        """

        self._form_applicable_level = form_applicable_level

    @property
    def form_result_id(self):
        """Gets the form_result_id of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_id of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._form_result_id

    @form_result_id.setter
    def form_result_id(self, form_result_id):
        """Sets the form_result_id of this AsmtFormResultRepresentation.


        :param form_result_id: The form_result_id of this AsmtFormResultRepresentation.  # noqa: E501
        :type: int
        """

        self._form_result_id = form_result_id

    @property
    def form_result_start_time(self):
        """Gets the form_result_start_time of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_start_time of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._form_result_start_time

    @form_result_start_time.setter
    def form_result_start_time(self, form_result_start_time):
        """Sets the form_result_start_time of this AsmtFormResultRepresentation.


        :param form_result_start_time: The form_result_start_time of this AsmtFormResultRepresentation.  # noqa: E501
        :type: datetime
        """

        self._form_result_start_time = form_result_start_time

    @property
    def form_result_end_time(self):
        """Gets the form_result_end_time of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_end_time of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._form_result_end_time

    @form_result_end_time.setter
    def form_result_end_time(self, form_result_end_time):
        """Sets the form_result_end_time of this AsmtFormResultRepresentation.


        :param form_result_end_time: The form_result_end_time of this AsmtFormResultRepresentation.  # noqa: E501
        :type: datetime
        """

        self._form_result_end_time = form_result_end_time

    @property
    def form_result_last_modified(self):
        """Gets the form_result_last_modified of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_last_modified of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._form_result_last_modified

    @form_result_last_modified.setter
    def form_result_last_modified(self, form_result_last_modified):
        """Sets the form_result_last_modified of this AsmtFormResultRepresentation.


        :param form_result_last_modified: The form_result_last_modified of this AsmtFormResultRepresentation.  # noqa: E501
        :type: datetime
        """

        self._form_result_last_modified = form_result_last_modified

    @property
    def form_result_status(self):
        """Gets the form_result_status of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_status of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._form_result_status

    @form_result_status.setter
    def form_result_status(self, form_result_status):
        """Sets the form_result_status of this AsmtFormResultRepresentation.


        :param form_result_status: The form_result_status of this AsmtFormResultRepresentation.  # noqa: E501
        :type: int
        """

        self._form_result_status = form_result_status

    @property
    def form_result_comment(self):
        """Gets the form_result_comment of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_comment of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_result_comment

    @form_result_comment.setter
    def form_result_comment(self, form_result_comment):
        """Sets the form_result_comment of this AsmtFormResultRepresentation.


        :param form_result_comment: The form_result_comment of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._form_result_comment = form_result_comment

    @property
    def form_result_skipped(self):
        """Gets the form_result_skipped of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_skipped of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: bool
        """
        return self._form_result_skipped

    @form_result_skipped.setter
    def form_result_skipped(self, form_result_skipped):
        """Sets the form_result_skipped of this AsmtFormResultRepresentation.


        :param form_result_skipped: The form_result_skipped of this AsmtFormResultRepresentation.  # noqa: E501
        :type: bool
        """

        self._form_result_skipped = form_result_skipped

    @property
    def form_result_skipped_reason(self):
        """Gets the form_result_skipped_reason of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_skipped_reason of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._form_result_skipped_reason

    @form_result_skipped_reason.setter
    def form_result_skipped_reason(self, form_result_skipped_reason):
        """Sets the form_result_skipped_reason of this AsmtFormResultRepresentation.


        :param form_result_skipped_reason: The form_result_skipped_reason of this AsmtFormResultRepresentation.  # noqa: E501
        :type: int
        """

        self._form_result_skipped_reason = form_result_skipped_reason

    @property
    def form_result_rs_resource_id_assessed_by(self):
        """Gets the form_result_rs_resource_id_assessed_by of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_rs_resource_id_assessed_by of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: RsResourceRepresentation
        """
        return self._form_result_rs_resource_id_assessed_by

    @form_result_rs_resource_id_assessed_by.setter
    def form_result_rs_resource_id_assessed_by(self, form_result_rs_resource_id_assessed_by):
        """Sets the form_result_rs_resource_id_assessed_by of this AsmtFormResultRepresentation.


        :param form_result_rs_resource_id_assessed_by: The form_result_rs_resource_id_assessed_by of this AsmtFormResultRepresentation.  # noqa: E501
        :type: RsResourceRepresentation
        """

        self._form_result_rs_resource_id_assessed_by = form_result_rs_resource_id_assessed_by

    @property
    def form_result_asp_net_user_created_by(self):
        """Gets the form_result_asp_net_user_created_by of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_asp_net_user_created_by of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_result_asp_net_user_created_by

    @form_result_asp_net_user_created_by.setter
    def form_result_asp_net_user_created_by(self, form_result_asp_net_user_created_by):
        """Sets the form_result_asp_net_user_created_by of this AsmtFormResultRepresentation.


        :param form_result_asp_net_user_created_by: The form_result_asp_net_user_created_by of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._form_result_asp_net_user_created_by = form_result_asp_net_user_created_by

    @property
    def form_result_is_required_by_system(self):
        """Gets the form_result_is_required_by_system of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_is_required_by_system of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: bool
        """
        return self._form_result_is_required_by_system

    @form_result_is_required_by_system.setter
    def form_result_is_required_by_system(self, form_result_is_required_by_system):
        """Sets the form_result_is_required_by_system of this AsmtFormResultRepresentation.


        :param form_result_is_required_by_system: The form_result_is_required_by_system of this AsmtFormResultRepresentation.  # noqa: E501
        :type: bool
        """

        self._form_result_is_required_by_system = form_result_is_required_by_system

    @property
    def form_result_asmt_form_version_id(self):
        """Gets the form_result_asmt_form_version_id of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The form_result_asmt_form_version_id of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_result_asmt_form_version_id

    @form_result_asmt_form_version_id.setter
    def form_result_asmt_form_version_id(self, form_result_asmt_form_version_id):
        """Sets the form_result_asmt_form_version_id of this AsmtFormResultRepresentation.


        :param form_result_asmt_form_version_id: The form_result_asmt_form_version_id of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._form_result_asmt_form_version_id = form_result_asmt_form_version_id

    @property
    def data(self):
        """Gets the data of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The data of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AsmtFormResultRepresentation.


        :param data: The data of this AsmtFormResultRepresentation.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def parent_entity_id(self):
        """Gets the parent_entity_id of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The parent_entity_id of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._parent_entity_id

    @parent_entity_id.setter
    def parent_entity_id(self, parent_entity_id):
        """Sets the parent_entity_id of this AsmtFormResultRepresentation.


        :param parent_entity_id: The parent_entity_id of this AsmtFormResultRepresentation.  # noqa: E501
        :type: str
        """

        self._parent_entity_id = parent_entity_id

    @property
    def links(self):
        """Gets the links of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The links of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AsmtFormResultRepresentation.


        :param links: The links of this AsmtFormResultRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this AsmtFormResultRepresentation.  # noqa: E501


        :return: The embedded of this AsmtFormResultRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this AsmtFormResultRepresentation.


        :param embedded: The embedded of this AsmtFormResultRepresentation.  # noqa: E501
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
        if issubclass(AsmtFormResultRepresentation, dict):
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
        if not isinstance(other, AsmtFormResultRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
