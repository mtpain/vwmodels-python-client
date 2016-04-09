# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ModelProgress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ModelProgress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'created_at': 'datetime',
            'event_description': 'str',
            'event_name': 'str',
            'modelrun_id': 'int',
            'progress_value': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'event_description': 'event_description',
            'event_name': 'event_name',
            'modelrun_id': 'modelrun_id',
            'progress_value': 'progress_value'
        }

        self._id = None
        self._created_at = None
        self._event_description = None
        self._event_name = None
        self._modelrun_id = None
        self._progress_value = None

    @property
    def id(self):
        """
        Gets the id of this ModelProgress.


        :return: The id of this ModelProgress.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelProgress.


        :param id: The id of this ModelProgress.
        :type: int
        """
        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this ModelProgress.


        :return: The created_at of this ModelProgress.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ModelProgress.


        :param created_at: The created_at of this ModelProgress.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def event_description(self):
        """
        Gets the event_description of this ModelProgress.


        :return: The event_description of this ModelProgress.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """
        Sets the event_description of this ModelProgress.


        :param event_description: The event_description of this ModelProgress.
        :type: str
        """
        self._event_description = event_description

    @property
    def event_name(self):
        """
        Gets the event_name of this ModelProgress.


        :return: The event_name of this ModelProgress.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this ModelProgress.


        :param event_name: The event_name of this ModelProgress.
        :type: str
        """
        self._event_name = event_name

    @property
    def modelrun_id(self):
        """
        Gets the modelrun_id of this ModelProgress.


        :return: The modelrun_id of this ModelProgress.
        :rtype: int
        """
        return self._modelrun_id

    @modelrun_id.setter
    def modelrun_id(self, modelrun_id):
        """
        Sets the modelrun_id of this ModelProgress.


        :param modelrun_id: The modelrun_id of this ModelProgress.
        :type: int
        """
        self._modelrun_id = modelrun_id

    @property
    def progress_value(self):
        """
        Gets the progress_value of this ModelProgress.


        :return: The progress_value of this ModelProgress.
        :rtype: float
        """
        return self._progress_value

    @progress_value.setter
    def progress_value(self, progress_value):
        """
        Sets the progress_value of this ModelProgress.


        :param progress_value: The progress_value of this ModelProgress.
        :type: float
        """
        self._progress_value = progress_value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

