# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from python_client.models.reset_request_device_reset_list import ResetRequestDeviceResetList  # noqa: F401,E501


class ResetRequest(object):
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
        'device_reset_list': 'list[ResetRequestDeviceResetList]',
        'project_id': 'str',
        'workflow_id': 'str'
    }

    attribute_map = {
        'device_reset_list': 'deviceResetList',
        'project_id': 'projectId',
        'workflow_id': 'workflowId'
    }

    def __init__(self, device_reset_list=None, project_id=None, workflow_id=None):  # noqa: E501
        """ResetRequest - a model defined in Swagger"""  # noqa: E501

        self._device_reset_list = None
        self._project_id = None
        self._workflow_id = None
        self.discriminator = None

        if device_reset_list is not None:
            self.device_reset_list = device_reset_list
        if project_id is not None:
            self.project_id = project_id
        if workflow_id is not None:
            self.workflow_id = workflow_id

    @property
    def device_reset_list(self):
        """Gets the device_reset_list of this ResetRequest.  # noqa: E501


        :return: The device_reset_list of this ResetRequest.  # noqa: E501
        :rtype: list[ResetRequestDeviceResetList]
        """
        return self._device_reset_list

    @device_reset_list.setter
    def device_reset_list(self, device_reset_list):
        """Sets the device_reset_list of this ResetRequest.


        :param device_reset_list: The device_reset_list of this ResetRequest.  # noqa: E501
        :type: list[ResetRequestDeviceResetList]
        """

        self._device_reset_list = device_reset_list

    @property
    def project_id(self):
        """Gets the project_id of this ResetRequest.  # noqa: E501


        :return: The project_id of this ResetRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ResetRequest.


        :param project_id: The project_id of this ResetRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ResetRequest.  # noqa: E501


        :return: The workflow_id of this ResetRequest.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ResetRequest.


        :param workflow_id: The workflow_id of this ResetRequest.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
