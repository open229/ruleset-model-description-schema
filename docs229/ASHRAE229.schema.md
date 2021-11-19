# Data Types

\pandocbegin{footnotesize}

+-----------+-----------------+----------+--------------+
| **Data    | **Description** | **JSON   | **Examples** |
| Type**    |                 | Schema   |              |
|           |                 | Type**   |              |
+===========+=================+==========+==============+
| `Integer` | A positive or   | integer  | 3, 19, -4    |
|           | negative whole  |          |              |
|           | number (i.e., a |          |              |
|           | number that can |          |              |
|           | be written      |          |              |
|           | without a       |          |              |
|           | fractional      |          |              |
|           | part).          |          |              |
+-----------+-----------------+----------+--------------+
| `Numeric` | A number that   | number   | 3.43, 0, -4, |
|           | may include a   |          | 1.03e4       |
|           | fractional part |          |              |
|           | with optional   |          |              |
|           | leading sign    |          |              |
|           | and optional    |          |              |
|           | exponent        |          |              |
|           | (engineering    |          |              |
|           | notation).      |          |              |
+-----------+-----------------+----------+--------------+
| `Boolean` | True or false.  | boolean  | true, false  |
+-----------+-----------------+----------+--------------+
| `String`  | A sequence of   | string   | Indirect     |
|           | characters of   |          | evaporative  |
|           | any length      |          | cooler       |
|           | using any       |          |              |
|           | (specified)     |          |              |
|           | character set.  |          |              |
+-----------+-----------------+----------+--------------+
| `ID`      | A               | string   | AHU-01       |
|           | referencencable |          |              |
|           | identification  |          |              |
|           | for a data      |          |              |
|           | group and       |          |              |
|           | sequence of     |          |              |
|           | characters of   |          |              |
|           | any length      |          |              |
|           | using any       |          |              |
|           | (specified)     |          |              |
|           | character set.  |          |              |
+-----------+-----------------+----------+--------------+
| `Null`    | Indicator that  | null     | null         |
|           | no value is     |          |              |
|           | provided. Only  |          |              |
|           | used in         |          |              |
|           | combination     |          |              |
|           | with other data |          |              |
|           | types, e.g.,    |          |              |
|           | 'Number/Null'.  |          |              |
+-----------+-----------------+----------+--------------+

\pandocend{footnotesize}



# Enumerations

## ConditioningType

\pandocbegin{footnotesize}

+---------------------+-----------------+
| **Enumerator**      | **Description** |
+=====================+=================+
| `HEATED_AND_COOLED` | Heated and      |
|                     | cooled          |
+---------------------+-----------------+
| `HEATED_ONLY`       | Heated only     |
+---------------------+-----------------+
| `SEMIHEATED`        | Semiheated      |
+---------------------+-----------------+
| `UNCONDITIONED`     | Unconditioned   |
+---------------------+-----------------+

\pandocend{footnotesize}



## SpaceFunctionType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `LABORATORY`   | Laboratory      |
+----------------+-----------------+
| `KITCHEN`      | Kitchen         |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## InfiltrationMethodType

\pandocbegin{footnotesize}

+------------------+------------------------+
| **Enumerator**   | **Description**        |
+==================+========================+
| `WEATHER_DRIVEN` | Weather Driven. The    |
|                  | amount of air leakage  |
|                  | is determined by using |
|                  | the                    |
|                  | infiltration_flow_rate |
|                  | with a correlation     |
|                  | usually involving      |
|                  | windspeed, height, and |
|                  | the difference between |
|                  | indoor and outdoor     |
|                  | temperature and is     |
|                  | then multiplied by the |
|                  | schedule.              |
+------------------+------------------------+
| `PRESSURE_BASED` | Pressure Based. The    |
|                  | amount of air leakage  |
|                  | is determined by       |
|                  | induced airflows from  |
|                  | pressure differences   |
|                  | between zones, air     |
|                  | distribution system    |
|                  | components, the        |
|                  | outside due to wind    |
|                  | speed and direction.   |
+------------------+------------------------+
| `CONSTANT`       | Constant. The schedule |
|                  | is ignored.            |
+------------------+------------------------+
| `OTHER`          | Other infiltration     |
|                  | methods.               |
+------------------+------------------------+

\pandocend{footnotesize}



## SurfaceClassificationType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `WALL`         | Vertical or     |
|                | nearly vertical |
|                | wall            |
+----------------+-----------------+
| `FLOOR`        | Floor           |
+----------------+-----------------+
| `CEILING`      | Ceiling         |
+----------------+-----------------+

\pandocend{footnotesize}



## SurfaceAdjacentTo

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `EXTERIOR`     | Exterior wall   |
|                | or roof which   |
|                | is adjacent to  |
|                | the exterior    |
|                | environment.    |
+----------------+-----------------+
| `GROUND`       | Slab-on-grad or |
|                | below grade     |
|                | surface if      |
|                | adjacent to     |
|                | ground.         |
+----------------+-----------------+
| `INTERIOR`     | Interior        |
|                | surface if      |
|                | adjacent to     |
|                | another space   |
|                | which is        |
|                | explicity       |
|                | modeled.        |
+----------------+-----------------+
| `IDENTICAL`    | Surface         |
|                | adjacent to a   |
|                | environment     |
|                | identical to    |
|                | the space.      |
|                | Sometimes this  |
|                | is described as |
|                | adiabatic       |
|                | surface since   |
|                | no heat is      |
|                | transfered. The |
|                | space on the    |
|                | other side of   |
|                | the surface is  |
|                | not explicity   |
|                | modeled.        |
+----------------+-----------------+
| `UNDEFINED`    | The surface     |
|                | adjacency       |
|                | cannot be       |
|                | determined by   |
|                | the software.   |
+----------------+-----------------+

\pandocend{footnotesize}



## SurfaceConstructionInputOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `LAYERS`       | Construction is |
|                | entered         |
|                | layer-by-layer. |
+----------------+-----------------+
| `SIMPLIFIED`   | Construction is |
|                | entered by      |
|                | R-value only.   |
+----------------+-----------------+

\pandocend{footnotesize}



## SubsurfaceClassificationType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `WINDOW`       | Window          |
+----------------+-----------------+
| `SKYLIGHT`     | Skylight        |
+----------------+-----------------+
| `DOOR`         | Door            |
+----------------+-----------------+
| `OTHER`        | Other types of  |
|                | subsurfaces     |
|                | that allow      |
|                | light to pass   |
+----------------+-----------------+

\pandocend{footnotesize}



## SubsurfaceDynamicGlazingType

\pandocbegin{footnotesize}

+---------------------+-----------------+
| **Enumerator**      | **Description** |
+=====================+=================+
| `NOT_DYNAMIC`       | Not dynamic     |
+---------------------+-----------------+
| `MANUAL_DYNAMIC`    | Manual dynamic  |
+---------------------+-----------------+
| `AUTOMATIC_DYNAMIC` | Automatic       |
|                     | dynamic         |
+---------------------+-----------------+

\pandocend{footnotesize}



## LightingDaylightingControlType

\pandocbegin{footnotesize}

+----------------------+-----------------+-------------+
| **Enumerator**       | **Description** | **Notes**   |
+======================+=================+=============+
| `STEPPED`            | Stepped         |             |
+----------------------+-----------------+-------------+
| `CONTINUOUS_DIMMING` | Continuous      |             |
|                      | Dimming         |             |
+----------------------+-----------------+-------------+
| `OTHER`              | Other types of  |             |
|                      | daylighting     |             |
|                      | control         |             |
+----------------------+-----------------+-------------+
| `NONE`               | None            | No          |
|                      |                 | daylighting |
|                      |                 | is used.    |
+----------------------+-----------------+-------------+

\pandocend{footnotesize}



## LightingOccupancyControlType

\pandocbegin{footnotesize}

+-------------------+-----------------+-----------+
| **Enumerator**    | **Description** | **Notes** |
+===================+=================+===========+
| `FULL_AUTO_ON`    | Full auto on    |           |
+-------------------+-----------------+-----------+
| `PARTIAL_AUTO_ON` | Parial auto on  |           |
+-------------------+-----------------+-----------+
| `MANUAL_ON`       | Manual on       |           |
+-------------------+-----------------+-----------+
| `OTHER`           | Other types of  |           |
|                   | occupancy       |           |
|                   | control         |           |
+-------------------+-----------------+-----------+
| `NONE`            | None            | No        |
|                   |                 | occupancy |
|                   |                 | controls  |
|                   |                 | is used.  |
+-------------------+-----------------+-----------+

\pandocend{footnotesize}



## MiscellaneousEquipmentType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `PLUG`         | Plug            |
+----------------+-----------------+
| `PROCESS`      | Process         |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## TransformerType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `DRY_TYPE`     | Dry Type        |
+----------------+-----------------+
| `FLUID_FILLED` | Fluid Filled    |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## ElectricalPhase

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `SINGLE_PHASE` | Single Phase    |
+----------------+-----------------+
| `THREE_PHASE`  | Three Phase     |
+----------------+-----------------+

\pandocend{footnotesize}



## ScheduleSequenceTypeOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `HOURLY`       | Hourly          |
+----------------+-----------------+
| `EVENT`        | Event           |
+----------------+-----------------+

\pandocend{footnotesize}



## ScheduleTypeOptions

\pandocbegin{footnotesize}

+----------------------------+-----------------+
| **Enumerator**             | **Description** |
+============================+=================+
| `MULTIPLIER_DIMENSIONLESS` | Multiplier      |
|                            | dimensionless   |
+----------------------------+-----------------+
| `TEMPERATURE`              | Temperature     |
+----------------------------+-----------------+
| `POWER`                    | Power           |
+----------------------------+-----------------+
| `FLOW_RATE`                | Flow rate       |
+----------------------------+-----------------+

\pandocend{footnotesize}



## DayOfWeek

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `SUNDAY`       | Sunday          |
+----------------+-----------------+
| `MONDAY`       | Monday          |
+----------------+-----------------+
| `TUESDAY`      | Tuesday         |
+----------------+-----------------+
| `WEDNESDAY`    | Wednesday       |
+----------------+-----------------+
| `THURSDAY`     | Thursday        |
+----------------+-----------------+
| `FRIDAY`       | Friday          |
+----------------+-----------------+
| `SATURDAY`     | Saturday        |
+----------------+-----------------+

\pandocend{footnotesize}



## CoolingDesignDayTypeOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `COOLING_0_4`  | Cooling design  |
|                | day 0.4% annual |
|                | cumulative      |
|                | frequency of    |
|                | occurance       |
+----------------+-----------------+
| `COOLING_1_0`  | Cooling design  |
|                | day 1.0% annual |
|                | cumulative      |
|                | frequency of    |
|                | occurance       |
+----------------+-----------------+
| `COOLING_2_0`  | Cooling design  |
|                | day 2.0% annual |
|                | cumulative      |
|                | frequency of    |
|                | occurance       |
+----------------+-----------------+

\pandocend{footnotesize}



## HeatingDesignDayTypeOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `HEATING_99_6` | Heating design  |
|                | day 99.6%       |
|                | annual          |
|                | cumulative      |
|                | frequency of    |
|                | occurance       |
+----------------+-----------------+
| `HEATING_99_0` | Heating design  |
|                | day 99.0%       |
|                | annual          |
|                | cumulative      |
|                | frequency of    |
|                | occurance       |
+----------------+-----------------+

\pandocend{footnotesize}



## HeatingSystemType

\pandocbegin{footnotesize}

+-----------------------+-----------------+
| **Enumerator**        | **Description** |
+=======================+=================+
| `HEAT_PUMP`           | Heat Pump       |
+-----------------------+-----------------+
| `FURNACE`             | Furnace         |
+-----------------------+-----------------+
| `ELECTRIC_RESISTANCE` | Electric        |
|                       | resistance      |
+-----------------------+-----------------+
| `FLUID_LOOP`          | Fluid loop      |
+-----------------------+-----------------+
| `BASEBOARD`           | Baseboard       |
+-----------------------+-----------------+
| `NONE`                | None            |
+-----------------------+-----------------+
| `OTHER`               | Other           |
+-----------------------+-----------------+

\pandocend{footnotesize}



## HeatpumpAuxilliaryHeatType

\pandocbegin{footnotesize}

+-----------------------+-----------------+
| **Enumerator**        | **Description** |
+=======================+=================+
| `ELECTRIC_RESISTANCE` | Electric        |
|                       | resistance      |
+-----------------------+-----------------+
| `FURNACE`             | Furnace         |
+-----------------------+-----------------+
| `NONE`                | None            |
+-----------------------+-----------------+
| `OTHER`               | Other           |
+-----------------------+-----------------+

\pandocend{footnotesize}



## HumidificationType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `ADIABATIC`    | Adiabatic       |
+----------------+-----------------+
| `NONE`         | None            |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## CoolingSystemType

\pandocbegin{footnotesize}

+--------------------+-----------------+
| **Enumerator**     | **Description** |
+====================+=================+
| `DIRECT_EXPANSION` | Direct          |
|                    | expansion       |
+--------------------+-----------------+
| `FLUID_LOOP`       | Fluid loop      |
+--------------------+-----------------+
| `NON_MECHANICAL`   | Non-mechanical  |
+--------------------+-----------------+
| `NONE`             | None            |
+--------------------+-----------------+
| `OTHER`            | Other           |
+--------------------+-----------------+

\pandocend{footnotesize}



## DehumidificationType

\pandocbegin{footnotesize}

+------------------------+-----------------+
| **Enumerator**         | **Description** |
+========================+=================+
| `MECHANCIAL_COOLING`   | Mechanical      |
|                        | cooling         |
+------------------------+-----------------+
| `DESICCANT`            | Desiccant       |
+------------------------+-----------------+
| `SERIES_HEAT_RECOVERY` | Series heat     |
|                        | recovery        |
+------------------------+-----------------+
| `NONE`                 | None            |
+------------------------+-----------------+
| `OTHER`                | Other           |
+------------------------+-----------------+

\pandocend{footnotesize}



## FanSystemTemperatureControlType

\pandocbegin{footnotesize}

+---------------------+-----------------+
| **Enumerator**      | **Description** |
+=====================+=================+
| `CONSTANT`          | Constant        |
+---------------------+-----------------+
| `OUTDOOR_AIR_RESET` | Outdoor air     |
|                     | reset           |
+---------------------+-----------------+
| `ZONE_RESET`        | Zone reset      |
+---------------------+-----------------+
| `SCHEDULED`         | Scheduled       |
+---------------------+-----------------+
| `OTHER`             | Other           |
+---------------------+-----------------+

\pandocend{footnotesize}



## FanSystemSupplyFanControlType

\pandocbegin{footnotesize}

+------------------------+-----------------+
| **Enumerator**         | **Description** |
+========================+=================+
| `CONSTANT`             | Constant        |
+------------------------+-----------------+
| `VARIABLE_SPEED_DRIVE` | Variable speed  |
|                        | drive           |
+------------------------+-----------------+
| `MULTISPEED`           | Multispeed      |
+------------------------+-----------------+
| `INLET_VANE`           | Inlet vane      |
+------------------------+-----------------+
| `DISCHARGE_DAMPER`     | Discharge       |
|                        | damper          |
+------------------------+-----------------+
| `OTHER`                | Other           |
+------------------------+-----------------+

\pandocend{footnotesize}



## FanSystemOperationType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `CYCLING`      | Cycling         |
+----------------+-----------------+
| `CONTINUOUS`   | Continuous      |
+----------------+-----------------+
| `KEEP_OFF`     | Off             |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## AirEconomizerType

\pandocbegin{footnotesize}

+----------------------------+-----------------+
| **Enumerator**             | **Description** |
+============================+=================+
| `FIXED_FRACTION`           | Fixed Fraction  |
+----------------------------+-----------------+
| `TEMPERATURE`              | Dry-bulb        |
|                            | temperature     |
+----------------------------+-----------------+
| `ENTHALPY`                 | Enthalpy        |
+----------------------------+-----------------+
| `DIFFERENTIAL_TEMPERATURE` | Differential    |
|                            | dry-bulb        |
|                            | temperature     |
+----------------------------+-----------------+
| `DIFFERENTIAL_ENTHALPY`    | Differential    |
|                            | enthalpy        |
+----------------------------+-----------------+
| `OTHER`                    | Other           |
+----------------------------+-----------------+
| `NONE`                     | None            |
+----------------------------+-----------------+

\pandocend{footnotesize}



## EnergyRecoveryType

\pandocbegin{footnotesize}

+-------------------------+-----------------+
| **Enumerator**          | **Description** |
+=========================+=================+
| `SENSIBLE_HEAT_EXHANGE` | Sensible heat   |
|                         | exchange        |
+-------------------------+-----------------+
| `ENTHALPY_HEAT_EXHANGE` | Enthalpy heat   |
|                         | exchange        |
+-------------------------+-----------------+
| `SENSIBLE_HEAT_WHEEL`   | Sensible heat   |
|                         | wheel           |
+-------------------------+-----------------+
| `ENTHALPY_HEAT_WHEEL`   | Enthalpy heat   |
|                         | wheel           |
+-------------------------+-----------------+
| `HEAT_PIPE`             | Heat pipe       |
+-------------------------+-----------------+
| `OTHER`                 | Other           |
+-------------------------+-----------------+
| `NONE`                  | None            |
+-------------------------+-----------------+

\pandocend{footnotesize}



## EnergyRecoveryOperation

\pandocbegin{footnotesize}

+----------------------------+-----------------+
| **Enumerator**             | **Description** |
+============================+=================+
| `WHEN_FANS_ON`             | When fans on    |
+----------------------------+-----------------+
| `WHEN_MINIMUM_OUTSIDE_AIR` | When minimum    |
|                            | outside air     |
+----------------------------+-----------------+
| `SCHEDULED`                | Scheduled       |
+----------------------------+-----------------+
| `OTHER`                    | Other           |
+----------------------------+-----------------+
| `NONE`                     | None            |
+----------------------------+-----------------+

\pandocend{footnotesize}



## EnergyRecoverySupplyAirTemperatureControl

\pandocbegin{footnotesize}

+-------------------+-----------------+
| **Enumerator**    | **Description** |
+===================+=================+
| `FIXED_SETPOINT`  | Fixed setpoint  |
+-------------------+-----------------+
| `MIXED_AIR_RESET` | Mixed air reset |
+-------------------+-----------------+
| `OTHER`           | Other           |
+-------------------+-----------------+
| `NONE`            | None            |
+-------------------+-----------------+

\pandocend{footnotesize}



## DemandControlVentilationControlType

\pandocbegin{footnotesize}

+------------------+-----------------+
| **Enumerator**   | **Description** |
+==================+=================+
| `CO2_RETURN_AIR` | CO2 return air  |
+------------------+-----------------+
| `CO2_ZONE`       | CO2 zone        |
+------------------+-----------------+
| `OTHER`          | Other           |
+------------------+-----------------+
| `NONE`           | None            |
+------------------+-----------------+

\pandocend{footnotesize}



## FanSpecificationMethodOptions

\pandocbegin{footnotesize}

+----------------+-----------------+-------------+
| **Enumerator** | **Description** | **Notes**   |
+================+=================+=============+
| `SIMPLE`       | Simple          | Specify the |
|                |                 | electric    |
|                |                 | power input |
|                |                 | of fan      |
+----------------+-----------------+-------------+
| `DETAILED`     | Detailed        | Specify the |
|                |                 | brake horse |
|                |                 | power,      |
|                |                 | design      |
|                |                 | pressure    |
|                |                 | rise        |
|                |                 | through,    |
|                |                 | total       |
|                |                 | efficiency, |
|                |                 | motor       |
|                |                 | efficiency  |
+----------------+-----------------+-------------+

\pandocend{footnotesize}



## TerminalType

\pandocbegin{footnotesize}

+---------------------------+-----------------+
| **Enumerator**            | **Description** |
+===========================+=================+
| `VARIABLE_AIR_VOLUME`     | Variable air    |
|                           | volume          |
+---------------------------+-----------------+
| `CONSTANT_AIR_VOLUME`     | Constant air    |
|                           | volume          |
+---------------------------+-----------------+
| `DUCTLESS`                | Ductless        |
+---------------------------+-----------------+
| `RADIANT`                 | Radiant         |
+---------------------------+-----------------+
| `FOUR_PIPE_FAN_COIL_UNIT` | Four pipe fan   |
|                           | coil unit       |
+---------------------------+-----------------+
| `TWO_PIPE_FAN_COIL_UNIT`  | Two pipe fan    |
|                           | coil unit       |
+---------------------------+-----------------+
| `BASEBOARD`               | Baseboard       |
+---------------------------+-----------------+
| `OTHER`                   | Other           |
+---------------------------+-----------------+

\pandocend{footnotesize}



## TerminalFanConfiguration

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `PARALLEL`     | Parallel        |
+----------------+-----------------+
| `SERIES`       | Series          |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## ReheatSourceType

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `ELECTRIC`     | Electric        |
+----------------+-----------------+
| `HOT_WATER`    | Hot water       |
+----------------+-----------------+
| `NONE`         | None            |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## FluidLoopFlowControlOptions

\pandocbegin{footnotesize}

+-----------------+-----------------+
| **Enumerator**  | **Description** |
+=================+=================+
| `FIXED_FLOW`    | Fixed flow      |
+-----------------+-----------------+
| `VARIABLE_FLOW` | Variable flow   |
+-----------------+-----------------+

\pandocend{footnotesize}



## FluidLoopTypeOptions

\pandocbegin{footnotesize}

+-----------------------+-----------------+
| **Enumerator**        | **Description** |
+=======================+=================+
| `HEATING`             | Heating         |
+-----------------------+-----------------+
| `COOLING`             | Cooling         |
+-----------------------+-----------------+
| `HEATING_AND_COOLING` | Heating and     |
|                       | cooling         |
+-----------------------+-----------------+
| `CONDENSER`           | Condenser       |
+-----------------------+-----------------+
| `OTHER`               | Other           |
+-----------------------+-----------------+

\pandocend{footnotesize}



## TemperatureResetTypeOptions

\pandocbegin{footnotesize}

+---------------------+-----------------+
| **Enumerator**      | **Description** |
+=====================+=================+
| `NO_RESET`          | No Reset        |
+---------------------+-----------------+
| `CONSTANT`          | Constant        |
+---------------------+-----------------+
| `OUTSIDE_AIR_RESET` | Outside air     |
|                     | reste           |
+---------------------+-----------------+
| `LOAD_RESET`        | Load Reset      |
+---------------------+-----------------+
| `OTHER`             | Other           |
+---------------------+-----------------+

\pandocend{footnotesize}



## FluidLoopOperationOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `CONTINUOUS`   | Continuous      |
+----------------+-----------------+
| `INTERMITTENT` | Intermittent    |
+----------------+-----------------+

\pandocend{footnotesize}



## PumpSpeedControlOptions

\pandocbegin{footnotesize}

+------------------+-----------------+
| **Enumerator**   | **Description** |
+==================+=================+
| `FIXED_SPEED`    | Fixed speed     |
+------------------+-----------------+
| `VARIABLE_SPEED` | Variable speed  |
+------------------+-----------------+

\pandocend{footnotesize}



## PumpSpecificationMethodOptions

\pandocbegin{footnotesize}

+----------------+-----------------+-------------+
| **Enumerator** | **Description** | **Notes**   |
+================+=================+=============+
| `SIMPLE`       | Simple          | Specify the |
|                |                 | electric    |
|                |                 | power input |
|                |                 | of pump     |
+----------------+-----------------+-------------+
| `DETAILED`     | Detailed        | Specify the |
|                |                 | motor       |
|                |                 | nameplate   |
|                |                 | power,      |
|                |                 | design      |
|                |                 | head,       |
|                |                 | impellor    |
|                |                 | efficiency, |
|                |                 | motor       |
|                |                 | efficiency  |
+----------------+-----------------+-------------+

\pandocend{footnotesize}



## BoilerCombustionOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `NATURAL`      | Natural         |
+----------------+-----------------+
| `FORCED`       | Forced          |
+----------------+-----------------+

\pandocend{footnotesize}



## BoilerEfficiencyMetricTypeOptions

\pandocbegin{footnotesize}

+---------------------------+-----------------+
| **Enumerator**            | **Description** |
+===========================+=================+
| `ANNUAL_FUEL_UTILIZATION` | Annual fuel     |
|                           | utilization     |
|                           | efficiency      |
+---------------------------+-----------------+
| `THERMAL`                 | Thermal         |
|                           | efficiency      |
+---------------------------+-----------------+
| `COMBUSTION`              | Combustion      |
|                           | efficiency      |
+---------------------------+-----------------+

\pandocend{footnotesize}



## ChillerPartLoadEfficiencyMetricTypeOptions

\pandocbegin{footnotesize}

+-------------------------------+-----------------+
| **Enumerator**                | **Description** |
+===============================+=================+
| `INTEGRATED_PART_LOAD_VALUE`  | Integrated part |
|                               | load value      |
|                               | efficiency      |
|                               | expressed as a  |
|                               | coefficient of  |
|                               | performance     |
|                               | (COP)           |
+-------------------------------+-----------------+
| `NONSTANDARD_PART_LOAD_VALUE` | Nonstandard     |
|                               | part load value |
|                               | efficiency      |
|                               | expressed as a  |
|                               | coefficient of  |
|                               | performance     |
|                               | (COP)           |
+-------------------------------+-----------------+
| `OTHER`                       | Other part load |
|                               | efficiency      |
|                               | metric          |
+-------------------------------+-----------------+

\pandocend{footnotesize}



## ChillerCompressorTypeOptions

\pandocbegin{footnotesize}

+-------------------------------------------+-----------------+
| **Enumerator**                            | **Description** |
+===========================================+=================+
| `SCREW`                                   | Screw           |
+-------------------------------------------+-----------------+
| `CENTRIFUGAL`                             | Centrifugal     |
+-------------------------------------------+-----------------+
| `RECIPROCATING`                           | Reciprocating   |
+-------------------------------------------+-----------------+
| `SCROLL`                                  | Scroll          |
+-------------------------------------------+-----------------+
| `POSITIVE_DISPLACEMENT`                   | Positive        |
|                                           | displacement    |
+-------------------------------------------+-----------------+
| `SINGLE_EFFECT_INDIRECT_FIRED_ABSORPTION` | Single-effect   |
|                                           | indirect-fired  |
|                                           | absorption      |
+-------------------------------------------+-----------------+
| `DOUBLE_EFFECT_INDIRECT_FIRED_ABSORPTION` | Double-effect   |
|                                           | indirect-fired  |
|                                           | absorption      |
+-------------------------------------------+-----------------+
| `SINGLE_EFFECT_DIRECT_FIRED_ABSORPTION`   | Single-effect   |
|                                           | direct-fired    |
|                                           | absorption      |
+-------------------------------------------+-----------------+
| `DOUBLE_EFFECT_DIRECT_FIRED_ABSORPTION`   | Double-effect   |
|                                           | direct-fired    |
|                                           | absorption      |
+-------------------------------------------+-----------------+
| `OTHER`                                   | Other           |
+-------------------------------------------+-----------------+

\pandocend{footnotesize}



## HeatRejectionTypeOptions

\pandocbegin{footnotesize}

+--------------------------------+-----------------+
| **Enumerator**                 | **Description** |
+================================+=================+
| `OPEN_CIRCUIT_COOLING_TOWER`   | Open-circuit    |
|                                | cooling tower   |
+--------------------------------+-----------------+
| `CLOSED_CIRCUIT_COOLING_TOWER` | Closed-circuit  |
|                                | cooling tower   |
|                                | or fluid cooler |
+--------------------------------+-----------------+
| `DRY_COOLER`                   | Dry-cooler or   |
|                                | air-cooled      |
|                                | fluid cooler    |
+--------------------------------+-----------------+
| `EVAPORATIVE_CONDENSER`        | Evaporative     |
|                                | condenser       |
+--------------------------------+-----------------+
| `AIR_COOLED_CONDENSER`         | Air cooled      |
|                                | condenser       |
+--------------------------------+-----------------+
| `OTHER`                        | Other           |
+--------------------------------+-----------------+

\pandocend{footnotesize}



## HeatRejectionFanTypeOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `AXIAL`        | Axial or        |
|                | Propellor       |
+----------------+-----------------+
| `CENTRIFUGAL`  | Centrifugal     |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## HeatRejectionFluidOptions

\pandocbegin{footnotesize}

+----------------+-----------------+-----------+
| **Enumerator** | **Description** | **Notes** |
+================+=================+===========+
| `WATER`        | Water           |           |
+----------------+-----------------+-----------+
| `REFRIGERANT`  | Refrigerant     | Including |
|                |                 | R-448A    |
+----------------+-----------------+-----------+
| `AMMONIA`      | Ammonia         |           |
+----------------+-----------------+-----------+
| `OTHER`        | Other           |           |
+----------------+-----------------+-----------+

\pandocend{footnotesize}



## HeatRejectionResetOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `CONSTANT`     | Constant        |
+----------------+-----------------+
| `LOAD_RESET`   | Load reset      |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## HeatRejectionFanSpeedControlOptions

