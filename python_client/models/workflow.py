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

from python_client.models.device_inner_system_reset_workflow_tasks import DeviceInnerSystemResetWorkflowTasks  # noqa: F401,E501


class Workflow(object):
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
        'add_to_inventory': 'bool',
        'added_on': 'int',
        'config_id': 'str',
        'curr_task_idx': 'int',
        'description': 'str',
        'end_time': 'int',
        'exec_time': 'int',
        'image_id': 'str',
        'lastupdate_on': 'int',
        'name': 'str',
        'start_time': 'int',
        'state': 'str',
        'tasks': 'list[DeviceInnerSystemResetWorkflowTasks]',
        'tenant_id': 'str',
        'type': 'str',
        'use_state': 'str',
        'version': 'int'
    }

    attribute_map = {
        'id': '_id',
        'add_to_inventory': 'addToInventory',
        'added_on': 'addedOn',
        'config_id': 'configId',
        'curr_task_idx': 'currTaskIdx',
        'description': 'description',
        'end_time': 'endTime',
        'exec_time': 'execTime',
        'image_id': 'imageId',
        'lastupdate_on': 'lastupdateOn',
        'name': 'name',
        'start_time': 'startTime',
        'state': 'state',
        'tasks': 'tasks',
        'tenant_id': 'tenantId',
        'type': 'type',
        'use_state': 'useState',
        'version': 'version'
    }

    def __init__(self, id=None, add_to_inventory=None, added_on=None, config_id=None, curr_task_idx=None, description=None, end_time=None, exec_time=None, image_id=None, lastupdate_on=None, name=None, start_time=None, state=None, tasks=None, tenant_id=None, type=None, use_state=None, version=None):  # noqa: E501
        """Workflow - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._add_to_inventory = None
        self._added_on = None
        self._config_id = None
        self._curr_task_idx = None
        self._description = None
        self._end_time = None
        self._exec_time = None
        self._image_id = None
        self._lastupdate_on = None
        self._name = None
        self._start_time = None
        self._state = None
        self._tasks = None
        self._tenant_id = None
        self._type = None
        self._use_state = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if add_to_inventory is not None:
            self.add_to_inventory = add_to_inventory
        if added_on is not None:
            self.added_on = added_on
        if config_id is not None:
            self.config_id = config_id
        if curr_task_idx is not None:
            self.curr_task_idx = curr_task_idx
        if description is not None:
            self.description = description
        if end_time is not None:
            self.end_time = end_time
        if exec_time is not None:
            self.exec_time = exec_time
        if image_id is not None:
            self.image_id = image_id
        if lastupdate_on is not None:
            self.lastupdate_on = lastupdate_on
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if state is not None:
            self.state = state
        if tasks is not None:
            self.tasks = tasks
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if use_state is not None:
            self.use_state = use_state
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this Workflow.  # noqa: E501


        :return: The id of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workflow.


        :param id: The id of this Workflow.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def add_to_inventory(self):
        """Gets the add_to_inventory of this Workflow.  # noqa: E501


        :return: The add_to_inventory of this Workflow.  # noqa: E501
        :rtype: bool
        """
        return self._add_to_inventory

    @add_to_inventory.setter
    def add_to_inventory(self, add_to_inventory):
        """Sets the add_to_inventory of this Workflow.


        :param add_to_inventory: The add_to_inventory of this Workflow.  # noqa: E501
        :type: bool
        """

        self._add_to_inventory = add_to_inventory

    @property
    def added_on(self):
        """Gets the added_on of this Workflow.  # noqa: E501


        :return: The added_on of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._added_on

    @added_on.setter
    def added_on(self, added_on):
        """Sets the added_on of this Workflow.


        :param added_on: The added_on of this Workflow.  # noqa: E501
        :type: int
        """

        self._added_on = added_on

    @property
    def config_id(self):
        """Gets the config_id of this Workflow.  # noqa: E501


        :return: The config_id of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this Workflow.


        :param config_id: The config_id of this Workflow.  # noqa: E501
        :type: str
        """

        self._config_id = config_id

    @property
    def curr_task_idx(self):
        """Gets the curr_task_idx of this Workflow.  # noqa: E501


        :return: The curr_task_idx of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._curr_task_idx

    @curr_task_idx.setter
    def curr_task_idx(self, curr_task_idx):
        """Sets the curr_task_idx of this Workflow.


        :param curr_task_idx: The curr_task_idx of this Workflow.  # noqa: E501
        :type: int
        """

        self._curr_task_idx = curr_task_idx

    @property
    def description(self):
        """Gets the description of this Workflow.  # noqa: E501


        :return: The description of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workflow.


        :param description: The description of this Workflow.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this Workflow.  # noqa: E501


        :return: The end_time of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Workflow.


        :param end_time: The end_time of this Workflow.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def exec_time(self):
        """Gets the exec_time of this Workflow.  # noqa: E501


        :return: The exec_time of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        """Sets the exec_time of this Workflow.


        :param exec_time: The exec_time of this Workflow.  # noqa: E501
        :type: int
        """

        self._exec_time = exec_time

    @property
    def image_id(self):
        """Gets the image_id of this Workflow.  # noqa: E501


        :return: The image_id of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Workflow.


        :param image_id: The image_id of this Workflow.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def lastupdate_on(self):
        """Gets the lastupdate_on of this Workflow.  # noqa: E501


        :return: The lastupdate_on of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._lastupdate_on

    @lastupdate_on.setter
    def lastupdate_on(self, lastupdate_on):
        """Sets the lastupdate_on of this Workflow.


        :param lastupdate_on: The lastupdate_on of this Workflow.  # noqa: E501
        :type: int
        """

        self._lastupdate_on = lastupdate_on

    @property
    def name(self):
        """Gets the name of this Workflow.  # noqa: E501


        :return: The name of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workflow.


        :param name: The name of this Workflow.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this Workflow.  # noqa: E501


        :return: The start_time of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Workflow.


        :param start_time: The start_time of this Workflow.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def state(self):
        """Gets the state of this Workflow.  # noqa: E501


        :return: The state of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Workflow.


        :param state: The state of this Workflow.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tasks(self):
        """Gets the tasks of this Workflow.  # noqa: E501


        :return: The tasks of this Workflow.  # noqa: E501
        :rtype: list[DeviceInnerSystemResetWorkflowTasks]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this Workflow.


        :param tasks: The tasks of this Workflow.  # noqa: E501
        :type: list[DeviceInnerSystemResetWorkflowTasks]
        """

        self._tasks = tasks

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Workflow.  # noqa: E501


        :return: The tenant_id of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Workflow.


        :param tenant_id: The tenant_id of this Workflow.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this Workflow.  # noqa: E501


        :return: The type of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Workflow.


        :param type: The type of this Workflow.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def use_state(self):
        """Gets the use_state of this Workflow.  # noqa: E501


        :return: The use_state of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._use_state

    @use_state.setter
    def use_state(self, use_state):
        """Sets the use_state of this Workflow.


        :param use_state: The use_state of this Workflow.  # noqa: E501
        :type: str
        """

        self._use_state = use_state

    @property
    def version(self):
        """Gets the version of this Workflow.  # noqa: E501


        :return: The version of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Workflow.


        :param version: The version of this Workflow.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
