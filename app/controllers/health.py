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

from django.views import View
from django.http import JsonResponse
from app.tasks.sum import sum_task
from app.signals import http_call


class Health(View):
    """Health Page Controller"""

    def get(self, request):
        # Delegate the task to RQ workers
        sum_task.delay(1, 2)

        # Trigger a django signal
        http_call.send(sender=self.__class__, message="Hello World")

        return JsonResponse({
            "status": "ok"
        })