\pandocbegin{footnotesize}

+------------------+-----------------+
| **Enumerator**   | **Description** |
+==================+=================+
| `CONSTANT`       | Constant        |
+------------------+-----------------+
| `TWO_SPEED`      | Two Speed       |
+------------------+-----------------+
| `VARIABLE_SPEED` | Variable Speed  |
+------------------+-----------------+
| `OTHER`          | Other           |
+------------------+-----------------+

\pandocend{footnotesize}



## ExternalFluidSourceTypeOptions

\pandocbegin{footnotesize}

+-----------------+-----------------+
| **Enumerator**  | **Description** |
+=================+=================+
| `CHILLED_WATER` | Chilled water   |
+-----------------+-----------------+
| `HOT_WATER`     | Hot water       |
+-----------------+-----------------+
| `STEAM`         | Steam           |
+-----------------+-----------------+

\pandocend{footnotesize}



## ServiceWaterHeatingConfigurationType

\pandocbegin{footnotesize}

+------------------------------------------------------+-----------------+
| **Enumerator**                                       | **Description** |
+======================================================+=================+
| `HERS_PARALLEL_PIPING`                               | HERS parallel   |
|                                                      | piping          |
+------------------------------------------------------+-----------------+
| `HERS_PIPE_INSULATION_ALL_LINES`                     | HERS pipe       |
|                                                      | insulation of   |
|                                                      | all lines       |
+------------------------------------------------------+-----------------+
| `HERS_RECIRCULATION_DEMAND_CONTROL_OCCUPANCY_SENSOR` | HERS            |
|                                                      | recirculation   |
|                                                      | demand control  |
|                                                      | occupancy       |
|                                                      | sensor          |
+------------------------------------------------------+-----------------+
| `HERS_RECIRCULATION_DEMAND_CONTROL_BUTTON`           | HERS            |
|                                                      | recirculation   |
|                                                      | demand control  |
|                                                      | pull botton     |
+------------------------------------------------------+-----------------+
| `HERS_RECIRCULATION_NON_DEMAND_CONTROL`              | HERS            |
|                                                      | recirculation   |
|                                                      | non-demand      |
|                                                      | control         |
+------------------------------------------------------+-----------------+
| `INSULATED_AND_PROTECTED_PIPE_BELOW_GRADE`           | Insulated and   |
|                                                      | protected pipe  |
|                                                      | below grade     |
+------------------------------------------------------+-----------------+
| `PARALLEL_PIPING`                                    | Parallel piping |
+------------------------------------------------------+-----------------+
| `PIPE_INSULATION_ALL_LINES`                          | Pipe insulation |
|                                                      | of all lines    |
+------------------------------------------------------+-----------------+
| `POINT_OF_USE`                                       | Point of use    |
+------------------------------------------------------+-----------------+
| `RECIRCULATION_DEMAND_CONTROL_OCCUPANCY_SENSOR`      | Recirculation   |
|                                                      | demand control  |
|                                                      | occupancy       |
|                                                      | sensor          |
+------------------------------------------------------+-----------------+
| `RECIRCULATION_DEMAND_CONTROL_BUTTON`                | Recirculation   |
|                                                      | demand control  |
|                                                      | pull botton     |
+------------------------------------------------------+-----------------+
| `RECIRCULATION_NON_DEMAND_CONTROL`                   | Recirculation   |
|                                                      | non-demand      |
|                                                      | control         |
+------------------------------------------------------+-----------------+
| `STANDARD`                                           | Standard        |
+------------------------------------------------------+-----------------+
| `OTHER`                                              | Other           |
+------------------------------------------------------+-----------------+

\pandocend{footnotesize}



## ServiceWaterHeatingHeatRecoveryType

\pandocbegin{footnotesize}

+------------------+-----------------+
| **Enumerator**   | **Description** |
+==================+=================+
| `NOT_APPLICABLE` | Not applicable  |
+------------------+-----------------+
| `VERTICAL`       | Vertical        |
+------------------+-----------------+
| `HORIZONTAL`     | Horizontal      |
+------------------+-----------------+
| `OTHER`          | Other           |
+------------------+-----------------+

\pandocend{footnotesize}



## ServiceWaterHeaterType

\pandocbegin{footnotesize}

+----------------------+-----------------+
| **Enumerator**       | **Description** |
+======================+=================+
| `CONVENTIONAL`       | Conventional    |
+----------------------+-----------------+
| `HEAT_PUMP_PACKAGED` | Heat pump       |
|                      | packaged        |
+----------------------+-----------------+
| `HEAT_PUMP_SPLIT`    | Heat pump split |
+----------------------+-----------------+
| `OTHER`              | Other           |
+----------------------+-----------------+

\pandocend{footnotesize}



## ComponentLocation

\pandocbegin{footnotesize}

+-------------------+-----------------+
| **Enumerator**    | **Description** |
+===================+=================+
| `IN_ZONE`         | In a zone       |
+-------------------+-----------------+
| `CONDITIONED`     | Conditioned     |
+-------------------+-----------------+
| `SEMICONDITIONED` | Semiconditioned |
+-------------------+-----------------+
| `OUTSIDE`         | Outside         |
+-------------------+-----------------+
| `GARAGE`          | Garage          |
+-------------------+-----------------+
| `ATTIC`           | Attic           |
+-------------------+-----------------+
| `CRAWL_SPACE`     | Crawl space     |
+-------------------+-----------------+
| `UNDERGROUND`     | Underground     |
+-------------------+-----------------+
| `UNCONDITIONED`   | Unconditioned   |
+-------------------+-----------------+
| `OTHER`           | Other           |
+-------------------+-----------------+

\pandocend{footnotesize}



## ServiceWaterHeaterTankType

\pandocbegin{footnotesize}

+---------------------------------------------+------------------+-----------+
| **Enumerator**                              | **Description**  | **Notes** |
+=============================================+==================+===========+
| `CONSUMER_INSTANTANEOUS`                    | Consumer         | Uses UEF  |
|                                             | instantaneous    |           |
+---------------------------------------------+------------------+-----------+
| `COMMERCIAL_INSTANTANEOUS`                  | Commercial       | Uses TE   |
|                                             | instantaneous    |           |
+---------------------------------------------+------------------+-----------+
| `CONSUMER_STORAGE`                          | Consumer storage | Uses UEF  |
+---------------------------------------------+------------------+-----------+
| `COMMERCIAL_STORAGE`                        | Consumer storage | Uses TE   |
|                                             |                  | and SBL   |
+---------------------------------------------+------------------+-----------+
| `RESIDENTIAL_DUTY_COMMERCIAL_INSTANTANEOUS` | Residential-Duty | Uses UEF  |
|                                             | Commercial       |           |
|                                             | Instantaneous    |           |
+---------------------------------------------+------------------+-----------+
| `INDIRECT`                                  | Indirect         |           |
+---------------------------------------------+------------------+-----------+
| `BOILER`                                    | Boiler           |           |
+---------------------------------------------+------------------+-----------+
| `COMMERCIAL_PACKAGED_BOILER`                | Commercial       |           |
|                                             | Packaged Boiler  |           |
+---------------------------------------------+------------------+-----------+
| `OTHER`                                     | Other            |           |
+---------------------------------------------+------------------+-----------+

\pandocend{footnotesize}



## ServiceWaterHeatingFixtureType

\pandocbegin{footnotesize}

+------------------+-----------------+
| **Enumerator**   | **Description** |
+==================+=================+
| `SHOWER`         | Shower          |
+------------------+-----------------+
| `BATH`           | Bath            |
+------------------+-----------------+
| `RESTROOM_SINK`  | Restroom Sink   |
+------------------+-----------------+
| `DISHWASHER`     | Dishwasher      |
+------------------+-----------------+
| `KITCHEN_SINK`   | Kitchen sink    |
+------------------+-----------------+
| `WASH_SINK`      | Wash sink       |
+------------------+-----------------+
| `CLOTHES_WASHER` | Clothes washing |
|                  | machine         |
+------------------+-----------------+
| `OTHER`          | Other           |
+------------------+-----------------+

\pandocend{footnotesize}



## ServiceWaterHeatingUseUnits

\pandocbegin{footnotesize}

+---------------------+-----------------+
| **Enumerator**      | **Description** |
+=====================+=================+
| `POWER_PER_PERSON`  | Power per       |
|                     | person          |
+---------------------+-----------------+
| `POWER_PER_AREA`    | Power per area  |
+---------------------+-----------------+
| `POWER`             | Power           |
+---------------------+-----------------+
| `VOLUME_PER_PERSON` | Volume per      |
|                     | person          |
+---------------------+-----------------+
| `VOLUME_PER_AREA`   | Volume per area |
+---------------------+-----------------+
| `VOLUME`            | Volume          |
+---------------------+-----------------+
| `OTHER`             | Other           |
+---------------------+-----------------+

\pandocend{footnotesize}



## EnergySourceTypeOptions

\pandocbegin{footnotesize}

+----------------+-----------------+
| **Enumerator** | **Description** |
+================+=================+
| `ELECTRICITY`  | Electricity     |
+----------------+-----------------+
| `NATURAL_GAS`  | Natural gas     |
+----------------+-----------------+
| `PROPANE`      | Propane         |
+----------------+-----------------+
| `FUEL_OIL`     | Fuel oil        |
+----------------+-----------------+
| `OTHER`        | Other           |
+----------------+-----------------+

\pandocend{footnotesize}



## RefrigerationType

\pandocbegin{footnotesize}

+----------------------------------------------+-----------------+
| **Enumerator**                               | **Description** |
+==============================================+=================+
| `COMMERCIAL_REFRIGERATION`                   | Commercial      |
|                                              | refrigeration   |
+----------------------------------------------+-----------------+
| `COMMERCIAL_REFRIGERATOR_SOLID_DOOR`         | Commercial      |
|                                              | refrigerator    |
|                                              | solid door      |
+----------------------------------------------+-----------------+
| `COMMERCIAL_REFRIGERATOR_TRANSPARENT_DOOR`   | Commercial      |
|                                              | refrigerator    |
|                                              | transparent     |
|                                              | door            |
+----------------------------------------------+-----------------+
| `COMMERCIAL_FREEZER_SOLID_DOOR`              | Commercial      |
|                                              | freezer solid   |
|                                              | door            |
+----------------------------------------------+-----------------+
| `COMMERCIAL_FREEZER_TRANSPARENT_DOOR`        | Commercial      |
|                                              | freezer         |
|                                              | transparent     |
|                                              | door            |
+----------------------------------------------+-----------------+
| `COMMERCIAL_PULLDOWN_REFRIGERATOR`           | Commercial      |
|                                              | pulldown        |
|                                              | refrigerator    |
+----------------------------------------------+-----------------+
| `COMMERCIAL_REFRIGERATOR_FREEZER_SOLID_DOOR` | Commercial      |
|                                              | refrigerator    |
|                                              | freezer solid   |
|                                              | door            |
+----------------------------------------------+-----------------+
| `OTHER`                                      | Other           |
+----------------------------------------------+-----------------+

\pandocend{footnotesize}



## RefrigerationCategory

\pandocbegin{footnotesize}

+-------------------------------+-----------------+
| **Enumerator**                | **Description** |
+===============================+=================+
| `HORIZONTAL_OPEN`             | Horizontal open |
+-------------------------------+-----------------+
| `HORIZONTAL_SOLID_DOOR`       | Horizontal      |
|                               | solid door      |
+-------------------------------+-----------------+
| `HORIZONTAL_TRANSPARENT_DOOR` | Horizontal      |
|                               | transparent     |
|                               | door            |
+-------------------------------+-----------------+
| `SEMIVERTICAL_OPEN`           | Semivertical    |
|                               | open            |
+-------------------------------+-----------------+
| `SERVICE_OVER_COUNTER`        | Service over    |
|                               | counter         |
+-------------------------------+-----------------+
| `VERTICAL_OPEN`               | Vertical open   |
+-------------------------------+-----------------+
| `VERTICAL_SOLID_DOOR`         | Vertical solid  |
|                               | door            |
+-------------------------------+-----------------+
| `VERTICAL_TRANSPARENT_DOOR`   | Vertical        |
|                               | transparent     |
|                               | door            |
+-------------------------------+-----------------+
| `OTHER`                       | Other           |
+-------------------------------+-----------------+

\pandocend{footnotesize}



## ApplicationTemperatureType

\pandocbegin{footnotesize}

+----------------+-----------------+-----------+
| **Enumerator** | **Description** | **Notes** |
+================+=================+===========+
| `MEDIUM`       | Medium          | 3.3 C +/- |
|                | temperature     | 1.1 C (38 |
|                |                 | F +/- 2   |
|                |                 | F)        |
+----------------+-----------------+-----------+
| `LOW`          | Low temperature | -17.8 C   |
|                |                 | +/- 1.1 C |
|                |                 | (0 F +/-  |
|                |                 | 2 F)      |
+----------------+-----------------+-----------+
| `ICE_CREAM`    | Ice cream       | -26.1 C   |
|                |                 | +/- 1.1 C |
|                |                 | (-15 F    |
|                |                 | +/- 2 F)  |
+----------------+-----------------+-----------+
| `OTHER`        | Other           |           |
+----------------+-----------------+-----------+

\pandocend{footnotesize}



# Data Groups

## ASHRAE229

\pandocbegin{footnotesize}

+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| **Name**                                     | **Description**      | **Data Type**                                                                                                         | **Units** | **Constraints** | **Req** | **Notes**    |
+==============================================+======================+=======================================================================================================================+===========+=================+=========+==============+
| `id`                                         | Scope-unique         | `ID`                                                                                                                  |           |                 | $✓$     |              |
|                                              | reference identifier |                                                                                                                       |           |                 |         |              |
|                                              | for instances of     |                                                                                                                       |           |                 |         |              |
|                                              | this data group.     |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `reporting_name`                             | Descriptive name     | `String`                                                                                                              |           |                 |         |              |
|                                              | used in RCT reports  |                                                                                                                       |           |                 |         |              |
|                                              | if id is not already |                                                                                                                       |           |                 |         |              |
|                                              | a descriptive name   |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `notes`                                      | Supplementary        | `String`                                                                                                              |           |                 |         |              |
|                                              | information to       |                                                                                                                       |           |                 |         |              |
|                                              | provide context to   |                                                                                                                       |           |                 |         |              |
|                                              | the model reviewer   |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `transformers`                               | Electrical           | `[{Transformer}]`                                                                                                     |           |                 |         | Contains a   |
|                                              | transformers at the  |                                                                                                                       |           |                 |         | list of      |
|                                              | building site        |                                                                                                                       |           |                 |         | transformers |
|                                              |                      |                                                                                                                       |           |                 |         | that convert |
|                                              |                      |                                                                                                                       |           |                 |         | electricity  |
|                                              |                      |                                                                                                                       |           |                 |         | from a       |
|                                              |                      |                                                                                                                       |           |                 |         | higher       |
|                                              |                      |                                                                                                                       |           |                 |         | voltage to   |
|                                              |                      |                                                                                                                       |           |                 |         | one used by  |
|                                              |                      |                                                                                                                       |           |                 |         | the          |
|                                              |                      |                                                                                                                       |           |                 |         | building,    |
|                                              |                      |                                                                                                                       |           |                 |         | exterior     |
|                                              |                      |                                                                                                                       |           |                 |         | lighting,    |
|                                              |                      |                                                                                                                       |           |                 |         | and other    |
|                                              |                      |                                                                                                                       |           |                 |         | services at  |
|                                              |                      |                                                                                                                       |           |                 |         | the site.    |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `buildings`                                  | Buildings on the     | `[{Building}]`                                                                                                        |           |                 |         | Contains a   |
|                                              | site                 |                                                                                                                       |           |                 |         | list of      |
|                                              |                      |                                                                                                                       |           |                 |         | buildings on |
|                                              |                      |                                                                                                                       |           |                 |         | the site     |
|                                              |                      |                                                                                                                       |           |                 |         | (often just  |
|                                              |                      |                                                                                                                       |           |                 |         | one).        |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `calendar`                                   | Information on the   | `{Calendar}`                                                                                                          |           |                 |         |              |
|                                              | calendar used with   |                                                                                                                       |           |                 |         |              |
|                                              | the simulation.      |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `schedules`                                  | Schedules for        | `[{Schedule}]`                                                                                                        |           |                 |         | Contains a   |
|                                              | internal loads,      |                                                                                                                       |           |                 |         | list of      |
|                                              | thermostats,         |                                                                                                                       |           |                 |         | schedules    |
|                                              | equipment operation  |                                                                                                                       |           |                 |         | used in      |
|                                              | and control, and any |                                                                                                                       |           |                 |         | model.       |
|                                              | other need.          |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `weather`                                    | Information on the   | `{Weather}`                                                                                                           |           |                 |         |              |
|                                              | local weather        |                                                                                                                       |           |                 |         |              |
|                                              | conditions used with |                                                                                                                       |           |                 |         |              |
|                                              | the simulation.      |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `measured_infiltration_pressure_difference`  | Differential         | `Numeric`                                                                                                             | Pa        | `≥0`            |         | Used as      |
|                                              | pressure difference  |                                                                                                                       |           |                 |         | rating       |
|                                              | used during          |                                                                                                                       |           |                 |         | conditions   |
|                                              | measurement for      |                                                                                                                       |           |                 |         | for air      |
|                                              | infiltration values. |                                                                                                                       |           |                 |         | leakage for  |
|                                              |                      |                                                                                                                       |           |                 |         | a building.  |
|                                              |                      |                                                                                                                       |           |                 |         | The most     |
|                                              |                      |                                                                                                                       |           |                 |         | common       |
|                                              |                      |                                                                                                                       |           |                 |         | values used  |
|                                              |                      |                                                                                                                       |           |                 |         | are 50 Pa or |
|                                              |                      |                                                                                                                       |           |                 |         | 75 Pa since  |
|                                              |                      |                                                                                                                       |           |                 |         | they         |
|                                              |                      |                                                                                                                       |           |                 |         | correspond   |
|                                              |                      |                                                                                                                       |           |                 |         | to common    |
|                                              |                      |                                                                                                                       |           |                 |         | rating       |
|                                              |                      |                                                                                                                       |           |                 |         | conditions.  |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `is_measured_infiltration_based_on_test`     | Indicates whether    | `Boolean`                                                                                                             |           |                 |         |              |
|                                              | the differential     |                                                                                                                       |           |                 |         |              |
|                                              | pressure difference  |                                                                                                                       |           |                 |         |              |
|                                              | used during          |                                                                                                                       |           |                 |         |              |
|                                              | measurement for      |                                                                                                                       |           |                 |         |              |
|                                              | infiltration values  |                                                                                                                       |           |                 |         |              |
|                                              | is based on pressure |                                                                                                                       |           |                 |         |              |
|                                              | testing of the       |                                                                                                                       |           |                 |         |              |
|                                              | building.            |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `overall_simulation_outputs`                 | Outputs from the     | `{OverallSimulationOutputs}`                                                                                          |           |                 |         |              |
|                                              | simluation summed    |                                                                                                                       |           |                 |         |              |
|                                              | for all buildings in |                                                                                                                       |           |                 |         |              |
|                                              | the simulation.      |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `ruleset_model_type`                         | Describes the        | `(<RulesetModelType2019ASHRAE901>,<RulesetModelTypeRESNET,<RulesetModelType2019T24Com>,<RulesetModelType2019T24Res>)` |           |                 |         |              |
|                                              | current model for    |                                                                                                                       |           |                 |         |              |
|                                              | rulesets with        |                                                                                                                       |           |                 |         |              |
|                                              | multiple simulation  |                                                                                                                       |           |                 |         |              |
|                                              | models               |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `compliance_path`                            | Indicates the chosen | `<CompliancePathType2019ASHRAE901>`                                                                                   |           |                 |         |              |
|                                              | compliance path if   |                                                                                                                       |           |                 |         |              |
|                                              | the ruleset has      |                                                                                                                       |           |                 |         |              |
|                                              | multiple compliance  |                                                                                                                       |           |                 |         |              |
|                                              | paths such as 90.1   |                                                                                                                       |           |                 |         |              |
|                                              | Appendix G has code  |                                                                                                                       |           |                 |         |              |
|                                              | compliance and       |                                                                                                                       |           |                 |         |              |
|                                              | beyond code          |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `building_rotation_angles`                   | A list of angles     | `[Numeric]`                                                                                                           | degrees   |                 |         | List of      |
|                                              | that building        |                                                                                                                       |           |                 |         | angles that  |
|                                              | simulations are      |                                                                                                                       |           |                 |         | the building |
|                                              | performed and        |                                                                                                                       |           |                 |         | has been     |
|                                              | results are          |                                                                                                                       |           |                 |         | rotated.     |
|                                              | provided.            |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `fluid_loops`                                | Fluid loops on the   | `[{FluidLoop}]`                                                                                                       |           |                 |         | Contains a   |
|                                              | site                 |                                                                                                                       |           |                 |         | list of      |
|                                              |                      |                                                                                                                       |           |                 |         | fluid loops  |
|                                              |                      |                                                                                                                       |           |                 |         | on the site. |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `service_water_heating_distribution_systems` | Service water        | `[{ServiceWaterHeatingDistributionSystem}]`                                                                           |           |                 |         | Contains a   |
|                                              | heating systems on   |                                                                                                                       |           |                 |         | list of      |
|                                              | the site             |                                                                                                                       |           |                 |         | service      |
|                                              |                      |                                                                                                                       |           |                 |         | water        |
|                                              |                      |                                                                                                                       |           |                 |         | heating      |
|                                              |                      |                                                                                                                       |           |                 |         | distribution |
|                                              |                      |                                                                                                                       |           |                 |         | systems at   |
|                                              |                      |                                                                                                                       |           |                 |         | the site.    |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `pumps`                                      | Pumps used on the    | `[{Pump}]`                                                                                                            |           |                 |         |              |
|                                              | site                 |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `boilers`                                    | Boilers used on the  | `[{Boiler}]`                                                                                                          |           |                 |         |              |
|                                              | site                 |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `chillers`                                   | Chillers used on the | `[{Chiller}]`                                                                                                         |           |                 |         |              |
|                                              | site                 |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `heat_rejections`                            | HeatRejections used  | `[{HeatRejection}]`                                                                                                   |           |                 |         |              |
|                                              | on the site          |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `external_fluid_source`                      | ExternalFluidSources | `[{ExternalFluidSource}]`                                                                                             |           |                 |         |              |
|                                              | used on the site     |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `site_zone_type`                             | Site zone type for   | `<ExteriorLightingZones2019ASHRAE901>`                                                                                |           |                 |         |              |
|                                              | Sec 9.4.2            |                                                                                                                       |           |                 |         |              |
+----------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



## Building

\pandocbegin{footnotesize}

+----------------------------+-----------------+------------------------+---------+---------------+
| **Name**                   | **Description** | **Data Type**          | **Req** | **Notes**     |
+============================+=================+========================+=========+===============+
| `id`                       | Scope-unique    | `ID`                   | $✓$     |               |
|                            | reference       |                        |         |               |
|                            | identifier for  |                        |         |               |
|                            | instances of    |                        |         |               |
|                            | this data group |                        |         |               |
+----------------------------+-----------------+------------------------+---------+---------------+
| `reporting_name`           | Descriptive     | `String`               |         |               |
|                            | name used in    |                        |         |               |
|                            | RCT reports if  |                        |         |               |
|                            | id is not       |                        |         |               |
|                            | already a       |                        |         |               |
|                            | descriptive     |                        |         |               |
|                            | name            |                        |         |               |
+----------------------------+-----------------+------------------------+---------+---------------+
| `notes`                    | Supplementary   | `String`               |         |               |
|                            | information to  |                        |         |               |
|                            | provide context |                        |         |               |
|                            | to the model    |                        |         |               |
|                            | reviewer        |                        |         |               |
+----------------------------+-----------------+------------------------+---------+---------------+
| `building_segments`        | Large portions  | `[{BuildingSegment}]`  |         | Contains a    |
|                            | of a building   |                        |         | list of       |
|                            | that share a    |                        |         | building      |
|                            | building area   |                        |         | segments in   |
|                            | type            |                        |         | the building. |
+----------------------------+-----------------+------------------------+---------+---------------+
| `elevators`                | Elevators       | `[{Elevator}]`         |         | Contains a    |
|                            |                 |                        |         | list of       |
|                            |                 |                        |         | elevators in  |
|                            |                 |                        |         | the building. |
+----------------------------+-----------------+------------------------+---------+---------------+
| `exterior_lighting`        | Exterior        | `[{ExteriorLighting}]` |         | Contains a    |
|                            | lighting        |                        |         | list of       |
|                            | systems         |                        |         | exterior      |
|                            |                 |                        |         | lighting      |
|                            |                 |                        |         | systems for   |
|                            |                 |                        |         | the building. |
+----------------------------+-----------------+------------------------+---------+---------------+
| `refrigeration_components` | Refrigeration   | `[{Refrigeration}]`    |         | Contains a    |
|                            |                 |                        |         | list of       |
|                            |                 |                        |         | refrigeration |
|                            |                 |                        |         | components in |
|                            |                 |                        |         | the building. |
+----------------------------+-----------------+------------------------+---------+---------------+
| `building_open_schedule`   | Reference to    | `$ID`                  | $✓$     | One represent |
|                            | the schedule    |                        |         | when the      |
|                            | containing      |                        |         | building is   |
|                            | indicating when |                        |         | open and zero |
|                            | the building is |                        |         | when closed.  |
|                            | open            |                        |         | Constraint to |
|                            |                 |                        |         | use when      |
|                            |                 |                        |         | implemented   |
|                            |                 |                        |         | :Schedule:    |
+----------------------------+-----------------+------------------------+---------+---------------+
| `has_site_shading`         | Indicates       | `Boolean`              |         |               |
|                            | whether the     |                        |         |               |
|                            | site has        |                        |         |               |
|                            | features that   |                        |         |               |
|                            | cast shadows on |                        |         |               |
|                            | the building    |                        |         |               |
+----------------------------+-----------------+------------------------+---------+---------------+

\pandocend{footnotesize}



## BuildingSegment

\pandocbegin{footnotesize}

+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| **Name**                                                | **Description** | **Data Type**                                                      | **Constraints** | **Req** | **Notes**    |
+=========================================================+=================+====================================================================+=================+=========+==============+
| `id`                                                    | Scope-unique    | `ID`                                                               |                 | $✓$     |              |
|                                                         | reference       |                                                                    |                 |         |              |
|                                                         | identifier for  |                                                                    |                 |         |              |
|                                                         | instances of    |                                                                    |                 |         |              |
|                                                         | this data group |                                                                    |                 |         |              |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `reporting_name`                                        | Descriptive     | `String`                                                           |                 |         |              |
|                                                         | name used in    |                                                                    |                 |         |              |
|                                                         | RCT reports if  |                                                                    |                 |         |              |
|                                                         | id is not       |                                                                    |                 |         |              |
|                                                         | already a       |                                                                    |                 |         |              |
|                                                         | descriptive     |                                                                    |                 |         |              |
|                                                         | name            |                                                                    |                 |         |              |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `notes`                                                 | Supplementary   | `String`                                                           |                 |         |              |
|                                                         | information to  |                                                                    |                 |         |              |
|                                                         | provide context |                                                                    |                 |         |              |
|                                                         | to the model    |                                                                    |                 |         |              |
|                                                         | reviewer        |                                                                    |                 |         |              |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `number_of_floors_above_grade`                          | Number of       | `Numeric`                                                          | `≥0`            |         | JG to verify |
|                                                         | floors above    |                                                                    |                 |         | if used in   |
|                                                         | grade           |                                                                    |                 |         | test case    |
|                                                         |                 |                                                                    |                 |         | description. |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `number_of_floors_below_grade`                          | Number of       | `Numeric`                                                          | `≥0`            |         | JG to verify |
|                                                         | floors below    |                                                                    |                 |         | if used in   |
|                                                         | grade           |                                                                    |                 |         | test case    |
|                                                         |                 |                                                                    |                 |         | description. |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `is_all_new`                                            | Indicates       | `Boolean`                                                          |                 |         | Projects     |
|                                                         | whether the     |                                                                    |                 |         | that include |
|                                                         | building        |                                                                    |                 |         | additions    |
|                                                         | segment is      |                                                                    |                 |         | should have  |
|                                                         | completely new  |                                                                    |                 |         | a building   |
|                                                         | construction    |                                                                    |                 |         | segments     |
|                                                         | (true) or       |                                                                    |                 |         | that are     |
|                                                         | existing        |                                                                    |                 |         | existing     |
|                                                         | (false).        |                                                                    |                 |         | (false) and  |
|                                                         |                 |                                                                    |                 |         | for the      |
|                                                         |                 |                                                                    |                 |         | addition     |
|                                                         |                 |                                                                    |                 |         | (true).      |
|                                                         |                 |                                                                    |                 |         | Curtain      |
|                                                         |                 |                                                                    |                 |         | rules such   |
|                                                         |                 |                                                                    |                 |         | as baseline  |
|                                                         |                 |                                                                    |                 |         | fenestration |
|                                                         |                 |                                                                    |                 |         | area will    |
|                                                         |                 |                                                                    |                 |         | apply        |
|                                                         |                 |                                                                    |                 |         | differently  |
|                                                         |                 |                                                                    |                 |         | to each      |
|                                                         |                 |                                                                    |                 |         | portion.     |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `zones`                                                 | Zones in the    | `[{Zone}]`                                                         |                 |         | Contains a   |
|                                                         | building        |                                                                    |                 |         | list of      |
|                                                         |                 |                                                                    |                 |         | zones in the |
|                                                         |                 |                                                                    |                 |         | building.    |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `heating_ventilation_air_conditioning_systems`          | HVAC systems in | `[{HeatingVentilationAirConditioningSystem}]`                      |                 |         | Contains a   |
|                                                         | the building    |                                                                    |                 |         | list of HVAC |
|                                                         |                 |                                                                    |                 |         | systems in   |
|                                                         |                 |                                                                    |                 |         | the          |
|                                                         |                 |                                                                    |                 |         | building.    |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `area_type_vertical_fenestration`                       | Building area   | `<VerticalFenestrationBuildingAreaType2019ASHRAE901>`              |                 |         | The          |
|                                                         | classification  |                                                                    |                 |         | enumeration  |
|                                                         | used for        |                                                                    |                 |         | is based on  |
|                                                         | vertical        |                                                                    |                 |         | the standard |
|                                                         | fenestration    |                                                                    |                 |         | used.        |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `lighting_building_area_type`                           | Building area   | `<LightingSpaceType2019ASHRAE901T951TG38>`                         |                 |         |              |
|                                                         | lighting area   |                                                                    |                 |         |              |
|                                                         | type            |                                                                    |                 |         |              |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+
| `area_type_heating_ventilation_air_conditioning_system` | Classification  | `<HeatingVentilationAirConditioningBuildingAreaType2019ASHRAE901>` |                 |         | The          |
|                                                         | used for HVAC   |                                                                    |                 |         | enumeration  |
|                                                         |                 |                                                                    |                 |         | is based on  |
|                                                         |                 |                                                                    |                 |         | the standard |
|                                                         |                 |                                                                    |                 |         | used. JG to  |
|                                                         |                 |                                                                    |                 |         | verify if    |
|                                                         |                 |                                                                    |                 |         | used in test |
|                                                         |                 |                                                                    |                 |         | case         |
|                                                         |                 |                                                                    |                 |         | description. |
+---------------------------------------------------------+-----------------+--------------------------------------------------------------------+-----------------+---------+--------------+

