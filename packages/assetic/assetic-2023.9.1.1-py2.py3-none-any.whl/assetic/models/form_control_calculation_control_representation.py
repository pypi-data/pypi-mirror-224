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


class FormControlCalculationControlRepresentation(object):
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
        'ordinal_postion': 'int',
        'form_control_name_source': 'str',
        'form_control_label_source': 'str'
    }

    attribute_map = {
        'ordinal_postion': 'OrdinalPostion',
        'form_control_name_source': 'FormControlNameSource',
        'form_control_label_source': 'FormControlLabelSource'
    }

    def __init__(self, ordinal_postion=None, form_control_name_source=None, form_control_label_source=None):  # noqa: E501
        """FormControlCalculationControlRepresentation - a model defined in Swagger"""  # noqa: E501

        self._ordinal_postion = None
        self._form_control_name_source = None
        self._form_control_label_source = None
        self.discriminator = None

        if ordinal_postion is not None:
            self.ordinal_postion = ordinal_postion
        if form_control_name_source is not None:
            self.form_control_name_source = form_control_name_source
        if form_control_label_source is not None:
            self.form_control_label_source = form_control_label_source

    @property
    def ordinal_postion(self):
        """Gets the ordinal_postion of this FormControlCalculationControlRepresentation.  # noqa: E501


        :return: The ordinal_postion of this FormControlCalculationControlRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._ordinal_postion

    @ordinal_postion.setter
    def ordinal_postion(self, ordinal_postion):
        """Sets the ordinal_postion of this FormControlCalculationControlRepresentation.


        :param ordinal_postion: The ordinal_postion of this FormControlCalculationControlRepresentation.  # noqa: E501
        :type: int
        """

        self._ordinal_postion = ordinal_postion

    @property
    def form_control_name_source(self):
        """Gets the form_control_name_source of this FormControlCalculationControlRepresentation.  # noqa: E501


        :return: The form_control_name_source of this FormControlCalculationControlRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_control_name_source

    @form_control_name_source.setter
    def form_control_name_source(self, form_control_name_source):
        """Sets the form_control_name_source of this FormControlCalculationControlRepresentation.


        :param form_control_name_source: The form_control_name_source of this FormControlCalculationControlRepresentation.  # noqa: E501
        :type: str
        """

        self._form_control_name_source = form_control_name_source

    @property
    def form_control_label_source(self):
        """Gets the form_control_label_source of this FormControlCalculationControlRepresentation.  # noqa: E501


        :return: The form_control_label_source of this FormControlCalculationControlRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._form_control_label_source

    @form_control_label_source.setter
    def form_control_label_source(self, form_control_label_source):
        """Sets the form_control_label_source of this FormControlCalculationControlRepresentation.


        :param form_control_label_source: The form_control_label_source of this FormControlCalculationControlRepresentation.  # noqa: E501
        :type: str
        """

        self._form_control_label_source = form_control_label_source

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
        if issubclass(FormControlCalculationControlRepresentation, dict):
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
        if not isinstance(other, FormControlCalculationControlRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
