# Copyright 2023 Infleqtion
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

from pydantic import BaseSettings


class Settings(BaseSettings):
    auth0_base_url: str = "https://coldquanta-dev.us.auth0.com"
    auth0_client_id: str = "ZzQdn5ZZq1dmpP5N55KINr33u47RBRiu"
    auth0_scope: str = "offline_access bec_dev_service:client"
    auth0_audience: str = "https://oraqle-dev.infleqtion.com/oqtant"
    signin_local_callback_url: str = "http://localhost:8080"
    base_url: str = "https://oraqle-dev.infleqtion.com/api/jobs"
    max_ind_var: int = 2
    max_job_batch_size: int = 30