\pandocend{footnotesize}



## Zone

\pandocbegin{footnotesize}

+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| **Name**                                 | **Description** | **Data Type**        | **Units** | **Constraints** | **Req** | **Notes**                               |
+==========================================+=================+======================+===========+=================+=========+=========================================+
| `id`                                     | Scope-unique    | `ID`                 |           |                 | $✓$     |                                         |
|                                          | reference       |                      |           |                 |         |                                         |
|                                          | identifier for  |                      |           |                 |         |                                         |
|                                          | instances of    |                      |           |                 |         |                                         |
|                                          | this data group |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `reporting_name`                         | Descriptive     | `String`             |           |                 |         |                                         |
|                                          | name used in    |                      |           |                 |         |                                         |
|                                          | RCT reports if  |                      |           |                 |         |                                         |
|                                          | id is not       |                      |           |                 |         |                                         |
|                                          | already a       |                      |           |                 |         |                                         |
|                                          | descriptive     |                      |           |                 |         |                                         |
|                                          | name            |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `notes`                                  | Supplementary   | `String`             |           |                 |         |                                         |
|                                          | information to  |                      |           |                 |         |                                         |
|                                          | provide context |                      |           |                 |         |                                         |
|                                          | to the model    |                      |           |                 |         |                                         |
|                                          | reviewer        |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `spaces`                                 | Spaces in the   | `[{Space}]`          |           |                 |         | Contains a list of spaces in the        |
|                                          | zone            |                      |           |                 |         | building.                               |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `volume`                                 | Volume of the   | `Numeric`            | m^3^      | `≥0`            |         |                                         |
|                                          | space           |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `surfaces`                               | Surfaces        | `[{Surface}]`        |           |                 |         | Contains a list of surfaces that define |
|                                          | surrounding the |                      |           |                 |         | the zone.                               |
|                                          | zone            |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `conditioning_type`                      | Space           | `<ConditioningType>` |           |                 |         |                                         |
|                                          | conditioning    |                      |           |                 |         |                                         |
|                                          | category        |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `infiltration`                           | Airleakage into | `{Infiltration}`     |           |                 |         | References a single infiltration data   |
|                                          | the zone.       |                      |           |                 |         | group.                                  |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `design_thermostat_cooling_setpoint`     | Setpoint        | `Numeric`            | C         |                 |         | JG to verify if used in test case       |
|                                          | temperature for |                      |           |                 |         | description.                            |
|                                          | cooling during  |                      |           |                 |         |                                         |
|                                          | occupied hours  |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `thermostat_cooling_setpoint_schedule`   | Reference to    | `$ID`                |           |                 | $✓$     | Constraint to use when implemented      |
|                                          | the schedule    |                      |           |                 |         | :Schedule:                              |
|                                          | containing the  |                      |           |                 |         |                                         |
|                                          | cooling         |                      |           |                 |         |                                         |
|                                          | setpoint        |                      |           |                 |         |                                         |
|                                          | temperatures    |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `design_thermostat_heating_setpoint`     | Setpoint        | `Numeric`            | C         |                 |         | JG to verify if used in test case       |
|                                          | temperature for |                      |           |                 |         | description.                            |
|                                          | heating during  |                      |           |                 |         |                                         |
|                                          | occupied hours  |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `thermostat_heating_setpoint_schedule`   | Reference to    | `$ID`                |           |                 | $✓$     | Constraint to use when implemented      |
|                                          | the schedule    |                      |           |                 |         | :Schedule:                              |
|                                          | containing the  |                      |           |                 |         |                                         |
|                                          | heating         |                      |           |                 |         |                                         |
|                                          | setpoint        |                      |           |                 |         |                                         |
|                                          | temperatures    |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `terminals`                              | List of         | `[{Terminal}]`       |           |                 |         | Multple terminals may be used such as   |
|                                          | terminals       |                      |           |                 |         | from a VAV system, a DOAS, and a        |
|                                          |                 |                      |           |                 |         | baseboard. JG to verify if used in test |
|                                          |                 |                      |           |                 |         | case description.                       |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `served_by_service_water_heating_system` | A service water | `$ID`                |           |                 |         | Contains a single ID of the service     |
|                                          | heating system  |                      |           |                 |         | water heating system serving the zone - |
|                                          | serving the     |                      |           |                 |         | from Unique Identification Number in    |
|                                          | zone            |                      |           |                 |         | ServiceWaterHeatingSystem. Constraint   |
|                                          |                 |                      |           |                 |         | to use when implemented                 |
|                                          |                 |                      |           |                 |         | :ServiceWaterHeatingDistributionSystem: |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `transfer_airflow_rate`                  | Transfer        | `Numeric`            | L/s       | `≥0`            |         | JG to verify if used in test case       |
|                                          | airflow rate    |                      |           |                 |         | description.                            |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `exhaust_airflow_rate`                   | Number of       | `Numeric`            | L/s       | `≥0`            |         | JG to verify if used in test case       |
|                                          | occupants in    |                      |           |                 |         | description.                            |
|                                          | the space       |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `non_mechanical_cooling_fan_power`       | Non-mechanical  | `Numeric`            | W         | `≥0`            |         | JG to verify if used in test case       |
|                                          | cooling fan     |                      |           |                 |         | description.                            |
|                                          | power           |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `non_mechanical_cooling_fan_airflow`     | Non-mechanical  | `Numeric`            | L/s       | `≥0`            |         | JG to verify if used in test case       |
|                                          | cooling fan     |                      |           |                 |         | description.                            |
|                                          | power           |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+
| `air_distribution_effectiveness`         | Air             | `Numeric`            |           | `≥0`            |         | JG to verify if used in test case       |
|                                          | distribution    |                      |           |                 |         | description.                            |
|                                          | effectiveness   |                      |           |                 |         |                                         |
+------------------------------------------+-----------------+----------------------+-----------+-----------------+---------+-----------------------------------------+

\pandocend{footnotesize}



## Space

\pandocbegin{footnotesize}

+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| **Name**                           | **Description** | **Data Type**                                                 | **Units** | **Constraints** | **Req** | **Notes**            |
+====================================+=================+===============================================================+===========+=================+=========+======================+
| `id`                               | Scope-unique    | `ID`                                                          |           |                 | $✓$     |                      |
|                                    | reference       |                                                               |           |                 |         |                      |
|                                    | identifier for  |                                                               |           |                 |         |                      |
|                                    | instances of    |                                                               |           |                 |         |                      |
|                                    | this data group |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `reporting_name`                   | Descriptive     | `String`                                                      |           |                 |         |                      |
|                                    | name used in    |                                                               |           |                 |         |                      |
|                                    | RCT reports if  |                                                               |           |                 |         |                      |
|                                    | id is not       |                                                               |           |                 |         |                      |
|                                    | already a       |                                                               |           |                 |         |                      |
|                                    | descriptive     |                                                               |           |                 |         |                      |
|                                    | name            |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `notes`                            | Supplementary   | `String`                                                      |           |                 |         |                      |
|                                    | information to  |                                                               |           |                 |         |                      |
|                                    | provide context |                                                               |           |                 |         |                      |
|                                    | to the model    |                                                               |           |                 |         |                      |
|                                    | reviewer        |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `interior_lighting`                | Internal        | `[{InteriorLighting}]`                                        |           |                 |         |                      |
|                                    | lighting that   |                                                               |           |                 |         |                      |
|                                    | produce         |                                                               |           |                 |         |                      |
|                                    | internal gains  |                                                               |           |                 |         |                      |
|                                    | for a space.    |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `miscellaneous_equipment`          | Miscellaneous   | `[{MiscellaneousEquipment}]`                                  |           |                 |         |                      |
|                                    | equipment loads |                                                               |           |                 |         |                      |
|                                    | that produce    |                                                               |           |                 |         |                      |
|                                    | internal gains  |                                                               |           |                 |         |                      |
|                                    | for a space.    |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `floor_area`                       | The floor area  | `Numeric`                                                     | m^2^      | `≥0`            |         | The floor area of a  |
|                                    | of the space.   |                                                               |           |                 |         | space within the     |
|                                    |                 |                                                               |           |                 |         | building, including  |
|                                    |                 |                                                               |           |                 |         | basements, mezzanine |
|                                    |                 |                                                               |           |                 |         | and                  |
|                                    |                 |                                                               |           |                 |         | intermediate-floored |
|                                    |                 |                                                               |           |                 |         | tiers, and           |
|                                    |                 |                                                               |           |                 |         | penthouses with a    |
|                                    |                 |                                                               |           |                 |         | headroom height of   |
|                                    |                 |                                                               |           |                 |         | 7.5 ft or greater.   |
|                                    |                 |                                                               |           |                 |         | It is measured from  |
|                                    |                 |                                                               |           |                 |         | the exterior faces   |
|                                    |                 |                                                               |           |                 |         | of walls or from the |
|                                    |                 |                                                               |           |                 |         | center-line of walls |
|                                    |                 |                                                               |           |                 |         | separating           |
|                                    |                 |                                                               |           |                 |         | buildings, but       |
|                                    |                 |                                                               |           |                 |         | excluding covered    |
|                                    |                 |                                                               |           |                 |         | walkways, open       |
|                                    |                 |                                                               |           |                 |         | roofed-over areas,   |
|                                    |                 |                                                               |           |                 |         | porches and similar  |
|                                    |                 |                                                               |           |                 |         | spaces, pipe         |
|                                    |                 |                                                               |           |                 |         | trenches, exterior   |
|                                    |                 |                                                               |           |                 |         | terraces or steps,   |
|                                    |                 |                                                               |           |                 |         | chimneys, roof       |
|                                    |                 |                                                               |           |                 |         | overhangs, and       |
|                                    |                 |                                                               |           |                 |         | similar features.    |
|                                    |                 |                                                               |           |                 |         | This is the floor    |
|                                    |                 |                                                               |           |                 |         | area that is         |
|                                    |                 |                                                               |           |                 |         | modeled.             |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `number_of_occupants`              | Number of       | `Numeric`                                                     |           | `≥0`            |         |                      |
|                                    | occupants in    |                                                               |           |                 |         |                      |
|                                    | the space       |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `occupant_multiplier_schedule`     | Reference to    | `$ID`                                                         |           |                 | $✓$     | Constraint to use    |
|                                    | the schedule    |                                                               |           |                 |         | when implemented     |
|                                    | containing the  |                                                               |           |                 |         | :Schedule:           |
|                                    | multiplier for  |                                                               |           |                 |         |                      |
|                                    | the number of   |                                                               |           |                 |         |                      |
|                                    | occupants       |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `occupant_sensible_heat_gain`      | Sensible heat   | `Numeric`                                                     | W         | `≥0`            |         | JG to verify if used |
|                                    | gain of each    |                                                               |           |                 |         | in test case         |
|                                    | occupant.       |                                                               |           |                 |         | description.         |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `status_type`                      | Choice of new,  | `(<SpaceStatusType2019ASHRAE901>,<GeneralStatusType2019T24>)` |           |                 |         |                      |
|                                    | existing,       |                                                               |           |                 |         |                      |
|                                    | addition,       |                                                               |           |                 |         |                      |
|                                    | alteration,     |                                                               |           |                 |         |                      |
|                                    | etc. for each   |                                                               |           |                 |         |                      |
|                                    | ruleset.        |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `space_function`                   | Generic         | `<SpaceFunctionType>`                                         |           |                 |         | The enumeration is   |
|                                    | function for    |                                                               |           |                 |         | based on the         |
|                                    | the space.      |                                                               |           |                 |         | standard used.       |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `lighting_space_type`              | Lighting space  | `<LightingSpaceType2019ASHRAE901TG37>`                        |           |                 |         | The enumeration is   |
|                                    | type            |                                                               |           |                 |         | based on the         |
|                                    | classification  |                                                               |           |                 |         | standard used.       |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `ventilations_space_type`          | Ventilation     | `<VentilationSpaceType2019ASHRAE901>`                         |           |                 |         | The enumeration is   |
|                                    | space type      |                                                               |           |                 |         | based on the         |
|                                    | classification  |                                                               |           |                 |         | standard used.       |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `service_water_heating_space_type` | Service water   | `<ServiceWaterHeatingSpaceType2019ASHRAE901>`                 |           |                 |         | The enumeration is   |
|                                    | heating space   |                                                               |           |                 |         | based on the         |
|                                    | type            |                                                               |           |                 |         | standard used.       |
|                                    | classification  |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+
| `service_weater_heating_uses`      | List of service | `[{ServiceWaterHeatingUse}]`                                  |           |                 |         |                      |
|                                    | water heating   |                                                               |           |                 |         |                      |
|                                    | uses            |                                                               |           |                 |         |                      |
+------------------------------------+-----------------+---------------------------------------------------------------+-----------+-----------------+---------+----------------------+

\pandocend{footnotesize}



## Infiltration

\pandocbegin{footnotesize}

+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| **Name**                    | **Description** | **Data Type**              | **Units** | **Constraints** | **Req** | **Notes**                                            |
+=============================+=================+============================+===========+=================+=========+======================================================+
| `id`                        | Scope-unique    | `ID`                       |           |                 | $✓$     |                                                      |
|                             | reference       |                            |           |                 |         |                                                      |
|                             | identifier for  |                            |           |                 |         |                                                      |
|                             | instances of    |                            |           |                 |         |                                                      |
|                             | this data group |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `reporting_name`            | Descriptive     | `String`                   |           |                 |         |                                                      |
|                             | name used in    |                            |           |                 |         |                                                      |
|                             | RCT reports if  |                            |           |                 |         |                                                      |
|                             | id is not       |                            |           |                 |         |                                                      |
|                             | already a       |                            |           |                 |         |                                                      |
|                             | descriptive     |                            |           |                 |         |                                                      |
|                             | name            |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `notes`                     | Supplementary   | `String`                   |           |                 |         |                                                      |
|                             | information to  |                            |           |                 |         |                                                      |
|                             | provide context |                            |           |                 |         |                                                      |
|                             | to the model    |                            |           |                 |         |                                                      |
|                             | reviewer        |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `modeling_method`           | The software    | `<InfiltrationMethodType>` |           |                 |         |                                                      |
|                             | methodology     |                            |           |                 |         |                                                      |
|                             | chosen for      |                            |           |                 |         |                                                      |
|                             | modeling        |                            |           |                 |         |                                                      |
|                             | infiltration    |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `algorithm_name`            | Name of the     | `String`                   |           |                 |         |                                                      |
|                             | algorithm used  |                            |           |                 |         |                                                      |
|                             | for modeling    |                            |           |                 |         |                                                      |
|                             | infiltration in |                            |           |                 |         |                                                      |
|                             | the specific    |                            |           |                 |         |                                                      |
|                             | simulation      |                            |           |                 |         |                                                      |
|                             | engine.         |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `measured_air_leakage_rate` | Meaured air     | `Numeric`                  | m^3^/s    | `≥0`            |         | Based on the pressure described in                   |
|                             | leakage rate    |                            |           |                 |         | ASHRAE229.measured_infiltration_pressure_difference. |
|                             | from            |                            |           |                 |         |                                                      |
|                             | infiltration of |                            |           |                 |         |                                                      |
|                             | outside air     |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `infiltration_flow_rate`    | Design          | `Numeric`                  | m^3^/s    | `≥0`            |         | Infiltration flow rate for simulation infiltration   |
|                             | infiltration    |                            |           |                 |         | models unadjusted for temperature difference or      |
|                             | flow rate       |                            |           |                 |         | windspeed or schedule often with a windspeed at 10   |
|                             |                 |                            |           |                 |         | mph (4.5 m/s).  This may vary in meaning between     |
|                             |                 |                            |           |                 |         | simulation engines.                                  |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+
| `multiplier_schedule`       | Referenced to   | `$ID`                      |           |                 |         | Constraint to use when implemented :Schedule:        |
|                             | the schedule    |                            |           |                 |         |                                                      |
|                             | containing the  |                            |           |                 |         |                                                      |
|                             | multiplier for  |                            |           |                 |         |                                                      |
|                             | the             |                            |           |                 |         |                                                      |
|                             | infiltration    |                            |           |                 |         |                                                      |
+-----------------------------+-----------------+----------------------------+-----------+-----------------+---------+------------------------------------------------------+

\pandocend{footnotesize}



## Surface

\pandocbegin{footnotesize}

+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| **Name**                     | **Description** | **Data Type**                                                                                          | **Units** | **Constraints** | **Req** | **Notes**    |
+==============================+=================+========================================================================================================+===========+=================+=========+==============+
| `id`                         | Scope-unique    | `ID`                                                                                                   |           |                 | $✓$     |              |
|                              | reference       |                                                                                                        |           |                 |         |              |
|                              | identifier for  |                                                                                                        |           |                 |         |              |
|                              | instances of    |                                                                                                        |           |                 |         |              |
|                              | this data group |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `reporting_name`             | Descriptive     | `String`                                                                                               |           |                 |         |              |
|                              | name used in    |                                                                                                        |           |                 |         |              |
|                              | RCT reports if  |                                                                                                        |           |                 |         |              |
|                              | id is not       |                                                                                                        |           |                 |         |              |
|                              | already a       |                                                                                                        |           |                 |         |              |
|                              | descriptive     |                                                                                                        |           |                 |         |              |
|                              | name            |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `notes`                      | Supplementary   | `String`                                                                                               |           |                 |         |              |
|                              | information to  |                                                                                                        |           |                 |         |              |
|                              | provide context |                                                                                                        |           |                 |         |              |
|                              | to the model    |                                                                                                        |           |                 |         |              |
|                              | reviewer        |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `subsurfaces`                | Suburfaces that | `[{Subsurface}]`                                                                                       |           |                 |         | Contains a   |
|                              | are on the      |                                                                                                        |           |                 |         | list of      |
|                              | surface         |                                                                                                        |           |                 |         | surfaces     |
|                              |                 |                                                                                                        |           |                 |         | that define  |
|                              |                 |                                                                                                        |           |                 |         | the space.   |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `classification`             | Classification  | `<SurfaceClassificationType>`                                                                          |           |                 |         | Options for  |
|                              | for the         |                                                                                                        |           |                 |         | surface      |
|                              | surface.        |                                                                                                        |           |                 |         | being        |
|                              |                 |                                                                                                        |           |                 |         | interior or  |
|                              |                 |                                                                                                        |           |                 |         | exterior     |
|                              |                 |                                                                                                        |           |                 |         | wall, floor, |
|                              |                 |                                                                                                        |           |                 |         | or ceiling.  |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `area`                       | area of the     | `Numeric`                                                                                              | m^2^      | `≥0`            |         | Measured     |
|                              | surface         |                                                                                                        |           |                 |         | from         |
|                              |                 |                                                                                                        |           |                 |         | interior     |
|                              |                 |                                                                                                        |           |                 |         | face area.   |
|                              |                 |                                                                                                        |           |                 |         | It is the    |
|                              |                 |                                                                                                        |           |                 |         | gross area   |
|                              |                 |                                                                                                        |           |                 |         | of the wall  |
|                              |                 |                                                                                                        |           |                 |         | and includes |
|                              |                 |                                                                                                        |           |                 |         | the area of  |
|                              |                 |                                                                                                        |           |                 |         | all          |
|                              |                 |                                                                                                        |           |                 |         | subsurfaces. |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `tilt`                       | Angle between   | `Numeric`                                                                                              | degrees   |                 |         | Example      |
|                              | vertical and    |                                                                                                        |           |                 |         | value would  |
|                              | the surface     |                                                                                                        |           |                 |         | be 0 = roof, |
|                              | outward normal  |                                                                                                        |           |                 |         | 90 = wall,   |
|                              |                 |                                                                                                        |           |                 |         | 180 =        |
|                              |                 |                                                                                                        |           |                 |         | downward     |
|                              |                 |                                                                                                        |           |                 |         | facing       |
|                              |                 |                                                                                                        |           |                 |         | surface      |
|                              |                 |                                                                                                        |           |                 |         | (exterior    |
|                              |                 |                                                                                                        |           |                 |         | floor)       |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `azimuth`                    | Clockwise angle | `Numeric`                                                                                              | degrees   | `≥0`            |         | Example      |
|                              | between North   |                                                                                                        |           |                 |         | values would |
|                              | and the         |                                                                                                        |           |                 |         | be 0 =       |
|                              | horizontal      |                                                                                                        |           |                 |         | north, 90 =  |
|                              | projection of   |                                                                                                        |           |                 |         | East, 180 =  |
|                              | the wall's      |                                                                                                        |           |                 |         | South, 270 = |
|                              | outward normal. |                                                                                                        |           |                 |         | West         |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `adjacent_to`                | Used to         | `(<SurfaceAdjacentTo>,<AdditionalSurfaceAdjacentToRESNET>,<AdditionalSurfaceAdjacentTo2019ASHRAE901>)` |           |                 |         | Determines   |
|                              | classify the    |                                                                                                        |           |                 |         | whether the  |
|                              | conditions on   |                                                                                                        |           |                 |         | other side   |
|                              | the surface.    |                                                                                                        |           |                 |         | of the       |
|                              |                 |                                                                                                        |           |                 |         | surface is   |
|                              |                 |                                                                                                        |           |                 |         | modeled and  |
|                              |                 |                                                                                                        |           |                 |         | if not what  |
|                              |                 |                                                                                                        |           |                 |         | assumptions  |
|                              |                 |                                                                                                        |           |                 |         | should be    |
|                              |                 |                                                                                                        |           |                 |         | used.        |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `adjacent_zone`              | ID of the       | `$ID`                                                                                                  |           |                 |         | Constraint   |
|                              | adjacent zone   |                                                                                                        |           |                 |         | to use when  |
|                              | for interior    |                                                                                                        |           |                 |         | implemented  |
|                              | surface. Only   |                                                                                                        |           |                 |         | :Zone:       |
|                              | required when   |                                                                                                        |           |                 |         |              |
|                              | adjacent zone   |                                                                                                        |           |                 |         |              |
|                              | is explicity    |                                                                                                        |           |                 |         |              |
|                              | modeled when    |                                                                                                        |           |                 |         |              |
|                              | adjacent_to is  |                                                                                                        |           |                 |         |              |
|                              | set to          |                                                                                                        |           |                 |         |              |
|                              | INTERIOR.       |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `does_cast_shade`            | Determines      | `Boolean`                                                                                              |           |                 |         |              |
|                              | whether the     |                                                                                                        |           |                 |         |              |
|                              | surface is      |                                                                                                        |           |                 |         |              |
|                              | modeled as      |                                                                                                        |           |                 |         |              |
|                              | casting shade   |                                                                                                        |           |                 |         |              |
|                              | on other        |                                                                                                        |           |                 |         |              |
|                              | exterior        |                                                                                                        |           |                 |         |              |
|                              | surfaces        |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `construction`               | Construction    | `{Construction}`                                                                                       |           |                 |         |              |
|                              | description of  |                                                                                                        |           |                 |         |              |
|                              | surface.        |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `surface_optical_properties` | Optical         | `{SurfaceOpticalProperties}`                                                                           |           |                 |         |              |
|                              | properties of   |                                                                                                        |           |                 |         |              |
|                              | the surface.    |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+
| `status_type`                | Choice of new,  | `<GeneralStatusType2019T24>`                                                                           |           |                 |         |              |
|                              | existing,       |                                                                                                        |           |                 |         |              |
|                              | addition,       |                                                                                                        |           |                 |         |              |
|                              | alteration,     |                                                                                                        |           |                 |         |              |
|                              | etc. for each   |                                                                                                        |           |                 |         |              |
|                              | ruleset.        |                                                                                                        |           |                 |         |              |
+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



## Construction

\pandocbegin{footnotesize}

