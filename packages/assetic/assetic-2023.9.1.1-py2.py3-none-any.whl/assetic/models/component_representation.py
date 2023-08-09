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


class ComponentRepresentation(object):
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
        'name': 'str',
        'label': 'str',
        'asset_id': 'str',
        'asset_category': 'str',
        'asset_category_id': 'str',
        'component_type': 'str',
        'network_measure_type': 'str',
        'dimension_unit': 'str',
        'material_type': 'str',
        'design_life': 'float',
        'external_identifier': 'str',
        'reference_value': 'float',
        'reference_date': 'datetime',
        'reval_date_built': 'datetime',
        'last_modified': 'datetime',
        'financial_class_id': 'int',
        'financial_class_name': 'str',
        'financial_sub_class_id': 'int',
        'financial_sub_class_name': 'str',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'label': 'Label',
        'asset_id': 'AssetId',
        'asset_category': 'AssetCategory',
        'asset_category_id': 'AssetCategoryId',
        'component_type': 'ComponentType',
        'network_measure_type': 'NetworkMeasureType',
        'dimension_unit': 'DimensionUnit',
        'material_type': 'MaterialType',
        'design_life': 'DesignLife',
        'external_identifier': 'ExternalIdentifier',
        'reference_value': 'ReferenceValue',
        'reference_date': 'ReferenceDate',
        'reval_date_built': 'RevalDateBuilt',
        'last_modified': 'LastModified',
        'financial_class_id': 'FinancialClassId',
        'financial_class_name': 'FinancialClassName',
        'financial_sub_class_id': 'FinancialSubClassId',
        'financial_sub_class_name': 'FinancialSubClassName',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, id=None, name=None, label=None, asset_id=None, asset_category=None, asset_category_id=None, component_type=None, network_measure_type=None, dimension_unit=None, material_type=None, design_life=None, external_identifier=None, reference_value=None, reference_date=None, reval_date_built=None, last_modified=None, financial_class_id=None, financial_class_name=None, financial_sub_class_id=None, financial_sub_class_name=None, links=None, embedded=None):  # noqa: E501
        """ComponentRepresentation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._label = None
        self._asset_id = None
        self._asset_category = None
        self._asset_category_id = None
        self._component_type = None
        self._network_measure_type = None
        self._dimension_unit = None
        self._material_type = None
        self._design_life = None
        self._external_identifier = None
        self._reference_value = None
        self._reference_date = None
        self._reval_date_built = None
        self._last_modified = None
        self._financial_class_id = None
        self._financial_class_name = None
        self._financial_sub_class_id = None
        self._financial_sub_class_name = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if asset_id is not None:
            self.asset_id = asset_id
        if asset_category is not None:
            self.asset_category = asset_category
        if asset_category_id is not None:
            self.asset_category_id = asset_category_id
        if component_type is not None:
            self.component_type = component_type
        if network_measure_type is not None:
            self.network_measure_type = network_measure_type
        if dimension_unit is not None:
            self.dimension_unit = dimension_unit
        if material_type is not None:
            self.material_type = material_type
        if design_life is not None:
            self.design_life = design_life
        if external_identifier is not None:
            self.external_identifier = external_identifier
        if reference_value is not None:
            self.reference_value = reference_value
        if reference_date is not None:
            self.reference_date = reference_date
        if reval_date_built is not None:
            self.reval_date_built = reval_date_built
        if last_modified is not None:
            self.last_modified = last_modified
        if financial_class_id is not None:
            self.financial_class_id = financial_class_id
        if financial_class_name is not None:
            self.financial_class_name = financial_class_name
        if financial_sub_class_id is not None:
            self.financial_sub_class_id = financial_sub_class_id
        if financial_sub_class_name is not None:
            self.financial_sub_class_name = financial_sub_class_name
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def id(self):
        """Gets the id of this ComponentRepresentation.  # noqa: E501


        :return: The id of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentRepresentation.


        :param id: The id of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ComponentRepresentation.  # noqa: E501


        :return: The name of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentRepresentation.


        :param name: The name of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this ComponentRepresentation.  # noqa: E501


        :return: The label of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ComponentRepresentation.


        :param label: The label of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def asset_id(self):
        """Gets the asset_id of this ComponentRepresentation.  # noqa: E501


        :return: The asset_id of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ComponentRepresentation.


        :param asset_id: The asset_id of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_category(self):
        """Gets the asset_category of this ComponentRepresentation.  # noqa: E501


        :return: The asset_category of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._asset_category

    @asset_category.setter
    def asset_category(self, asset_category):
        """Sets the asset_category of this ComponentRepresentation.


        :param asset_category: The asset_category of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._asset_category = asset_category

    @property
    def asset_category_id(self):
        """Gets the asset_category_id of this ComponentRepresentation.  # noqa: E501


        :return: The asset_category_id of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._asset_category_id

    @asset_category_id.setter
    def asset_category_id(self, asset_category_id):
        """Sets the asset_category_id of this ComponentRepresentation.


        :param asset_category_id: The asset_category_id of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._asset_category_id = asset_category_id

    @property
    def component_type(self):
        """Gets the component_type of this ComponentRepresentation.  # noqa: E501


        :return: The component_type of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this ComponentRepresentation.


        :param component_type: The component_type of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._component_type = component_type

    @property
    def network_measure_type(self):
        """Gets the network_measure_type of this ComponentRepresentation.  # noqa: E501


        :return: The network_measure_type of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._network_measure_type

    @network_measure_type.setter
    def network_measure_type(self, network_measure_type):
        """Sets the network_measure_type of this ComponentRepresentation.


        :param network_measure_type: The network_measure_type of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._network_measure_type = network_measure_type

    @property
    def dimension_unit(self):
        """Gets the dimension_unit of this ComponentRepresentation.  # noqa: E501


        :return: The dimension_unit of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._dimension_unit

    @dimension_unit.setter
    def dimension_unit(self, dimension_unit):
        """Sets the dimension_unit of this ComponentRepresentation.


        :param dimension_unit: The dimension_unit of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._dimension_unit = dimension_unit

    @property
    def material_type(self):
        """Gets the material_type of this ComponentRepresentation.  # noqa: E501


        :return: The material_type of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._material_type

    @material_type.setter
    def material_type(self, material_type):
        """Sets the material_type of this ComponentRepresentation.


        :param material_type: The material_type of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._material_type = material_type

    @property
    def design_life(self):
        """Gets the design_life of this ComponentRepresentation.  # noqa: E501


        :return: The design_life of this ComponentRepresentation.  # noqa: E501
        :rtype: float
        """
        return self._design_life

    @design_life.setter
    def design_life(self, design_life):
        """Sets the design_life of this ComponentRepresentation.


        :param design_life: The design_life of this ComponentRepresentation.  # noqa: E501
        :type: float
        """

        self._design_life = design_life

    @property
    def external_identifier(self):
        """Gets the external_identifier of this ComponentRepresentation.  # noqa: E501


        :return: The external_identifier of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """Sets the external_identifier of this ComponentRepresentation.


        :param external_identifier: The external_identifier of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def reference_value(self):
        """Gets the reference_value of this ComponentRepresentation.  # noqa: E501


        :return: The reference_value of this ComponentRepresentation.  # noqa: E501
        :rtype: float
        """
        return self._reference_value

    @reference_value.setter
    def reference_value(self, reference_value):
        """Sets the reference_value of this ComponentRepresentation.


        :param reference_value: The reference_value of this ComponentRepresentation.  # noqa: E501
        :type: float
        """

        self._reference_value = reference_value

    @property
    def reference_date(self):
        """Gets the reference_date of this ComponentRepresentation.  # noqa: E501


        :return: The reference_date of this ComponentRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._reference_date

    @reference_date.setter
    def reference_date(self, reference_date):
        """Sets the reference_date of this ComponentRepresentation.


        :param reference_date: The reference_date of this ComponentRepresentation.  # noqa: E501
        :type: datetime
        """

        self._reference_date = reference_date

    @property
    def reval_date_built(self):
        """Gets the reval_date_built of this ComponentRepresentation.  # noqa: E501


        :return: The reval_date_built of this ComponentRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._reval_date_built

    @reval_date_built.setter
    def reval_date_built(self, reval_date_built):
        """Sets the reval_date_built of this ComponentRepresentation.


        :param reval_date_built: The reval_date_built of this ComponentRepresentation.  # noqa: E501
        :type: datetime
        """

        self._reval_date_built = reval_date_built

    @property
    def last_modified(self):
        """Gets the last_modified of this ComponentRepresentation.  # noqa: E501


        :return: The last_modified of this ComponentRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ComponentRepresentation.


        :param last_modified: The last_modified of this ComponentRepresentation.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def financial_class_id(self):
        """Gets the financial_class_id of this ComponentRepresentation.  # noqa: E501


        :return: The financial_class_id of this ComponentRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._financial_class_id

    @financial_class_id.setter
    def financial_class_id(self, financial_class_id):
        """Sets the financial_class_id of this ComponentRepresentation.


        :param financial_class_id: The financial_class_id of this ComponentRepresentation.  # noqa: E501
        :type: int
        """

        self._financial_class_id = financial_class_id

    @property
    def financial_class_name(self):
        """Gets the financial_class_name of this ComponentRepresentation.  # noqa: E501


        :return: The financial_class_name of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._financial_class_name

    @financial_class_name.setter
    def financial_class_name(self, financial_class_name):
        """Sets the financial_class_name of this ComponentRepresentation.


        :param financial_class_name: The financial_class_name of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._financial_class_name = financial_class_name

    @property
    def financial_sub_class_id(self):
        """Gets the financial_sub_class_id of this ComponentRepresentation.  # noqa: E501


        :return: The financial_sub_class_id of this ComponentRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._financial_sub_class_id

    @financial_sub_class_id.setter
    def financial_sub_class_id(self, financial_sub_class_id):
        """Sets the financial_sub_class_id of this ComponentRepresentation.


        :param financial_sub_class_id: The financial_sub_class_id of this ComponentRepresentation.  # noqa: E501
        :type: int
        """

        self._financial_sub_class_id = financial_sub_class_id

    @property
    def financial_sub_class_name(self):
        """Gets the financial_sub_class_name of this ComponentRepresentation.  # noqa: E501


        :return: The financial_sub_class_name of this ComponentRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._financial_sub_class_name

    @financial_sub_class_name.setter
    def financial_sub_class_name(self, financial_sub_class_name):
        """Sets the financial_sub_class_name of this ComponentRepresentation.


        :param financial_sub_class_name: The financial_sub_class_name of this ComponentRepresentation.  # noqa: E501
        :type: str
        """

        self._financial_sub_class_name = financial_sub_class_name

    @property
    def links(self):
        """Gets the links of this ComponentRepresentation.  # noqa: E501


        :return: The links of this ComponentRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ComponentRepresentation.


        :param links: The links of this ComponentRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this ComponentRepresentation.  # noqa: E501


        :return: The embedded of this ComponentRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this ComponentRepresentation.


        :param embedded: The embedded of this ComponentRepresentation.  # noqa: E501
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
        if issubclass(ComponentRepresentation, dict):
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
        if not isinstance(other, ComponentRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
