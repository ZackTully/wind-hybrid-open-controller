# Copyright 2021 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# See https://nrel.github.io/wind-hybrid-open-controller for documentation

from whoc.interfaces.interface_base import InterfaceBase


class HerculesWindBatteryInterface(InterfaceBase):
    def __init__(self, input_dict):
        super().__init__()

    def get_measurements(self, hercules_dict):
        measurements = {
            "py_sims": {"battery": hercules_dict["py_sims"]["battery_0"]["outputs"]},
            "wind_farm": {
                "turbine_powers": hercules_dict["hercules_comms"]["amr_wind"]["wind_farm_0"][
                    "turbine_powers"
                ],
                "turbine_wind_directions": hercules_dict["hercules_comms"]["amr_wind"][
                    "wind_farm_0"
                ]["turbine_wind_directions"],
            },
        }

        return measurements

    def check_setpoints(self, setpoints_dict):
        setpoints = {}
        return setpoints

    def send_setpoints(self, hercules_dict, setpoints_dict=None):
        hercules_dict.update({"setpoints": setpoints_dict})
        return hercules_dict