+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| **Name**                            | **Description** | **Data Type**                       | **Units**      | **Constraints** | **Req** | **Notes**       |
+=====================================+=================+=====================================+================+=================+=========+=================+
| `id`                                | Scope-unique    | `ID`                                |                |                 | $✓$     |                 |
|                                     | reference       |                                     |                |                 |         |                 |
|                                     | identifier for  |                                     |                |                 |         |                 |
|                                     | instances of    |                                     |                |                 |         |                 |
|                                     | this data group |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `reporting_name`                    | Descriptive     | `String`                            |                |                 |         |                 |
|                                     | name used in    |                                     |                |                 |         |                 |
|                                     | RCT reports if  |                                     |                |                 |         |                 |
|                                     | id is not       |                                     |                |                 |         |                 |
|                                     | already a       |                                     |                |                 |         |                 |
|                                     | descriptive     |                                     |                |                 |         |                 |
|                                     | name            |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `notes`                             | Supplementary   | `String`                            |                |                 |         |                 |
|                                     | information to  |                                     |                |                 |         |                 |
|                                     | provide context |                                     |                |                 |         |                 |
|                                     | to the model    |                                     |                |                 |         |                 |
|                                     | reviewer        |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `surface_construction_input_option` | Identifies      | `<SurfaceConstructionInputOptions>` |                |                 |         |                 |
|                                     | whether         |                                     |                |                 |         |                 |
|                                     | construction is |                                     |                |                 |         |                 |
|                                     | entered         |                                     |                |                 |         |                 |
|                                     | layer-by-layer  |                                     |                |                 |         |                 |
|                                     | or simplified   |                                     |                |                 |         |                 |
|                                     | (R-value)       |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `fraction_framing`                  | Fraction of the | `Numeric`                           |                | `≥0,≤1`         |         | Fraction of the |
|                                     | construction    |                                     |                |                 |         | construction    |
|                                     | that is         |                                     |                |                 |         | using           |
|                                     | framing.        |                                     |                |                 |         | framing_layers, |
|                                     |                 |                                     |                |                 |         | the remaining   |
|                                     |                 |                                     |                |                 |         | portion uses    |
|                                     |                 |                                     |                |                 |         | the             |
|                                     |                 |                                     |                |                 |         | primary_layers. |
|                                     |                 |                                     |                |                 |         | If blank,       |
|                                     |                 |                                     |                |                 |         | assume zero     |
|                                     |                 |                                     |                |                 |         | framing.        |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `primary_layers`                    | List of names   | `[{Material}]`                      |                |                 |         | For             |
|                                     | of layer        |                                     |                |                 |         | constructions   |
|                                     | descriptions    |                                     |                |                 |         | with framing    |
|                                     | starting from   |                                     |                |                 |         | and cavity heat |
|                                     | the outside     |                                     |                |                 |         | transfer paths, |
|                                     | surface for     |                                     |                |                 |         | use this for    |
|                                     | primary heat    |                                     |                |                 |         | the cavity. For |
|                                     | path            |                                     |                |                 |         | constructions   |
|                                     |                 |                                     |                |                 |         | with            |
|                                     |                 |                                     |                |                 |         | homogeneous     |
|                                     |                 |                                     |                |                 |         | layer, use this |
|                                     |                 |                                     |                |                 |         | element only.   |
|                                     |                 |                                     |                |                 |         | Air films       |
|                                     |                 |                                     |                |                 |         | should not be   |
|                                     |                 |                                     |                |                 |         | included in the |
|                                     |                 |                                     |                |                 |         | list of layers. |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `framing_layers`                    | List of names   | `[{Material}]`                      |                |                 |         | For             |
|                                     | of layer        |                                     |                |                 |         | constructions   |
|                                     | descriptions    |                                     |                |                 |         | with framing    |
|                                     | starting from   |                                     |                |                 |         | and cavity heat |
|                                     | the outside     |                                     |                |                 |         | transfer paths, |
|                                     | surface for the |                                     |                |                 |         | use this for    |
|                                     | framing heat    |                                     |                |                 |         | the framing     |
|                                     | path            |                                     |                |                 |         | otherwise leave |
|                                     |                 |                                     |                |                 |         | blank. Air      |
|                                     |                 |                                     |                |                 |         | films should    |
|                                     |                 |                                     |                |                 |         | not be included |
|                                     |                 |                                     |                |                 |         | in the list of  |
|                                     |                 |                                     |                |                 |         | layers.         |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `insulation_location`               | The location of | `String`                            |                |                 |         |                 |
|                                     | the insulation  |                                     |                |                 |         |                 |
|                                     | related to the  |                                     |                |                 |         |                 |
|                                     | surface         |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `u_factor`                          | suface U-factor | `Numeric`                           | W/m^2^$\cdot$K | `≥0`            |         | Includes        |
|                                     |                 |                                     |                |                 |         | interior and    |
|                                     |                 |                                     |                |                 |         | exterior air    |
|                                     |                 |                                     |                |                 |         | films as        |
|                                     |                 |                                     |                |                 |         | specified by    |
|                                     |                 |                                     |                |                 |         | the referenced  |
|                                     |                 |                                     |                |                 |         | standard.       |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `c_factor`                          | surface         | `Numeric`                           | W/m^2^$\cdot$K | `≥0`            |         |                 |
|                                     | C-factor        |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `f_factor`                          | surface         | `Numeric`                           | W/m$\cdot$K    | `≥0`            |         |                 |
|                                     | F-factor        |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `r_value`                           | r-value of the  | `Numeric`                           | K$\cdot$m^2^/W | `≥0`            |         |                 |
|                                     | insulation for  |                                     |                |                 |         |                 |
|                                     | the surface     |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `has_radiant_heating`               | Includes        | `Boolean`                           |                |                 |         |                 |
|                                     | embedded        |                                     |                |                 |         |                 |
|                                     | radiant heating |                                     |                |                 |         |                 |
|                                     | elements        |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+
| `has_radiant_cooling`               | Includes        | `Boolean`                           |                |                 |         |                 |
|                                     | embedded        |                                     |                |                 |         |                 |
|                                     | radiant cooling |                                     |                |                 |         |                 |
|                                     | elements        |                                     |                |                 |         |                 |
+-------------------------------------+-----------------+-------------------------------------+----------------+-----------------+---------+-----------------+

\pandocend{footnotesize}



## Material

\pandocbegin{footnotesize}

+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| **Name**               | **Description** | **Data    | **Units**      | **Constraints** | **Req** | **Notes**            |
|                        |                 | Type**    |                |                 |         |                      |
+========================+=================+===========+================+=================+=========+======================+
| `id`                   | Scope-unique    | `ID`      |                |                 | $✓$     |                      |
|                        | reference       |           |                |                 |         |                      |
|                        | identifier for  |           |                |                 |         |                      |
|                        | instances of    |           |                |                 |         |                      |
|                        | this data group |           |                |                 |         |                      |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `reporting_name`       | Descriptive     | `String`  |                |                 |         |                      |
|                        | name used in    |           |                |                 |         |                      |
|                        | RCT reports if  |           |                |                 |         |                      |
|                        | id is not       |           |                |                 |         |                      |
|                        | already a       |           |                |                 |         |                      |
|                        | descriptive     |           |                |                 |         |                      |
|                        | name            |           |                |                 |         |                      |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `notes`                | Supplementary   | `String`  |                |                 |         |                      |
|                        | information to  |           |                |                 |         |                      |
|                        | provide context |           |                |                 |         |                      |
|                        | to the model    |           |                |                 |         |                      |
|                        | reviewer        |           |                |                 |         |                      |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `thickness`            | The thickness   | `Numeric` | m              | `>0`            |         |                      |
|                        | of the material |           |                |                 |         |                      |
|                        | layer           |           |                |                 |         |                      |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `thermal_conductivity` | The thermal     | `Numeric` | W/m$\cdot$K    | `≥0`            |         | When                 |
|                        | conductivity of |           |                |                 |         | thermal_conductivity |
|                        | the material    |           |                |                 |         | is specified,        |
|                        | layer           |           |                |                 |         | r_value should not   |
|                        |                 |           |                |                 |         | be provided.         |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `density`              | The density of  | `Numeric` | kg/m^3^        | `≥0`            |         |                      |
|                        | the material    |           |                |                 |         |                      |
|                        | layer           |           |                |                 |         |                      |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `specific_heat`        | The specific    | `Numeric` | J/kg$\cdot$K   | `≥0`            |         |                      |
|                        | heat of the     |           |                |                 |         |                      |
|                        | material layer  |           |                |                 |         |                      |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+
| `r_value`              | r-value of the  | `Numeric` | K$\cdot$m^2^/W | `≥0`            |         | When r_value is      |
|                        | insulation for  |           |                |                 |         | specified,           |
|                        | the material    |           |                |                 |         | thermal_conductivity |
|                        | layer           |           |                |                 |         | should not be        |
|                        |                 |           |                |                 |         | provided. Typically  |
|                        |                 |           |                |                 |         | used for insulation  |
|                        |                 |           |                |                 |         | or air gaps.         |
+------------------------+-----------------+-----------+----------------+-----------------+---------+----------------------+

\pandocend{footnotesize}



## SurfaceOpticalProperties

\pandocbegin{footnotesize}

+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| **Name**                       | **Description** | **Data    | **Constraints** | **Req** | **Notes**   |
|                                |                 | Type**    |                 |         |             |
+================================+=================+===========+=================+=========+=============+
| `id`                           | Scope-unique    | `ID`      |                 | $✓$     |             |
|                                | reference       |           |                 |         |             |
|                                | identifier for  |           |                 |         |             |
|                                | instances of    |           |                 |         |             |
|                                | this data group |           |                 |         |             |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `reporting_name`               | Descriptive     | `String`  |                 |         |             |
|                                | name used in    |           |                 |         |             |
|                                | RCT reports if  |           |                 |         |             |
|                                | id is not       |           |                 |         |             |
|                                | already a       |           |                 |         |             |
|                                | descriptive     |           |                 |         |             |
|                                | name            |           |                 |         |             |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `notes`                        | Supplementary   | `String`  |                 |         |             |
|                                | information to  |           |                 |         |             |
|                                | provide context |           |                 |         |             |
|                                | to the model    |           |                 |         |             |
|                                | reviewer        |           |                 |         |             |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `absorptance_thermal_exterior` | Thermal         | `Numeric` | `≥0`            |         | May also be |
|                                | absorptance of  |           |                 |         | called      |
|                                | long wavelength |           |                 |         | thermal     |
|                                | radiation on    |           |                 |         | emittance,  |
|                                | the exterior    |           |                 |         | emittance   |
|                                | surface.        |           |                 |         | or          |
|                                |                 |           |                 |         | emissivity  |
|                                |                 |           |                 |         | and         |
|                                |                 |           |                 |         | represents  |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | fraction of |
|                                |                 |           |                 |         | incident    |
|                                |                 |           |                 |         | long        |
|                                |                 |           |                 |         | wavelength  |
|                                |                 |           |                 |         | radiation   |
|                                |                 |           |                 |         | that is     |
|                                |                 |           |                 |         | absorbed by |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | material    |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `absorptance_solar_exterior`   | Thermal         | `Numeric` | `≥0`            |         | Equals one  |
|                                | absorptance of  |           |                 |         | minus the   |
|                                | short           |           |                 |         | solar       |
|                                | wavelength      |           |                 |         | reflectance |
|                                | radiation on    |           |                 |         | (for opaque |
|                                | the exterior    |           |                 |         | materials)  |
|                                | surface.        |           |                 |         | and         |
|                                |                 |           |                 |         | represents  |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | fraction of |
|                                |                 |           |                 |         | incident    |
|                                |                 |           |                 |         | solar       |
|                                |                 |           |                 |         | radiation   |
|                                |                 |           |                 |         | that is     |
|                                |                 |           |                 |         | absorbed by |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | material    |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `absorptance_visible_exterior` | Thermal         | `Numeric` | `≥0`            |         | Equals one  |
|                                | absorptance of  |           |                 |         | minus the   |
|                                | visible         |           |                 |         | visible     |
|                                | radiation on    |           |                 |         | reflectance |
|                                | the exterior    |           |                 |         | (for opaque |
|                                | surface.        |           |                 |         | materials)  |
|                                |                 |           |                 |         | and         |
|                                |                 |           |                 |         | represents  |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | fraction of |
|                                |                 |           |                 |         | incident    |
|                                |                 |           |                 |         | visible     |
|                                |                 |           |                 |         | wavelength  |
|                                |                 |           |                 |         | radiation   |
|                                |                 |           |                 |         | that is     |
|                                |                 |           |                 |         | absorbed by |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | material    |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `absorptance_thermal_interior` | Thermal         | `Numeric` | `≥0`            |         | May also be |
|                                | absorptance of  |           |                 |         | called      |
|                                | long wavelength |           |                 |         | thermal     |
|                                | radiation on    |           |                 |         | emittance,  |
|                                | the interior    |           |                 |         | emittance   |
|                                | surface.        |           |                 |         | or          |
|                                |                 |           |                 |         | emissivity  |
|                                |                 |           |                 |         | and         |
|                                |                 |           |                 |         | represents  |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | fraction of |
|                                |                 |           |                 |         | incident    |
|                                |                 |           |                 |         | long        |
|                                |                 |           |                 |         | wavelength  |
|                                |                 |           |                 |         | radiation   |
|                                |                 |           |                 |         | that is     |
|                                |                 |           |                 |         | absorbed by |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | material    |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `absorptance_solar_interior`   | Thermal         | `Numeric` | `≥0`            |         | Equals one  |
|                                | absorptance of  |           |                 |         | minus the   |
|                                | short           |           |                 |         | solar       |
|                                | wavelength      |           |                 |         | reflectance |
|                                | radiation on    |           |                 |         | (for opaque |
|                                | the interior    |           |                 |         | materials)  |
|                                | surface.        |           |                 |         | and         |
|                                |                 |           |                 |         | represents  |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | fraction of |
|                                |                 |           |                 |         | incident    |
|                                |                 |           |                 |         | solar       |
|                                |                 |           |                 |         | radiation   |
|                                |                 |           |                 |         | that is     |
|                                |                 |           |                 |         | absorbed by |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | material    |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+
| `absorptance_visible_interior` | Thermal         | `Numeric` | `≥0`            |         | Equals one  |
|                                | absorptance of  |           |                 |         | minus the   |
|                                | visible         |           |                 |         | visible     |
|                                | radiation on    |           |                 |         | reflectance |
|                                | the interior    |           |                 |         | (for opaque |
|                                | surface.        |           |                 |         | materials)  |
|                                |                 |           |                 |         | and         |
|                                |                 |           |                 |         | represents  |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | fraction of |
|                                |                 |           |                 |         | incident    |
|                                |                 |           |                 |         | visible     |
|                                |                 |           |                 |         | wavelength  |
|                                |                 |           |                 |         | radiation   |
|                                |                 |           |                 |         | that is     |
|                                |                 |           |                 |         | absorbed by |
|                                |                 |           |                 |         | the         |
|                                |                 |           |                 |         | material    |
+--------------------------------+-----------------+-----------+-----------------+---------+-------------+

\pandocend{footnotesize}



## Subsurface

\pandocbegin{footnotesize}

+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| **Name**                                | **Description**   | **Data Type**                                    | **Units**      | **Constraints** | **Req** | **Notes**     |
+=========================================+===================+==================================================+================+=================+=========+===============+
| `id`                                    | Scope-unique      | `ID`                                             |                |                 | $✓$     |               |
|                                         | reference         |                                                  |                |                 |         |               |
|                                         | identifier for    |                                                  |                |                 |         |               |
|                                         | instances of this |                                                  |                |                 |         |               |
|                                         | data group        |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `reporting_name`                        | Descriptive name  | `String`                                         |                |                 |         |               |
|                                         | used in RCT       |                                                  |                |                 |         |               |
|                                         | reports if id is  |                                                  |                |                 |         |               |
|                                         | not already a     |                                                  |                |                 |         |               |
|                                         | descriptive name  |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `notes`                                 | Supplementary     | `String`                                         |                |                 |         |               |
|                                         | information to    |                                                  |                |                 |         |               |
|                                         | provide context   |                                                  |                |                 |         |               |
|                                         | to the model      |                                                  |                |                 |         |               |
|                                         | reviewer          |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `classification`                        | Classification    | `<SubsurfaceClassificationType>`                 |                |                 |         |               |
|                                         | for the           |                                                  |                |                 |         |               |
|                                         | subsurface being  |                                                  |                |                 |         |               |
|                                         | window, skylight, |                                                  |                |                 |         |               |
|                                         | door.             |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `subclassification`                     | Standard specific | `<SubsurfaceSubclassificationType2019ASHRAE901>` |                |                 |         |               |
|                                         | subclassification |                                                  |                |                 |         |               |
|                                         | for subsurfaces   |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `is_operable`                           | Identifies        | `Boolean`                                        |                |                 |         | This applies  |
|                                         | whether window    |                                                  |                |                 |         | to windows    |
|                                         | subsurface can be |                                                  |                |                 |         | and skylights |
|                                         | opened and closed |                                                  |                |                 |         | but not to    |
|                                         | including by      |                                                  |                |                 |         | doors.        |
|                                         | pivoting or       |                                                  |                |                 |         |               |
|                                         | sliding.          |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `has_open_sensor`                       | Has sensor and    | `Boolean`                                        |                |                 |         |               |
|                                         | reports to        |                                                  |                |                 |         |               |
|                                         | building control  |                                                  |                |                 |         |               |
|                                         | system when the   |                                                  |                |                 |         |               |
|                                         | window or door is |                                                  |                |                 |         |               |
|                                         | open.             |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `framing_type`                          | The material of   | `<SubsurfaceFrameType2019ASHRAE901>`             |                |                 |         | This applies  |
|                                         | the framing.      |                                                  |                |                 |         | to windows    |
|                                         |                   |                                                  |                |                 |         | and skylights |
|                                         |                   |                                                  |                |                 |         | but not to    |
|                                         |                   |                                                  |                |                 |         | doors.        |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `glazed_area`                           | Area of           | `Numeric`                                        | m^2^           | `≥0`            |         |               |
|                                         | subsurface        |                                                  |                |                 |         |               |
|                                         | including glass   |                                                  |                |                 |         |               |
|                                         | and transparent   |                                                  |                |                 |         |               |
|                                         | surfaces          |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `opaque_area`                           | Area of           | `Numeric`                                        | m^2^           | `≥0`            |         |               |
|                                         | subsurface        |                                                  |                |                 |         |               |
|                                         | framing for a     |                                                  |                |                 |         |               |
|                                         | window or         |                                                  |                |                 |         |               |
|                                         | skylight or       |                                                  |                |                 |         |               |
|                                         | opaque portion    |                                                  |                |                 |         |               |
|                                         | for a door.       |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `u_factor`                              | Overall           | `Numeric`                                        | W/m^2^$\cdot$K | `≥0`            |         | Includes      |
|                                         | Subsurface        |                                                  |                |                 |         | interior and  |
|                                         | U-factor          |                                                  |                |                 |         | exterior air  |
|                                         |                   |                                                  |                |                 |         | films as      |
|                                         |                   |                                                  |                |                 |         | specified by  |
|                                         |                   |                                                  |                |                 |         | the           |
|                                         |                   |                                                  |                |                 |         | referenced    |
|                                         |                   |                                                  |                |                 |         | standard.     |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `dynamic_glazing_type`                  | Type of dynamic   | `<SubsurfaceDynamicGlazingType>`                 |                |                 |         | Indicates if  |
|                                         | glazing for the   |                                                  |                |                 |         | the glazed    |
|                                         | window subsurface |                                                  |                |                 |         | subsurface    |
|                                         |                   |                                                  |                |                 |         | can change    |
|                                         |                   |                                                  |                |                 |         | it's          |
|                                         |                   |                                                  |                |                 |         | performance   |
|                                         |                   |                                                  |                |                 |         | properties    |
|                                         |                   |                                                  |                |                 |         | and if it is  |
|                                         |                   |                                                  |                |                 |         | automatic or  |
|                                         |                   |                                                  |                |                 |         | not.          |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `solar_heat_gain_coefficient`           | Subsurface SHGC   | `Numeric`                                        |                | `≥0`            |         | For dynamic   |
|                                         |                   |                                                  |                |                 |         | glazing       |
|                                         |                   |                                                  |                |                 |         | represents    |
|                                         |                   |                                                  |                |                 |         | the minimum   |
|                                         |                   |                                                  |                |                 |         | SHGC          |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `maximum_solar_heat_gain_coefficient`   | Maximum           | `Numeric`                                        |                | `≥0`            |         | Only used for |
|                                         | Subsurface SHGC   |                                                  |                |                 |         | dynamic       |
|                                         | for Dynamic       |                                                  |                |                 |         | glazing       |
|                                         | Glazing           |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `visible_transmittance`                 | Subsurface VT     | `Numeric`                                        |                | `≥0`            |         | For dynamic   |
|                                         |                   |                                                  |                |                 |         | glazing       |
|                                         |                   |                                                  |                |                 |         | represents    |
|                                         |                   |                                                  |                |                 |         | the maximum   |
|                                         |                   |                                                  |                |                 |         | visible       |
|                                         |                   |                                                  |                |                 |         | transmittance |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `minimum_visible_transmittance`         | Minimum           | `Numeric`                                        |                | `≥0`            |         | Only used for |
|                                         | Subsurface VT for |                                                  |                |                 |         | dynamic       |
|                                         | Dynamic Glazing   |                                                  |                |                 |         | glazing       |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `depth_of_overhang`                     | Distance from the | `Numeric`                                        | m              | `≥0`            |         |               |
|                                         | edge of the       |                                                  |                |                 |         |               |
|                                         | overhang to the   |                                                  |                |                 |         |               |
|                                         | subsurface.       |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `has_shading_overhang`                  | Identifies        | `Boolean`                                        |                |                 |         |               |
|                                         | whether           |                                                  |                |                 |         |               |
|                                         | subsurface has    |                                                  |                |                 |         |               |
|                                         | overhangs         |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `has_shading_sidefins`                  | Identifies        | `Boolean`                                        |                |                 |         |               |
|                                         | whether           |                                                  |                |                 |         |               |
|                                         | subsurface has    |                                                  |                |                 |         |               |
|                                         | sidefins          |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `has_manual_interior_shades`            | Are there         | `Boolean`                                        |                |                 |         |               |
|                                         | manually-operated |                                                  |                |                 |         |               |
|                                         | interior shading  |                                                  |                |                 |         |               |
|                                         | such as blinds,   |                                                  |                |                 |         |               |
|                                         | curtains or       |                                                  |                |                 |         |               |
|                                         | shades            |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `solar_transmittance_multiplier_summer` | Solar             | `Numeric`                                        |                | `≥0`            |         | Often used to |
|                                         | transmittance     |                                                  |                |                 |         | account for   |
|                                         | multiplier for    |                                                  |                |                 |         | interior      |
|                                         | summer            |                                                  |                |                 |         | shading such  |
|                                         |                   |                                                  |                |                 |         | as drapes.    |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `solar_transmittance_multiplier_winter` | Solar             | `Numeric`                                        |                | `≥0`            |         | Often used to |
|                                         | transmittance     |                                                  |                |                 |         | account for   |
|                                         | multiplier for    |                                                  |                |                 |         | interior      |
|                                         | summer            |                                                  |                |                 |         | shading such  |
|                                         |                   |                                                  |                |                 |         | as drapes.    |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `has_automatic_shades`                  | Are there         | `Boolean`                                        |                |                 |         |               |
|                                         | automatic         |                                                  |                |                 |         |               |
|                                         | interior shading  |                                                  |                |                 |         |               |
|                                         | such as blinds,   |                                                  |                |                 |         |               |
|                                         | curtains or       |                                                  |                |                 |         |               |
|                                         | shades            |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+
| `status_type`                           | Choice of new,    | `<GeneralStatusType2019T24>`                     |                |                 |         |               |
|                                         | existing,         |                                                  |                |                 |         |               |
|                                         | addition,         |                                                  |                |                 |         |               |
|                                         | alteration, etc.  |                                                  |                |                 |         |               |
|                                         | for each ruleset. |                                                  |                |                 |         |               |
+-----------------------------------------+-------------------+--------------------------------------------------+----------------+-----------------+---------+---------------+

\pandocend{footnotesize}



## InteriorLighting

\pandocbegin{footnotesize}

+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| **Name**                                              | **Description** | **Data Type**                        | **Units** | **Req** | **Notes**   |
+=======================================================+=================+======================================+===========+=========+=============+
| `id`                                                  | Scope-unique    | `ID`                                 |           | $✓$     |             |
|                                                       | reference       |                                      |           |         |             |
|                                                       | identifier for  |                                      |           |         |             |
|                                                       | instances of    |                                      |           |         |             |
|                                                       | this data group |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `reporting_name`                                      | Descriptive     | `String`                             |           |         |             |
|                                                       | name used in    |                                      |           |         |             |
|                                                       | RCT reports if  |                                      |           |         |             |
|                                                       | id is not       |                                      |           |         |             |
|                                                       | already a       |                                      |           |         |             |
|                                                       | descriptive     |                                      |           |         |             |
|                                                       | name            |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `notes`                                               | Supplementary   | `String`                             |           |         |             |
|                                                       | information to  |                                      |           |         |             |
|                                                       | provide context |                                      |           |         |             |
|                                                       | to the model    |                                      |           |         |             |
|                                                       | reviewer        |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `purpose_type`                                        | Lighting space  | `<LightingPurposeType2019ASHRAE901>` |           |         | The         |
|                                                       | type            |                                      |           |         | enumeration |
|                                                       | classification  |                                      |           |         | is based on |
|                                                       |                 |                                      |           |         | the         |
|                                                       |                 |                                      |           |         | standard    |
|                                                       |                 |                                      |           |         | used.       |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `power_per_area`                                      | Total power for | `Numeric`                            | W/m^2^    |         | When        |
|                                                       | lights divided  |                                      |           |         | computing   |
|                                                       | by the area of  |                                      |           |         | the power   |
|                                                       | the space.      |                                      |           |         | per area    |
|                                                       |                 |                                      |           |         | use the     |
|                                                       |                 |                                      |           |         | area of the |
|                                                       |                 |                                      |           |         | entire      |
|                                                       |                 |                                      |           |         | space.      |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `lighting_multiplier_schedule`                        | Reference to    | `$ID`                                |           | $✓$     | Constraint  |
|                                                       | the schedule    |                                      |           |         | to use when |
|                                                       | containing the  |                                      |           |         | implemented |
|                                                       | multiplier for  |                                      |           |         | :Schedule:  |
|                                                       | lighting        |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `occupancy_control_type`                              | Indicates the   | `<LightingOccupancyControlType>`     |           |         |             |
|                                                       | type of         |                                      |           |         |             |
|                                                       | occupancy       |                                      |           |         |             |
|                                                       | controls        |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `daylighting_control_type`                            | Indicates the   | `<LightingDaylightingControlType>`   |           |         |             |
|                                                       | type of         |                                      |           |         |             |
|                                                       | daylighting     |                                      |           |         |             |
|                                                       | controls        |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `are_schedules_used_for_modeling_occupancy_control`   | Indicates that  | `Boolean`                            |           |         |             |
|                                                       | schedule values |                                      |           |         |             |
|                                                       | are used for    |                                      |           |         |             |
|                                                       | modeling the    |                                      |           |         |             |
|                                                       | impacts of      |                                      |           |         |             |
|                                                       | occupancy       |                                      |           |         |             |
|                                                       | controls on     |                                      |           |         |             |
|                                                       | lighting.       |                                      |           |         |             |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+
| `are_schedules_used_for_modeling_daylighting_control` | Indicates that  | `Boolean`                            |           |         | For         |
|                                                       | schedule values |                                      |           |         | simulations |
|                                                       | are used for    |                                      |           |         | that are    |
|                                                       | modeling the    |                                      |           |         | modeling    |
|                                                       | impacts of      |                                      |           |         | daylighting |
|                                                       | daylighting     |                                      |           |         | by          |
|                                                       | controls on     |                                      |           |         | computing   |
|                                                       | lighting.       |                                      |           |         | the         |
|                                                       |                 |                                      |           |         | illumance   |
|                                                       |                 |                                      |           |         | this should |
|                                                       |                 |                                      |           |         | be false.   |
+-------------------------------------------------------+-----------------+--------------------------------------+-----------+---------+-------------+

\pandocend{footnotesize}



## MiscellaneousEquipment

\pandocbegin{footnotesize}

+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| **Name**                       | **Description** | **Data Type**                  | **Units** | **Constraints** | **Req** | **Notes**   |
+================================+=================+================================+===========+=================+=========+=============+
| `id`                           | Scope-unique    | `ID`                           |           |                 | $✓$     |             |
|                                | reference       |                                |           |                 |         |             |
|                                | identifier for  |                                |           |                 |         |             |
|                                | instances of    |                                |           |                 |         |             |
|                                | this data group |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `reporting_name`               | Descriptive     | `String`                       |           |                 |         |             |
|                                | name used in    |                                |           |                 |         |             |
|                                | RCT reports if  |                                |           |                 |         |             |
|                                | id is not       |                                |           |                 |         |             |
|                                | already a       |                                |           |                 |         |             |
|                                | descriptive     |                                |           |                 |         |             |
|                                | name            |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `notes`                        | Supplementary   | `String`                       |           |                 |         |             |
|                                | information to  |                                |           |                 |         |             |
|                                | provide context |                                |           |                 |         |             |
|                                | to the model    |                                |           |                 |         |             |
|                                | reviewer        |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `energy_type`                  | Source of       | `<EnergySourceTypeOptions>`    |           |                 |         |             |
|                                | energy for the  |                                |           |                 |         |             |
|                                | miscelleous     |                                |           |                 |         |             |
|                                | equipment in    |                                |           |                 |         |             |
|                                | the space       |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `peak_usage`                   | Peak energy     | `Numeric`                      | W         |                 |         |             |
|                                | usage per hour  |                                |           |                 |         |             |
|                                | by the          |                                |           |                 |         |             |
|                                | miscelleous     |                                |           |                 |         |             |
|                                | equipment in    |                                |           |                 |         |             |
|                                | the space.      |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `multiplier_schedule`          | Referenced to   | `$ID`                          |           |                 | $✓$     | Constraint  |
|                                | the schedule    |                                |           |                 |         | to use when |
|                                | containing the  |                                |           |                 |         | implemented |
|                                | multiplier for  |                                |           |                 |         | :Schedule:  |
|                                | the             |                                |           |                 |         |             |
|                                | miscellenous    |                                |           |                 |         |             |
|                                | equipment       |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `sensible_fraction`            | Fraction of     | `Numeric`                      |           | `≥0, ≤1`        |         | Sensible    |
|                                | energy that is  |                                |           |                 |         | plus latent |
|                                | a sensible load |                                |           |                 |         | do not      |
|                                | on the space.   |                                |           |                 |         | necessarily |
|                                |                 |                                |           |                 |         | add up to   |
|                                |                 |                                |           |                 |         | 1.0.        |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `latent_fraction`              | Fraction of     | `Numeric`                      |           | `≥0, ≤1`        |         | Sensible    |
|                                | energy that is  |                                |           |                 |         | plus latent |
|                                | a latent load   |                                |           |                 |         | do not      |
|                                | on the space.   |                                |           |                 |         | necessarily |
|                                |                 |                                |           |                 |         | add up to   |
|                                |                 |                                |           |                 |         | 1.0.        |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `miscellaneous_equipment_type` | Type of         | `<MiscellaneousEquipmentType>` |           |                 |         |             |
|                                | miscellaneous   |                                |           |                 |         |             |
|                                | equipment       |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+
| `has_automatic_control`        | Indicates that  | `Boolean`                      |           |                 |         |             |
|                                | the receptacles |                                |           |                 |         |             |
|                                | have automatic  |                                |           |                 |         |             |
|                                | controls        |                                |           |                 |         |             |
+--------------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-------------+

