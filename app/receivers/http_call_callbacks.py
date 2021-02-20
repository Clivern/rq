# Copyright 2021 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from app.signals import http_call


def http_call_callback1(sender, message, **kwargs):
    """
    HTTP Call Callback 1

    Args:
        sender: the signal sender class name
        message: the message
        kwargs: additional arguments
    """
    print("New HTTP Call Action1 with Message: {message}".format(message=message))


def http_call_callback2(sender, message, **kwargs):
    """
    HTTP Call Callback 2

    Args:
        sender: the signal sender class name
        message: the message
        kwargs: additional arguments
    """
    print("New HTTP Call Action2 with Message: {message}".format(message=message))


# Attach signal with callback
http_call.connect(http_call_callback1)

http_call.connect(http_call_callback2)