\pandocend{footnotesize}



## Transformer

\pandocbegin{footnotesize}

+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| **Name**         | **Description** | **Data Type**       | **Units** | **Constraints** | **Req** | **Notes**   |
+==================+=================+=====================+===========+=================+=========+=============+
| `id`             | Scope-unique    | `ID`                |           |                 | $✓$     |             |
|                  | reference       |                     |           |                 |         |             |
|                  | identifier for  |                     |           |                 |         |             |
|                  | instances of    |                     |           |                 |         |             |
|                  | this data group |                     |           |                 |         |             |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `reporting_name` | Descriptive     | `String`            |           |                 |         |             |
|                  | name used in    |                     |           |                 |         |             |
|                  | RCT reports if  |                     |           |                 |         |             |
|                  | id is not       |                     |           |                 |         |             |
|                  | already a       |                     |           |                 |         |             |
|                  | descriptive     |                     |           |                 |         |             |
|                  | name            |                     |           |                 |         |             |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `notes`          | Supplementary   | `String`            |           |                 |         |             |
|                  | information to  |                     |           |                 |         |             |
|                  | provide context |                     |           |                 |         |             |
|                  | to the model    |                     |           |                 |         |             |
|                  | reviewer        |                     |           |                 |         |             |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `type`           | The type of     | `<TransformerType>` |           |                 |         |             |
|                  | transformer     |                     |           |                 |         |             |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `phase`          | The number of   | `<ElectricalPhase>` |           |                 |         |             |
|                  | electrical      |                     |           |                 |         |             |
|                  | phases          |                     |           |                 |         |             |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `efficiency`     | Transformer     | `Numeric`           |           | `≥0, ≤1`        |         | Expresses   |
|                  | efficiency      |                     |           |                 |         | the         |
|                  |                 |                     |           |                 |         | efficiency  |
|                  |                 |                     |           |                 |         | of the      |
|                  |                 |                     |           |                 |         | transformer |
|                  |                 |                     |           |                 |         | as a        |
|                  |                 |                     |           |                 |         | fraction    |
|                  |                 |                     |           |                 |         | from 0 to   |
|                  |                 |                     |           |                 |         | 1, where 1  |
|                  |                 |                     |           |                 |         | would       |
|                  |                 |                     |           |                 |         | represent   |
|                  |                 |                     |           |                 |         | 100%        |
|                  |                 |                     |           |                 |         | efficiency. |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `capacity`       | Rated Capacity  | `Numeric`           | V$\cdot$A | `≥0`            |         |             |
|                  | of the          |                     |           |                 |         |             |
|                  | Transformer     |                     |           |                 |         |             |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+
| `peak_load`      | Annual Peak     | `Numeric`           | W         | `≥0`            |         | Peak        |
|                  | electric load   |                     |           |                 |         | electric    |
|                  | on the          |                     |           |                 |         | load on the |
|                  | transformer     |                     |           |                 |         | transfomer  |
|                  |                 |                     |           |                 |         | based on an |
|                  |                 |                     |           |                 |         | annual      |
|                  |                 |                     |           |                 |         | simulation  |
|                  |                 |                     |           |                 |         | with        |
|                  |                 |                     |           |                 |         | typical     |
|                  |                 |                     |           |                 |         | weather     |
|                  |                 |                     |           |                 |         | file.       |
+------------------+-----------------+---------------------+-----------+-----------------+---------+-------------+

\pandocend{footnotesize}



## Schedule

\pandocbegin{footnotesize}

+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| **Name**                              | **Description** | **Data Type**                        | **Units** | **Req** | **Notes**              |
+=======================================+=================+======================================+===========+=========+========================+
| `id`                                  | Scope-unique    | `ID`                                 |           | $✓$     |                        |
|                                       | reference       |                                      |           |         |                        |
|                                       | identifier for  |                                      |           |         |                        |
|                                       | instances of    |                                      |           |         |                        |
|                                       | this data group |                                      |           |         |                        |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `reporting_name`                      | Descriptive     | `String`                             |           |         |                        |
|                                       | name used in    |                                      |           |         |                        |
|                                       | RCT reports if  |                                      |           |         |                        |
|                                       | id is not       |                                      |           |         |                        |
|                                       | already a       |                                      |           |         |                        |
|                                       | descriptive     |                                      |           |         |                        |
|                                       | name            |                                      |           |         |                        |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `notes`                               | Supplementary   | `String`                             |           |         |                        |
|                                       | information to  |                                      |           |         |                        |
|                                       | provide context |                                      |           |         |                        |
|                                       | to the model    |                                      |           |         |                        |
|                                       | reviewer        |                                      |           |         |                        |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `purpose`                             | The purpose of  | `String`                             |           |         | Describe the purpose   |
|                                       | schedule        |                                      |           |         | of the schedule and    |
|                                       |                 |                                      |           |         | how it can be used.    |
|                                       |                 |                                      |           |         | Not an enumerations.   |
|                                       |                 |                                      |           |         | The purpose assigned   |
|                                       |                 |                                      |           |         | by BEM tool should     |
|                                       |                 |                                      |           |         | match across RMRs.     |
|                                       |                 |                                      |           |         | Examples include       |
|                                       |                 |                                      |           |         | thermostat, multiplier |
|                                       |                 |                                      |           |         | for lighting,          |
|                                       |                 |                                      |           |         | availability for       |
|                                       |                 |                                      |           |         | equipment.             |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `schedule_sequence_type`              | Schedule        | `<ScheduleSequenceTypeOptions>`      |           |         |                        |
|                                       | sequence type   |                                      |           |         |                        |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `hourly_values`                       | Hourly Values   | `[Numeric][0..8760]`                 |           |         | Used when              |
|                                       | of Schedule     |                                      |           |         | schedule_sequence_type |
|                                       |                 |                                      |           |         | is HOURLY. Can also    |
|                                       |                 |                                      |           |         | use functions like     |
|                                       |                 |                                      |           |         | EFLH(), MAX(), MIN()   |
|                                       |                 |                                      |           |         | to determine overall   |
|                                       |                 |                                      |           |         | characteristics for    |
|                                       |                 |                                      |           |         | the list of schedule   |
|                                       |                 |                                      |           |         | values.                |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `event_times`                         | Event times     | `[Numeric]`                          | s         |         | Used when              |
|                                       | when the        |                                      |           |         | schedule_sequence_type |
|                                       | schedule        |                                      |           |         | is EVENT to describe   |
|                                       | changes         |                                      |           |         | the time of the year   |
|                                       |                 |                                      |           |         | in seconds that the    |
|                                       |                 |                                      |           |         | schedule changes       |
|                                       |                 |                                      |           |         | value.                 |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `event_values`                        | Event value at  | `[Numeric]`                          |           |         | Used when              |
|                                       | corresponding   |                                      |           |         | schedule_sequence_type |
|                                       | event time.     |                                      |           |         | is EVENT. New values   |
|                                       |                 |                                      |           |         | starting at            |
|                                       |                 |                                      |           |         | corresponding to the   |
|                                       |                 |                                      |           |         | event time until       |
|                                       |                 |                                      |           |         | following event time   |
|                                       |                 |                                      |           |         | minus one second. Can  |
|                                       |                 |                                      |           |         | also use functions     |
|                                       |                 |                                      |           |         | like EFLH(), MAX(),    |
|                                       |                 |                                      |           |         | MIN() to determine     |
|                                       |                 |                                      |           |         | overall                |
|                                       |                 |                                      |           |         | characteristics for    |
|                                       |                 |                                      |           |         | the list of schedule   |
|                                       |                 |                                      |           |         | values.                |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `type`                                | The type of     | `<ScheduleTypeOptions>`              |           |         | Primarily indicates if |
|                                       | schedule        |                                      |           |         | the values may be      |
|                                       |                 |                                      |           |         | represented by units   |
|                                       |                 |                                      |           |         | such as C for          |
|                                       |                 |                                      |           |         | temperature or W for   |
|                                       |                 |                                      |           |         | power or m3/s for flow |
|                                       |                 |                                      |           |         | rate or are            |
|                                       |                 |                                      |           |         | dimensionless          |
|                                       |                 |                                      |           |         | multipliers.           |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `prescribed_schedule`                 | True if any     | `<PrescribedSchedules2019ASHRAE901>` |           |         |                        |
|                                       | schedule values |                                      |           |         |                        |
|                                       | have changed    |                                      |           |         |                        |
|                                       | from what       |                                      |           |         |                        |
|                                       | appears in the  |                                      |           |         |                        |
|                                       | schedule        |                                      |           |         |                        |
|                                       | library         |                                      |           |         |                        |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+
| `is_schedule_modified_for_workaround` | True if any     | `Boolean`                            |           |         |                        |
|                                       | schedule has    |                                      |           |         |                        |
|                                       | been modified   |                                      |           |         |                        |
|                                       | for a           |                                      |           |         |                        |
|                                       | workaround      |                                      |           |         |                        |
+---------------------------------------+-----------------+--------------------------------------+-----------+---------+------------------------+

\pandocend{footnotesize}



## Calendar

\pandocbegin{footnotesize}

+-----------------------------+-----------------+---------------+
| **Name**                    | **Description** | **Data Type** |
+=============================+=================+===============+
| `notes`                     | Supplementary   | `String`      |
|                             | information to  |               |
|                             | provide context |               |
|                             | to the model    |               |
|                             | reviewer        |               |
+-----------------------------+-----------------+---------------+
| `day_of_week_for_january_1` | Day of the week | `<DayOfWeek>` |
|                             | for January 1   |               |
+-----------------------------+-----------------+---------------+
| `is_leap_year`              | The schedules   | `Boolean`     |
|                             | assume it is a  |               |
|                             | leap year       |               |
+-----------------------------+-----------------+---------------+
| `has_daylight_saving_time`  | The schedules   | `Boolean`     |
|                             | adjust for      |               |
|                             | Daylight Saving |               |
|                             | Time            |               |
+-----------------------------+-----------------+---------------+

\pandocend{footnotesize}



## Weather

\pandocbegin{footnotesize}

+-------------------------------+-----------------+---------------------------------+---------+-------------+
| **Name**                      | **Description** | **Data Type**                   | **Req** | **Notes**   |
+===============================+=================+=================================+=========+=============+
| `notes`                       | Supplementary   | `String`                        |         |             |
|                               | information to  |                                 |         |             |
|                               | provide context |                                 |         |             |
|                               | to the model    |                                 |         |             |
|                               | reviewer        |                                 |         |             |
+-------------------------------+-----------------+---------------------------------+---------+-------------+
| `ground_temperature_schedule` | Ground          | `$ID`                           |         | Constraint  |
|                               | temperature     |                                 |         | to use when |
|                               | schedule name   |                                 |         | implemented |
|                               |                 |                                 |         | :Schedule:  |
+-------------------------------+-----------------+---------------------------------+---------+-------------+
| `weather_file_name`           | The file name   | `String`                        |         | The file    |
|                               | for the weather |                                 |         | name for    |
|                               | file including  |                                 |         | the annual  |
|                               | extension.      |                                 |         | weather     |
|                               |                 |                                 |         | file such   |
|                               |                 |                                 |         | as from     |
|                               |                 |                                 |         | TMY, TRY,   |
|                               |                 |                                 |         | CWEC, CTZ,  |
|                               |                 |                                 |         | WYEC or     |
|                               |                 |                                 |         | other       |
|                               |                 |                                 |         | sources.    |
+-------------------------------+-----------------+---------------------------------+---------+-------------+
| `climate_zone`                | The designation | `<ClimateZone2019ASHRAE901>`    | $✓$     | The         |
|                               | of the climate  |                                 |         | enumeration |
|                               | zone where the  |                                 |         | is based on |
|                               | building is     |                                 |         | the         |
|                               | located         |                                 |         | standard    |
|                               |                 |                                 |         | used.       |
+-------------------------------+-----------------+---------------------------------+---------+-------------+
| `cooling_design_day_type`     | The frequency   | `<CoolingDesignDayTypeOptions>` |         |             |
|                               | of occurance    |                                 |         |             |
|                               | type for        |                                 |         |             |
|                               | cooling design  |                                 |         |             |
|                               | day             |                                 |         |             |
+-------------------------------+-----------------+---------------------------------+---------+-------------+
| `heating_design_day_type`     | The frequency   | `<HeatingDesignDayTypeOptions>` |         |             |
|                               | of occurance    |                                 |         |             |
|                               | type for        |                                 |         |             |
|                               | heating design  |                                 |         |             |
|                               | day             |                                 |         |             |
+-------------------------------+-----------------+---------------------------------+---------+-------------+

\pandocend{footnotesize}



## Elevator

\pandocbegin{footnotesize}

+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| **Name**                                  | **Description** | **Data    | **Units** | **Req** | **Notes**   |
|                                           |                 | Type**    |           |         |             |
+===========================================+=================+===========+===========+=========+=============+
| `id`                                      | Scope-unique    | `ID`      |           | $✓$     |             |
|                                           | reference       |           |           |         |             |
|                                           | identifier for  |           |           |         |             |
|                                           | instances of    |           |           |         |             |
|                                           | this data group |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `reporting_name`                          | Descriptive     | `String`  |           |         |             |
|                                           | name used in    |           |           |         |             |
|                                           | RCT reports if  |           |           |         |             |
|                                           | id is not       |           |           |         |             |
|                                           | already a       |           |           |         |             |
|                                           | descriptive     |           |           |         |             |
|                                           | name            |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `notes`                                   | Supplementary   | `String`  |           |         |             |
|                                           | information to  |           |           |         |             |
|                                           | provide context |           |           |         |             |
|                                           | to the model    |           |           |         |             |
|                                           | reviewer        |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `motor_power`                             | Elevator peak   | `Numeric` | W         |         | The motor   |
|                                           | motor power     |           |           |         | power can   |
|                                           |                 |           |           |         | be provided |
|                                           |                 |           |           |         | either      |
|                                           |                 |           |           |         | together    |
|                                           |                 |           |           |         | with or,    |
|                                           |                 |           |           |         | instead of, |
|                                           |                 |           |           |         | the         |
|                                           |                 |           |           |         | detailed    |
|                                           |                 |           |           |         | elements    |
|                                           |                 |           |           |         | used to     |
|                                           |                 |           |           |         | calculate   |
|                                           |                 |           |           |         | it.         |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_counterweight`                       | Elevator car    | `Numeric` | kg        |         |             |
|                                           | counterweight   |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_weight`                              | Weight of       | `Numeric` | kg        |         |             |
|                                           | elevator car    |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `design_elevator_load`                    | Elevator load   | `Numeric` | kg        |         |             |
|                                           | at which to     |           |           |         |             |
|                                           | operate         |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `speed`                                   | Design speed of | `Numeric` | m/s       |         |             |
|                                           | the elevator    |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_area`                                | Floor area of   | `Numeric` | m^2^      |         |             |
|                                           | elevator cab    |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_lighting_power`                      | Lighitng power  | `Numeric` | W         |         |             |
|                                           | of cab          |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_ventilation_fan_power`               | Ventilation fan | `Numeric` | W         |         |             |
|                                           | power of cab    |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_ventilation_fan_flow`                | Airflow of cab  | `Numeric` | L/s       |         |             |
|                                           | ventfan         |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_motor_multiplier_schedule`           | Elevator motor  | `$ID`     |           |         | Constraint  |
|                                           | operation       |           |           |         | to use when |
|                                           | multiplier      |           |           |         | implemented |
|                                           | schedule name   |           |           |         | :Schedule:  |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_ventilation_fan_multiplier_schedule` | Elevator        | `$ID`     |           |         | Constraint  |
|                                           | ventilation fan |           |           |         | to use when |
|                                           | operation       |           |           |         | implemented |
|                                           | mulitplier      |           |           |         | :Schedule:  |
|                                           | schedule name   |           |           |         |             |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+
| `cab_lighting_multiplier_schedule`        | Elevator        | `$ID`     |           |         | Constraint  |
|                                           | lighting        |           |           |         | to use when |
|                                           | multiplier      |           |           |         | implemented |
|                                           | schedule name   |           |           |         | :Schedule:  |
+-------------------------------------------+-----------------+-----------+-----------+---------+-------------+

\pandocend{footnotesize}



## HeatingVentilationAirConditioningSystem

\pandocbegin{footnotesize}

+------------------+-----------------+------------------------------+---------+--------------+
| **Name**         | **Description** | **Data Type**                | **Req** | **Notes**    |
+==================+=================+==============================+=========+==============+
| `id`             | Scope-unique    | `ID`                         | $✓$     |              |
|                  | reference       |                              |         |              |
|                  | identifier for  |                              |         |              |
|                  | instances of    |                              |         |              |
|                  | this data group |                              |         |              |
+------------------+-----------------+------------------------------+---------+--------------+
| `reporting_name` | Descriptive     | `String`                     |         |              |
|                  | name used in    |                              |         |              |
|                  | RCT reports if  |                              |         |              |
|                  | id is not       |                              |         |              |
|                  | already a       |                              |         |              |
|                  | descriptive     |                              |         |              |
|                  | name            |                              |         |              |
+------------------+-----------------+------------------------------+---------+--------------+
| `notes`          | Supplementary   | `String`                     |         |              |
|                  | information to  |                              |         |              |
|                  | provide context |                              |         |              |
|                  | to the model    |                              |         |              |
|                  | reviewer        |                              |         |              |
+------------------+-----------------+------------------------------+---------+--------------+
| `fan_systems`    | Fan systems     | `[{FanSystems}]`             |         | Normally one |
|                  |                 |                              |         | fan system   |
|                  |                 |                              |         | is used but  |
|                  |                 |                              |         | second fan   |
|                  |                 |                              |         | systems may  |
|                  |                 |                              |         | be used when |
|                  |                 |                              |         | a direct     |
|                  |                 |                              |         | outdoor air  |
|                  |                 |                              |         | system is    |
|                  |                 |                              |         | used. JG to  |
|                  |                 |                              |         | verify if    |
|                  |                 |                              |         | used in test |
|                  |                 |                              |         | case         |
|                  |                 |                              |         | description. |
+------------------+-----------------+------------------------------+---------+--------------+
| `heating_system` | Heating system  | `{HeatingSystem}`            |         | JG to verify |
|                  |                 |                              |         | if used in   |
|                  |                 |                              |         | test case    |
|                  |                 |                              |         | description. |
+------------------+-----------------+------------------------------+---------+--------------+
| `cooling_system` | Cooling system  | `{CoolingSystem}`            |         | JG to verify |
|                  |                 |                              |         | if used in   |
|                  |                 |                              |         | test case    |
|                  |                 |                              |         | description. |
+------------------+-----------------+------------------------------+---------+--------------+
| `preheat_system` | Pre-heating     | `{HeatingSystem}`            |         | JG to verify |
|                  | system          |                              |         | if used in   |
|                  |                 |                              |         | test case    |
|                  |                 |                              |         | description. |
+------------------+-----------------+------------------------------+---------+--------------+
| `status_type`    | Choice of new,  | `<GeneralStatusType2019T24>` |         |              |
|                  | existing,       |                              |         |              |
|                  | addition,       |                              |         |              |
|                  | alteration,     |                              |         |              |
|                  | etc. for each   |                              |         |              |
|                  | ruleset.        |                              |         |              |
+------------------+-----------------+------------------------------+---------+--------------+

\pandocend{footnotesize}



## HeatingSystem

\pandocbegin{footnotesize}

+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| **Name**                                            | **Description**             | **Data Type**                  | **Units** | **Constraints** | **Req** | **Notes**    |
+=====================================================+=============================+================================+===========+=================+=========+==============+
| `id`                                                | Scope-unique reference      | `ID`                           |           |                 | $✓$     |              |
|                                                     | identifier for instances of |                                |           |                 |         |              |
|                                                     | this data group             |                                |           |                 |         |              |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `reporting_name`                                    | Descriptive name used in    | `String`                       |           |                 |         |              |
|                                                     | RCT reports if id is not    |                                |           |                 |         |              |
|                                                     | already a descriptive name  |                                |           |                 |         |              |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `notes`                                             | Supplementary information   | `String`                       |           |                 |         |              |
|                                                     | to provide context to the   |                                |           |                 |         |              |
|                                                     | model reviewer              |                                |           |                 |         |              |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `heating_system_type`                               | Heating system type         | `<HeatingSystemType>`          |           |                 |         | JG to verify |
|                                                     |                             |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `hot_water_loop`                                    | Referenced to the hot water | `$ID`                          |           |                 |         | Constraint   |
|                                                     | fluid loop                  |                                |           |                 |         | to use when  |
|                                                     |                             |                                |           |                 |         | implemented  |
|                                                     |                             |                                |           |                 |         | :FluidLoop:  |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `heat_capacity`                                     | Heating capacity            | `Numeric`                      | W         | `≥0`            |         | The design   |
|                                                     |                             |                                |           |                 |         | heat         |
|                                                     |                             |                                |           |                 |         | capacity.    |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `oversizing_factor`                                 | The oversizing factor       | `Numeric`                      |           | `≥0`            |         | Used for     |
|                                                     | applied to the peak load    |                                |           |                 |         | furnace or   |
|                                                     | that results in the heat    |                                |           |                 |         | heat pump.   |
|                                                     | capacity. Zero indicates no |                                |           |                 |         | JG to verify |
|                                                     | oversizing.                 |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `is_autosized`                                      | True if the component is    | `Boolean`                      |           |                 |         | JG to verify |
|                                                     | automatically sized by the  |                                |           |                 |         | if used in   |
|                                                     | simulation software         |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `heating_coil_setpoint`                             | Setpoint of the air leaving | `Numeric`                      | C         |                 |         | JG to verify |
|                                                     | the heating coil            |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `full_load_efficiency`                              | Full Low Efficiency         | `Numeric`                      | W/W       |                 |         | Used for     |
|                                                     | expressed as a coefficient  |                                |           |                 |         | furnace or   |
|                                                     | of performance or thermal   |                                |           |                 |         | heat pump.   |
|                                                     | efficiency                  |                                |           |                 |         | JG to verify |
|                                                     |                             |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `part_load_efficiency`                              | Efficiency value based on   | `Numeric`                      |           | `≥0, ≤1`        |         | Used for     |
|                                                     | the selected                |                                |           |                 |         | furnace or   |
|                                                     | part_load_efficiency_metric |                                |           |                 |         | heat pump.   |
|                                                     |                             |                                |           |                 |         | JG to verify |
|                                                     |                             |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `heatpump_auxilliary_heat_type`                     | Heatpump auxilliary heat    | `<HeatpumpAuxilliaryHeatType>` |           |                 |         | JG to verify |
|                                                     | type used for backup        |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `heatpump_auxilliary_heat_high_temperature_shutoff` | Heatpump auxilliary heat    | `Numeric`                      | C         |                 |         | JG to verify |
|                                                     | high temperature shutoff    |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `heatpump_low_temperature_shutoff`                  | Heatpump low temperature    | `Numeric`                      | C         |                 |         | JG to verify |
|                                                     | shutoff                     |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+
| `humidification_type`                               | Humidification type         | `<HumidificationType>`         |           |                 |         | JG to verify |
|                                                     |                             |                                |           |                 |         | if used in   |
|                                                     |                             |                                |           |                 |         | test case    |
|                                                     |                             |                                |           |                 |         | description. |
+-----------------------------------------------------+-----------------------------+--------------------------------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



## CoolingSystem

\pandocbegin{footnotesize}

+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| **Name**                 | **Description**             | **Data Type**            | **Units** | **Constraints** | **Req** | **Notes**     |
+==========================+=============================+==========================+===========+=================+=========+===============+
| `id`                     | Scope-unique reference      | `ID`                     |           |                 | $✓$     |               |
|                          | identifier for instances of |                          |           |                 |         |               |
|                          | this data group             |                          |           |                 |         |               |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `reporting_name`         | Descriptive name used in    | `String`                 |           |                 |         |               |
|                          | RCT reports if id is not    |                          |           |                 |         |               |
|                          | already a descriptive name  |                          |           |                 |         |               |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `notes`                  | Supplementary information   | `String`                 |           |                 |         |               |
|                          | to provide context to the   |                          |           |                 |         |               |
|                          | model reviewer              |                          |           |                 |         |               |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `cooling_system_type`    | Cooling system type         | `<CoolingSystemType>`    |           |                 |         | JG to verify  |
|                          |                             |                          |           |                 |         | if used in    |
|                          |                             |                          |           |                 |         | test case     |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `total_cool_capacity`    | Total cooling capacity      | `Numeric`                | W         | `≥0`            |         | Designed      |
|                          |                             |                          |           |                 |         | total cooling |
|                          |                             |                          |           |                 |         | capacity. JG  |
|                          |                             |                          |           |                 |         | to verify if  |
|                          |                             |                          |           |                 |         | used in test  |
|                          |                             |                          |           |                 |         | case          |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `sensible_cool_capacity` | Sensible cooling capacity   | `Numeric`                | W         | `≥0`            |         | Designed      |
|                          |                             |                          |           |                 |         | sensible      |
|                          |                             |                          |           |                 |         | cooling       |
|                          |                             |                          |           |                 |         | capacity      |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `oversizing_factor`      | The oversizing factor       | `Numeric`                |           | `≥0`            |         | JG to verify  |
|                          | applied to the peak load    |                          |           |                 |         | if used in    |
|                          | that results in the heat    |                          |           |                 |         | test case     |
|                          | capacity. Zero indicates no |                          |           |                 |         | description.  |
|                          | oversizing.                 |                          |           |                 |         |               |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `is_autosized`           | True if the component is    | `Boolean`                |           |                 |         | JG to verify  |
|                          | automatically sized by the  |                          |           |                 |         | if used in    |
|                          | simulation software         |                          |           |                 |         | test case     |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `chilled_water_loop`     | Referenced to the Chilled   | `$ID`                    |           |                 |         | Constraint to |
|                          | water fluid loop            |                          |           |                 |         | use when      |
|                          |                             |                          |           |                 |         | implemented   |
|                          |                             |                          |           |                 |         | :FluidLoop:   |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `condenser_water_loop`   | Referenced to the Condenser | `$ID`                    |           |                 |         | Constraint to |
|                          | water fluid loop            |                          |           |                 |         | use when      |
|                          |                             |                          |           |                 |         | implemented   |
|                          |                             |                          |           |                 |         | :FluidLoop:   |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `full_load_efficiency`   | Full Low Efficiency         | `Numeric`                | W/W       |                 |         | Used for      |
|                          | expressed as a coefficient  |                          |           |                 |         | direct        |
|                          | of performance (COP)        |                          |           |                 |         | expansion. JG |
|                          |                             |                          |           |                 |         | to verify if  |
|                          |                             |                          |           |                 |         | used in test  |
|                          |                             |                          |           |                 |         | case          |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `part_load_efficiency`   | Efficiency value based on   | `Numeric`                |           | `≥0, ≤1`        |         | Used for      |
|                          | the selected                |                          |           |                 |         | direct        |
|                          | part_load_efficiency_metric |                          |           |                 |         | expansion. JG |
|                          |                             |                          |           |                 |         | to verify if  |
|                          |                             |                          |           |                 |         | used in test  |
|                          |                             |                          |           |                 |         | case          |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `dehumidification_type`  | Dehumidification type       | `<DehumidificationType>` |           |                 |         | JG to verify  |
|                          |                             |                          |           |                 |         | if used in    |
|                          |                             |                          |           |                 |         | test case     |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+
| `cooling_turndown_ratio` | Cooling turndown ratio      | `Numeric`                |           |                 |         | Cooling       |
|                          |                             |                          |           |                 |         | capacity      |
|                          |                             |                          |           |                 |         | turndown      |
|                          |                             |                          |           |                 |         | before        |
|                          |                             |                          |           |                 |         | simultanenous |
|                          |                             |                          |           |                 |         | heating and   |
|                          |                             |                          |           |                 |         | cooling       |
|                          |                             |                          |           |                 |         | occurs. JG to |
|                          |                             |                          |           |                 |         | verify if     |
|                          |                             |                          |           |                 |         | used in test  |
|                          |                             |                          |           |                 |         | case          |
|                          |                             |                          |           |                 |         | description.  |
+--------------------------+-----------------------------+--------------------------+-----------+-----------------+---------+---------------+

\pandocend{footnotesize}



## FanSystem

\pandocbegin{footnotesize}

+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| **Name**                                | **Description** | **Data Type**                       | **Units** | **Constraints** | **Req** | **Notes**    |
+=========================================+=================+=====================================+===========+=================+=========+==============+
| `id`                                    | Scope-unique    | `ID`                                |           |                 | $✓$     |              |
|                                         | reference       |                                     |           |                 |         |              |
|                                         | identifier for  |                                     |           |                 |         |              |
|                                         | instances of    |                                     |           |                 |         |              |
|                                         | this data group |                                     |           |                 |         |              |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `reporting_name`                        | Descriptive     | `String`                            |           |                 |         |              |
|                                         | name used in    |                                     |           |                 |         |              |
|                                         | RCT reports if  |                                     |           |                 |         |              |
|                                         | id is not       |                                     |           |                 |         |              |
|                                         | already a       |                                     |           |                 |         |              |
|                                         | descriptive     |                                     |           |                 |         |              |
|                                         | name            |                                     |           |                 |         |              |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `notes`                                 | Supplementary   | `String`                            |           |                 |         |              |
|                                         | information to  |                                     |           |                 |         |              |
|                                         | provide context |                                     |           |                 |         |              |
|                                         | to the model    |                                     |           |                 |         |              |
|                                         | reviewer        |                                     |           |                 |         |              |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `supply_fans`                           | List of supply  | `[{Fan}]`                           |           |                 |         | JG to verify |
|                                         | fans            |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `return_fans`                           | List of return  | `[{Fan}]`                           |           |                 |         | JG to verify |
|                                         | fans            |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `exhaust_fans`                          | List of exhaust | `[{Fan}]`                           |           |                 |         | JG to verify |
|                                         | fans            |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `relief_fans`                           | List of relief  | `[{Fan}]`                           |           |                 |         | JG to verify |
|                                         | fans            |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `air_economizer`                        | Air side        | `{AirEconomizer}`                   |           |                 |         |              |
|                                         | economizer      |                                     |           |                 |         |              |
|                                         | related to the  |                                     |           |                 |         |              |
|                                         | fan system      |                                     |           |                 |         |              |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `air_energy_recovery`                   | Air side energy | `{AirEnergyRecovery}`               |           |                 |         |              |
|                                         | recovery        |                                     |           |                 |         |              |
|                                         | related to the  |                                     |           |                 |         |              |
|                                         | fan system      |                                     |           |                 |         |              |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `is_variable_air_volume`                | If the fan      | `Boolean`                           |           |                 |         | JG to verify |
|                                         | system is       |                                     |           |                 |         | if used in   |
|                                         | variable air    |                                     |           |                 |         | test case    |
|                                         | volume.         |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `temperature_control`                   | Supply air      | `<FanSystemTemperatureControlType>` |           |                 |         | JG to verify |
|                                         | temperature     |                                     |           |                 |         | if used in   |
|                                         | control type    |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `operation_during_occupied`             | Operation       | `<FanSystemOperationType>`          |           |                 |         | JG to verify |
|                                         | during occupied |                                     |           |                 |         | if used in   |
|                                         | times type      |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `operation_during_unoccupied`           | Operation       | `<FanSystemOperationType>`          |           |                 |         | JG to verify |
|                                         | during          |                                     |           |                 |         | if used in   |
|                                         | unoccupied      |                                     |           |                 |         | test case    |
|                                         | times type      |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `fan_control`                           | Supply fan      | `<FanSystemSupplyFanControlType>`   |           |                 |         | JG to verify |
|                                         | control type    |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `supply_air_temperature_setpoint`       | Supply air      | `Numeric`                           | C         |                 |         | JG to verify |
|                                         | temperature     |                                     |           |                 |         | if used in   |
|                                         | setpoint        |                                     |           |                 |         | test case    |
|                                         | temperarue      |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `reset_differential_temperature`        | Supply air      | `Numeric`                           | C         |                 |         | JG to verify |
|                                         | temperature     |                                     |           |                 |         | if used in   |
|                                         | reset           |                                     |           |                 |         | test case    |
|                                         | differential    |                                     |           |                 |         | description. |
|                                         | temperature at  |                                     |           |                 |         |              |
|                                         | minimum cooling |                                     |           |                 |         |              |
|                                         | load            |                                     |           |                 |         |              |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `supply_air_temperature_reset_schedule` | Supply air      | `$ID`                               |           |                 |         | JG to verify |
|                                         | temperature     |                                     |           |                 |         | if used in   |
|                                         | reset schedule  |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
|                                         |                 |                                     |           |                 |         | Constraint   |
|                                         |                 |                                     |           |                 |         | to use when  |
|                                         |                 |                                     |           |                 |         | implemented  |
|                                         |                 |                                     |           |                 |         | :Schedule:   |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `operating_schedule`                    | Operating       | `$ID`                               |           |                 |         | Zero when    |
|                                         | schedule name   |                                     |           |                 |         | fan is off.  |
|                                         |                 |                                     |           |                 |         | JG to verify |
|                                         |                 |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
|                                         |                 |                                     |           |                 |         | Constraint   |
|                                         |                 |                                     |           |                 |         | to use when  |
|                                         |                 |                                     |           |                 |         | implemented  |
|                                         |                 |                                     |           |                 |         | :Schedule:   |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `minimum_airflow`                       | Minimum volume  | `Numeric`                           | L/s       |                 |         | JG to verify |
|                                         | airflow         |                                     |           |                 |         | if used in   |
|                                         |                 |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `minimum_outdoor_airflow`               | Minimum outdoor | `Numeric`                           | L/s       |                 |         | JG to verify |
|                                         | air volume      |                                     |           |                 |         | if used in   |
|                                         | airflow         |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `maximum_outdoor_airflow`               | Maximum outdoor | `Numeric`                           | L/s       |                 |         | JG to verify |
|                                         | air volume      |                                     |           |                 |         | if used in   |
|                                         | airflow         |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `air_filter_merv_rating`                | The MERV rating | `Numeric`                           |           | `≥1, ≤20`       |         | JG to verify |
|                                         | of the air      |                                     |           |                 |         | if used in   |
|                                         | filter          |                                     |           |                 |         | test case    |
|                                         |                 |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+
| `has_fully_ducted_return`               | If the fan      | `Boolean`                           |           |                 |         | JG to verify |
|                                         | system has      |                                     |           |                 |         | if used in   |
|                                         | fully ducted    |                                     |           |                 |         | test case    |
|                                         | return.         |                                     |           |                 |         | description. |
+-----------------------------------------+-----------------+-------------------------------------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



## AirEconomizer

\pandocbegin{footnotesize}

+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| **Name**                                    | **Description** | **Data Type**         | **Units** | **Req** | **Notes**    |
+=============================================+=================+=======================+===========+=========+==============+
| `id`                                        | Scope-unique    | `ID`                  |           | $✓$     |              |
|                                             | reference       |                       |           |         |              |
|                                             | identifier for  |                       |           |         |              |
|                                             | instances of    |                       |           |         |              |
|                                             | this data group |                       |           |         |              |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| `reporting_name`                            | Descriptive     | `String`              |           |         |              |
|                                             | name used in    |                       |           |         |              |
|                                             | RCT reports if  |                       |           |         |              |
|                                             | id is not       |                       |           |         |              |
|                                             | already a       |                       |           |         |              |
|                                             | descriptive     |                       |           |         |              |
|                                             | name            |                       |           |         |              |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| `notes`                                     | Supplementary   | `String`              |           |         |              |
|                                             | information to  |                       |           |         |              |
|                                             | provide context |                       |           |         |              |
|                                             | to the model    |                       |           |         |              |
|                                             | reviewer        |                       |           |         |              |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| `air_economizer_type`                       | Air economizer  | `<AirEconomizerType>` |           |         | JG to verify |
|                                             | type            |                       |           |         | if used in   |
|                                             |                 |                       |           |         | test case    |
|                                             |                 |                       |           |         | description. |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| `economizer_high_limit_temperature_shutoff` | Economizer high | `Numeric`             | C         |         | JG to verify |
|                                             | limit           |                       |           |         | if used in   |
|                                             | temperature     |                       |           |         | test case    |
|                                             | shutoff         |                       |           |         | description. |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| `economizer_design_sensible_effectiveness`  | Economizer      | `Numeric`             |           |         | JG to verify |
|                                             | design sensible |                       |           |         | if used in   |
|                                             | effectiveness   |                       |           |         | test case    |
|                                             |                 |                       |           |         | description. |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+
| `economizer_design_latent_effectiveness`    | Economizer      | `Numeric`             |           |         | JG to verify |
|                                             | design sensible |                       |           |         | if used in   |
|                                             | effectiveness   |                       |           |         | test case    |
|                                             |                 |                       |           |         | description. |
+---------------------------------------------+-----------------+-----------------------+-----------+---------+--------------+

\pandocend{footnotesize}



## AirEnergyRecovery

\pandocbegin{footnotesize}

+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| **Name**                                         | **Description** | **Data Type**                                 | **Req** | **Notes**    |
+==================================================+=================+===============================================+=========+==============+
| `id`                                             | Scope-unique    | `ID`                                          | $✓$     |              |
|                                                  | reference       |                                               |         |              |
|                                                  | identifier for  |                                               |         |              |
|                                                  | instances of    |                                               |         |              |
|                                                  | this data group |                                               |         |              |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| `reporting_name`                                 | Descriptive     | `String`                                      |         |              |
|                                                  | name used in    |                                               |         |              |
|                                                  | RCT reports if  |                                               |         |              |
|                                                  | id is not       |                                               |         |              |
|                                                  | already a       |                                               |         |              |
|                                                  | descriptive     |                                               |         |              |
|                                                  | name            |                                               |         |              |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| `notes`                                          | Supplementary   | `String`                                      |         |              |
|                                                  | information to  |                                               |         |              |
|                                                  | provide context |                                               |         |              |
|                                                  | to the model    |                                               |         |              |
|                                                  | reviewer        |                                               |         |              |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| `energy_recovery_type`                           | Energy recovery | `<EnergyRecoveryType>`                        |         | JG to verify |
|                                                  | type            |                                               |         | if used in   |
|                                                  |                 |                                               |         | test case    |
|                                                  |                 |                                               |         | description. |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| `enthalpy_recovery_ratio`                        | Enthalpy        | `Numeric`                                     |         | JG to verify |
|                                                  | recovery ratio  |                                               |         | if used in   |
|                                                  |                 |                                               |         | test case    |
|                                                  |                 |                                               |         | description. |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| `energy_recovery_operation`                      | Energy recovery | `<EnergyRecoveryOperation>`                   |         | JG to verify |
|                                                  | operation       |                                               |         | if used in   |
|                                                  |                 |                                               |         | test case    |
|                                                  |                 |                                               |         | description. |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+
| `energy_recovery_supply_air_temperature_control` | Energy recovery | `<EnergyRecoverySupplyAirTemperatureControl>` |         | JG to verify |
|                                                  | supply air      |                                               |         | if used in   |
|                                                  | temperature     |                                               |         | test case    |
|                                                  | control         |                                               |         | description. |
+--------------------------------------------------+-----------------+-----------------------------------------------+---------+--------------+

\pandocend{footnotesize}



## Fan

\pandocbegin{footnotesize}

+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| **Name**                | **Description** | **Data Type**                     | **Units** | **Req** | **Notes**            |
+=========================+=================+===================================+===========+=========+======================+
| `id`                    | Scope-unique    | `ID`                              |           | $✓$     |                      |
|                         | reference       |                                   |           |         |                      |
|                         | identifier for  |                                   |           |         |                      |
|                         | instances of    |                                   |           |         |                      |
|                         | this data group |                                   |           |         |                      |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `reporting_name`        | Descriptive     | `String`                          |           |         |                      |
|                         | name used in    |                                   |           |         |                      |
|                         | RCT reports if  |                                   |           |         |                      |
|                         | id is not       |                                   |           |         |                      |
|                         | already a       |                                   |           |         |                      |
|                         | descriptive     |                                   |           |         |                      |
|                         | name            |                                   |           |         |                      |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `notes`                 | Supplementary   | `String`                          |           |         |                      |
|                         | information to  |                                   |           |         |                      |
|                         | provide context |                                   |           |         |                      |
|                         | to the model    |                                   |           |         |                      |
|                         | reviewer        |                                   |           |         |                      |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `design_airflow`        | Design airflow  | `Numeric`                         | L/s       |         | JG to verify if used |
|                         |                 |                                   |           |         | in test case         |
|                         |                 |                                   |           |         | description.         |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `specification_method`  | Options for how | `<FanSpecificationMethodOptions>` |           |         |                      |
|                         | the fan is      |                                   |           |         |                      |
|                         | specified       |                                   |           |         |                      |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `design_electric_power` | Design electric | `Numeric`                         | W         |         | JG to verify if used |
|                         | fan power       |                                   |           |         | in test case         |
|                         |                 |                                   |           |         | description.         |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `design_pressure_rise`  | Pressure rise   | `Numeric`                         | m         |         | Only used when       |
|                         | through fan at  |                                   |           |         | specification_method |
|                         | design flow     |                                   |           |         | is set to Detailed   |
|                         | conditions      |                                   |           |         |                      |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `nameplate_power`       | nameplate       | `Numeric`                         | W         |         | JG to verify if used |
|                         | horsepower of   |                                   |           |         | in test case         |
|                         | fan             |                                   |           |         | description.         |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `total_efficiency`      | Fan motor       | `Numeric`                         | W         |         | Only used when       |
|                         | efficiency      |                                   |           |         | specification_method |
|                         |                 |                                   |           |         | is set to Detailed   |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `motor_efficiency`      | Fan motor       | `Numeric`                         | W         |         | Only used when       |
|                         | efficiency      |                                   |           |         | specification_method |
|                         |                 |                                   |           |         | is set to Detailed   |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+
| `status_type`           | Choice of new,  | `<GeneralStatusType2019T24>`      |           |         |                      |
|                         | existing,       |                                   |           |         |                      |
|                         | addition,       |                                   |           |         |                      |
|                         | alteration,     |                                   |           |         |                      |
|                         | etc. for each   |                                   |           |         |                      |
|                         | ruleset.        |                                   |           |         |                      |
+-------------------------+-----------------+-----------------------------------+-----------+---------+----------------------+

\pandocend{footnotesize}



## Terminal

\pandocbegin{footnotesize}

+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| **Name**                                                 | **Description**   | **Data Type**                | **Units** | **Req** | **Notes**                                 |
+==========================================================+===================+==============================+===========+=========+===========================================+
| `id`                                                     | Scope-unique      | `ID`                         |           | $✓$     |                                           |
|                                                          | reference         |                              |           |         |                                           |
|                                                          | identifier for    |                              |           |         |                                           |
|                                                          | instances of this |                              |           |         |                                           |
|                                                          | data group        |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `reporting_name`                                         | Descriptive name  | `String`                     |           |         |                                           |
|                                                          | used in RCT       |                              |           |         |                                           |
|                                                          | reports if id is  |                              |           |         |                                           |
|                                                          | not already a     |                              |           |         |                                           |
|                                                          | descriptive name  |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `notes`                                                  | Supplementary     | `String`                     |           |         |                                           |
|                                                          | information to    |                              |           |         |                                           |
|                                                          | provide context   |                              |           |         |                                           |
|                                                          | to the model      |                              |           |         |                                           |
|                                                          | reviewer          |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `type`                                                   | Type of terminal  | `<TerminalType>`             |           |         | JG to verify if used in test case         |
|                                                          |                   |                              |           |         | description.                              |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `served_by_heating_ventilation_air_conditioning_systems` | HVAC systems      | `$ID`                        |           |         | Contains ID of the HVAC system serving    |
|                                                          | serving the       |                              |           |         | the terminal - from Unique Identification |
|                                                          | terminal          |                              |           |         | Number in                                 |
|                                                          |                   |                              |           |         | HeatingVentilationAirConditioningSystem.  |
|                                                          |                   |                              |           |         | Constraint to use when implemented        |
|                                                          |                   |                              |           |         | :HeatingVentilationAirConditioningSystem: |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `reheat_source`                                          | Source of reheat  | `<ReheatSourceType>`         |           |         | JG to verify if used in test case         |
|                                                          |                   |                              |           |         | description.                              |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `reheat_from_loop`                                       | Referenced to the | `$ID`                        |           |         | Only used when reheat_source is hot       |
|                                                          | fluid loop used   |                              |           |         | water. Constraint to use when implemented |
|                                                          | for reheat        |                              |           |         | :FluidLoop:                               |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `fan`                                                    | Terminal fan      | `{Fan}`                      |           |         | JG to verify if used in test case         |
|                                                          |                   |                              |           |         | description.                              |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `fan_configuration`                                      | Fan configuration | `<TerminalFanConfiguration>` |           |         | JG to verify if used in test case         |
|                                                          |                   |                              |           |         | description.                              |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `primary_airflow`                                        | Zone terminal     | `Numeric`                    | L/s       |         | JG to verify if used in test case         |
|                                                          | primary airflow   |                              |           |         | description.                              |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `secondary_airflow`                                      | Zone terminal     | `Numeric`                    | L/s       |         | JG to verify if used in test case         |
|                                                          | secondary_airflow |                              |           |         | description.                              |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `supply_temperature_setpoint`                            | Zone terminal     | `Numeric`                    | C         |         | JG to verify if used in test case         |
|                                                          | supply            |                              |           |         | description.                              |
|                                                          | temperature       |                              |           |         |                                           |
|                                                          | setpoint          |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `minimum_airflow`                                        | Zone terminal     | `Numeric`                    | L/s       |         | JG to verify if used in test case         |
|                                                          | minimum volume    |                              |           |         | description.                              |
|                                                          | airflow           |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `minimum_outdoor_airflow`                                | Zone terminal     | `Numeric`                    | L/s       |         | JG to verify if used in test case         |
|                                                          | minimum outdoor   |                              |           |         | description.                              |
|                                                          | air volume        |                              |           |         |                                           |
|                                                          | airflow           |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `minimum_outdoor_airflow_multiplier_schedule`            | Zone terminal     | `$ID`                        |           |         | JG to verify if used in test case         |
|                                                          | minimum outdoor   |                              |           |         | description. Constraint to use when       |
|                                                          | air volume        |                              |           |         | implemented :Schedule:                    |
|                                                          | airflow           |                              |           |         |                                           |
|                                                          | multiplier        |                              |           |         |                                           |
|                                                          | schedule name     |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+
| `heat_capacity`                                          | Heat capacity for | `Numeric`                    | W         |         | JG to verify if used in test case         |
|                                                          | baseboard or      |                              |           |         | description.                              |
|                                                          | radiant system    |                              |           |         |                                           |
+----------------------------------------------------------+-------------------+------------------------------+-----------+---------+-------------------------------------------+

\pandocend{footnotesize}



## FluidLoop

\pandocbegin{footnotesize}

+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| **Name**                                   | **Description** | **Data Type**                 | **Units**   | **Req** | **Notes**  |
+============================================+=================+===============================+=============+=========+============+
| `id`                                       | Scope-unique    | `ID`                          |             | $✓$     |            |
|                                            | reference       |                               |             |         |            |
|                                            | identifier for  |                               |             |         |            |
|                                            | instances of    |                               |             |         |            |
|                                            | this data group |                               |             |         |            |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `reporting_name`                           | Descriptive     | `String`                      |             |         |            |
|                                            | name used in    |                               |             |         |            |
|                                            | RCT reports if  |                               |             |         |            |
|                                            | id is not       |                               |             |         |            |
|                                            | already a       |                               |             |         |            |
|                                            | descriptive     |                               |             |         |            |
|                                            | name            |                               |             |         |            |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `notes`                                    | Supplementary   | `String`                      |             |         |            |
|                                            | information to  |                               |             |         |            |
|                                            | provide context |                               |             |         |            |
|                                            | to the model    |                               |             |         |            |
|                                            | reviewer        |                               |             |         |            |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `type`                                     | Type of loop    | `<FluidLoopTypeOptions>`      |             |         |            |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `pump_power_per_flow_rate`                 | Total design    | `Numeric`                     | W/s$\cdot$L |         | This is    |
|                                            | pump power      |                               |             |         | the pump   |
|                                            | divided by the  |                               |             |         | power per  |
|                                            | loop design     |                               |             |         | flow rate  |
|                                            | flow rate       |                               |             |         | for the    |
|                                            |                 |                               |             |         | entire     |
|                                            |                 |                               |             |         | pumping    |
|                                            |                 |                               |             |         | system on  |
|                                            |                 |                               |             |         | the        |
|                                            |                 |                               |             |         | current    |
|                                            |                 |                               |             |         | FluidLoop. |
|                                            |                 |                               |             |         | The power  |
|                                            |                 |                               |             |         | and flow   |
|                                            |                 |                               |             |         | rate       |
|                                            |                 |                               |             |         | should be  |
|                                            |                 |                               |             |         | for the    |
|                                            |                 |                               |             |         | current    |
|                                            |                 |                               |             |         | FluidLoop  |
|                                            |                 |                               |             |         | only and   |
|                                            |                 |                               |             |         | does not   |
|                                            |                 |                               |             |         | include    |
|                                            |                 |                               |             |         | power and  |
|                                            |                 |                               |             |         | flow rate  |
|                                            |                 |                               |             |         | in any     |
|                                            |                 |                               |             |         | child      |
|                                            |                 |                               |             |         | loops.     |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `child_loops`                              | Other fluid     | `[{FluidLoop}]`               |             |         | Secondary  |
|                                            | loops connected |                               |             |         | loops      |
|                                            | to this one as  |                               |             |         | should be  |
|                                            | children.       |                               |             |         | described  |
|                                            |                 |                               |             |         | as child   |
|                                            |                 |                               |             |         | loops.     |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `cooling_or_condensing_design_and_control` |                 | `{FluidLoopDesignAndControl}` |             |         |            |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+
| `heating_design_and_control`               |                 | `{FluidLoopDesignAndControl}` |             |         |            |
+--------------------------------------------+-----------------+-------------------------------+-------------+---------+------------+

\pandocend{footnotesize}



## FluidLoopDesignAndControl

\pandocbegin{footnotesize}

+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| **Name**                                         | **Description** | **Data Type**                   | **Units** | **Req** |
+==================================================+=================+=================================+===========+=========+
| `id`                                             | Scope-unique    | `ID`                            |           | $✓$     |
|                                                  | reference       |                                 |           |         |
|                                                  | identifier for  |                                 |           |         |
|                                                  | instances of    |                                 |           |         |
|                                                  | this data group |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `reporting_name`                                 | Descriptive     | `String`                        |           |         |
|                                                  | name used in    |                                 |           |         |
|                                                  | RCT reports if  |                                 |           |         |
|                                                  | id is not       |                                 |           |         |
|                                                  | already a       |                                 |           |         |
|                                                  | descriptive     |                                 |           |         |
|                                                  | name            |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `notes`                                          | Supplementary   | `String`                        |           |         |
|                                                  | information to  |                                 |           |         |
|                                                  | provide context |                                 |           |         |
|                                                  | to the model    |                                 |           |         |
|                                                  | reviewer        |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `design_supply_temperature`                      | Design Supply   | `Numeric`                       | C         |         |
|                                                  | Temperature     |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `design_return_temperature`                      | Design Return   | `Numeric`                       | C         |         |
|                                                  | Temperature     |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `is_sized_using_coincident_load`                 | True if the     | `Boolean`                       |           |         |
|                                                  | loop is sized   |                                 |           |         |
|                                                  | based on        |                                 |           |         |
|                                                  | coincident load |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `minimum_flow_fraction`                          | Minimum         | `Numeric`                       |           |         |
|                                                  | fraction of     |                                 |           |         |
|                                                  | full flow       |                                 |           |         |
|                                                  | allowed         |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `operation`                                      | Type of         | `<FluidLoopOperationOptions>`   |           |         |
|                                                  | operation used  |                                 |           |         |
|                                                  | by loop         |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `flow_control`                                   | Flow control    | `<FluidLoopFlowControlOptions>` |           |         |
|                                                  | options         |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `temperature_reset_type`                         | Type of         | `<TemperatureResetTypeOptions>` |           |         |
|                                                  | temperature     |                                 |           |         |
|                                                  | reset used by   |                                 |           |         |
|                                                  | loop            |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `outdoor_high_for_loop_supply_temperature_reset` | Outdoor high    | `Numeric`                       | C         |         |
|                                                  | for loop supply |                                 |           |         |
|                                                  | temp reset      |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `outdoor_low_for_loop_supply_temperature_reset`  | Outdoor low for | `Numeric`                       | C         |         |
|                                                  | loop supply     |                                 |           |         |
|                                                  | temp reset      |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `loop_supply_temperature_at_outdoor_high`        | Loop supply     | `Numeric`                       | C         |         |
|                                                  | temperature at  |                                 |           |         |
|                                                  | outdoor high    |                                 |           |         |
|                                                  | temperature     |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+
| `loop_supply_temperature_at_outdoor_low`         | Loop supply     | `Numeric`                       | C         |         |
|                                                  | temperature at  |                                 |           |         |
|                                                  | outdoor low     |                                 |           |         |
|                                                  | temperature     |                                 |           |         |
+--------------------------------------------------+-----------------+---------------------------------+-----------+---------+

\pandocend{footnotesize}



## Pump

\pandocbegin{footnotesize}

+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| **Name**                | **Description** | **Data Type**                      | **Units** | **Constraints** | **Req** | **Notes**            |
+=========================+=================+====================================+===========+=================+=========+======================+
| `id`                    | Scope-unique    | `ID`                               |           |                 | $✓$     |                      |
|                         | reference       |                                    |           |                 |         |                      |
|                         | identifier for  |                                    |           |                 |         |                      |
|                         | instances of    |                                    |           |                 |         |                      |
|                         | this data group |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `reporting_name`        | Descriptive     | `String`                           |           |                 |         |                      |
|                         | name used in    |                                    |           |                 |         |                      |
|                         | RCT reports if  |                                    |           |                 |         |                      |
|                         | id is not       |                                    |           |                 |         |                      |
|                         | already a       |                                    |           |                 |         |                      |
|                         | descriptive     |                                    |           |                 |         |                      |
|                         | name            |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `notes`                 | Supplementary   | `String`                           |           |                 |         |                      |
|                         | information to  |                                    |           |                 |         |                      |
|                         | provide context |                                    |           |                 |         |                      |
|                         | to the model    |                                    |           |                 |         |                      |
|                         | reviewer        |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `loop_or_piping`        | Referenced to   | `$ID`                              |           |                 | $✓$     | Constraint to use    |
|                         | the fluid loop  |                                    |           |                 |         | when implemented     |
|                         | or service      |                                    |           |                 |         | :FluidLoop: or       |
|                         | water heating   |                                    |           |                 |         | :ServiceWaterPiping: |
|                         | piping          |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `specification_method`  | Options for how | `<PumpSpecificationMethodOptions>` |           |                 |         |                      |
|                         | the pump is     |                                    |           |                 |         |                      |
|                         | specified       |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `design_electric_power` | Pump design     | `Numeric`                          | W         |                 |         | Pump electric power  |
|                         | electric power  |                                    |           |                 |         | at design            |
|                         |                 |                                    |           |                 |         | conditions. Only     |
|                         |                 |                                    |           |                 |         | used when            |
|                         |                 |                                    |           |                 |         | specification_method |
|                         |                 |                                    |           |                 |         | is set to Simple     |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `motor_nameplate_power` | Pump motor      | `Numeric`                          | W         |                 |         | Only used when       |
|                         | nameplate power |                                    |           |                 |         | specification_method |
|                         |                 |                                    |           |                 |         | is set to Detailed   |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `design_head`           | Head of the     | `Numeric`                          | m         |                 |         | Only used when       |
|                         | pump at design  |                                    |           |                 |         | specification_method |
|                         | flow conditions |                                    |           |                 |         | is set to Detailed   |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `impeller_efficiency`   | Full load       | `Numeric`                          |           | `≥0, ≤1`        |         | Only used when       |
|                         | efficiency of   |                                    |           |                 |         | specification_method |
|                         | the impeller    |                                    |           |                 |         | is set to Detailed   |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `motor_efficiency`      | Full load       | `Numeric`                          |           | `≥0, ≤1`        |         | Only used when       |
|                         | efficiency of   |                                    |           |                 |         | specification_method |
|                         | the pump motor  |                                    |           |                 |         | is set to Detailed   |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `speed_control`         | Options for     | `<PumpSpeedControlOptions>`        |           |                 |         |                      |
|                         | pump speed      |                                    |           |                 |         |                      |
|                         | control         |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `design_flow`           | Design Pump     | `Numeric`                          | L/s       |                 |         |                      |
|                         | Flowrate        |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `is_flow_autosized`     | True if the     | `Boolean`                          |           |                 |         |                      |
|                         | design_flow is  |                                    |           |                 |         |                      |
|                         | autosized       |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+
| `is_variable_speed`     | True if         | `Boolean`                          |           |                 |         |                      |
|                         | variable speed  |                                    |           |                 |         |                      |
|                         | drive such a    |                                    |           |                 |         |                      |
|                         | VFD             |                                    |           |                 |         |                      |
+-------------------------+-----------------+------------------------------------+-----------+-----------------+---------+----------------------+

\pandocend{footnotesize}



## Boiler

\pandocbegin{footnotesize}

+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| **Name**                   | **Description**   | **Data Type**                         | **Units** | **Constraints** | **Req** | **Notes**    |
+============================+===================+=======================================+===========+=================+=========+==============+
| `id`                       | Scope-unique      | `ID`                                  |           |                 | $✓$     |              |
|                            | reference         |                                       |           |                 |         |              |
|                            | identifier for    |                                       |           |                 |         |              |
|                            | instances of this |                                       |           |                 |         |              |
|                            | data group        |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `reporting_name`           | Descriptive name  | `String`                              |           |                 |         |              |
|                            | used in RCT       |                                       |           |                 |         |              |
|                            | reports if id is  |                                       |           |                 |         |              |
|                            | not already a     |                                       |           |                 |         |              |
|                            | descriptive name  |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `notes`                    | Supplementary     | `String`                              |           |                 |         |              |
|                            | information to    |                                       |           |                 |         |              |
|                            | provide context   |                                       |           |                 |         |              |
|                            | to the model      |                                       |           |                 |         |              |
|                            | reviewer          |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `loop`                     | Referenced to the | `$ID`                                 |           |                 | $✓$     | Constraint   |
|                            | fluid loop        |                                       |           |                 |         | to use when  |
|                            |                   |                                       |           |                 |         | implemented  |
|                            |                   |                                       |           |                 |         | :FluidLoop:  |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `design_capacity`          | Heating capacity  | `Numeric`                             | W         |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `rated_capacity`           | Heating capacity  | `Numeric`                             | W         |                 |         | At rating    |
|                            |                   |                                       |           |                 |         | conditions.  |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `minimum_load_ratio`       | Minimum fraction  | `Numeric`                             |           |                 |         |              |
|                            | of full load      |                                       |           |                 |         |              |
|                            | allowed           |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `draft_type`               | Combustion option | `<BoilerCombustionOptions>`           |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `energy_source_type`       | Source of energy  | `<EnergySourceTypeOptions>`           |           |                 |         |              |
|                            | for the boiler    |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `efficiency_metric`        | The type of       | `<BoilerEfficiencyMetricTypeOptions>` |           |                 |         |              |
|                            | efficiency metric |                                       |           |                 |         |              |
|                            | used              |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `efficiency`               | Efficiency value  | `Numeric`                             |           | `≥0, ≤1`        |         |              |
|                            | based on the      |                                       |           |                 |         |              |
|                            | selected          |                                       |           |                 |         |              |
|                            | efficiency_metric |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `output_validation_points` | Energy validation | `[{BoilerOutputValidationPoint}]`     |           |                 |         | Load is      |
|                            | points            |                                       |           |                 |         | input to     |
|                            |                   |                                       |           |                 |         | each         |
|                            |                   |                                       |           |                 |         | validation   |
|                            |                   |                                       |           |                 |         | point and    |
|                            |                   |                                       |           |                 |         | energy       |
|                            |                   |                                       |           |                 |         | output is    |
|                            |                   |                                       |           |                 |         | the result.  |
|                            |                   |                                       |           |                 |         | A minimum    |
|                            |                   |                                       |           |                 |         | number of    |
|                            |                   |                                       |           |                 |         | four points  |
|                            |                   |                                       |           |                 |         | is           |
|                            |                   |                                       |           |                 |         | recommended. |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `auxiliary_power`          | Auxiliary power   | `Numeric`                             | W         |                 |         | Power for    |
|                            |                   |                                       |           |                 |         | boiler pump, |
|                            |                   |                                       |           |                 |         | combustion   |
|                            |                   |                                       |           |                 |         | fan, or      |
|                            |                   |                                       |           |                 |         | other        |
|                            |                   |                                       |           |                 |         | auxiliary    |
|                            |                   |                                       |           |                 |         | that         |
|                            |                   |                                       |           |                 |         | operates     |
|                            |                   |                                       |           |                 |         | when boiler  |
|                            |                   |                                       |           |                 |         | operates.    |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `operation_lower_limit`    | Heating load      | `Numeric`                             | W         |                 |         |              |
|                            | range operation,  |                                       |           |                 |         |              |
|                            | lower limit       |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+
| `operation_upper_limit`    | Heating load      | `Numeric`                             | W         |                 |         |              |
|                            | range operation,  |                                       |           |                 |         |              |
|                            | upper limit       |                                       |           |                 |         |              |
+----------------------------+-------------------+---------------------------------------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



## BoilerOutputValidationPoint

\pandocbegin{footnotesize}

+----------+-----------------+-----------+-----------+-----------+
| **Name** | **Description** | **Data    | **Units** | **Notes** |
|          |                 | Type**    |           |           |
+==========+=================+===========+===========+===========+
| `load`   | Load            | `Numeric` | W         | No name   |
|          |                 |           |           | and id is |
|          |                 |           |           | needed    |
|          |                 |           |           | since     |
|          |                 |           |           | typically |
|          |                 |           |           | used as   |
|          |                 |           |           | one of a  |
|          |                 |           |           | series.   |
+----------+-----------------+-----------+-----------+-----------+
| `result` | Result          | `Numeric` | W         |           |
+----------+-----------------+-----------+-----------+-----------+

\pandocend{footnotesize}



## Chiller

\pandocbegin{footnotesize}

+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| **Name**                      | **Description**             | **Data Type**                                  | **Units** | **Constraints** | **Req** | **Notes**   |
+===============================+=============================+================================================+===========+=================+=========+=============+
| `id`                          | Scope-unique reference      | `ID`                                           |           |                 | $✓$     |             |
|                               | identifier for instances of |                                                |           |                 |         |             |
|                               | this data group             |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `reporting_name`              | Descriptive name used in    | `String`                                       |           |                 |         |             |
|                               | RCT reports if id is not    |                                                |           |                 |         |             |
|                               | already a descriptive name  |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `notes`                       | Supplementary information   | `String`                                       |           |                 |         |             |
|                               | to provide context to the   |                                                |           |                 |         |             |
|                               | model reviewer              |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `cooling_loop`                | Referenced to the cooling   | `$ID`                                          |           |                 | $✓$     | Constraint  |
|                               | fluid loop                  |                                                |           |                 |         | to use when |
|                               |                             |                                                |           |                 |         | implemented |
|                               |                             |                                                |           |                 |         | :FluidLoop: |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `condensing_loop`             | Referenced to the           | `$ID`                                          |           |                 |         | No          |
|                               | condensing fluid loop       |                                                |           |                 |         | condensing  |
|                               |                             |                                                |           |                 |         | loop name   |
|                               |                             |                                                |           |                 |         | implies     |
|                               |                             |                                                |           |                 |         | air-cooled  |
|                               |                             |                                                |           |                 |         | chiller.    |
|                               |                             |                                                |           |                 |         | Constraint  |
|                               |                             |                                                |           |                 |         | to use when |
|                               |                             |                                                |           |                 |         | implemented |
|                               |                             |                                                |           |                 |         | :FluidLoop: |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `compressor_type`             | Compressor Type             | `<ChillerCompressorTypeOptions>`               |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `energy_source_type`          | Source of energy for the    | `<EnergySourceTypeOptions>`                    |           |                 |         |             |
|                               | chiller                     |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `design_capacity`             | Chiller Design Cooling      | `Numeric`                                      | W         |                 |         |             |
|                               | Capacity                    |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `rated_capacity`              | Chiller Design Cooling      | `Numeric`                                      | W         |                 |         | At rating   |
|                               | Capacity                    |                                                |           |                 |         | conditions. |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `minimum_load_ratio`          | Minimum fraction of full    | `Numeric`                                      |           |                 |         |             |
|                               | load allowed                |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `design_flow_evaporator`      | Chiller evaporator design   | `Numeric`                                      | L/s       |                 |         |             |
|                               | flow                        |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `design_flow_condenser`       | Chiller condenser design    | `Numeric`                                      | L/s       |                 |         |             |
|                               | flow                        |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `full_load_efficiency`        | Full Low Efficiency         | `Numeric`                                      | W/W       |                 |         |             |
|                               | expressed as a coefficient  |                                                |           |                 |         |             |
|                               | of performance (COP)        |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `part_load_efficiency`        | Efficiency value based on   | `Numeric`                                      |           | `≥0, ≤1`        |         |             |
|                               | the selected                |                                                |           |                 |         |             |
|                               | part_load_efficiency_metric |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `part_load_efficiency_metric` | The type of part load       | `<ChillerPartLoadEfficiencyMetricTypeOptions>` |           |                 |         |             |
|                               | efficiency metric used      |                                                |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `capacity_validation_points`  | Capacity validation points  | `[{ChillerCapacityValidationPoint}]`           |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+
| `power_validation_points`     | Energy validation points    | `[{ChillerPowerValidationPoint}]`              |           |                 |         |             |
+-------------------------------+-----------------------------+------------------------------------------------+-----------+-----------------+---------+-------------+

\pandocend{footnotesize}



## ChillerCapacityValidationPoint

\pandocbegin{footnotesize}

+------------------------------------+-----------------+-----------+-----------+-------------+
| **Name**                           | **Description** | **Data    | **Units** | **Notes**   |
|                                    |                 | Type**    |           |             |
+====================================+=================+===========+===========+=============+
| `chilled_water_supply_temperature` | Chilled water   | `Numeric` | C         | No name and |
|                                    | supply          |           |           | id is       |
|                                    | temperature     |           |           | needed      |
|                                    |                 |           |           | since used  |
|                                    |                 |           |           | as one of a |
|                                    |                 |           |           | series. The |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | is leaving  |
|                                    |                 |           |           | the         |
|                                    |                 |           |           | chiller.    |
+------------------------------------+-----------------+-----------+-----------+-------------+
| `condenser_temperature`            | Second          | `Numeric` | C         | Outside air |
|                                    | temperature     |           |           | dry-bulb    |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | for air     |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chillers    |
|                                    |                 |           |           | and         |
|                                    |                 |           |           | condenser   |
|                                    |                 |           |           | water       |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | for water   |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chillers.   |
|                                    |                 |           |           | For water   |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chillers,   |
|                                    |                 |           |           | this is the |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | as the      |
|                                    |                 |           |           | water       |
|                                    |                 |           |           | enters the  |
|                                    |                 |           |           | chiller.    |
|                                    |                 |           |           | For air     |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chilers     |
|                                    |                 |           |           | this the    |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | of the      |
|                                    |                 |           |           | ambient     |
|                                    |                 |           |           | air.        |
+------------------------------------+-----------------+-----------+-----------+-------------+
| `result`                           | Result          | `Numeric` | W         |             |
+------------------------------------+-----------------+-----------+-----------+-------------+

\pandocend{footnotesize}



## ChillerPowerValidationPoint

\pandocbegin{footnotesize}

+------------------------------------+-----------------+-----------+-----------+-------------+
| **Name**                           | **Description** | **Data    | **Units** | **Notes**   |
|                                    |                 | Type**    |           |             |
+====================================+=================+===========+===========+=============+
| `chilled_water_supply_temperature` | Chilled water   | `Numeric` | C         | No name and |
|                                    | supply          |           |           | id is       |
|                                    | temperature     |           |           | needed      |
|                                    |                 |           |           | since used  |
|                                    |                 |           |           | as one of a |
|                                    |                 |           |           | series. The |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | is leaving  |
|                                    |                 |           |           | the         |
|                                    |                 |           |           | chiller.    |
+------------------------------------+-----------------+-----------+-----------+-------------+
| `condenser_temperature`            | Second          | `Numeric` | C         | Outside air |
|                                    | temperature     |           |           | dry-bulb    |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | for air     |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chillers    |
|                                    |                 |           |           | and         |
|                                    |                 |           |           | condenser   |
|                                    |                 |           |           | water       |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | for water   |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chillers.   |
|                                    |                 |           |           | For water   |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chillers,   |
|                                    |                 |           |           | this is the |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | as the      |
|                                    |                 |           |           | water       |
|                                    |                 |           |           | enters the  |
|                                    |                 |           |           | chiller.    |
|                                    |                 |           |           | For air     |
|                                    |                 |           |           | cooled      |
|                                    |                 |           |           | chilers     |
|                                    |                 |           |           | this the    |
|                                    |                 |           |           | temperature |
|                                    |                 |           |           | of the      |
|                                    |                 |           |           | ambient     |
|                                    |                 |           |           | air.        |
+------------------------------------+-----------------+-----------+-----------+-------------+
| `load`                             | Load            | `Numeric` | W         |             |
+------------------------------------+-----------------+-----------+-----------+-------------+
| `result`                           | Result          | `Numeric` | W         |             |
+------------------------------------+-----------------+-----------+-----------+-------------+

\pandocend{footnotesize}



## HeatRejection

\pandocbegin{footnotesize}

+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| **Name**                     | **Description** | **Data Type**                           | **Units** | **Req** | **Notes**   |
+==============================+=================+=========================================+===========+=========+=============+
| `id`                         | Scope-unique    | `ID`                                    |           | $✓$     |             |
|                              | reference       |                                         |           |         |             |
|                              | identifier for  |                                         |           |         |             |
|                              | instances of    |                                         |           |         |             |
|                              | this data group |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `reporting_name`             | Descriptive     | `String`                                |           |         |             |
|                              | name used in    |                                         |           |         |             |
|                              | RCT reports if  |                                         |           |         |             |
|                              | id is not       |                                         |           |         |             |
|                              | already a       |                                         |           |         |             |
|                              | descriptive     |                                         |           |         |             |
|                              | name            |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `notes`                      | Supplementary   | `String`                                |           |         |             |
|                              | information to  |                                         |           |         |             |
|                              | provide context |                                         |           |         |             |
|                              | to the model    |                                         |           |         |             |
|                              | reviewer        |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `loop`                       | Referenced to   | `$ID`                                   |           | $✓$     | Constraint  |
|                              | the fluid loop  |                                         |           |         | to use when |
|                              |                 |                                         |           |         | implemented |
|                              |                 |                                         |           |         | :FluidLoop: |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `type`                       | Heat Rejection  | `<HeatRejectionTypeOptions>`            |           |         |             |
|                              | Type            |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `fan_type`                   | Heat Rejection  | `<HeatRejectionFanTypeOptions>`         |           |         |             |
|                              | Fan Type        |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `fluid`                      | Fluid Cooled by | `<HeatRejectionFluidOptions>`           |           |         |             |
|                              | Heat Rejection  |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `range`                      | Heat rejection  | `Numeric`                               | C         |         |             |
|                              | Range           |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `approach`                   | Heat rejection  | `Numeric`                               | C         |         |             |
|                              | Approach        |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `reset_type`                 | Leaving         | `<HeatRejectionResetOptions>`           |           |         |             |
|                              | Temperature     |                                         |           |         |             |
|                              | reset strategy  |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `minimum_reset_temperature`  | Minimum leaving | `Numeric`                               | C         |         |             |
|                              | temperature     |                                         |           |         |             |
|                              | setpoint        |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `fan_power`                  | Fan Power       | `Numeric`                               | W         |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `fan_speed_control`          | Fan Speed       | `<HeatRejectionFanSpeedControlOptions>` |           |         |             |
|                              | Control Type    |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `design_supply_temperature`  | Design leaving  | `Numeric`                               | C         |         |             |
|                              | water           |                                         |           |         |             |
|                              | temperature     |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `design_wetbulb_temperature` | Design wetbulb  | `Numeric`                               | C         |         | 0.4% ASHRAE |
|                              | temperature     |                                         |           |         | MCWB        |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `design_water_flowrate`      | Design          | `Numeric`                               | L/s       |         |             |
|                              | condenser water |                                         |           |         |             |
|                              | flow rate       |                                         |           |         |             |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+
| `rated_water_flowrate`       | Rated condenser | `Numeric`                               | L/s       |         | At rating   |
|                              | water flow rate |                                         |           |         | conditions. |
+------------------------------+-----------------+-----------------------------------------+-----------+---------+-------------+

\pandocend{footnotesize}



## ExternalFluidSource

\pandocbegin{footnotesize}

+----------------------+-----------------+------------------------------------+---------+-------------+
| **Name**             | **Description** | **Data Type**                      | **Req** | **Notes**   |
+======================+=================+====================================+=========+=============+
| `id`                 | Scope-unique    | `ID`                               | $✓$     |             |
|                      | reference       |                                    |         |             |
|                      | identifier for  |                                    |         |             |
|                      | instances of    |                                    |         |             |
|                      | this data group |                                    |         |             |
+----------------------+-----------------+------------------------------------+---------+-------------+
| `reporting_name`     | Descriptive     | `String`                           |         |             |
|                      | name used in    |                                    |         |             |
|                      | RCT reports if  |                                    |         |             |
|                      | id is not       |                                    |         |             |
|                      | already a       |                                    |         |             |
|                      | descriptive     |                                    |         |             |
|                      | name            |                                    |         |             |
+----------------------+-----------------+------------------------------------+---------+-------------+
| `notes`              | Supplementary   | `String`                           |         |             |
|                      | information to  |                                    |         |             |
|                      | provide context |                                    |         |             |
|                      | to the model    |                                    |         |             |
|                      | reviewer        |                                    |         |             |
+----------------------+-----------------+------------------------------------+---------+-------------+
| `loop`               | Referenced to   | `$ID`                              | $✓$     | Constraint  |
|                      | the fluid loop  |                                    |         | to use when |
|                      |                 |                                    |         | implemented |
|                      |                 |                                    |         | :FluidLoop: |
+----------------------+-----------------+------------------------------------+---------+-------------+
| `type`               | Type of         | `<ExternalFluidSourceTypeOptions>` |         |             |
|                      | external fluid  |                                    |         |             |
|                      | source          |                                    |         |             |
+----------------------+-----------------+------------------------------------+---------+-------------+
| `energy_source_type` | Source of       | `<EnergySourceTypeOptions>`        |         |             |
|                      | energy for the  |                                    |         |             |
|                      | external fluid  |                                    |         |             |
|                      | source          |                                    |         |             |
+----------------------+-----------------+------------------------------------+---------+-------------+

\pandocend{footnotesize}



## ServiceWaterHeatingDistributionSystem

\pandocbegin{footnotesize}

+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| **Name**                                            | **Description** | **Data Type**                                            | **Units** | **Constraints** | **Req** | **Notes**    |
+=====================================================+=================+==========================================================+===========+=================+=========+==============+
| `id`                                                | Scope-unique    | `ID`                                                     |           |                 | $✓$     |              |
|                                                     | reference       |                                                          |           |                 |         |              |
|                                                     | identifier for  |                                                          |           |                 |         |              |
|                                                     | instances of    |                                                          |           |                 |         |              |
|                                                     | this data group |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `reporting_name`                                    | Descriptive     | `String`                                                 |           |                 |         |              |
|                                                     | name used in    |                                                          |           |                 |         |              |
|                                                     | RCT reports if  |                                                          |           |                 |         |              |
|                                                     | id is not       |                                                          |           |                 |         |              |
|                                                     | already a       |                                                          |           |                 |         |              |
|                                                     | descriptive     |                                                          |           |                 |         |              |
|                                                     | name            |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `notes`                                             | Supplementary   | `String`                                                 |           |                 |         |              |
|                                                     | information to  |                                                          |           |                 |         |              |
|                                                     | provide context |                                                          |           |                 |         |              |
|                                                     | to the model    |                                                          |           |                 |         |              |
|                                                     | reviewer        |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `design_supply_temperature`                         | Design supply   | `Numeric`                                                | C         |                 |         | From         |
|                                                     | temperature     |                                                          |           |                 |         | CBECC-Com.   |
|                                                     | setpoint of     |                                                          |           |                 |         |              |
|                                                     | service water   |                                                          |           |                 |         |              |
|                                                     | heating loop    |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `design_supply_temperature_difference`              | Design supply   | `Numeric`                                                | C         |                 |         | From         |
|                                                     | temperature     |                                                          |           |                 |         | CBECC-Com.   |
|                                                     | difference      |                                                          |           |                 |         |              |
|                                                     | (deltaT) of     |                                                          |           |                 |         |              |
|                                                     | service water   |                                                          |           |                 |         |              |
|                                                     | heating loop    |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `tanks`                                             | Tanks within    | `[{Tank}]`                                               |           |                 |         | Contains a   |
|                                                     | service water   |                                                          |           |                 |         | list of      |
|                                                     | heating         |                                                          |           |                 |         | storage      |
|                                                     | distribution    |                                                          |           |                 |         | tanks that   |
|                                                     | system          |                                                          |           |                 |         | are part of  |
|                                                     |                 |                                                          |           |                 |         | this service |
|                                                     |                 |                                                          |           |                 |         | water        |
|                                                     |                 |                                                          |           |                 |         | heating      |
|                                                     |                 |                                                          |           |                 |         | distribution |
|                                                     |                 |                                                          |           |                 |         | system but   |
|                                                     |                 |                                                          |           |                 |         | not part of  |
|                                                     |                 |                                                          |           |                 |         | individual   |
|                                                     |                 |                                                          |           |                 |         | service      |
|                                                     |                 |                                                          |           |                 |         | water        |
|                                                     |                 |                                                          |           |                 |         | heaters.     |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `is_central_system`                                 | Indicates       | `Boolean`                                                |           |                 |         | From         |
|                                                     | whether it is a |                                                          |           |                 |         | CBECC-Com.   |
|                                                     | central service |                                                          |           |                 |         |              |
|                                                     | water heater    |                                                          |           |                 |         |              |
|                                                     | distribution    |                                                          |           |                 |         |              |
|                                                     | system          |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `service_water_piping`                              | Other service   | `[{ServiceWaterPiping}]`                                 |           |                 |         |              |
|                                                     | water piping    |                                                          |           |                 |         |              |
|                                                     | connected to    |                                                          |           |                 |         |              |
|                                                     | this one as     |                                                          |           |                 |         |              |
|                                                     | children.       |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `distribution_compactness`                          | Type of compact | `<ServiceWaterHeatingDistributionCompactness2019T24Com>` |           |                 |         | From         |
|                                                     | distribution    |                                                          |           |                 |         | CBECC-Com.   |
|                                                     | system          |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `control_type`                                      | Type of         | `<ServiceWaterHeatingControlType2019T24Com>`             |           |                 |         | From         |
|                                                     | distribution    |                                                          |           |                 |         | CBECC-Com.   |
|                                                     | system          |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `configuration_type`                                | Type of         | `<ServiceWaterHeatingConfigurationType>`                 |           |                 |         | From         |
|                                                     | configuration   |                                                          |           |                 |         | CBECC-Com.   |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `is_recovered_heat_from_drain_used_by_water_heater` | Indicates       | `Boolean`                                                |           |                 |         | From         |
|                                                     | whether the     |                                                          |           |                 |         | CBECC-Res.   |
|                                                     | recovered heat  |                                                          |           |                 |         |              |
|                                                     | from the shower |                                                          |           |                 |         |              |
|                                                     | drain used by   |                                                          |           |                 |         |              |
|                                                     | the service     |                                                          |           |                 |         |              |
|                                                     | water heater    |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `drain_heat_recovery_efficiency`                    | Shower heat     | `Numeric`                                                | m         | `≥0`            |         | From         |
|                                                     | drain recovery  |                                                          |           |                 |         | CBECC-Com.   |
|                                                     | efficiency      |                                                          |           |                 |         | May use the  |
|                                                     |                 |                                                          |           |                 |         | Canadian     |
|                                                     |                 |                                                          |           |                 |         | Standards    |
|                                                     |                 |                                                          |           |                 |         | Association  |
|                                                     |                 |                                                          |           |                 |         | Rated        |
|                                                     |                 |                                                          |           |                 |         | Recovery     |
|                                                     |                 |                                                          |           |                 |         | Efficiency.  |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `drain_heat_recovery_type`                          | Drain heat      | `<ServiceWaterHeatingHeatRecoveryType>`                  |           |                 |         | From         |
|                                                     | recovery type   |                                                          |           |                 |         | CBECC-Res.   |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `flow_multiplier_schedule`                          | service water   | `$ID`                                                    |           |                 |         | Constraint   |
|                                                     | heating Loop    |                                                          |           |                 |         | to use when  |
|                                                     | flow muliplier  |                                                          |           |                 |         | implemented  |
|                                                     | schedule name   |                                                          |           |                 |         | :Schedule:   |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `entering_water_mains_temperature_schedule`         | Temperature     | `$ID`                                                    |           |                 |         | Constraint   |
|                                                     | schedule for    |                                                          |           |                 |         | to use when  |
|                                                     | unheated        |                                                          |           |                 |         | implemented  |
|                                                     | entering water  |                                                          |           |                 |         | :Schedule:   |
|                                                     | to the building |                                                          |           |                 |         |              |
|                                                     | site often      |                                                          |           |                 |         |              |
|                                                     | referenced as   |                                                          |           |                 |         |              |
|                                                     | mains           |                                                          |           |                 |         |              |
|                                                     | temperature.    |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+
| `is_ground_temperature_used_for_entering_water`     | Indicates       | `Boolean`                                                |           |                 |         |              |
|                                                     | whether ground  |                                                          |           |                 |         |              |
|                                                     | temperature is  |                                                          |           |                 |         |              |
|                                                     | the source of   |                                                          |           |                 |         |              |
|                                                     | the entering    |                                                          |           |                 |         |              |
|                                                     | water           |                                                          |           |                 |         |              |
|                                                     | temperature     |                                                          |           |                 |         |              |
+-----------------------------------------------------+-----------------+----------------------------------------------------------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



## ServiceWaterPiping

\pandocbegin{footnotesize}

+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| **Name**                     | **Description**   | **Data Type**            | **Units** | **Constraints** | **Req** | **Notes**   |
+==============================+===================+==========================+===========+=================+=========+=============+
| `id`                         | Scope-unique      | `ID`                     |           |                 | $✓$     |             |
|                              | reference         |                          |           |                 |         |             |
|                              | identifier for    |                          |           |                 |         |             |
|                              | instances of this |                          |           |                 |         |             |
|                              | data group        |                          |           |                 |         |             |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `reporting_name`             | Descriptive name  | `String`                 |           |                 |         |             |
|                              | used in RCT       |                          |           |                 |         |             |
|                              | reports if id is  |                          |           |                 |         |             |
|                              | not already a     |                          |           |                 |         |             |
|                              | descriptive name  |                          |           |                 |         |             |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `notes`                      | Supplementary     | `String`                 |           |                 |         |             |
|                              | information to    |                          |           |                 |         |             |
|                              | provide context   |                          |           |                 |         |             |
|                              | to the model      |                          |           |                 |         |             |
|                              | reviewer          |                          |           |                 |         |             |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `is_recirculation_loop`      | Indicates if      | `Boolean`                |           |                 |         |             |
|                              | service water     |                          |           |                 |         |             |
|                              | heating piping is |                          |           |                 |         |             |
|                              | a loop and        |                          |           |                 |         |             |
|                              | recirculates      |                          |           |                 |         |             |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `insulation_thickness`       | Pipe insulation   | `Numeric`                | m         | `≥0`            |         | From        |
|                              | thickness         |                          |           |                 |         | CBECC-Com.  |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `loop_pipe_location`         | Loop pipe         | `<ComponentLocation>`    |           |                 |         | From        |
|                              | location          |                          |           |                 |         | CBECC-Com.  |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `zone_location`              | Zone reference of | `$ID`                    |           |                 |         | From        |
|                              | where the         |                          |           |                 |         | CBECC-Com.  |
|                              | component is      |                          |           |                 |         | Constraint  |
|                              | located when      |                          |           |                 |         | to use when |
|                              | IN_ZONE is        |                          |           |                 |         | implemented |
|                              | selected from     |                          |           |                 |         | :Zone:      |
|                              | ComponentLocation |                          |           |                 |         |             |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `length`                     | Pipe length       | `Numeric`                | m         | `≥0`            |         | From RESNET |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `diameter`                   | Pipe section      | `Numeric`                | m         | `≥0`            |         | From        |
|                              | diameter          |                          |           |                 |         | CBECC-Res.  |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+
| `child_service_water_piping` | Other service     | `[{ServiceWaterPiping}]` |           |                 |         |             |
|                              | water piping      |                          |           |                 |         |             |
|                              | connected to this |                          |           |                 |         |             |
|                              | one as children.  |                          |           |                 |         |             |
+------------------------------+-------------------+--------------------------+-----------+-----------------+---------+-------------+

\pandocend{footnotesize}



## SolarThermal

\pandocbegin{footnotesize}

+------------------------------+-----------------+-----------+---------+------------+
| **Name**                     | **Description** | **Data    | **Req** | **Notes**  |
|                              |                 | Type**    |         |            |
+==============================+=================+===========+=========+============+
| `id`                         | Scope-unique    | `ID`      | $✓$     |            |
|                              | reference       |           |         |            |
|                              | identifier for  |           |         |            |
|                              | instances of    |           |         |            |
|                              | this data group |           |         |            |
+------------------------------+-----------------+-----------+---------+------------+
| `reporting_name`             | Descriptive     | `String`  |         |            |
|                              | name used in    |           |         |            |
|                              | RCT reports if  |           |         |            |
|                              | id is not       |           |         |            |
|                              | already a       |           |         |            |
|                              | descriptive     |           |         |            |
|                              | name            |           |         |            |
+------------------------------+-----------------+-----------+---------+------------+
| `notes`                      | Supplementary   | `String`  |         |            |
|                              | information to  |           |         |            |
|                              | provide context |           |         |            |
|                              | to the model    |           |         |            |
|                              | reviewer        |           |         |            |
+------------------------------+-----------------+-----------+---------+------------+
| `angle_from_true_north`      | Solar heater    | `Numeric` |         | From       |
|                              | angle from true |           |         | CBECC-Com. |
|                              | north,          |           |         |            |
|                              | clockwise       |           |         |            |
+------------------------------+-----------------+-----------+---------+------------+
| `solar_savings_fraction`     | Solar savings   | `Numeric` |         | Based on   |
|                              | fraction        |           |         | ICC-SRCC   |
|                              |                 |           |         | rating.    |
|                              |                 |           |         | From       |
|                              |                 |           |         | CBECC-Com. |
+------------------------------+-----------------+-----------+---------+------------+
| `collector_area`             | Solar collector | `Numeric` |         | From       |
|                              | area            |           |         | CBECC-Com. |
+------------------------------+-----------------+-----------+---------+------------+
| `collector_type_description` | Description of  | `String`  |         | From       |
|                              | solar collector |           |         | CBECC-Com. |
|                              | type            |           |         |            |
+------------------------------+-----------------+-----------+---------+------------+
| `collector_slope`            | Solar slope     | `Numeric` |         | From       |
|                              | from horizontal |           |         | CBECC-Com. |
+------------------------------+-----------------+-----------+---------+------------+
| `tank`                       | Tank that is    | `{Tank}`  |         | Contains a |
|                              | part of the     |           |         | storage    |
|                              | solar thermal   |           |         | tank that  |
|                              | system          |           |         | is part of |
|                              |                 |           |         | the solar  |
|                              |                 |           |         | thermal    |
|                              |                 |           |         | system.    |
+------------------------------+-----------------+-----------+---------+------------+

\pandocend{footnotesize}



## ServiceWaterHeatingEquipment

\pandocbegin{footnotesize}

+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| **Name**                                    | **Description** | **Data Type**                                    | **Units** | **Constraints** | **Req** | **Notes**                               |
+=============================================+=================+==================================================+===========+=================+=========+=========================================+
| `id`                                        | Scope-unique    | `ID`                                             |           |                 | $✓$     |                                         |
|                                             | reference       |                                                  |           |                 |         |                                         |
|                                             | identifier for  |                                                  |           |                 |         |                                         |
|                                             | instances of    |                                                  |           |                 |         |                                         |
|                                             | this data group |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `reporting_name`                            | Descriptive     | `String`                                         |           |                 |         |                                         |
|                                             | name used in    |                                                  |           |                 |         |                                         |
|                                             | RCT reports if  |                                                  |           |                 |         |                                         |
|                                             | id is not       |                                                  |           |                 |         |                                         |
|                                             | already a       |                                                  |           |                 |         |                                         |
|                                             | descriptive     |                                                  |           |                 |         |                                         |
|                                             | name            |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `notes`                                     | Supplementary   | `String`                                         |           |                 |         |                                         |
|                                             | information to  |                                                  |           |                 |         |                                         |
|                                             | provide context |                                                  |           |                 |         |                                         |
|                                             | to the model    |                                                  |           |                 |         |                                         |
|                                             | reviewer        |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `heater_fuel_type`                          | Service water   | `<EnergySourceTypeOptions>`                      |           |                 |         |                                         |
|                                             | heating heater  |                                                  |           |                 |         |                                         |
|                                             | fuel type       |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `service_water_heating_distribution_system` | Referenced to   | `$ID`                                            |           |                 | $✓$     | Constraint to use when implemented      |
|                                             | the service     |                                                  |           |                 |         | :ServiceWaterHeatingDistributionSystem: |
|                                             | water heating   |                                                  |           |                 |         |                                         |
|                                             | distribution    |                                                  |           |                 |         |                                         |
|                                             | system          |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `energy_factor`                             | Energy factor   | `Numeric`                                        |           | `≥0`            |         | From CBECC-Com.                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `thermal_efficiency`                        | Service water   | `Numeric`                                        |           | `≥0`            |         |                                         |
|                                             | heating heater  |                                                  |           |                 |         |                                         |
|                                             | thermal         |                                                  |           |                 |         |                                         |
|                                             | efficiency      |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `standby_loss_fraction`                     | Standby loss    | `Numeric`                                        |           |                 |         | From CBECC-Com.                         |
|                                             | fraction        |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `uniform_energy_factor`                     | Uniform energy  | `Numeric`                                        |           | `≥0`            |         | From CBECC-Com.                         |
|                                             | factor          |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `first_hour_rating`                         | First hour      | `Numeric`                                        | L         | `≥0`            |         | From CBECC-Com.                         |
|                                             | rating volume   |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `output_validation_points`                  | Capacity        | `[{ServiceWaterHeaterValidationPoint}]`          |           |                 |         |                                         |
|                                             | validation      |                                                  |           |                 |         |                                         |
|                                             | points          |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `input_power`                               | Input power     | `Numeric`                                        | W         | `≥0`            |         | From CBECC-Com.                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `rated_capacity`                            | Rated capacity  | `Numeric`                                        | W         |                 |         | From CBECC-Com.                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `minimum_capacity`                          | Minimum         | `Numeric`                                        | W         | `≥0`            |         | From CBECC-Com.                         |
|                                             | capacity        |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `recovery_efficiency`                       | Recovery        | `Numeric`                                        |           |                 |         | From CBECC-Com.                         |
|                                             | efficiency      |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `setpoint_temperature`                      | Set point       | `Numeric`                                        | C         |                 |         |                                         |
|                                             | temperature     |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `compressor_location`                       | Description of  | `String`                                         |           |                 |         | Used when compressor is not located in  |
|                                             | where the heat  |                                                  |           |                 |         | a specific zone. From CBECC-Com.        |
|                                             | pump for the    |                                                  |           |                 |         |                                         |
|                                             | water heater is |                                                  |           |                 |         |                                         |
|                                             | located         |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `compressor_zone`                           | Zone reference  | `$ID`                                            |           |                 |         | From CBECC-Com. Constraint to use when  |
|                                             | of where the    |                                                  |           |                 |         | implemented :Zone:                      |
|                                             | heat pump for   |                                                  |           |                 |         |                                         |
|                                             | the water       |                                                  |           |                 |         |                                         |
|                                             | heater is       |                                                  |           |                 |         |                                         |
|                                             | located         |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `compressor_heat_rejection_source`          | Heat pump heat  | `<ComponentLocation>`                            |           |                 |         | From CBECC-Res.                         |
|                                             | rejection       |                                                  |           |                 |         |                                         |
|                                             | source          |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `compressor_heat_rejection_zone`            | Heat pump heat  | `$ID`                                            |           |                 |         | From CBECC-Res. Constraint to use when  |
|                                             | rejection zone  |                                                  |           |                 |         | implemented :Zone:                      |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `compressor_capacity_validation_points`     | Capacity        | `[{HeatPumpWaterHeaterCapacityValidationPoint}]` |           |                 |         |                                         |
|                                             | validation      |                                                  |           |                 |         |                                         |
|                                             | points          |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `compressor_power_validation_points`        | Coefficient of  | `[{HeatPumpWaterHeaterPowerValidationPoint}]`    |           |                 |         |                                         |
|                                             | performance     |                                                  |           |                 |         |                                         |
|                                             | validation      |                                                  |           |                 |         |                                         |
|                                             | points          |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `draft_fan_power`                           | Power for the   | `Numeric`                                        | W         | `≥0`            |         | From CBECC-Com.                         |
|                                             | draft fan       |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `has_electrical_ignition`                   | Indicates       | `Boolean`                                        |           |                 |         | From CBECC-Com.                         |
|                                             | whether the     |                                                  |           |                 |         |                                         |
|                                             | water heater    |                                                  |           |                 |         |                                         |
|                                             | has electrical  |                                                  |           |                 |         |                                         |
|                                             | ignition        |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `heater_type`                               | Service water   | `<ServiceWaterHeaterType>`                       |           |                 |         |                                         |
|                                             | heater type     |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `tank`                                      | Tank that is    | `{Tank}`                                         |           |                 |         | Contains a storage tank that is part of |
|                                             | part of the     |                                                  |           |                 |         | the service water heating equipment.    |
|                                             | service water   |                                                  |           |                 |         |                                         |
|                                             | heating         |                                                  |           |                 |         |                                         |
|                                             | equipment       |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `status_type`                               | Choice of new,  | `<GeneralStatusType2019T24>`                     |           |                 |         |                                         |
|                                             | existing,       |                                                  |           |                 |         |                                         |
|                                             | addition,       |                                                  |           |                 |         |                                         |
|                                             | alteration,     |                                                  |           |                 |         |                                         |
|                                             | etc. for each   |                                                  |           |                 |         |                                         |
|                                             | ruleset.        |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+
| `solar_thermal_systems`                     | Solar thermal   | `[{SolarThermal}]`                               |           |                 |         | Contains a list of Solar thermal        |
|                                             | systems used    |                                                  |           |                 |         | systems that are part of this service   |
|                                             | for heating     |                                                  |           |                 |         | water heating distribution system.      |
|                                             | service water   |                                                  |           |                 |         |                                         |
+---------------------------------------------+-----------------+--------------------------------------------------+-----------+-----------------+---------+-----------------------------------------+

\pandocend{footnotesize}



## ServiceWaterHeaterValidationPoint

\pandocbegin{footnotesize}

+----------+-----------------+-----------+-----------+-----------+
| **Name** | **Description** | **Data    | **Units** | **Notes** |
|          |                 | Type**    |           |           |
+==========+=================+===========+===========+===========+
| `load`   | Load            | `Numeric` | W         | No name   |
|          |                 |           |           | and id is |
|          |                 |           |           | needed    |
|          |                 |           |           | since     |
|          |                 |           |           | typically |
|          |                 |           |           | used as   |
|          |                 |           |           | one of a  |
|          |                 |           |           | series.   |
+----------+-----------------+-----------+-----------+-----------+
| `result` | Result          | `Numeric` | W         |           |
+----------+-----------------+-----------+-----------+-----------+

\pandocend{footnotesize}



## HeatPumpWaterHeaterCapacityValidationPoint

\pandocbegin{footnotesize}

+-------------------------------+-----------------+-----------+-----------+-----------+
| **Name**                      | **Description** | **Data    | **Units** | **Notes** |
|                               |                 | Type**    |           |           |
+===============================+=================+===========+===========+===========+
| `evaporator_air_temperature`  | Outside dry     | `Numeric` | C         | No name   |
|                               | bulb            |           |           | and id is |
|                               | temperatures of |           |           | needed    |
|                               | air             |           |           | since     |
|                               |                 |           |           | used as   |
|                               |                 |           |           | one of a  |
|                               |                 |           |           | series.   |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `condenser_water_temperature` | Entering        | `Numeric` | C         |           |
|                               | condenser       |           |           |           |
|                               | temperature of  |           |           |           |
|                               | water           |           |           |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `evaporator_air_flow`         | Air flow across | `Numeric` | L/s       |           |
|                               | evaporator      |           |           |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `condenser_water_flow`        | Water flow      | `Numeric` | L/s       |           |
|                               | across          |           |           |           |
|                               | condenser       |           |           |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `result`                      | Result          | `Numeric` | W         |           |
+-------------------------------+-----------------+-----------+-----------+-----------+

\pandocend{footnotesize}



## HeatPumpWaterHeaterPowerValidationPoint

\pandocbegin{footnotesize}

+-------------------------------+-----------------+-----------+-----------+-----------+
| **Name**                      | **Description** | **Data    | **Units** | **Notes** |
|                               |                 | Type**    |           |           |
+===============================+=================+===========+===========+===========+
| `evaporator_air_temperature`  | Outside dry     | `Numeric` | C         | No name   |
|                               | bulb            |           |           | and id is |
|                               | temperatures of |           |           | needed    |
|                               | air             |           |           | since     |
|                               |                 |           |           | used as   |
|                               |                 |           |           | one of a  |
|                               |                 |           |           | series.   |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `condenser_water_temperature` | Entering        | `Numeric` | C         |           |
|                               | condenser       |           |           |           |
|                               | temperature of  |           |           |           |
|                               | water           |           |           |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `evaporator_air_flow`         | Air flow across | `Numeric` | L/s       |           |
|                               | evaporator      |           |           |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `condenser_water_flow`        | Water flow      | `Numeric` | L/s       |           |
|                               | across          |           |           |           |
|                               | condenser       |           |           |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `load`                        | Load            | `Numeric` | W         |           |
+-------------------------------+-----------------+-----------+-----------+-----------+
| `result`                      | Result          | `Numeric` | W         |           |
+-------------------------------+-----------------+-----------+-----------+-----------+

\pandocend{footnotesize}



## Tank

\pandocbegin{footnotesize}

+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| **Name**              | **Description** | **Data Type**                  | **Units**      | **Constraints** | **Req** | **Notes**     |
+=======================+=================+================================+================+=================+=========+===============+
| `id`                  | Scope-unique    | `ID`                           |                |                 | $✓$     |               |
|                       | reference       |                                |                |                 |         |               |
|                       | identifier for  |                                |                |                 |         |               |
|                       | instances of    |                                |                |                 |         |               |
|                       | this data group |                                |                |                 |         |               |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `reporting_name`      | Descriptive     | `String`                       |                |                 |         |               |
|                       | name used in    |                                |                |                 |         |               |
|                       | RCT reports if  |                                |                |                 |         |               |
|                       | id is not       |                                |                |                 |         |               |
|                       | already a       |                                |                |                 |         |               |
|                       | descriptive     |                                |                |                 |         |               |
|                       | name            |                                |                |                 |         |               |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `notes`               | Supplementary   | `String`                       |                |                 |         |               |
|                       | information to  |                                |                |                 |         |               |
|                       | provide context |                                |                |                 |         |               |
|                       | to the model    |                                |                |                 |         |               |
|                       | reviewer        |                                |                |                 |         |               |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `storage_capacity`    | Storage         | `Numeric`                      | L              | `≥0`            |         | From          |
|                       | capacity of     |                                |                |                 |         | CBECC-Com.    |
|                       | tank in         |                                |                |                 |         |               |
|                       | distribution    |                                |                |                 |         |               |
|                       | system          |                                |                |                 |         |               |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `type`                | Service water   | `<ServiceWaterHeaterTankType>` |                |                 |         |               |
|                       | heater tank     |                                |                |                 |         |               |
|                       | type            |                                |                |                 |         |               |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `height`              | Tank height     | `Numeric`                      | m              | `≥0`            |         | From          |
|                       |                 |                                |                |                 |         | CBECC-Com.    |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `interior_insulation` | Tank interior   | `Numeric`                      | K$\cdot$m^2^/W | `≥0`            |         | Insulation    |
|                       | insulation      |                                |                |                 |         | that is part  |
|                       | R-value         |                                |                |                 |         | of the tank   |
|                       |                 |                                |                |                 |         | and is inside |
|                       |                 |                                |                |                 |         | of the        |
|                       |                 |                                |                |                 |         | housing. From |
|                       |                 |                                |                |                 |         | CBECC-Res.    |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `exterior_insulation` | Tank interior   | `Numeric`                      | K$\cdot$m^2^/W | `≥0`            |         | A blanket of  |
|                       | insulation      |                                |                |                 |         | insulation    |
|                       | R-value         |                                |                |                 |         | that          |
|                       |                 |                                |                |                 |         | surrounds the |
|                       |                 |                                |                |                 |         | exterior of   |
|                       |                 |                                |                |                 |         | the tank.     |
|                       |                 |                                |                |                 |         | From          |
|                       |                 |                                |                |                 |         | CBECC-Res.    |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `location`            | Location        | `<ComponentLocation>`          |                |                 |         | From          |
|                       |                 |                                |                |                 |         | CBECC-Res.    |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+
| `location_zone`       | Tank zone       | `$ID`                          |                |                 |         | Only used     |
|                       | location        |                                |                |                 |         | when          |
|                       |                 |                                |                |                 |         | tank_location |
|                       |                 |                                |                |                 |         | indicates the |
|                       |                 |                                |                |                 |         | tank is       |
|                       |                 |                                |                |                 |         | located in a  |
|                       |                 |                                |                |                 |         | zone. From    |
|                       |                 |                                |                |                 |         | CBECC-Res.    |
|                       |                 |                                |                |                 |         | Constraint to |
|                       |                 |                                |                |                 |         | use when      |
|                       |                 |                                |                |                 |         | implemented   |
|                       |                 |                                |                |                 |         | :Zone:        |
+-----------------------+-----------------+--------------------------------+----------------+-----------------+---------+---------------+

\pandocend{footnotesize}



## ServiceWaterHeatingUse

\pandocbegin{footnotesize}

+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| **Name**                                   | **Description**                       | **Data Type**                                 | **Units** | **Req** | **Notes**                               |
+============================================+=======================================+===============================================+===========+=========+=========================================+
| `id`                                       | Scope-unique reference identifier for | `ID`                                          |           | $✓$     |                                         |
|                                            | instances of this data group          |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `reporting_name`                           | Descriptive name used in RCT reports  | `String`                                      |           |         |                                         |
|                                            | if id is not already a descriptive    |                                               |           |         |                                         |
|                                            | name                                  |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `notes`                                    | Supplementary information to provide  | `String`                                      |           |         |                                         |
|                                            | context to the model reviewer         |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `area_type`                                | Service Water Heating Loop Area Type  | `<ServiceWaterHeatingSpaceType2019ASHRAE901>` |           |         | The enumeration is based on the         |
|                                            |                                       |                                               |           |         | standard used.                          |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `water_serves_type`                        | The use of the water serves the type  | `<ServiceWaterHeatingFixtureType>`            |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `served_by_distribution_system`            | ID fo the                             | `$ID`                                         |           |         | From CBECC-Res. Constraint to use when  |
|                                            | ServiceWaterHeatingDistributionSystem |                                               |           |         | implemented                             |
|                                            | that serves this end use              |                                               |           |         | :ServiceWaterHeatingDistributionSystem: |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `use`                                      | Usage of service hot water            | `Numeric`                                     |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `use_units`                                | Type of units for use of service hot  | `<ServiceWaterHeatingUseUnits>`               |           |         |                                         |
|                                            | water                                 |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `use_multiplier_schedule`                  | Reference to the schedule containing  | `$ID`                                         |           | $✓$     | Constraint to use when implemented      |
|                                            | the multiplier for the use of service |                                               |           |         | :Schedule:                              |
|                                            | hot water                             |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `temperature_at_fixture`                   | Reference to the schedule containing  | `Numeric`                                     | C         |         | From RESNET                             |
|                                            | the multiplier for the use of service |                                               |           |         |                                         |
|                                            | hot water                             |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `is_heat_recovered_by_drain`               | Indicates if heat is being recovered  | `Boolean`                                     |           |         | From CBECC-Res.                         |
|                                            | from the drain                        |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+
| `is_recovered_heat_used_by_cold_side_feed` | Indicates if heat is being recovered  | `Boolean`                                     |           |         | From CBECC-Res.                         |
|                                            | from the drain is used on the cold    |                                               |           |         |                                         |
|                                            | side feed                             |                                               |           |         |                                         |
+--------------------------------------------+---------------------------------------+-----------------------------------------------+-----------+---------+-----------------------------------------+

\pandocend{footnotesize}



## ExteriorLighting

\pandocbegin{footnotesize}

+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| **Name**         | **Description** | **Data Type**                                  | **Units** | **Constraints** | **Req** | **Notes**  |
+==================+=================+================================================+===========+=================+=========+============+
| `id`             | Scope-unique    | `ID`                                           |           |                 | $✓$     |            |
|                  | reference       |                                                |           |                 |         |            |
|                  | identifier for  |                                                |           |                 |         |            |
|                  | instances of    |                                                |           |                 |         |            |
|                  | this data group |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `reporting_name` | Descriptive     | `String`                                       |           |                 |         |            |
|                  | name used in    |                                                |           |                 |         |            |
|                  | RCT reports if  |                                                |           |                 |         |            |
|                  | id is not       |                                                |           |                 |         |            |
|                  | already a       |                                                |           |                 |         |            |
|                  | descriptive     |                                                |           |                 |         |            |
|                  | name            |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `notes`          | Supplementary   | `String`                                       |           |                 |         |            |
|                  | information to  |                                                |           |                 |         |            |
|                  | provide context |                                                |           |                 |         |            |
|                  | to the model    |                                                |           |                 |         |            |
|                  | reviewer        |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `type`           | The type of     | `<ExteriorLightingAreas2019ASHRAE901TableG36>` |           |                 |         |            |
|                  | exterior        |                                                |           |                 |         |            |
|                  | lighting        |                                                |           |                 |         |            |
|                  | fixture	none    |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `area`           | Area of the     | `Numeric`                                      | m^2^      | `>0`            |         |            |
|                  | exterior        |                                                |           |                 |         |            |
|                  | functional      |                                                |           |                 |         |            |
|                  | space.          |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `length`         | Linear length   | `Numeric`                                      | m         | `≥0`            |         | For        |
|                  | measure for     |                                                |           |                 |         | example,   |
|                  | exterior        |                                                |           |                 |         | used when  |
|                  | functional      |                                                |           |                 |         | expressing |
|                  | space           |                                                |           |                 |         | street     |
|                  |                 |                                                |           |                 |         | frontage   |
|                  |                 |                                                |           |                 |         | or door    |
|                  |                 |                                                |           |                 |         | width      |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `power`          | Nominal power   | `Numeric`                                      | W         | `>0`            |         |            |
|                  | of exterior     |                                                |           |                 |         |            |
|                  | lighting        |                                                |           |                 |         |            |
|                  | fixtures        |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+
| `fixture_height` | Installation    | `Numeric`                                      | m         | `>0`            |         |            |
|                  | height of       |                                                |           |                 |         |            |
|                  | exterior        |                                                |           |                 |         |            |
|                  | fixture         |                                                |           |                 |         |            |
+------------------+-----------------+------------------------------------------------+-----------+-----------------+---------+------------+

\pandocend{footnotesize}



## Refrigeration

\pandocbegin{footnotesize}

+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| **Name**                    | **Description** | **Data Type**                  | **Units** | **Constraints** | **Req** | **Notes**       |
+=============================+=================+================================+===========+=================+=========+=================+
| `id`                        | Scope-unique    | `ID`                           |           |                 | $✓$     |                 |
|                             | reference       |                                |           |                 |         |                 |
|                             | identifier for  |                                |           |                 |         |                 |
|                             | instances of    |                                |           |                 |         |                 |
|                             | this data group |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `reporting_name`            | Descriptive     | `String`                       |           |                 |         |                 |
|                             | name used in    |                                |           |                 |         |                 |
|                             | RCT reports if  |                                |           |                 |         |                 |
|                             | id is not       |                                |           |                 |         |                 |
|                             | already a       |                                |           |                 |         |                 |
|                             | descriptive     |                                |           |                 |         |                 |
|                             | name            |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `notes`                     | Supplementary   | `String`                       |           |                 |         |                 |
|                             | information to  |                                |           |                 |         |                 |
|                             | provide context |                                |           |                 |         |                 |
|                             | to the model    |                                |           |                 |         |                 |
|                             | reviewer        |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `type`                      | Refrigeration   | `<RefrigerationType>`          |           |                 |         |                 |
|                             | equipment type  |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `equipment_category`        | Equipment Class | `<RefrigerationCategory>`      |           |                 |         |                 |
|                             | from referenced |                                |           |                 |         |                 |
|                             | standard        |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `is_self_contained`         | Indicates       | `Boolean`                      |           |                 |         | If not          |
|                             | whether unit is |                                |           |                 |         | self-contained, |
|                             | self-contained  |                                |           |                 |         | show as false,  |
|                             |                 |                                |           |                 |         | and indicates   |
|                             |                 |                                |           |                 |         | that it has     |
|                             |                 |                                |           |                 |         | remote          |
|                             |                 |                                |           |                 |         | condenser       |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `application_temperature`   | Equipment       | `<ApplicationTemperatureType>` |           |                 |         | Based on AHRI   |
|                             | application     |                                |           |                 |         | 1200            |
|                             | temperature     |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `power`                     | Nominal power   | `Numeric`                      | W         | `>0`            |         |                 |
|                             | of              |                                |           |                 |         |                 |
|                             | refrigeration   |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `power_multiplier_schedule` | Refrigeration   | `$ID`                          |           |                 |         | Constraint to   |
|                             | power           |                                |           |                 |         | use when        |
|                             | multiplier      |                                |           |                 |         | implemented     |
|                             | schedule name   |                                |           |                 |         | :Schedule:      |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `sensible_fraction`         | Fraction of     | `Numeric`                      |           | `≥-1, ≤1`       |         |                 |
|                             | energy that is  |                                |           |                 |         |                 |
|                             | a sensible load |                                |           |                 |         |                 |
|                             | on the space.   |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `heat_gain_fraction`        | Fraction of     | `Numeric`                      |           | `≥-1, ≤1`       |         |                 |
|                             | energy that is  |                                |           |                 |         |                 |
|                             | a heat gain to  |                                |           |                 |         |                 |
|                             | the space.      |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `case_volume`               | volume of a     | `Numeric`                      | m^3^      |                 |         |                 |
|                             | refrigerated    |                                |           |                 |         |                 |
|                             | case in cubic   |                                |           |                 |         |                 |
|                             | meters          |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `total_display_area`        | display area of | `Numeric`                      | m^2^      |                 |         |                 |
|                             | a refrigerated  |                                |           |                 |         |                 |
|                             | case in square  |                                |           |                 |         |                 |
|                             | meters          |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+
| `zone_case_location`        | Zone where case | `$ID`                          |           |                 |         |                 |
|                             | is located      |                                |           |                 |         |                 |
+-----------------------------+-----------------+--------------------------------+-----------+-----------------+---------+-----------------+

\pandocend{footnotesize}



## OverallSimulationOutputs

\pandocbegin{footnotesize}

+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| **Name**                                          | **Description** | **Data    | **Units** | **Constraints** | **Req** | **Notes**    |
|                                                   |                 | Type**    |           |                 |         |              |
+===================================================+=================+===========+===========+=================+=========+==============+
| `id`                                              | Scope-unique    | `ID`      |           |                 | $✓$     |              |
|                                                   | reference       |           |           |                 |         |              |
|                                                   | identifier for  |           |           |                 |         |              |
|                                                   | instances of    |           |           |                 |         |              |
|                                                   | this data group |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `reporting_name`                                  | Descriptive     | `String`  |           |                 |         |              |
|                                                   | name used in    |           |           |                 |         |              |
|                                                   | RCT reports if  |           |           |                 |         |              |
|                                                   | id is not       |           |           |                 |         |              |
|                                                   | already a       |           |           |                 |         |              |
|                                                   | descriptive     |           |           |                 |         |              |
|                                                   | name            |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `notes`                                           | Supplementary   | `String`  |           |                 |         |              |
|                                                   | information to  |           |           |                 |         |              |
|                                                   | provide context |           |           |                 |         |              |
|                                                   | to the model    |           |           |                 |         |              |
|                                                   | reviewer        |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `refrigeration_energy_enduse`                     | Annual          | `Numeric` | kWh       |                 |         |              |
|                                                   | refrigeration   |           |           |                 |         |              |
|                                                   | energy end use  |           |           |                 |         |              |
|                                                   | from simulation |           |           |                 |         |              |
|                                                   | output          |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `service_water_heating_annual_enduse_electricity` | Annual          | `Numeric` | kWh       | `≥0`            |         |              |
|                                                   | electricity     |           |           |                 |         |              |
|                                                   | energy end_use  |           |           |                 |         |              |
|                                                   | for SWH loops   |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `service_water_heating_annual_enduse_fossilfuel`  | Annual fossil   | `Numeric` | J         | `≥0`            |         |              |
|                                                   | fuel energy     |           |           |                 |         |              |
|                                                   | end_use for SWH |           |           |                 |         |              |
|                                                   | loops           |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `unmet_heating_load_hours`                        | total hours any | `Numeric` | J         | `≥0`            |         | JG to verify |
|                                                   | HVAC Zone       |           |           |                 |         | if used in   |
|                                                   | heating         |           |           |                 |         | test case    |
|                                                   | temperature     |           |           |                 |         | description. |
|                                                   | setpoint not    |           |           |                 |         |              |
|                                                   | met             |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+
| `unmet_cooling_load_hours`                        | total hours any | `Numeric` | J         | `≥0`            |         | JG to verify |
|                                                   | HVAC Zone       |           |           |                 |         | if used in   |
|                                                   | cooling         |           |           |                 |         | test case    |
|                                                   | temperature     |           |           |                 |         | description. |
|                                                   | setpoint not    |           |           |                 |         |              |
|                                                   | met             |           |           |                 |         |              |
+---------------------------------------------------+-----------------+-----------+-----------+-----------------+---------+--------------+

\pandocend{footnotesize}



