# Data Types
| Data Type |                                                           Description                                                           | JSON Schema Type |          Examples           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------|
| `Integer` | A positive or negative whole number (i.e., a number that can be written without a fractional part).                             | integer          | 3, 19, -4                   |
| `Numeric` | A number that may include a fractional part with optional leading sign and optional exponent (engineering notation).            | number           | 3.43, 0, -4, 1.03e4         |
| `Boolean` | True or false.                                                                                                                  | boolean          | true, false                 |
| `String`  | A sequence of characters of any length using any (specified) character set.                                                     | string           | Indirect evaporative cooler |
| `ID`      | A referencencable identification for a data group and sequence of characters of any length using any (specified) character set. | string           | AHU-01                      |
| `Null`    | Indicator that no value is provided. Only used in combination with other data types, e.g., 'Number/Null'.                       | null             | null                        |

# ConditioningType
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `HEATED_AND_COOLED` | Heated and cooled |       |
| `HEATED_ONLY`       | Heated only       |       |
| `SEMIHEATED`        | Semiheated        |       |
| `UNCONDITIONED`     | Unconditioned     |       |

# SpaceFunctionType
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `LABORATORY` | Laboratory  |       |
| `KITCHEN`    | Kitchen     |       |
| `OTHER`      | Other       |       |

# InfiltrationMethodType
|      Enumerator      |                                                                                                                      Description                                                                                                                      | Notes |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| `WEATHER_DRIVEN`     | Weather Driven. The amount of air leakage is determined by using the infiltration_flow_rate with a correlation usually involving windspeed, height, and the difference between indoor and outdoor temperature and is then multiplied by the schedule. |       |
| `PRESSURE_BASED`     | Pressure Based. The amount of air leakage is determined by induced airflows from pressure differences between zones, air distribution system components, the outside due to wind speed and direction.                                                 |       |
| `CONSTANT`           | Constant. The schedule is ignored.                                                                                                                                                                                                                    |       |
| `CONSTANT_SCHEDULED` | Constant multiplied by the schedule.                                                                                                                                                                                                                  |       |
| `OTHER`              | Other infiltration methods.                                                                                                                                                                                                                           |       |

# SurfaceClassificationType
| Enumerator |           Description            | Notes |
|------------|----------------------------------|-------|
| `WALL`     | Vertical or nearly vertical wall |       |
| `FLOOR`    | Floor                            |       |
| `CEILING`  | Ceiling                          |       |

# SurfaceAdjacentTo
| Enumerator  |                                                                                                 Description                                                                                                  | Notes |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| `EXTERIOR`  | Exterior wall or roof which is adjacent to the exterior environment.                                                                                                                                         |       |
| `GROUND`    | Slab-on-grad or below grade surface if adjacent to ground.                                                                                                                                                   |       |
| `INTERIOR`  | Interior surface if adjacent to another space which is explicity modeled.                                                                                                                                    |       |
| `IDENTICAL` | Surface adjacent to a environment identical to the space. Sometimes this is described as adiabatic surface since no heat is transfered. The space on the other side of the surface is not explicity modeled. |       |
| `UNDEFINED` | The surface adjacency cannot be determined by the software.                                                                                                                                                  |       |

# SurfaceConstructionInputOptions
|  Enumerator  |               Description                | Notes |
|--------------|------------------------------------------|-------|
| `LAYERS`     | Construction is entered layer-by-layer.  |       |
| `SIMPLIFIED` | Construction is entered by R-value only. |       |

# SubsurfaceClassificationType
| Enumerator |                     Description                     | Notes |
|------------|-----------------------------------------------------|-------|
| `WINDOW`   | Window                                              |       |
| `SKYLIGHT` | Skylight                                            |       |
| `DOOR`     | Door                                                |       |
| `OTHER`    | Other types of subsurfaces that allow light to pass |       |

# SubsurfaceDynamicGlazingType
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `NOT_DYNAMIC`       | Not dynamic       |       |
| `MANUAL_DYNAMIC`    | Manual dynamic    |       |
| `AUTOMATIC_DYNAMIC` | Automatic dynamic |       |

# LightingDaylightingControlType
|      Enumerator      |            Description             |          Notes          |
|----------------------|------------------------------------|-------------------------|
| `STEPPED`            | Stepped                            |                         |
| `CONTINUOUS_DIMMING` | Continuous Dimming                 |                         |
| `OTHER`              | Other types of daylighting control |                         |
| `NONE`               | None                               | No daylighting is used. |

# LightingOccupancyControlType
|    Enumerator     |           Description            |             Notes              |
|-------------------|----------------------------------|--------------------------------|
| `FULL_AUTO_ON`    | Full auto on                     |                                |
| `PARTIAL_AUTO_ON` | Parial auto on                   |                                |
| `MANUAL_ON`       | Manual on                        |                                |
| `OTHER`           | Other types of occupancy control |                                |
| `NONE`            | None                             | No occupancy controls is used. |

# MiscellaneousEquipmentType
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `PLUG`     | Plug        |       |
| `PROCESS`  | Process     |       |
| `OTHER`    | Other       |       |

# TransformerType
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `DRY_TYPE`     | Dry Type     |       |
| `FLUID_FILLED` | Fluid Filled |       |
| `OTHER`        | Other        |       |

# ElectricalPhase
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `SINGLE_PHASE` | Single Phase |       |
| `THREE_PHASE`  | Three Phase  |       |

# ScheduleSequenceTypeOptions
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `HOURLY`   | Hourly      |       |
| `EVENT`    | Event       |       |

# ScheduleTypeOptions
|         Enumerator         |       Description        | Notes |
|----------------------------|--------------------------|-------|
| `MULTIPLIER_DIMENSIONLESS` | Multiplier dimensionless |       |
| `TEMPERATURE`              | Temperature              |       |
| `POWER`                    | Power                    |       |
| `FLOW_RATE`                | Flow rate                |       |

# DayOfWeek
| Enumerator  | Description | Notes |
|-------------|-------------|-------|
| `SUNDAY`    | Sunday      |       |
| `MONDAY`    | Monday      |       |
| `TUESDAY`   | Tuesday     |       |
| `WEDNESDAY` | Wednesday   |       |
| `THURSDAY`  | Thursday    |       |
| `FRIDAY`    | Friday      |       |
| `SATURDAY`  | Saturday    |       |

# CoolingDesignDayTypeOptions
|  Enumerator   |                           Description                            | Notes |
|---------------|------------------------------------------------------------------|-------|
| `COOLING_0_4` | Cooling design day 0.4% annual cumulative frequency of occurance |       |
| `COOLING_1_0` | Cooling design day 1.0% annual cumulative frequency of occurance |       |
| `COOLING_2_0` | Cooling design day 2.0% annual cumulative frequency of occurance |       |

# HeatingDesignDayTypeOptions
|   Enumerator   |                            Description                            | Notes |
|----------------|-------------------------------------------------------------------|-------|
| `HEATING_99_6` | Heating design day 99.6% annual cumulative frequency of occurance |       |
| `HEATING_99_0` | Heating design day 99.0% annual cumulative frequency of occurance |       |

# HeatingSystemType
|      Enumerator       |     Description     | Notes |
|-----------------------|---------------------|-------|
| `HEAT_PUMP`           | Heat Pump           |       |
| `FURNACE`             | Furnace             |       |
| `ELECTRIC_RESISTANCE` | Electric resistance |       |
| `FLUID_LOOP`          | Fluid loop          |       |
| `BASEBOARD`           | Baseboard           |       |
| `NONE`                | None                |       |
| `OTHER`               | Other               |       |

# HeatpumpAuxilliaryHeatType
|      Enumerator       |     Description     | Notes |
|-----------------------|---------------------|-------|
| `ELECTRIC_RESISTANCE` | Electric resistance |       |
| `FURNACE`             | Furnace             |       |
| `NONE`                | None                |       |
| `OTHER`               | Other               |       |

# HumidificationType
| Enumerator  | Description | Notes |
|-------------|-------------|-------|
| `ADIABATIC` | Adiabatic   |       |
| `NONE`      | None        |       |
| `OTHER`     | Other       |       |

# CoolingSystemType
|     Enumerator     |   Description    | Notes |
|--------------------|------------------|-------|
| `DIRECT_EXPANSION` | Direct expansion |       |
| `FLUID_LOOP`       | Fluid loop       |       |
| `NON_MECHANICAL`   | Non-mechanical   |       |
| `NONE`             | None             |       |
| `OTHER`            | Other            |       |

# DehumidificationType
|       Enumerator       |     Description      | Notes |
|------------------------|----------------------|-------|
| `MECHANCIAL_COOLING`   | Mechanical cooling   |       |
| `DESICCANT`            | Desiccant            |       |
| `SERIES_HEAT_RECOVERY` | Series heat recovery |       |
| `NONE`                 | None                 |       |
| `OTHER`                | Other                |       |

# FanSystemTemperatureControlType
|              Enumerator               |             Description             | Notes |
|---------------------------------------|-------------------------------------|-------|
| `CONSTANT`                            | Constant                            |       |
| `OUTDOOR_AIR_RESET`                   | Outdoor air reset                   |       |
| `ZONE_RESET`                          | Zone reset                          |       |
| `LOAD_RESET_TO_SPACE_TEMPERATURE`     | Load Reset To Space Temperature     |       |
| `LOAD_RESET_DIFFERENTIAL_TEMPERATURE` | Load Reset Differential Temperature |       |
| `SCHEDULED`                           | Scheduled                           |       |
| `OTHER`                               | Other                               |       |

# FanSystemSupplyFanControlType
|       Enumerator       |     Description      | Notes |
|------------------------|----------------------|-------|
| `CONSTANT`             | Constant             |       |
| `VARIABLE_SPEED_DRIVE` | Variable speed drive |       |
| `MULTISPEED`           | Multispeed           |       |
| `INLET_VANE`           | Inlet vane           |       |
| `DISCHARGE_DAMPER`     | Discharge damper     |       |
| `OTHER`                | Other                |       |

# FanSystemOperationType
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `CYCLING`    | Cycling     |       |
| `CONTINUOUS` | Continuous  |       |
| `KEEP_OFF`   | Off         |       |
| `OTHER`      | Other       |       |

# FanSystemSupplyFanVolumeResetType
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `CONSTANT`   | Constant    |       |
| `LOAD_RESET` | Load Reset  |       |
| `OTHER`      | Other       |       |

# AirEconomizerType
|         Enumerator         |            Description            | Notes |
|----------------------------|-----------------------------------|-------|
| `FIXED_FRACTION`           | Fixed Fraction                    |       |
| `TEMPERATURE`              | Dry-bulb temperature              |       |
| `ENTHALPY`                 | Enthalpy                          |       |
| `DIFFERENTIAL_TEMPERATURE` | Differential dry-bulb temperature |       |
| `DIFFERENTIAL_ENTHALPY`    | Differential enthalpy             |       |
| `OTHER`                    | Other                             |       |

# EnergyRecoveryType
|       Enumerator        |      Description       | Notes |
|-------------------------|------------------------|-------|
| `SENSIBLE_HEAT_EXHANGE` | Sensible heat exchange |       |
| `ENTHALPY_HEAT_EXHANGE` | Enthalpy heat exchange |       |
| `SENSIBLE_HEAT_WHEEL`   | Sensible heat wheel    |       |
| `ENTHALPY_HEAT_WHEEL`   | Enthalpy heat wheel    |       |
| `HEAT_PIPE`             | Heat pipe              |       |
| `OTHER`                 | Other                  |       |
| `NONE`                  | None                   |       |

# EnergyRecoveryOperation
|         Enumerator         |       Description        | Notes |
|----------------------------|--------------------------|-------|
| `WHEN_FANS_ON`             | When fans on             |       |
| `WHEN_MINIMUM_OUTSIDE_AIR` | When minimum outside air |       |
| `SCHEDULED`                | Scheduled                |       |
| `OTHER`                    | Other                    |       |
| `NONE`                     | None                     |       |

# EnergyRecoverySupplyAirTemperatureControl
|    Enumerator     |   Description   | Notes |
|-------------------|-----------------|-------|
| `FIXED_SETPOINT`  | Fixed setpoint  |       |
| `MIXED_AIR_RESET` | Mixed air reset |       |
| `OTHER`           | Other           |       |
| `NONE`            | None            |       |

# DemandControlVentilationControlType
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `CO2_RETURN_AIR` | CO2 return air |       |
| `CO2_ZONE`       | CO2 zone       |       |
| `OTHER`          | Other          |       |
| `NONE`           | None           |       |

# FanSpecificationMethodOptions
| Enumerator | Description |                                              Notes                                              |
|------------|-------------|-------------------------------------------------------------------------------------------------|
| `SIMPLE`   | Simple      | Specify the electric power input of fan                                                         |
| `DETAILED` | Detailed    | Specify the brake horse power, design pressure rise through, total efficiency, motor efficiency |

# TerminalType
|        Enumerator         |       Description       | Notes |
|---------------------------|-------------------------|-------|
| `VARIABLE_AIR_VOLUME`     | Variable air volume     |       |
| `CONSTANT_AIR_VOLUME`     | Constant air volume     |       |
| `RADIANT`                 | Radiant                 |       |
| `FOUR_PIPE_FAN_COIL_UNIT` | Four pipe fan coil unit |       |
| `TWO_PIPE_FAN_COIL_UNIT`  | Two pipe fan coil unit  |       |
| `BASEBOARD`               | Baseboard               |       |
| `OTHER`                   | Other                   |       |

# TerminalFanConfiguration
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `PARALLEL` | Parallel    |       |
| `SERIES`   | Series      |       |
| `OTHER`    | Other       |       |

# ReheatSourceType
| Enumerator  | Description | Notes |
|-------------|-------------|-------|
| `ELECTRIC`  | Electric    |       |
| `HOT_WATER` | Hot water   |       |
| `NONE`      | None        |       |
| `OTHER`     | Other       |       |

# FluidLoopFlowControlOptions
|   Enumerator    |  Description  | Notes |
|-----------------|---------------|-------|
| `FIXED_FLOW`    | Fixed flow    |       |
| `VARIABLE_FLOW` | Variable flow |       |

# FluidLoopTypeOptions
|      Enumerator       |     Description     | Notes |
|-----------------------|---------------------|-------|
| `HEATING`             | Heating             |       |
| `COOLING`             | Cooling             |       |
| `HEATING_AND_COOLING` | Heating and cooling |       |
| `CONDENSER`           | Condenser           |       |
| `OTHER`               | Other               |       |

# TemperatureResetTypeOptions
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `NO_RESET`          | No Reset          |       |
| `CONSTANT`          | Constant          |       |
| `OUTSIDE_AIR_RESET` | Outside air reset |       |
| `LOAD_RESET`        | Load Reset        |       |
| `OTHER`             | Other             |       |

# FluidLoopOperationOptions
|   Enumerator   |      Description       | Notes |
|----------------|------------------------|-------|
| `CONTINUOUS`   | Continuous             |       |
| `INTERMITTENT` | Intermittent/on-demand |       |
| `SCHEDULED`    | Scheduled              |       |

# PumpSpeedControlOptions
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `FIXED_SPEED`    | Fixed speed    |       |
| `VARIABLE_SPEED` | Variable speed |       |

# PumpSpecificationMethodOptions
| Enumerator | Description |                                         Notes                                         |
|------------|-------------|---------------------------------------------------------------------------------------|
| `SIMPLE`   | Simple      | Specify the electric power input of pump                                              |
| `DETAILED` | Detailed    | Specify the motor nameplate power, design head, impellor efficiency, motor efficiency |

# BoilerCombustionOptions
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `NATURAL`  | Natural     |       |
| `FORCED`   | Forced      |       |

# BoilerEfficiencyMetricTypeOptions
|        Enumerator         |            Description             | Notes |
|---------------------------|------------------------------------|-------|
| `ANNUAL_FUEL_UTILIZATION` | Annual fuel utilization efficiency |       |
| `THERMAL`                 | Thermal efficiency                 |       |
| `COMBUSTION`              | Combustion efficiency              |       |

# ChillerPartLoadEfficiencyMetricTypeOptions
|          Enumerator           |                                      Description                                       | Notes |
|-------------------------------|----------------------------------------------------------------------------------------|-------|
| `INTEGRATED_PART_LOAD_VALUE`  | Integrated part load value efficiency expressed as a coefficient of performance (COP)  |       |
| `NONSTANDARD_PART_LOAD_VALUE` | Nonstandard part load value efficiency expressed as a coefficient of performance (COP) |       |
| `OTHER`                       | Other part load efficiency metric                                                      |       |

# ChillerCompressorTypeOptions
|                Enumerator                 |               Description               | Notes |
|-------------------------------------------|-----------------------------------------|-------|
| `SCREW`                                   | Screw                                   |       |
| `CENTRIFUGAL`                             | Centrifugal                             |       |
| `RECIPROCATING`                           | Reciprocating                           |       |
| `SCROLL`                                  | Scroll                                  |       |
| `POSITIVE_DISPLACEMENT`                   | Positive displacement                   |       |
| `SINGLE_EFFECT_INDIRECT_FIRED_ABSORPTION` | Single-effect indirect-fired absorption |       |
| `DOUBLE_EFFECT_INDIRECT_FIRED_ABSORPTION` | Double-effect indirect-fired absorption |       |
| `SINGLE_EFFECT_DIRECT_FIRED_ABSORPTION`   | Single-effect direct-fired absorption   |       |
| `DOUBLE_EFFECT_DIRECT_FIRED_ABSORPTION`   | Double-effect direct-fired absorption   |       |
| `OTHER`                                   | Other                                   |       |

# HeatRejectionTypeOptions
|           Enumerator           |                 Description                  | Notes |
|--------------------------------|----------------------------------------------|-------|
| `OPEN_CIRCUIT_COOLING_TOWER`   | Open-circuit cooling tower                   |       |
| `CLOSED_CIRCUIT_COOLING_TOWER` | Closed-circuit cooling tower or fluid cooler |       |
| `DRY_COOLER`                   | Dry-cooler or air-cooled fluid cooler        |       |
| `EVAPORATIVE_CONDENSER`        | Evaporative condenser                        |       |
| `AIR_COOLED_CONDENSER`         | Air cooled condenser                         |       |
| `OTHER`                        | Other                                        |       |

# HeatRejectionFanTypeOptions
|  Enumerator   |    Description     | Notes |
|---------------|--------------------|-------|
| `AXIAL`       | Axial or Propellor |       |
| `CENTRIFUGAL` | Centrifugal        |       |
| `OTHER`       | Other              |       |

# HeatRejectionFluidOptions
|  Enumerator   | Description |      Notes       |
|---------------|-------------|------------------|
| `WATER`       | Water       |                  |
| `REFRIGERANT` | Refrigerant | Including R-448A |
| `AMMONIA`     | Ammonia     |                  |
| `OTHER`       | Other       |                  |

# HeatRejectionResetOptions
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `CONSTANT`   | Constant    |       |
| `LOAD_RESET` | Load reset  |       |
| `OTHER`      | Other       |       |

# HeatRejectionFanSpeedControlOptions
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `CONSTANT`       | Constant       |       |
| `TWO_SPEED`      | Two Speed      |       |
| `VARIABLE_SPEED` | Variable Speed |       |
| `OTHER`          | Other          |       |

# ExternalFluidSourceTypeOptions
|   Enumerator    |  Description  | Notes |
|-----------------|---------------|-------|
| `CHILLED_WATER` | Chilled water |       |
| `HOT_WATER`     | Hot water     |       |
| `STEAM`         | Steam         |       |

# ServiceWaterHeatingConfigurationType
|                      Enumerator                      |                    Description                     | Notes |
|------------------------------------------------------|----------------------------------------------------|-------|
| `HERS_PARALLEL_PIPING`                               | HERS parallel piping                               |       |
| `HERS_PIPE_INSULATION_ALL_LINES`                     | HERS pipe insulation of all lines                  |       |
| `HERS_RECIRCULATION_DEMAND_CONTROL_OCCUPANCY_SENSOR` | HERS recirculation demand control occupancy sensor |       |
| `HERS_RECIRCULATION_DEMAND_CONTROL_BUTTON`           | HERS recirculation demand control pull botton      |       |
| `HERS_RECIRCULATION_NON_DEMAND_CONTROL`              | HERS recirculation non-demand control              |       |
| `INSULATED_AND_PROTECTED_PIPE_BELOW_GRADE`           | Insulated and protected pipe below grade           |       |
| `PARALLEL_PIPING`                                    | Parallel piping                                    |       |
| `PIPE_INSULATION_ALL_LINES`                          | Pipe insulation of all lines                       |       |
| `POINT_OF_USE`                                       | Point of use                                       |       |
| `RECIRCULATION_DEMAND_CONTROL_OCCUPANCY_SENSOR`      | Recirculation demand control occupancy sensor      |       |
| `RECIRCULATION_DEMAND_CONTROL_BUTTON`                | Recirculation demand control pull botton           |       |
| `RECIRCULATION_NON_DEMAND_CONTROL`                   | Recirculation non-demand control                   |       |
| `STANDARD`                                           | Standard                                           |       |
| `OTHER`                                              | Other                                              |       |

# ServiceWaterHeatingHeatRecoveryType
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `NOT_APPLICABLE` | Not applicable |       |
| `VERTICAL`       | Vertical       |       |
| `HORIZONTAL`     | Horizontal     |       |
| `OTHER`          | Other          |       |

# ServiceWaterHeaterType
|      Enumerator      |    Description     | Notes |
|----------------------|--------------------|-------|
| `CONVENTIONAL`       | Conventional       |       |
| `HEAT_PUMP_PACKAGED` | Heat pump packaged |       |
| `HEAT_PUMP_SPLIT`    | Heat pump split    |       |
| `OTHER`              | Other              |       |

# ComponentLocation
|    Enumerator     |   Description   | Notes |
|-------------------|-----------------|-------|
| `IN_ZONE`         | In a zone       |       |
| `CONDITIONED`     | Conditioned     |       |
| `SEMICONDITIONED` | Semiconditioned |       |
| `OUTSIDE`         | Outside         |       |
| `GARAGE`          | Garage          |       |
| `ATTIC`           | Attic           |       |
| `CRAWL_SPACE`     | Crawl space     |       |
| `UNDERGROUND`     | Underground     |       |
| `UNCONDITIONED`   | Unconditioned   |       |
| `OTHER`           | Other           |       |

# ServiceWaterHeaterTankType
|                 Enumerator                  |                Description                |      Notes      |
|---------------------------------------------|-------------------------------------------|-----------------|
| `CONSUMER_INSTANTANEOUS`                    | Consumer instantaneous                    | Uses UEF        |
| `COMMERCIAL_INSTANTANEOUS`                  | Commercial instantaneous                  | Uses TE         |
| `CONSUMER_STORAGE`                          | Consumer storage                          | Uses UEF        |
| `COMMERCIAL_STORAGE`                        | Consumer storage                          | Uses TE and SBL |
| `RESIDENTIAL_DUTY_COMMERCIAL_INSTANTANEOUS` | Residential-Duty Commercial Instantaneous | Uses UEF        |
| `INDIRECT`                                  | Indirect                                  |                 |
| `BOILER`                                    | Boiler                                    |                 |
| `COMMERCIAL_PACKAGED_BOILER`                | Commercial Packaged Boiler                |                 |
| `OTHER`                                     | Other                                     |                 |

# ServiceWaterHeatingFixtureType
|    Enumerator    |       Description       | Notes |
|------------------|-------------------------|-------|
| `SHOWER`         | Shower                  |       |
| `BATH`           | Bath                    |       |
| `RESTROOM_SINK`  | Restroom Sink           |       |
| `DISHWASHER`     | Dishwasher              |       |
| `KITCHEN_SINK`   | Kitchen sink            |       |
| `WASH_SINK`      | Wash sink               |       |
| `CLOTHES_WASHER` | Clothes washing machine |       |
| `OTHER`          | Other                   |       |

# ServiceWaterHeatingUseUnits
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `POWER_PER_PERSON`  | Power per person  |       |
| `POWER_PER_AREA`    | Power per area    |       |
| `POWER`             | Power             |       |
| `VOLUME_PER_PERSON` | Volume per person |       |
| `VOLUME_PER_AREA`   | Volume per area   |       |
| `VOLUME`            | Volume            |       |
| `OTHER`             | Other             |       |

# EnergySourceTypeOptions
|  Enumerator   | Description | Notes |
|---------------|-------------|-------|
| `ELECTRICITY` | Electricity |       |
| `NATURAL_GAS` | Natural gas |       |
| `PROPANE`     | Propane     |       |
| `FUEL_OIL`    | Fuel oil    |       |
| `OTHER`       | Other       |       |

# RefrigerationType
|                  Enumerator                  |                Description                 | Notes |
|----------------------------------------------|--------------------------------------------|-------|
| `COMMERCIAL_REFRIGERATION`                   | Commercial refrigeration                   |       |
| `COMMERCIAL_REFRIGERATOR_SOLID_DOOR`         | Commercial refrigerator solid door         |       |
| `COMMERCIAL_REFRIGERATOR_TRANSPARENT_DOOR`   | Commercial refrigerator transparent door   |       |
| `COMMERCIAL_FREEZER_SOLID_DOOR`              | Commercial freezer solid door              |       |
| `COMMERCIAL_FREEZER_TRANSPARENT_DOOR`        | Commercial freezer transparent door        |       |
| `COMMERCIAL_PULLDOWN_REFRIGERATOR`           | Commercial pulldown refrigerator           |       |
| `COMMERCIAL_REFRIGERATOR_FREEZER_SOLID_DOOR` | Commercial refrigerator freezer solid door |       |
| `OTHER`                                      | Other                                      |       |

# RefrigerationCategory
|          Enumerator           |         Description         | Notes |
|-------------------------------|-----------------------------|-------|
| `HORIZONTAL_OPEN`             | Horizontal open             |       |
| `HORIZONTAL_SOLID_DOOR`       | Horizontal solid door       |       |
| `HORIZONTAL_TRANSPARENT_DOOR` | Horizontal transparent door |       |
| `SEMIVERTICAL_OPEN`           | Semivertical open           |       |
| `SERVICE_OVER_COUNTER`        | Service over counter        |       |
| `VERTICAL_OPEN`               | Vertical open               |       |
| `VERTICAL_SOLID_DOOR`         | Vertical solid door         |       |
| `VERTICAL_TRANSPARENT_DOOR`   | Vertical transparent door   |       |
| `OTHER`                       | Other                       |       |

# ApplicationTemperatureType
| Enumerator  |    Description     |               Notes               |
|-------------|--------------------|-----------------------------------|
| `MEDIUM`    | Medium temperature | 3.3 C +/- 1.1 C (38 F +/- 2 F)    |
| `LOW`       | Low temperature    | -17.8 C +/- 1.1 C (0 F +/- 2 F)   |
| `ICE_CREAM` | Ice cream          | -26.1 C +/- 1.1 C (-15 F +/- 2 F) |
| `OTHER`     | Other              |                                   |

# ASHRAE229
|                     Name                     |                                                                     Description                                                                      |                                                       Data Type                                                       |  Units  | Range | Req |                                                                             Notes                                                                              |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                         | Scope-unique reference identifier for instances of this data group.                                                                                  | `ID`                                                                                                                  |         |       | ✓   |                                                                                                                                                                |
| `reporting_name`                             | Descriptive name used in RCT reports if id is not already a descriptive name                                                                         | `String`                                                                                                              |         |       |     |                                                                                                                                                                |
| `notes`                                      | Supplementary information to provide context to the model reviewer                                                                                   | `String`                                                                                                              |         |       |     |                                                                                                                                                                |
| `transformers`                               | Electrical transformers at the building site                                                                                                         | `[{Transformer}]`                                                                                                     |         |       |     | Contains a list of transformers that convert electricity from a higher voltage to one used by the building, exterior lighting, and other services at the site. |
| `buildings`                                  | Buildings on the site                                                                                                                                | `[{Building}]`                                                                                                        |         |       |     | Contains a list of buildings on the site (often just one).                                                                                                     |
| `calendar`                                   | Information on the calendar used with the simulation.                                                                                                | `{Calendar}`                                                                                                          |         |       |     |                                                                                                                                                                |
| `schedules`                                  | Schedules for internal loads, thermostats, equipment operation and control, and any other need.                                                      | `[{Schedule}]`                                                                                                        |         |       |     | Contains a list of schedules used in model.                                                                                                                    |
| `weather`                                    | Information on the local weather conditions used with the simulation.                                                                                | `{Weather}`                                                                                                           |         |       |     |                                                                                                                                                                |
| `measured_infiltration_pressure_difference`  | Differential pressure difference used during measurement for infiltration values.                                                                    | `Numeric`                                                                                                             | Pa      | `≥0`  |     | Used as rating conditions for air leakage for a building. The most common values used are 50 Pa or 75 Pa since they correspond to common rating conditions.    |
| `is_measured_infiltration_based_on_test`     | Indicates whether the differential pressure difference used during measurement for infiltration values is based on pressure testing of the building. | `Boolean`                                                                                                             |         |       |     |                                                                                                                                                                |
| `overall_simulation_outputs`                 | Outputs from the simluation summed for all buildings in the simulation.                                                                              | `{OverallSimulationOutputs}`                                                                                          |         |       |     |                                                                                                                                                                |
| `ruleset_model_type`                         | Describes the current model for rulesets with multiple simulation models                                                                             | `(<RulesetModelType2019ASHRAE901>,<RulesetModelTypeRESNET,<RulesetModelType2019T24Com>,<RulesetModelType2019T24Res>)` |         |       |     |                                                                                                                                                                |
| `compliance_path`                            | Indicates the chosen compliance path if the ruleset has multiple compliance paths such as 90.1 Appendix G has code compliance and beyond code        | `<CompliancePathType2019ASHRAE901>`                                                                                   |         |       |     |                                                                                                                                                                |
| `building_rotation_angles`                   | A list of angles that building simulations are performed and results are provided.                                                                   | `[Numeric]`                                                                                                           | degrees |       |     | List of angles that the building has been rotated.                                                                                                             |
| `fluid_loops`                                | Fluid loops on the site                                                                                                                              | `[{FluidLoop}]`                                                                                                       |         |       |     | Contains a list of fluid loops on the site.                                                                                                                    |
| `service_water_heating_distribution_systems` | Service water heating systems on the site                                                                                                            | `[{ServiceWaterHeatingDistributionSystem}]`                                                                           |         |       |     | Contains a list of service water heating distribution systems at the site.                                                                                     |
| `pumps`                                      | Pumps used on the site                                                                                                                               | `[{Pump}]`                                                                                                            |         |       |     |                                                                                                                                                                |
| `boilers`                                    | Boilers used on the site                                                                                                                             | `[{Boiler}]`                                                                                                          |         |       |     |                                                                                                                                                                |
| `chillers`                                   | Chillers used on the site                                                                                                                            | `[{Chiller}]`                                                                                                         |         |       |     |                                                                                                                                                                |
| `heat_rejections`                            | HeatRejections used on the site                                                                                                                      | `[{HeatRejection}]`                                                                                                   |         |       |     |                                                                                                                                                                |
| `external_fluid_source`                      | ExternalFluidSources used on the site                                                                                                                | `[{ExternalFluidSource}]`                                                                                             |         |       |     |                                                                                                                                                                |
| `site_zone_type`                             | Site zone type for Sec 9.4.2                                                                                                                         | `<ExteriorLightingZones2019ASHRAE901>`                                                                                |         |       |     |                                                                                                                                                                |

# Building
|            Name            |                                 Description                                  |       Data Type        | Units | Range | Req |                                                    Notes                                                    |
|----------------------------|------------------------------------------------------------------------------|------------------------|-------|-------|-----|-------------------------------------------------------------------------------------------------------------|
| `id`                       | Scope-unique reference identifier for instances of this data group           | `ID`                   |       |       | ✓   |                                                                                                             |
| `reporting_name`           | Descriptive name used in RCT reports if id is not already a descriptive name | `String`               |       |       |     |                                                                                                             |
| `notes`                    | Supplementary information to provide context to the model reviewer           | `String`               |       |       |     |                                                                                                             |
| `building_segments`        | Large portions of a building that share a building area type                 | `[{BuildingSegment}]`  |       |       |     | Contains a list of building segments in the building.                                                       |
| `elevators`                | Elevators                                                                    | `[{Elevator}]`         |       |       |     | Contains a list of elevators in the building.                                                               |
| `exterior_lighting`        | Exterior lighting systems                                                    | `[{ExteriorLighting}]` |       |       |     | Contains a list of exterior lighting systems for the building.                                              |
| `refrigeration_components` | Refrigeration                                                                | `[{Refrigeration}]`    |       |       |     | Contains a list of refrigeration components in the building.                                                |
| `building_open_schedule`   | Reference to the schedule containing indicating when the building is open    | `$ID`                  |       |       | ✓   | One represent when the building is open and zero when closed. Constraint to use when implemented :Schedule: |
| `has_site_shading`         | Indicates whether the site has features that cast shadows on the building    | `Boolean`              |       |       |     |                                                                                                             |

# BuildingSegment
|                          Name                           |                                            Description                                             |                             Data Type                              | Units | Range | Req |                                                                                                      Notes                                                                                                      |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                                    | Scope-unique reference identifier for instances of this data group                                 | `ID`                                                               |       |       | ✓   |                                                                                                                                                                                                                 |
| `reporting_name`                                        | Descriptive name used in RCT reports if id is not already a descriptive name                       | `String`                                                           |       |       |     |                                                                                                                                                                                                                 |
| `notes`                                                 | Supplementary information to provide context to the model reviewer                                 | `String`                                                           |       |       |     |                                                                                                                                                                                                                 |
| `number_of_floors_above_grade`                          | Number of floors above grade                                                                       | `Numeric`                                                          |       | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                  |
| `number_of_floors_below_grade`                          | Number of floors below grade                                                                       | `Numeric`                                                          |       | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                  |
| `is_all_new`                                            | Indicates whether the building segment is completely new construction (true) or existing (false).  | `Boolean`                                                          |       |       |     | Projects that include additions should have a building segments that are existing (false) and for the addition (true). Curtain rules such as baseline fenestration area will apply differently to each portion. |
| `zones`                                                 | Zones in the building                                                                              | `[{Zone}]`                                                         |       |       |     | Contains a list of zones in the building.                                                                                                                                                                       |
| `heating_ventilation_air_conditioning_systems`          | HVAC systems in the building                                                                       | `[{HeatingVentilationAirConditioningSystem}]`                      |       |       |     | Contains a list of HVAC systems in the building.                                                                                                                                                                |
| `area_type_vertical_fenestration`                       | Building area classification used for vertical fenestration                                        | `<VerticalFenestrationBuildingAreaType2019ASHRAE901>`              |       |       |     | The enumeration is based on the standard used.                                                                                                                                                                  |
| `lighting_building_area_type`                           | Building area lighting area type                                                                   | `<LightingSpaceType2019ASHRAE901T951TG38>`                         |       |       |     |                                                                                                                                                                                                                 |
| `area_type_heating_ventilation_air_conditioning_system` | Classification used for HVAC                                                                       | `<HeatingVentilationAirConditioningBuildingAreaType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used. JG to verify if used in test case description.                                                                                                                   |

# Zone
|                   Name                   |                                 Description                                  |      Data Type       | Units | Range | Req |                                                                                                                                                           Notes                                                                                                                                                            |
|------------------------------------------|------------------------------------------------------------------------------|----------------------|-------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                     | Scope-unique reference identifier for instances of this data group           | `ID`                 |       |       | ✓   | No multipliers or floor multipliers are used with the Zone data group so each zone should be individually identified.                                                                                                                                                                                                      |
| `reporting_name`                         | Descriptive name used in RCT reports if id is not already a descriptive name | `String`             |       |       |     |                                                                                                                                                                                                                                                                                                                            |
| `notes`                                  | Supplementary information to provide context to the model reviewer           | `String`             |       |       |     |                                                                                                                                                                                                                                                                                                                            |
| `spaces`                                 | Spaces in the zone                                                           | `[{Space}]`          |       |       |     | Contains a list of spaces in the building.                                                                                                                                                                                                                                                                                 |
| `floor_number`                           | Floor number                                                                 | `Numeric`            |       |       |     | Used to group zones on a floor so the number indicates that different zones share a floor. The number should increase for increasing heights and be negative values for stories generally below ground and should generally correspond to numbering of floors on the plans. JG to verify if used in test case description. |
| `volume`                                 | Volume of the space                                                          | `Numeric`            | m3    | `≥0`  |     |                                                                                                                                                                                                                                                                                                                            |
| `surfaces`                               | Surfaces surrounding the zone                                                | `[{Surface}]`        |       |       |     | Contains a list of surfaces that define the zone.                                                                                                                                                                                                                                                                          |
| `conditioning_type`                      | Space conditioning category                                                  | `<ConditioningType>` |       |       |     |                                                                                                                                                                                                                                                                                                                            |
| `infiltration`                           | Airleakage into the zone.                                                    | `{Infiltration}`     |       |       |     | References a single infiltration data group.                                                                                                                                                                                                                                                                               |
| `design_thermostat_cooling_setpoint`     | Setpoint temperature for cooling during occupied hours                       | `Numeric`            | C     |       |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |
| `thermostat_cooling_setpoint_schedule`   | Reference to the schedule containing the cooling setpoint temperatures       | `$ID`                |       |       | ✓   | Constraint to use when implemented :Schedule:                                                                                                                                                                                                                                                                              |
| `design_thermostat_heating_setpoint`     | Setpoint temperature for heating during occupied hours                       | `Numeric`            | C     |       |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |
| `thermostat_heating_setpoint_schedule`   | Reference to the schedule containing the heating setpoint temperatures       | `$ID`                |       |       | ✓   | Constraint to use when implemented :Schedule:                                                                                                                                                                                                                                                                              |
| `terminals`                              | List of terminals                                                            | `[{Terminal}]`       |       |       |     | Multple terminals may be used such as from a VAV system, a DOAS, and a baseboard. JG to verify if used in test case description.                                                                                                                                                                                           |
| `served_by_service_water_heating_system` | A service water heating system serving the zone                              | `$ID`                |       |       |     | Contains a single ID of the service water heating system serving the zone - from Unique Identification Number in ServiceWaterHeatingSystem. Constraint to use when implemented :ServiceWaterHeatingDistributionSystem:                                                                                                     |
| `transfer_airflow_rate`                  | Airflow rate for transfer air                                                | `Numeric`            | L/s   |       |     | Net transfer air. Positive values indicate transfer air in to the zone and negative values show transfer out of the zone. JG to verify if used in test case description.                                                                                                                                                   |
| `exhaust_airflow_rate`                   | Airflow rate for exhaust air                                                 | `Numeric`            | L/s   | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |
| `makeup_airflow_rate`                    | Airflow rate for makeup air                                                  | `Numeric`            | L/s   | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |
| `non_mechanical_cooling_fan_power`       | Non-mechanical cooling fan power                                             | `Numeric`            | W     | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |
| `non_mechanical_cooling_fan_airflow`     | Non-mechanical cooling fan airflow                                           | `Numeric`            | L/s   | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |
| `air_distribution_effectiveness`         | Air distribution effectiveness                                               | `Numeric`            |       | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                             |

# Space
|                Name                |                                   Description                                   |                           Data Type                           | Units | Range | Req |                                                                                                                                                                                                                                                  Notes                                                                                                                                                                                                                                                  |
|------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------|-------|-------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                               | Scope-unique reference identifier for instances of this data group              | `ID`                                                          |       |       | ✓   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `reporting_name`                   | Descriptive name used in RCT reports if id is not already a descriptive name    | `String`                                                      |       |       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `notes`                            | Supplementary information to provide context to the model reviewer              | `String`                                                      |       |       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `interior_lighting`                | Internal lighting that produce internal gains for a space.                      | `[{InteriorLighting}]`                                        |       |       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `miscellaneous_equipment`          | Miscellaneous equipment loads that produce internal gains for a space.          | `[{MiscellaneousEquipment}]`                                  |       |       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `floor_area`                       | The floor area of the space.                                                    | `Numeric`                                                     | m2    | `≥0`  |     | The floor area of a space within the building, including basements, mezzanine and intermediate-floored tiers, and penthouses with a headroom height of 7.5 ft or greater. It is measured from the exterior faces of walls or from the center-line of walls separating buildings, but excluding covered walkways, open roofed-over areas, porches and similar spaces, pipe trenches, exterior terraces or steps, chimneys, roof overhangs, and similar features. This is the floor area that is modeled. |
| `number_of_occupants`              | Number of occupants in the space                                                | `Numeric`                                                     |       | `≥0`  |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `occupant_multiplier_schedule`     | Reference to the schedule containing the multiplier for the number of occupants | `$ID`                                                         |       |       | ✓   | Constraint to use when implemented :Schedule:                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `occupant_sensible_heat_gain`      | Sensible heat gain of each occupant.                                            | `Numeric`                                                     | W     | `≥0`  |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `status_type`                      | Choice of new, existing, addition, alteration, etc. for each ruleset.           | `(<SpaceStatusType2019ASHRAE901>,<GeneralStatusType2019T24>)` |       |       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `space_function`                   | Generic function for the space.                                                 | `<SpaceFunctionType>`                                         |       |       |     | The enumeration is based on the standard used.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `lighting_space_type`              | Lighting space type classification                                              | `<LightingSpaceType2019ASHRAE901TG37>`                        |       |       |     | The enumeration is based on the standard used.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ventilations_space_type`          | Ventilation space type classification                                           | `<VentilationSpaceType2019ASHRAE901>`                         |       |       |     | The enumeration is based on the standard used.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `service_water_heating_space_type` | Service water heating space type classification                                 | `<ServiceWaterHeatingSpaceType2019ASHRAE901>`                 |       |       |     | The enumeration is based on the standard used.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `service_weater_heating_uses`      | List of service water heating uses                                              | `[{ServiceWaterHeatingUse}]`                                  |       |       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

# Infiltration
|            Name             |                                       Description                                       |         Data Type          | Units | Range | Req |                                                                                                           Notes                                                                                                            |
|-----------------------------|-----------------------------------------------------------------------------------------|----------------------------|-------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | Scope-unique reference identifier for instances of this data group                      | `ID`                       |       |       | ✓   |                                                                                                                                                                                                                            |
| `reporting_name`            | Descriptive name used in RCT reports if id is not already a descriptive name            | `String`                   |       |       |     |                                                                                                                                                                                                                            |
| `notes`                     | Supplementary information to provide context to the model reviewer                      | `String`                   |       |       |     |                                                                                                                                                                                                                            |
| `modeling_method`           | The software methodology chosen for modeling infiltration                               | `<InfiltrationMethodType>` |       |       |     |                                                                                                                                                                                                                            |
| `algorithm_name`            | Name of the algorithm used for modeling infiltration in the specific simulation engine. | `String`                   |       |       |     |                                                                                                                                                                                                                            |
| `measured_air_leakage_rate` | Meaured air leakage rate from infiltration of outside air                               | `Numeric`                  | m3/s  | `≥0`  |     | Based on the pressure described in ASHRAE229.measured_infiltration_pressure_difference.                                                                                                                                    |
| `infiltration_flow_rate`    | Design infiltration flow rate                                                           | `Numeric`                  | m3/s  | `≥0`  |     | Infiltration flow rate for simulation infiltration models unadjusted for temperature difference or windspeed or schedule often with a windspeed at 10 mph (4.5 m/s).  This may vary in meaning between simulation engines. |
| `multiplier_schedule`       | Referenced to the schedule containing the multiplier for the infiltration               | `$ID`                      |       |       |     | Constraint to use when implemented :Schedule:                                                                                                                                                                              |

# Surface
|             Name             |                                                               Description                                                                |                                               Data Type                                                |  Units  | Range | Req |                                                    Notes                                                     |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------|-------|-----|--------------------------------------------------------------------------------------------------------------|
| `id`                         | Scope-unique reference identifier for instances of this data group                                                                       | `ID`                                                                                                   |         |       | ✓   |                                                                                                              |
| `reporting_name`             | Descriptive name used in RCT reports if id is not already a descriptive name                                                             | `String`                                                                                               |         |       |     |                                                                                                              |
| `notes`                      | Supplementary information to provide context to the model reviewer                                                                       | `String`                                                                                               |         |       |     |                                                                                                              |
| `subsurfaces`                | Suburfaces that are on the surface                                                                                                       | `[{Subsurface}]`                                                                                       |         |       |     | Contains a list of surfaces that define the space.                                                           |
| `classification`             | Classification for the surface.                                                                                                          | `<SurfaceClassificationType>`                                                                          |         |       |     | Options for surface being interior or exterior wall, floor, or ceiling.                                      |
| `area`                       | area of the surface                                                                                                                      | `Numeric`                                                                                              | m2      | `≥0`  |     | Measured from interior face area. It is the gross area of the wall and includes the area of all subsurfaces. |
| `tilt`                       | Angle between vertical and the surface outward normal                                                                                    | `Numeric`                                                                                              | degrees |       |     | Example value would be 0 = roof, 90 = wall, 180 = downward facing surface (exterior floor)                   |
| `azimuth`                    | Clockwise angle between North and the horizontal projection of the wall's outward normal.                                                | `Numeric`                                                                                              | degrees | `≥0`  |     | Example values would be 0 = north, 90 = East, 180 = South, 270 = West                                        |
| `adjacent_to`                | Used to classify the conditions on the surface.                                                                                          | `(<SurfaceAdjacentTo>,<AdditionalSurfaceAdjacentToRESNET>,<AdditionalSurfaceAdjacentTo2019ASHRAE901>)` |         |       |     | Determines whether the other side of the surface is modeled and if not what assumptions should be used.      |
| `adjacent_zone`              | ID of the adjacent zone for interior surface. Only required when adjacent zone is explicity modeled when adjacent_to is set to INTERIOR. | `$ID`                                                                                                  |         |       |     | Constraint to use when implemented :Zone:                                                                    |
| `does_cast_shade`            | Determines whether the surface is modeled as casting shade on other exterior surfaces                                                    | `Boolean`                                                                                              |         |       |     |                                                                                                              |
| `construction`               | Construction description of surface.                                                                                                     | `{Construction}`                                                                                       |         |       |     |                                                                                                              |
| `surface_optical_properties` | Optical properties of the surface.                                                                                                       | `{SurfaceOpticalProperties}`                                                                           |         |       |     |                                                                                                              |
| `status_type`                | Choice of new, existing, addition, alteration, etc. for each ruleset.                                                                    | `<GeneralStatusType2019T24>`                                                                           |         |       |     |                                                                                                              |

# Construction
|                Name                 |                                           Description                                           |              Data Type              | Units  |  Range  | Req |                                                                                                      Notes                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------|--------|---------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                | Scope-unique reference identifier for instances of this data group                              | `ID`                                |        |         | ✓   |                                                                                                                                                                                                                  |
| `reporting_name`                    | Descriptive name used in RCT reports if id is not already a descriptive name                    | `String`                            |        |         |     |                                                                                                                                                                                                                  |
| `notes`                             | Supplementary information to provide context to the model reviewer                              | `String`                            |        |         |     |                                                                                                                                                                                                                  |
| `surface_construction_input_option` | Identifies whether construction is entered layer-by-layer or simplified (R-value)               | `<SurfaceConstructionInputOptions>` |        |         |     |                                                                                                                                                                                                                  |
| `fraction_framing`                  | Fraction of the construction that is framing.                                                   | `Numeric`                           |        | `≥0,≤1` |     | Fraction of the construction using framing_layers, the remaining portion uses the primary_layers. If blank, assume zero framing.                                                                                 |
| `primary_layers`                    | List of names of layer descriptions starting from the outside surface for primary heat path     | `[{Material}]`                      |        |         |     | For constructions with framing and cavity heat transfer paths, use this for the cavity. For constructions with homogeneous layer, use this element only. Air films should not be included in the list of layers. |
| `framing_layers`                    | List of names of layer descriptions starting from the outside surface for the framing heat path | `[{Material}]`                      |        |         |     | For constructions with framing and cavity heat transfer paths, use this for the framing otherwise leave blank. Air films should not be included in the list of layers.                                           |
| `insulation_location`               | The location of the insulation related to the surface                                           | `String`                            |        |         |     |                                                                                                                                                                                                                  |
| `u_factor`                          | suface U-factor                                                                                 | `Numeric`                           | W/m2-K | `≥0`    |     | Includes interior and exterior air films as specified by the referenced standard.                                                                                                                                |
| `c_factor`                          | surface C-factor                                                                                | `Numeric`                           | W/m2-K | `≥0`    |     |                                                                                                                                                                                                                  |
| `f_factor`                          | surface F-factor                                                                                | `Numeric`                           | W/m-K  | `≥0`    |     |                                                                                                                                                                                                                  |
| `r_value`                           | r-value of the insulation for the surface                                                       | `Numeric`                           | K-m2/W | `≥0`    |     |                                                                                                                                                                                                                  |
| `has_radiant_heating`               | Includes embedded radiant heating elements                                                      | `Boolean`                           |        |         |     |                                                                                                                                                                                                                  |
| `has_radiant_cooling`               | Includes embedded radiant cooling elements                                                      | `Boolean`                           |        |         |     |                                                                                                                                                                                                                  |

# Material
|          Name          |                                 Description                                  | Data Type | Units  | Range | Req |                                                       Notes                                                        |
|------------------------|------------------------------------------------------------------------------|-----------|--------|-------|-----|--------------------------------------------------------------------------------------------------------------------|
| `id`                   | Scope-unique reference identifier for instances of this data group           | `ID`      |        |       | ✓   |                                                                                                                    |
| `reporting_name`       | Descriptive name used in RCT reports if id is not already a descriptive name | `String`  |        |       |     |                                                                                                                    |
| `notes`                | Supplementary information to provide context to the model reviewer           | `String`  |        |       |     |                                                                                                                    |
| `thickness`            | The thickness of the material layer                                          | `Numeric` | m      | `>0`  |     |                                                                                                                    |
| `thermal_conductivity` | The thermal conductivity of the material layer                               | `Numeric` | W/m-K  | `≥0`  |     | When thermal_conductivity is specified, r_value should not be provided.                                            |
| `density`              | The density of the material layer                                            | `Numeric` | kg/m3  | `≥0`  |     |                                                                                                                    |
| `specific_heat`        | The specific heat of the material layer                                      | `Numeric` | J/kg-K | `≥0`  |     |                                                                                                                    |
| `r_value`              | r-value of the insulation for the material layer                             | `Numeric` | K-m2/W | `≥0`  |     | When r_value is specified, thermal_conductivity should not be provided. Typically used for insulation or air gaps. |

# SurfaceOpticalProperties
|              Name              |                                 Description                                  | Data Type | Units | Range | Req |                                                                                 Notes                                                                                 |
|--------------------------------|------------------------------------------------------------------------------|-----------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                           | Scope-unique reference identifier for instances of this data group           | `ID`      |       |       | ✓   |                                                                                                                                                                       |
| `reporting_name`               | Descriptive name used in RCT reports if id is not already a descriptive name | `String`  |       |       |     |                                                                                                                                                                       |
| `notes`                        | Supplementary information to provide context to the model reviewer           | `String`  |       |       |     |                                                                                                                                                                       |
| `absorptance_thermal_exterior` | Thermal absorptance of long wavelength radiation on the exterior surface.    | `Numeric` |       | `≥0`  |     | May also be called thermal emittance, emittance or emissivity and represents the fraction of incident long wavelength radiation that is absorbed by the material      |
| `absorptance_solar_exterior`   | Thermal absorptance of short wavelength radiation on the exterior surface.   | `Numeric` |       | `≥0`  |     | Equals one minus the solar reflectance (for opaque materials) and represents the fraction of incident solar radiation that is absorbed by the material                |
| `absorptance_visible_exterior` | Thermal absorptance of visible radiation on the exterior surface.            | `Numeric` |       | `≥0`  |     | Equals one minus the visible reflectance (for opaque materials) and represents the fraction of incident visible wavelength radiation that is absorbed by the material |
| `absorptance_thermal_interior` | Thermal absorptance of long wavelength radiation on the interior surface.    | `Numeric` |       | `≥0`  |     | May also be called thermal emittance, emittance or emissivity and represents the fraction of incident long wavelength radiation that is absorbed by the material      |
| `absorptance_solar_interior`   | Thermal absorptance of short wavelength radiation on the interior surface.   | `Numeric` |       | `≥0`  |     | Equals one minus the solar reflectance (for opaque materials) and represents the fraction of incident solar radiation that is absorbed by the material                |
| `absorptance_visible_interior` | Thermal absorptance of visible radiation on the interior surface.            | `Numeric` |       | `≥0`  |     | Equals one minus the visible reflectance (for opaque materials) and represents the fraction of incident visible wavelength radiation that is absorbed by the material |

# Subsurface
|                  Name                   |                                           Description                                           |                    Data Type                     | Units  | Range | Req |                                                  Notes                                                   |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------|--------|-------|-----|----------------------------------------------------------------------------------------------------------|
| `id`                                    | Scope-unique reference identifier for instances of this data group                              | `ID`                                             |        |       | ✓   |                                                                                                          |
| `reporting_name`                        | Descriptive name used in RCT reports if id is not already a descriptive name                    | `String`                                         |        |       |     |                                                                                                          |
| `notes`                                 | Supplementary information to provide context to the model reviewer                              | `String`                                         |        |       |     |                                                                                                          |
| `classification`                        | Classification for the subsurface being window, skylight, door.                                 | `<SubsurfaceClassificationType>`                 |        |       |     |                                                                                                          |
| `subclassification`                     | Standard specific subclassification for subsurfaces                                             | `<SubsurfaceSubclassificationType2019ASHRAE901>` |        |       |     |                                                                                                          |
| `is_operable`                           | Identifies whether window subsurface can be opened and closed including by pivoting or sliding. | `Boolean`                                        |        |       |     | This applies to windows and skylights but not to doors.                                                  |
| `has_open_sensor`                       | Has sensor and reports to building control system when the window or door is open.              | `Boolean`                                        |        |       |     |                                                                                                          |
| `framing_type`                          | The material of the framing.                                                                    | `<SubsurfaceFrameType2019ASHRAE901>`             |        |       |     | This applies to windows and skylights but not to doors.                                                  |
| `glazed_area`                           | Area of subsurface including glass and transparent surfaces                                     | `Numeric`                                        | m2     | `≥0`  |     |                                                                                                          |
| `opaque_area`                           | Area of subsurface framing for a window or skylight or opaque portion for a door.               | `Numeric`                                        | m2     | `≥0`  |     |                                                                                                          |
| `u_factor`                              | Overall Subsurface U-factor                                                                     | `Numeric`                                        | W/m2-K | `≥0`  |     | Includes interior and exterior air films as specified by the referenced standard.                        |
| `dynamic_glazing_type`                  | Type of dynamic glazing for the window subsurface                                               | `<SubsurfaceDynamicGlazingType>`                 |        |       |     | Indicates if the glazed subsurface can change it's performance properties and if it is automatic or not. |
| `solar_heat_gain_coefficient`           | Subsurface SHGC                                                                                 | `Numeric`                                        |        | `≥0`  |     | For dynamic glazing represents the minimum SHGC                                                          |
| `maximum_solar_heat_gain_coefficient`   | Maximum Subsurface SHGC for Dynamic Glazing                                                     | `Numeric`                                        |        | `≥0`  |     | Only used for dynamic glazing                                                                            |
| `visible_transmittance`                 | Subsurface VT                                                                                   | `Numeric`                                        |        | `≥0`  |     | For dynamic glazing represents the maximum visible transmittance                                         |
| `minimum_visible_transmittance`         | Minimum Subsurface VT for Dynamic Glazing                                                       | `Numeric`                                        |        | `≥0`  |     | Only used for dynamic glazing                                                                            |
| `depth_of_overhang`                     | Distance from the edge of the overhang to the subsurface.                                       | `Numeric`                                        | m      | `≥0`  |     |                                                                                                          |
| `has_shading_overhang`                  | Identifies whether subsurface has overhangs                                                     | `Boolean`                                        |        |       |     |                                                                                                          |
| `has_shading_sidefins`                  | Identifies whether subsurface has sidefins                                                      | `Boolean`                                        |        |       |     |                                                                                                          |
| `has_manual_interior_shades`            | Are there manually-operated interior shading such as blinds, curtains or shades                 | `Boolean`                                        |        |       |     |                                                                                                          |
| `solar_transmittance_multiplier_summer` | Solar transmittance multiplier for summer                                                       | `Numeric`                                        |        | `≥0`  |     | Often used to account for interior shading such as drapes.                                               |
| `solar_transmittance_multiplier_winter` | Solar transmittance multiplier for summer                                                       | `Numeric`                                        |        | `≥0`  |     | Often used to account for interior shading such as drapes.                                               |
| `has_automatic_shades`                  | Are there automatic interior shading such as blinds, curtains or shades                         | `Boolean`                                        |        |       |     |                                                                                                          |
| `status_type`                           | Choice of new, existing, addition, alteration, etc. for each ruleset.                           | `<GeneralStatusType2019T24>`                     |        |       |     |                                                                                                          |

# InteriorLighting
|                         Name                          |                                              Description                                              |              Data Type               | Units | Range | Req |                                             Notes                                              |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------|-------|-------|-----|------------------------------------------------------------------------------------------------|
| `id`                                                  | Scope-unique reference identifier for instances of this data group                                    | `ID`                                 |       |       | ✓   |                                                                                                |
| `reporting_name`                                      | Descriptive name used in RCT reports if id is not already a descriptive name                          | `String`                             |       |       |     |                                                                                                |
| `notes`                                               | Supplementary information to provide context to the model reviewer                                    | `String`                             |       |       |     |                                                                                                |
| `purpose_type`                                        | Lighting space type classification                                                                    | `<LightingPurposeType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used.                                                 |
| `power_per_area`                                      | Total power for lights divided by the area of the space.                                              | `Numeric`                            | W/m2  |       |     | When computing the power per area use the area of the entire space.                            |
| `lighting_multiplier_schedule`                        | Reference to the schedule containing the multiplier for lighting                                      | `$ID`                                |       |       | ✓   | Constraint to use when implemented :Schedule:                                                  |
| `occupancy_control_type`                              | Indicates the type of occupancy controls                                                              | `<LightingOccupancyControlType>`     |       |       |     |                                                                                                |
| `daylighting_control_type`                            | Indicates the type of daylighting controls                                                            | `<LightingDaylightingControlType>`   |       |       |     |                                                                                                |
| `are_schedules_used_for_modeling_occupancy_control`   | Indicates that schedule values are used for modeling the impacts of occupancy controls on lighting.   | `Boolean`                            |       |       |     |                                                                                                |
| `are_schedules_used_for_modeling_daylighting_control` | Indicates that schedule values are used for modeling the impacts of daylighting controls on lighting. | `Boolean`                            |       |       |     | For simulations that are modeling daylighting by computing the illumance this should be false. |

# MiscellaneousEquipment
|              Name              |                                     Description                                     |           Data Type            | Units |  Range   | Req |                         Notes                          |
|--------------------------------|-------------------------------------------------------------------------------------|--------------------------------|-------|----------|-----|--------------------------------------------------------|
| `id`                           | Scope-unique reference identifier for instances of this data group                  | `ID`                           |       |          | ✓   |                                                        |
| `reporting_name`               | Descriptive name used in RCT reports if id is not already a descriptive name        | `String`                       |       |          |     |                                                        |
| `notes`                        | Supplementary information to provide context to the model reviewer                  | `String`                       |       |          |     |                                                        |
| `energy_type`                  | Source of energy for the miscelleous equipment in the space                         | `<EnergySourceTypeOptions>`    |       |          |     |                                                        |
| `peak_usage`                   | Peak energy usage per hour by the miscelleous equipment in the space.               | `Numeric`                      | W     |          |     |                                                        |
| `multiplier_schedule`          | Referenced to the schedule containing the multiplier for the miscellenous equipment | `$ID`                          |       |          | ✓   | Constraint to use when implemented :Schedule:          |
| `sensible_fraction`            | Fraction of energy that is a sensible load on the space.                            | `Numeric`                      |       | `≥0, ≤1` |     | Sensible plus latent do not necessarily add up to 1.0. |
| `latent_fraction`              | Fraction of energy that is a latent load on the space.                              | `Numeric`                      |       | `≥0, ≤1` |     | Sensible plus latent do not necessarily add up to 1.0. |
| `miscellaneous_equipment_type` | Type of miscellaneous equipment                                                     | `<MiscellaneousEquipmentType>` |       |          |     |                                                        |
| `has_automatic_control`        | Indicates that the receptacles have automatic controls                              | `Boolean`                      |       |          |     |                                                        |

# Transformer
|       Name       |                                 Description                                  |      Data Type      | Units |  Range   | Req |                                                      Notes                                                      |
|------------------|------------------------------------------------------------------------------|---------------------|-------|----------|-----|-----------------------------------------------------------------------------------------------------------------|
| `id`             | Scope-unique reference identifier for instances of this data group           | `ID`                |       |          | ✓   |                                                                                                                 |
| `reporting_name` | Descriptive name used in RCT reports if id is not already a descriptive name | `String`            |       |          |     |                                                                                                                 |
| `notes`          | Supplementary information to provide context to the model reviewer           | `String`            |       |          |     |                                                                                                                 |
| `type`           | The type of transformer                                                      | `<TransformerType>` |       |          |     |                                                                                                                 |
| `phase`          | The number of electrical phases                                              | `<ElectricalPhase>` |       |          |     |                                                                                                                 |
| `efficiency`     | Transformer efficiency                                                       | `Numeric`           |       | `≥0, ≤1` |     | Expresses the efficiency of the transformer as a fraction from 0 to 1, where 1 would represent 100% efficiency. |
| `capacity`       | Rated Capacity of the Transformer                                            | `Numeric`           | V-A   | `≥0`     |     |                                                                                                                 |
| `peak_load`      | Annual Peak electric load on the transformer                                 | `Numeric`           | W     | `≥0`     |     | Peak electric load on the transfomer based on an annual simulation with typical weather file.                   |

# Schedule
|                 Name                  |                                    Description                                     |              Data Type               | Units | Range | Req |                                                                                                                                 Notes                                                                                                                                 |
|---------------------------------------|------------------------------------------------------------------------------------|--------------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                  | Scope-unique reference identifier for instances of this data group                 | `ID`                                 |       |       | ✓   |                                                                                                                                                                                                                                                                       |
| `reporting_name`                      | Descriptive name used in RCT reports if id is not already a descriptive name       | `String`                             |       |       |     |                                                                                                                                                                                                                                                                       |
| `notes`                               | Supplementary information to provide context to the model reviewer                 | `String`                             |       |       |     |                                                                                                                                                                                                                                                                       |
| `purpose`                             | The purpose of schedule                                                            | `String`                             |       |       |     | Describe the purpose of the schedule and how it can be used. Not an enumerations. The purpose assigned by BEM tool should match across RMRs. Examples include thermostat, multiplier for lighting, availability for equipment.                                        |
| `schedule_sequence_type`              | Schedule sequence type                                                             | `<ScheduleSequenceTypeOptions>`      |       |       |     |                                                                                                                                                                                                                                                                       |
| `hourly_values`                       | Hourly Values of Schedule                                                          | `[Numeric][0..8760]`                 |       |       |     | Used when schedule_sequence_type is HOURLY. Can also use functions like EFLH(), MAX(), MIN() to determine overall characteristics for the list of schedule values.                                                                                                    |
| `event_times`                         | Event times when the schedule changes                                              | `[Numeric]`                          | s     |       |     | Used when schedule_sequence_type is EVENT to describe the time of the year in seconds that the schedule changes value.                                                                                                                                                |
| `event_values`                        | Event value at corresponding event time.                                           | `[Numeric]`                          |       |       |     | Used when schedule_sequence_type is EVENT. New values starting at corresponding to the event time until following event time minus one second. Can also use functions like EFLH(), MAX(), MIN() to determine overall characteristics for the list of schedule values. |
| `type`                                | The type of schedule                                                               | `<ScheduleTypeOptions>`              |       |       |     | Primarily indicates if the values may be represented by units such as C for temperature or W for power or m3/s for flow rate or are dimensionless multipliers.                                                                                                        |
| `prescribed_schedule`                 | True if any schedule values have changed from what appears in the schedule library | `<PrescribedSchedules2019ASHRAE901>` |       |       |     |                                                                                                                                                                                                                                                                       |
| `is_schedule_modified_for_workaround` | True if any schedule has been modified for a workaround                            | `Boolean`                            |       |       |     |                                                                                                                                                                                                                                                                       |

# Calendar
|            Name             |                            Description                             |   Data Type   | Units | Range | Req | Notes |
|-----------------------------|--------------------------------------------------------------------|---------------|-------|-------|-----|-------|
| `notes`                     | Supplementary information to provide context to the model reviewer | `String`      |       |       |     |       |
| `day_of_week_for_january_1` | Day of the week for January 1                                      | `<DayOfWeek>` |       |       |     |       |
| `is_leap_year`              | The schedules assume it is a leap year                             | `Boolean`     |       |       |     |       |
| `has_daylight_saving_time`  | The schedules adjust for Daylight Saving Time                      | `Boolean`     |       |       |     |       |

# Weather
|             Name              |                            Description                             |            Data Type            | Units | Range | Req |                                               Notes                                                |
|-------------------------------|--------------------------------------------------------------------|---------------------------------|-------|-------|-----|----------------------------------------------------------------------------------------------------|
| `notes`                       | Supplementary information to provide context to the model reviewer | `String`                        |       |       |     |                                                                                                    |
| `ground_temperature_schedule` | Ground temperature schedule name                                   | `$ID`                           |       |       |     | Constraint to use when implemented :Schedule:                                                      |
| `weather_file_name`           | The file name for the weather file including extension.            | `String`                        |       |       |     | The file name for the annual weather file such as from TMY, TRY, CWEC, CTZ, WYEC or other sources. |
| `climate_zone`                | The designation of the climate zone where the building is located  | `<ClimateZone2019ASHRAE901>`    |       |       | ✓   | The enumeration is based on the standard used.                                                     |
| `cooling_design_day_type`     | The frequency of occurance type for cooling design day             | `<CoolingDesignDayTypeOptions>` |       |       |     |                                                                                                    |
| `heating_design_day_type`     | The frequency of occurance type for heating design day             | `<HeatingDesignDayTypeOptions>` |       |       |     |                                                                                                    |

# Elevator
|                   Name                    |                                 Description                                  | Data Type | Units | Range | Req |                                                      Notes                                                       |
|-------------------------------------------|------------------------------------------------------------------------------|-----------|-------|-------|-----|------------------------------------------------------------------------------------------------------------------|
| `id`                                      | Scope-unique reference identifier for instances of this data group           | `ID`      |       |       | ✓   |                                                                                                                  |
| `reporting_name`                          | Descriptive name used in RCT reports if id is not already a descriptive name | `String`  |       |       |     |                                                                                                                  |
| `notes`                                   | Supplementary information to provide context to the model reviewer           | `String`  |       |       |     |                                                                                                                  |
| `motor_power`                             | Elevator peak motor power                                                    | `Numeric` | W     |       |     | The motor power can be provided either together with or, instead of, the detailed elements used to calculate it. |
| `cab_counterweight`                       | Elevator car counterweight                                                   | `Numeric` | kg    |       |     |                                                                                                                  |
| `cab_weight`                              | Weight of elevator car                                                       | `Numeric` | kg    |       |     |                                                                                                                  |
| `design_elevator_load`                    | Elevator load at which to operate                                            | `Numeric` | kg    |       |     |                                                                                                                  |
| `speed`                                   | Design speed of the elevator                                                 | `Numeric` | m/s   |       |     |                                                                                                                  |
| `cab_area`                                | Floor area of elevator cab                                                   | `Numeric` | m2    |       |     |                                                                                                                  |
| `cab_lighting_power`                      | Lighitng power of cab                                                        | `Numeric` | W     |       |     |                                                                                                                  |
| `cab_ventilation_fan_power`               | Ventilation fan power of cab                                                 | `Numeric` | W     |       |     |                                                                                                                  |
| `cab_ventilation_fan_flow`                | Airflow of cab ventfan                                                       | `Numeric` | L/s   |       |     |                                                                                                                  |
| `cab_motor_multiplier_schedule`           | Elevator motor operation multiplier schedule name                            | `$ID`     |       |       |     | Constraint to use when implemented :Schedule:                                                                    |
| `cab_ventilation_fan_multiplier_schedule` | Elevator ventilation fan operation mulitplier schedule name                  | `$ID`     |       |       |     | Constraint to use when implemented :Schedule:                                                                    |
| `cab_lighting_multiplier_schedule`        | Elevator lighting multiplier schedule name                                   | `$ID`     |       |       |     | Constraint to use when implemented :Schedule:                                                                    |

# HeatingVentilationAirConditioningSystem
|       Name       |                                 Description                                  |          Data Type           | Units | Range | Req |                                                                            Notes                                                                            |
|------------------|------------------------------------------------------------------------------|------------------------------|-------|-------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`             | Scope-unique reference identifier for instances of this data group           | `ID`                         |       |       | ✓   |                                                                                                                                                             |
| `reporting_name` | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                     |       |       |     |                                                                                                                                                             |
| `notes`          | Supplementary information to provide context to the model reviewer           | `String`                     |       |       |     |                                                                                                                                                             |
| `fan_systems`    | Fan systems                                                                  | `[{FanSystem}]`              |       |       |     | Normally one fan system is used but second fan systems may be used when a direct outdoor air system is used. JG to verify if used in test case description. |
| `heating_system` | Heating system                                                               | `{HeatingSystem}`            |       |       |     | JG to verify if used in test case description.                                                                                                              |
| `cooling_system` | Cooling system                                                               | `{CoolingSystem}`            |       |       |     | JG to verify if used in test case description.                                                                                                              |
| `preheat_system` | Pre-heating system                                                           | `{HeatingSystem}`            |       |       |     | JG to verify if used in test case description.                                                                                                              |
| `status_type`    | Choice of new, existing, addition, alteration, etc. for each ruleset.        | `<GeneralStatusType2019T24>` |       |       |     |                                                                                                                                                             |

# HeatingSystem
|                        Name                         |                                                   Description                                                   |           Data Type            | Units |  Range   | Req |                                     Notes                                     |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------|-------|----------|-----|-------------------------------------------------------------------------------|
| `id`                                                | Scope-unique reference identifier for instances of this data group                                              | `ID`                           |       |          | ✓   |                                                                               |
| `reporting_name`                                    | Descriptive name used in RCT reports if id is not already a descriptive name                                    | `String`                       |       |          |     |                                                                               |
| `notes`                                             | Supplementary information to provide context to the model reviewer                                              | `String`                       |       |          |     |                                                                               |
| `heating_system_type`                               | Heating system type                                                                                             | `<HeatingSystemType>`          |       |          |     | JG to verify if used in test case description.                                |
| `energy_source_type`                                | Source of energy for the chiller                                                                                | `<EnergySourceTypeOptions>`    |       |          |     |                                                                               |
| `hot_water_loop`                                    | Referenced to the hot water fluid loop                                                                          | `$ID`                          |       |          |     | Constraint to use when implemented :FluidLoop:                                |
| `heat_capacity`                                     | Heating capacity                                                                                                | `Numeric`                      | W     | `≥0`     |     | The design heat capacity.                                                     |
| `oversizing_factor`                                 | The oversizing factor applied to the peak load that results in the heat capacity. Zero indicates no oversizing. | `Numeric`                      |       | `≥0`     |     | Used for furnace or heat pump. JG to verify if used in test case description. |
| `is_autosized`                                      | True if the component is automatically sized by the simulation software                                         | `Boolean`                      |       |          |     | JG to verify if used in test case description.                                |
| `heating_coil_setpoint`                             | Setpoint of the air leaving the heating coil                                                                    | `Numeric`                      | C     |          |     | JG to verify if used in test case description.                                |
| `full_load_efficiency`                              | Full Low Efficiency expressed as a coefficient of performance or thermal efficiency                             | `Numeric`                      | W/W   |          |     | Used for furnace or heat pump. JG to verify if used in test case description. |
| `part_load_efficiency`                              | Efficiency value based on the selected part_load_efficiency_metric                                              | `Numeric`                      |       | `≥0, ≤1` |     | Used for furnace or heat pump. JG to verify if used in test case description. |
| `heatpump_auxilliary_heat_type`                     | Heatpump auxilliary heat type used for backup                                                                   | `<HeatpumpAuxilliaryHeatType>` |       |          |     | JG to verify if used in test case description.                                |
| `heatpump_auxilliary_heat_high_temperature_shutoff` | Heatpump auxilliary heat high temperature shutoff                                                               | `Numeric`                      | C     |          |     | JG to verify if used in test case description.                                |
| `heatpump_low_temperature_shutoff`                  | Heatpump low temperature shutoff                                                                                | `Numeric`                      | C     |          |     | JG to verify if used in test case description.                                |
| `humidification_type`                               | Humidification type                                                                                             | `<HumidificationType>`         |       |          |     | JG to verify if used in test case description.                                |

# CoolingSystem
|           Name           |                                                   Description                                                   |        Data Type         | Units |  Range   | Req |                                                           Notes                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------|-------|----------|-----|---------------------------------------------------------------------------------------------------------------------------|
| `id`                     | Scope-unique reference identifier for instances of this data group                                              | `ID`                     |       |          | ✓   |                                                                                                                           |
| `reporting_name`         | Descriptive name used in RCT reports if id is not already a descriptive name                                    | `String`                 |       |          |     |                                                                                                                           |
| `notes`                  | Supplementary information to provide context to the model reviewer                                              | `String`                 |       |          |     |                                                                                                                           |
| `cooling_system_type`    | Cooling system type                                                                                             | `<CoolingSystemType>`    |       |          |     | JG to verify if used in test case description.                                                                            |
| `total_cool_capacity`    | Total cooling capacity                                                                                          | `Numeric`                | W     | `≥0`     |     | Designed total cooling capacity. JG to verify if used in test case description.                                           |
| `sensible_cool_capacity` | Sensible cooling capacity                                                                                       | `Numeric`                | W     | `≥0`     |     | Designed sensible cooling capacity                                                                                        |
| `oversizing_factor`      | The oversizing factor applied to the peak load that results in the heat capacity. Zero indicates no oversizing. | `Numeric`                |       | `≥0`     |     | JG to verify if used in test case description.                                                                            |
| `is_autosized`           | True if the component is automatically sized by the simulation software                                         | `Boolean`                |       |          |     | JG to verify if used in test case description.                                                                            |
| `chilled_water_loop`     | Referenced to the Chilled water fluid loop                                                                      | `$ID`                    |       |          |     | Constraint to use when implemented :FluidLoop:                                                                            |
| `condenser_water_loop`   | Referenced to the Condenser water fluid loop                                                                    | `$ID`                    |       |          |     | Constraint to use when implemented :FluidLoop:                                                                            |
| `full_load_efficiency`   | Full Low Efficiency expressed as a coefficient of performance (COP)                                             | `Numeric`                | W/W   |          |     | Used for direct expansion. JG to verify if used in test case description.                                                 |
| `part_load_efficiency`   | Efficiency value based on the selected part_load_efficiency_metric                                              | `Numeric`                |       | `≥0, ≤1` |     | Used for direct expansion. JG to verify if used in test case description.                                                 |
| `dehumidification_type`  | Dehumidification type                                                                                           | `<DehumidificationType>` |       |          |     | JG to verify if used in test case description.                                                                            |
| `cooling_turndown_ratio` | Cooling turndown ratio                                                                                          | `Numeric`                |       |          |     | Cooling capacity turndown before simultanenous heating and cooling occurs. JG to verify if used in test case description. |

# FanSystem
|                     Name                     |                                  Description                                  |                Data Type                | Units |   Range   | Req |                                                                                                                                                                      Notes                                                                                                                                                                       |
|----------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------|-------|-----------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                         | Scope-unique reference identifier for instances of this data group            | `ID`                                    |       |           | ✓   |                                                                                                                                                                                                                                                                                                                                                  |
| `reporting_name`                             | Descriptive name used in RCT reports if id is not already a descriptive name  | `String`                                |       |           |     |                                                                                                                                                                                                                                                                                                                                                  |
| `notes`                                      | Supplementary information to provide context to the model reviewer            | `String`                                |       |           |     |                                                                                                                                                                                                                                                                                                                                                  |
| `supply_fans`                                | List of supply fans                                                           | `[{Fan}]`                               |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `return_fans`                                | List of return fans                                                           | `[{Fan}]`                               |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `exhaust_fans`                               | List of exhaust fans                                                          | `[{Fan}]`                               |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `relief_fans`                                | List of relief fans                                                           | `[{Fan}]`                               |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `air_economizer`                             | Air side economizer related to the fan system                                 | `{AirEconomizer}`                       |       |           |     |                                                                                                                                                                                                                                                                                                                                                  |
| `air_energy_recovery`                        | Air side energy recovery related to the fan system                            | `{AirEnergyRecovery}`                   |       |           |     |                                                                                                                                                                                                                                                                                                                                                  |
| `is_variable_air_volume`                     | If the fan system is variable air volume.                                     | `Boolean`                               |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `temperature_control`                        | Supply air temperature control type                                           | `<FanSystemTemperatureControlType>`     |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `operation_during_occupied`                  | Operation during occupied times type                                          | `<FanSystemOperationType>`              |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `operation_during_unoccupied`                | Operation during unoccupied times type                                        | `<FanSystemOperationType>`              |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `fan_control`                                | Supply fan control type                                                       | `<FanSystemSupplyFanControlType>`       |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `supply_air_temperature_setpoint`            | Supply air temperature setpoint temperarue                                    | `Numeric`                               | C     |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `reset_differential_temperature`             | Supply air temperature reset differential temperature at minimum cooling load | `Numeric`                               | K     |           |     | When temperature_control is LOAD_RESET_TO_SPACE_TEMPERATURE this temperate is added to the supply air temperature at minimum cooling load conditions. When temperature_control is LOAD_RESET_DIFFERENTIAL_TEMPERATURE this temperate is the temperate below space tempature when no cooling load. JG to verify if used in test case description. |
| `supply_air_temperature_reset_load_fraction` | Supply air temperature reset load fraction                                    | `Numeric`                               |       |           |     | When temperature_control is a reset option this is the threshold fraction to use below which supply air temperature reset begins and ramps down to zero. JG to verify if used in test case description.                                                                                                                                          |
| `supply_air_temperature_reset_schedule`      | Supply air temperature reset schedule                                         | `$ID`                                   |       |           |     | JG to verify if used in test case description. Constraint to use when implemented :Schedule:                                                                                                                                                                                                                                                     |
| `fan_volume_reset_type`                      | Fan volume reset control type                                                 | `<FanSystemSupplyFanVolumeResetType>`   |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `fan_volume_reset_load_fraction`             | Fan volume reset load fraction                                                | `Numeric`                               |       |           |     | When fan_volume_reset_type is LOAD_RESET this is the fraction of the load for minimum air flow.  JG to verify if used in test case description.                                                                                                                                                                                                  |
| `operating_schedule`                         | Operating schedule name                                                       | `$ID`                                   |       |           |     | Zero when fan is off. JG to verify if used in test case description. Constraint to use when implemented :Schedule:                                                                                                                                                                                                                               |
| `exhaust_schedule`                           | Exhaust fan schedule name                                                     | `$ID`                                   |       |           |     | Zero when fan is off. JG to verify if used in test case description. Constraint to use when implemented :Schedule:                                                                                                                                                                                                                               |
| `minimum_airflow`                            | Minimum volume airflow                                                        | `Numeric`                               | L/s   |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `minimum_outdoor_airflow`                    | Minimum outdoor air volume airflow                                            | `Numeric`                               | L/s   |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `maximum_outdoor_airflow`                    | Maximum outdoor air volume airflow                                            | `Numeric`                               | L/s   |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `air_filter_merv_rating`                     | The MERV rating of the air filter                                             | `Numeric`                               |       | `≥1, ≤20` |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `has_fully_ducted_return`                    | If the fan system has fully ducted return.                                    | `Boolean`                               |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |
| `demand_control_ventilation_control`         | Demand control ventilation control type                                       | `<DemandControlVentilationControlType>` |       |           |     | JG to verify if used in test case description.                                                                                                                                                                                                                                                                                                   |

# AirEconomizer
|               Name               |                                 Description                                  |       Data Type       | Units | Range | Req |                     Notes                      |
|----------------------------------|------------------------------------------------------------------------------|-----------------------|-------|-------|-----|------------------------------------------------|
| `id`                             | Scope-unique reference identifier for instances of this data group           | `ID`                  |       |       | ✓   |                                                |
| `reporting_name`                 | Descriptive name used in RCT reports if id is not already a descriptive name | `String`              |       |       |     |                                                |
| `notes`                          | Supplementary information to provide context to the model reviewer           | `String`              |       |       |     |                                                |
| `type`                           | Type                                                                         | `<AirEconomizerType>` |       |       |     | JG to verify if used in test case description. |
| `high_limit_temperature_shutoff` | High limit temperature shutoff                                               | `Numeric`             | C     |       |     | JG to verify if used in test case description. |
| `design_sensible_effectiveness`  | Design sensible effectiveness                                                | `Numeric`             |       |       |     | JG to verify if used in test case description. |
| `design_latent_effectiveness`    | Design sensible effectiveness                                                | `Numeric`             |       |       |     | JG to verify if used in test case description. |

# AirEnergyRecovery
|                       Name                       |                                 Description                                  |                   Data Type                   | Units | Range | Req |                     Notes                      |
|--------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------|-------|-------|-----|------------------------------------------------|
| `id`                                             | Scope-unique reference identifier for instances of this data group           | `ID`                                          |       |       | ✓   |                                                |
| `reporting_name`                                 | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                                      |       |       |     |                                                |
| `notes`                                          | Supplementary information to provide context to the model reviewer           | `String`                                      |       |       |     |                                                |
| `energy_recovery_type`                           | Energy recovery type                                                         | `<EnergyRecoveryType>`                        |       |       |     | JG to verify if used in test case description. |
| `enthalpy_recovery_ratio`                        | Enthalpy recovery ratio                                                      | `Numeric`                                     |       |       |     | JG to verify if used in test case description. |
| `energy_recovery_operation`                      | Energy recovery operation                                                    | `<EnergyRecoveryOperation>`                   |       |       |     | JG to verify if used in test case description. |
| `energy_recovery_supply_air_temperature_control` | Energy recovery supply air temperature control                               | `<EnergyRecoverySupplyAirTemperatureControl>` |       |       |     | JG to verify if used in test case description. |

# Fan
|            Name            |                                 Description                                  |             Data Type             | Units |  Range   | Req |                                                                                                                        Notes                                                                                                                         |
|----------------------------|------------------------------------------------------------------------------|-----------------------------------|-------|----------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                       | Scope-unique reference identifier for instances of this data group           | `ID`                              |       |          | ✓   |                                                                                                                                                                                                                                                      |
| `reporting_name`           | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                          |       |          |     |                                                                                                                                                                                                                                                      |
| `notes`                    | Supplementary information to provide context to the model reviewer           | `String`                          |       |          |     |                                                                                                                                                                                                                                                      |
| `design_airflow`           | Design airflow                                                               | `Numeric`                         | L/s   |          |     | JG to verify if used in test case description.                                                                                                                                                                                                       |
| `specification_method`     | Options for how the fan is specified                                         | `<FanSpecificationMethodOptions>` |       |          |     |                                                                                                                                                                                                                                                      |
| `design_electric_power`    | Design electric fan power                                                    | `Numeric`                         | W     |          |     | Only used when specification_method is set to Simple. JG to verify if used in test case description.                                                                                                                                                 |
| `design_pressure_rise`     | Pressure rise through fan at design flow conditions                          | `Numeric`                         | m     |          |     | Only used when specification_method is set to Detailed                                                                                                                                                                                               |
| `nameplate_power`          | nameplate power of fan                                                       | `Numeric`                         | W     |          |     | Only used when specification_method is set to Detailed. JG to verify if used in test case description.                                                                                                                                               |
| `input_power`              | input power of fan                                                           | `Numeric`                         | W     |          |     | Power delivered to the fan’s shaft and does not include the mechanical drive losses. Equivalent to fan brake horsepower for inch-pound units. Only used when specification_method is set to Detailed. JG to verify if used in test case description. |
| `total_efficiency`         | Total fan efficiency                                                         | `Numeric`                         |       | `≥0, ≤1` |     | Only used when specification_method is set to Detailed.                                                                                                                                                                                              |
| `motor_efficiency`         | Fan motor efficiency                                                         | `Numeric`                         |       | `≥0, ≤1` |     | Only used when specification_method is set to Detailed.                                                                                                                                                                                              |
| `status_type`              | Choice of new, existing, addition, alteration, etc. for each ruleset.        | `<GeneralStatusType2019T24>`      |       |          |     |                                                                                                                                                                                                                                                      |
| `output_validation_points` | Energy validation points                                                     | `[{FanOutputValidationPoint}]`    |       |          |     | Airflow is input to each validation point and energy output is the result. A minimum number of four points is recommended.                                                                                                                           |

# FanOutputValidationPoint
|   Name    | Description | Data Type | Units | Range | Req |                               Notes                               |
|-----------|-------------|-----------|-------|-------|-----|-------------------------------------------------------------------|
| `airflow` | Load        | `Numeric` | L/s   |       |     | No name and id is needed since typically used as one of a series. |
| `result`  | Result      | `Numeric` | W     |       |     |                                                                   |

# Terminal
|                           Name                           |                                 Description                                  |          Data Type           | Units | Range | Req |                                                                                                      Notes                                                                                                       |
|----------------------------------------------------------|------------------------------------------------------------------------------|------------------------------|-------|-------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                                     | Scope-unique reference identifier for instances of this data group           | `ID`                         |       |       | ✓   |                                                                                                                                                                                                                  |
| `reporting_name`                                         | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                     |       |       |     |                                                                                                                                                                                                                  |
| `notes`                                                  | Supplementary information to provide context to the model reviewer           | `String`                     |       |       |     |                                                                                                                                                                                                                  |
| `type`                                                   | Type of terminal                                                             | `<TerminalType>`             |       |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `served_by_heating_ventilation_air_conditioning_systems` | HVAC systems serving the terminal                                            | `$ID`                        |       |       |     | Contains ID of the HVAC system serving the terminal - from Unique Identification Number in HeatingVentilationAirConditioningSystem. Constraint to use when implemented :HeatingVentilationAirConditioningSystem: |
| `reheat_source`                                          | Source of reheat                                                             | `<ReheatSourceType>`         |       |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `reheat_from_loop`                                       | Referenced to the fluid loop used for reheat                                 | `$ID`                        |       |       |     | Only used when reheat_source is hot water. Constraint to use when implemented :FluidLoop:                                                                                                                        |
| `fan`                                                    | Terminal fan                                                                 | `{Fan}`                      |       |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `fan_configuration`                                      | Fan configuration                                                            | `<TerminalFanConfiguration>` |       |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `primary_airflow`                                        | Zone terminal primary airflow                                                | `Numeric`                    | L/s   |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `secondary_airflow`                                      | Zone terminal secondary_airflow                                              | `Numeric`                    | L/s   |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `supply_temperature_setpoint`                            | Zone terminal supply temperature setpoint                                    | `Numeric`                    | C     |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `minimum_airflow`                                        | Zone terminal minimum volume airflow                                         | `Numeric`                    | L/s   |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `minimum_outdoor_airflow`                                | Zone terminal minimum outdoor air volume airflow                             | `Numeric`                    | L/s   |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `minimum_outdoor_airflow_multiplier_schedule`            | Zone terminal minimum outdoor air volume airflow multiplier schedule name    | `$ID`                        |       |       |     | JG to verify if used in test case description. Constraint to use when implemented :Schedule:                                                                                                                     |
| `heat_capacity`                                          | Heat capacity for baseboard or radiant system                                | `Numeric`                    | W     |       |     | JG to verify if used in test case description.                                                                                                                                                                   |
| `is_supply_ducted`                                       | True if the the supply is ducted.                                            | `Boolean`                    |       |       |     |                                                                                                                                                                                                                  |
| `is_fan_first_stage_heat`                                | True if the the fan is run as the first stage of heating before reheat coil. | `Boolean`                    |       |       |     |                                                                                                                                                                                                                  |

# FluidLoop
|                    Name                    |                                 Description                                  |           Data Type           | Units | Range | Req |                                                                                                           Notes                                                                                                            |
|--------------------------------------------|------------------------------------------------------------------------------|-------------------------------|-------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                       | Scope-unique reference identifier for instances of this data group           | `ID`                          |       |       | ✓   |                                                                                                                                                                                                                            |
| `reporting_name`                           | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                      |       |       |     |                                                                                                                                                                                                                            |
| `notes`                                    | Supplementary information to provide context to the model reviewer           | `String`                      |       |       |     |                                                                                                                                                                                                                            |
| `type`                                     | Type of loop                                                                 | `<FluidLoopTypeOptions>`      |       |       |     |                                                                                                                                                                                                                            |
| `pump_power_per_flow_rate`                 | Total design pump power divided by the loop design flow rate                 | `Numeric`                     | W/s-L |       |     | This is the pump power per flow rate for the entire pumping system on the current FluidLoop. The power and flow rate should be for the current FluidLoop only and does not include power and flow rate in any child loops. |
| `child_loops`                              | Other fluid loops connected to this one as children.                         | `[{FluidLoop}]`               |       |       |     | Secondary loops should be described as child loops.                                                                                                                                                                        |
| `cooling_or_condensing_design_and_control` |                                                                              | `{FluidLoopDesignAndControl}` |       |       |     |                                                                                                                                                                                                                            |
| `heating_design_and_control`               |                                                                              | `{FluidLoopDesignAndControl}` |       |       |     |                                                                                                                                                                                                                            |

# FluidLoopDesignAndControl
|                       Name                       |                                 Description                                  |            Data Type            | Units | Range | Req |                                                                                 Notes                                                                                 |
|--------------------------------------------------|------------------------------------------------------------------------------|---------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                             | Scope-unique reference identifier for instances of this data group           | `ID`                            |       |       | ✓   |                                                                                                                                                                       |
| `reporting_name`                                 | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                        |       |       |     |                                                                                                                                                                       |
| `notes`                                          | Supplementary information to provide context to the model reviewer           | `String`                        |       |       |     |                                                                                                                                                                       |
| `design_supply_temperature`                      | Design Supply Temperature                                                    | `Numeric`                       | C     |       |     |                                                                                                                                                                       |
| `design_return_temperature`                      | Design Return Temperature                                                    | `Numeric`                       | C     |       |     |                                                                                                                                                                       |
| `is_sized_using_coincident_load`                 | True if the loop is sized based on coincident load                           | `Boolean`                       |       |       |     |                                                                                                                                                                       |
| `minimum_flow_fraction`                          | Minimum fraction of full flow allowed                                        | `Numeric`                       |       |       |     |                                                                                                                                                                       |
| `operation`                                      | Type of operation used by loop                                               | `<FluidLoopOperationOptions>`   |       |       |     |                                                                                                                                                                       |
| `operation_schedule`                             | Operation schedule                                                           | `$ID`                           |       |       |     | One represents when the fluid loop is operating and zero when not operating. Only used when operation equals SCHEDULED. Constraint to use when implemented :Schedule: |
| `flow_control`                                   | Flow control options                                                         | `<FluidLoopFlowControlOptions>` |       |       |     |                                                                                                                                                                       |
| `temperature_reset_type`                         | Type of temperature reset used by loop                                       | `<TemperatureResetTypeOptions>` |       |       |     |                                                                                                                                                                       |
| `outdoor_high_for_loop_supply_temperature_reset` | Outdoor high for loop supply temp reset                                      | `Numeric`                       | C     |       |     | Used when temperature_reset_type = OUTSIDE_AIR_RESET                                                                                                                  |
| `outdoor_low_for_loop_supply_temperature_reset`  | Outdoor low for loop supply temp reset                                       | `Numeric`                       | C     |       |     | Used when temperature_reset_type = OUTSIDE_AIR_RESET                                                                                                                  |
| `loop_supply_temperature_at_outdoor_high`        | Loop supply temperature at outdoor high temperature                          | `Numeric`                       | C     |       |     | Used when temperature_reset_type = OUTSIDE_AIR_RESET                                                                                                                  |
| `loop_supply_temperature_at_outdoor_low`         | Loop supply temperature at outdoor low temperature                           | `Numeric`                       | C     |       |     | Used when temperature_reset_type = OUTSIDE_AIR_RESET                                                                                                                  |
| `loop_supply_temperature_at_low_load`            | Loop supply temperature at low load                                          | `Numeric`                       | C     |       |     | Used when temperature_reset_type = LOAD_RESET                                                                                                                         |

# Pump
|          Name           |                                 Description                                  |             Data Type              | Units |  Range   | Req |                                             Notes                                              |
|-------------------------|------------------------------------------------------------------------------|------------------------------------|-------|----------|-----|------------------------------------------------------------------------------------------------|
| `id`                    | Scope-unique reference identifier for instances of this data group           | `ID`                               |       |          | ✓   |                                                                                                |
| `reporting_name`        | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                           |       |          |     |                                                                                                |
| `notes`                 | Supplementary information to provide context to the model reviewer           | `String`                           |       |          |     |                                                                                                |
| `loop_or_piping`        | Referenced to the fluid loop or service water heating piping                 | `$ID`                              |       |          | ✓   | Constraint to use when implemented :FluidLoop: or :ServiceWaterPiping:                         |
| `specification_method`  | Options for how the pump is specified                                        | `<PumpSpecificationMethodOptions>` |       |          |     |                                                                                                |
| `design_electric_power` | Pump design electric power                                                   | `Numeric`                          | W     |          |     | Pump electric power at design conditions. Only used when specification_method is set to Simple |
| `motor_nameplate_power` | Pump motor nameplate power                                                   | `Numeric`                          | W     |          |     | Only used when specification_method is set to Detailed                                         |
| `design_head`           | Head of the pump at design flow conditions                                   | `Numeric`                          | m     |          |     | Only used when specification_method is set to Detailed                                         |
| `impeller_efficiency`   | Full load efficiency of the impeller                                         | `Numeric`                          |       | `≥0, ≤1` |     | Only used when specification_method is set to Detailed                                         |
| `motor_efficiency`      | Full load efficiency of the pump motor                                       | `Numeric`                          |       | `≥0, ≤1` |     | Only used when specification_method is set to Detailed                                         |
| `speed_control`         | Options for pump speed control                                               | `<PumpSpeedControlOptions>`        |       |          |     |                                                                                                |
| `design_flow`           | Design Pump Flowrate                                                         | `Numeric`                          | L/s   |          |     |                                                                                                |
| `minium_flow`           | Minimum Pump Flowrate                                                        | `Numeric`                          | L/s   |          |     |                                                                                                |
| `is_flow_autosized`     | True if the design_flow is autosized                                         | `Boolean`                          |       |          |     |                                                                                                |

# Boiler
|            Name            |                                 Description                                  |               Data Type               | Units |  Range   | Req |                                                          Notes                                                          |
|----------------------------|------------------------------------------------------------------------------|---------------------------------------|-------|----------|-----|-------------------------------------------------------------------------------------------------------------------------|
| `id`                       | Scope-unique reference identifier for instances of this data group           | `ID`                                  |       |          | ✓   |                                                                                                                         |
| `reporting_name`           | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                              |       |          |     |                                                                                                                         |
| `notes`                    | Supplementary information to provide context to the model reviewer           | `String`                              |       |          |     |                                                                                                                         |
| `loop`                     | Referenced to the fluid loop                                                 | `$ID`                                 |       |          | ✓   | Constraint to use when implemented :FluidLoop:                                                                          |
| `design_capacity`          | Heating capacity                                                             | `Numeric`                             | W     |          |     |                                                                                                                         |
| `rated_capacity`           | Heating capacity                                                             | `Numeric`                             | W     |          |     | At rating conditions.                                                                                                   |
| `minimum_load_ratio`       | Minimum fraction of full load allowed                                        | `Numeric`                             |       |          |     |                                                                                                                         |
| `draft_type`               | Combustion option                                                            | `<BoilerCombustionOptions>`           |       |          |     |                                                                                                                         |
| `energy_source_type`       | Source of energy for the boiler                                              | `<EnergySourceTypeOptions>`           |       |          |     |                                                                                                                         |
| `efficiency_metric`        | The type of efficiency metric used                                           | `<BoilerEfficiencyMetricTypeOptions>` |       |          |     |                                                                                                                         |
| `efficiency`               | Efficiency value based on the selected efficiency_metric                     | `Numeric`                             |       | `≥0, ≤1` |     |                                                                                                                         |
| `output_validation_points` | Energy validation points                                                     | `[{BoilerOutputValidationPoint}]`     |       |          |     | Load is input to each validation point and energy output is the result. A minimum number of four points is recommended. |
| `auxiliary_power`          | Auxiliary power                                                              | `Numeric`                             | W     |          |     | Power for boiler pump, combustion fan, or other auxiliary that operates when boiler operates.                           |
| `operation_lower_limit`    | Heating load range operation, lower limit                                    | `Numeric`                             | W     |          |     |                                                                                                                         |
| `operation_upper_limit`    | Heating load range operation, upper limit                                    | `Numeric`                             | W     |          |     |                                                                                                                         |

# BoilerOutputValidationPoint
|   Name   | Description | Data Type | Units | Range | Req |                               Notes                               |
|----------|-------------|-----------|-------|-------|-----|-------------------------------------------------------------------|
| `load`   | Load        | `Numeric` | W     |       |     | No name and id is needed since typically used as one of a series. |
| `result` | Result      | `Numeric` | W     |       |     |                                                                   |

# Chiller
|             Name              |                                 Description                                  |                   Data Type                    | Units |  Range   | Req |                                               Notes                                                |
|-------------------------------|------------------------------------------------------------------------------|------------------------------------------------|-------|----------|-----|----------------------------------------------------------------------------------------------------|
| `id`                          | Scope-unique reference identifier for instances of this data group           | `ID`                                           |       |          | ✓   |                                                                                                    |
| `reporting_name`              | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                                       |       |          |     |                                                                                                    |
| `notes`                       | Supplementary information to provide context to the model reviewer           | `String`                                       |       |          |     |                                                                                                    |
| `cooling_loop`                | Referenced to the cooling fluid loop                                         | `$ID`                                          |       |          | ✓   | Constraint to use when implemented :FluidLoop:                                                     |
| `condensing_loop`             | Referenced to the condensing fluid loop                                      | `$ID`                                          |       |          |     | No condensing loop name implies air-cooled chiller. Constraint to use when implemented :FluidLoop: |
| `compressor_type`             | Compressor Type                                                              | `<ChillerCompressorTypeOptions>`               |       |          |     |                                                                                                    |
| `energy_source_type`          | Source of energy for the chiller                                             | `<EnergySourceTypeOptions>`                    |       |          |     |                                                                                                    |
| `design_capacity`             | Chiller Design Cooling Capacity                                              | `Numeric`                                      | W     |          |     |                                                                                                    |
| `rated_capacity`              | Chiller Rated Cooling Capacity                                               | `Numeric`                                      | W     |          |     | At rating conditions.                                                                              |
| `minimum_load_ratio`          | Minimum fraction of full load allowed                                        | `Numeric`                                      |       |          |     |                                                                                                    |
| `design_flow_evaporator`      | Chiller evaporator design flow                                               | `Numeric`                                      | L/s   |          |     |                                                                                                    |
| `design_flow_condenser`       | Chiller condenser design flow                                                | `Numeric`                                      | L/s   |          |     |                                                                                                    |
| `full_load_efficiency`        | Full Low Efficiency expressed as a coefficient of performance (COP)          | `Numeric`                                      | W/W   |          |     |                                                                                                    |
| `part_load_efficiency`        | Efficiency value based on the selected part_load_efficiency_metric           | `Numeric`                                      |       | `≥0, ≤1` |     |                                                                                                    |
| `part_load_efficiency_metric` | The type of part load efficiency metric used                                 | `<ChillerPartLoadEfficiencyMetricTypeOptions>` |       |          |     |                                                                                                    |
| `capacity_validation_points`  | Capacity validation points                                                   | `[{ChillerCapacityValidationPoint}]`           |       |          |     |                                                                                                    |
| `power_validation_points`     | Energy validation points                                                     | `[{ChillerPowerValidationPoint}]`              |       |          |     |                                                                                                    |

# ChillerCapacityValidationPoint
|                Name                |           Description            | Data Type | Units | Range | Req |                                                                                                                                  Notes                                                                                                                                  |
|------------------------------------|----------------------------------|-----------|-------|-------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `chilled_water_supply_temperature` | Chilled water supply temperature | `Numeric` | C     |       |     | No name and id is needed since used as one of a series. The temperature is leaving the chiller.                                                                                                                                                                         |
| `condenser_temperature`            | Second temperature               | `Numeric` | C     |       |     | Outside air dry-bulb temperature for air cooled chillers and condenser water temperature for water cooled chillers. For water cooled chillers, this is the temperature as the water enters the chiller. For air cooled chilers this the temperature of the ambient air. |
| `result`                           | Result                           | `Numeric` | W     |       |     |                                                                                                                                                                                                                                                                         |

# ChillerPowerValidationPoint
|                Name                |           Description            | Data Type | Units | Range | Req |                                                                                                                                  Notes                                                                                                                                  |
|------------------------------------|----------------------------------|-----------|-------|-------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `chilled_water_supply_temperature` | Chilled water supply temperature | `Numeric` | C     |       |     | No name and id is needed since used as one of a series. The temperature is leaving the chiller.                                                                                                                                                                         |
| `condenser_temperature`            | Second temperature               | `Numeric` | C     |       |     | Outside air dry-bulb temperature for air cooled chillers and condenser water temperature for water cooled chillers. For water cooled chillers, this is the temperature as the water enters the chiller. For air cooled chilers this the temperature of the ambient air. |
| `load`                             | Load                             | `Numeric` | W     |       |     |                                                                                                                                                                                                                                                                         |
| `result`                           | Result                           | `Numeric` | W     |       |     |                                                                                                                                                                                                                                                                         |

# HeatRejection
|             Name             |                                 Description                                  |                Data Type                | Units | Range | Req |                     Notes                      |
|------------------------------|------------------------------------------------------------------------------|-----------------------------------------|-------|-------|-----|------------------------------------------------|
| `id`                         | Scope-unique reference identifier for instances of this data group           | `ID`                                    |       |       | ✓   |                                                |
| `reporting_name`             | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                                |       |       |     |                                                |
| `notes`                      | Supplementary information to provide context to the model reviewer           | `String`                                |       |       |     |                                                |
| `loop`                       | Referenced to the fluid loop                                                 | `$ID`                                   |       |       | ✓   | Constraint to use when implemented :FluidLoop: |
| `type`                       | Heat Rejection Type                                                          | `<HeatRejectionTypeOptions>`            |       |       |     |                                                |
| `fan_type`                   | Heat Rejection Fan Type                                                      | `<HeatRejectionFanTypeOptions>`         |       |       |     |                                                |
| `fluid`                      | Fluid Cooled by Heat Rejection                                               | `<HeatRejectionFluidOptions>`           |       |       |     |                                                |
| `range`                      | Heat rejection Range                                                         | `Numeric`                               | C     |       |     |                                                |
| `approach`                   | Heat rejection Approach                                                      | `Numeric`                               | C     |       |     |                                                |
| `reset_type`                 | Leaving Temperature reset strategy                                           | `<HeatRejectionResetOptions>`           |       |       |     |                                                |
| `minimum_reset_temperature`  | Minimum leaving temperature setpoint                                         | `Numeric`                               | C     |       |     |                                                |
| `fan_power`                  | Fan Power                                                                    | `Numeric`                               | W     |       |     |                                                |
| `fan_speed_control`          | Fan Speed Control Type                                                       | `<HeatRejectionFanSpeedControlOptions>` |       |       |     |                                                |
| `design_supply_temperature`  | Design leaving water temperature                                             | `Numeric`                               | C     |       |     |                                                |
| `design_wetbulb_temperature` | Design wetbulb temperature                                                   | `Numeric`                               | C     |       |     | 0.4% ASHRAE MCWB                               |
| `design_water_flowrate`      | Design condenser water flow rate                                             | `Numeric`                               | L/s   |       |     |                                                |
| `rated_water_flowrate`       | Rated condenser water flow rate                                              | `Numeric`                               | L/s   |       |     | At rating conditions.                          |

# ExternalFluidSource
|         Name         |                                 Description                                  |             Data Type              | Units | Range | Req |                     Notes                      |
|----------------------|------------------------------------------------------------------------------|------------------------------------|-------|-------|-----|------------------------------------------------|
| `id`                 | Scope-unique reference identifier for instances of this data group           | `ID`                               |       |       | ✓   |                                                |
| `reporting_name`     | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                           |       |       |     |                                                |
| `notes`              | Supplementary information to provide context to the model reviewer           | `String`                           |       |       |     |                                                |
| `loop`               | Referenced to the fluid loop                                                 | `$ID`                              |       |       | ✓   | Constraint to use when implemented :FluidLoop: |
| `type`               | Type of external fluid source                                                | `<ExternalFluidSourceTypeOptions>` |       |       |     |                                                |
| `energy_source_type` | Source of energy for the external fluid source                               | `<EnergySourceTypeOptions>`        |       |       |     |                                                |

# ServiceWaterHeatingDistributionSystem
|                        Name                         |                                                 Description                                                  |                        Data Type                         | Units |  Range   | Req |                                                                       Notes                                                                        |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-------|----------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                                | Scope-unique reference identifier for instances of this data group                                           | `ID`                                                     |       |          | ✓   |                                                                                                                                                    |
| `reporting_name`                                    | Descriptive name used in RCT reports if id is not already a descriptive name                                 | `String`                                                 |       |          |     |                                                                                                                                                    |
| `notes`                                             | Supplementary information to provide context to the model reviewer                                           | `String`                                                 |       |          |     |                                                                                                                                                    |
| `design_supply_temperature`                         | Design supply temperature setpoint of service water heating loop                                             | `Numeric`                                                | C     |          |     | From CBECC-Com.                                                                                                                                    |
| `design_supply_temperature_difference`              | Design supply temperature difference (deltaT) of service water heating loop                                  | `Numeric`                                                | C     |          |     | From CBECC-Com.                                                                                                                                    |
| `tanks`                                             | Tanks within service water heating distribution system                                                       | `[{Tank}]`                                               |       |          |     | Contains a list of storage tanks that are part of this service water heating distribution system but not part of individual service water heaters. |
| `is_central_system`                                 | Indicates whether it is a central service water heater distribution system                                   | `Boolean`                                                |       |          |     | From CBECC-Com.                                                                                                                                    |
| `service_water_piping`                              | Other service water piping connected to this one as children.                                                | `[{ServiceWaterPiping}]`                                 |       |          |     |                                                                                                                                                    |
| `distribution_compactness`                          | Type of compact distribution system                                                                          | `<ServiceWaterHeatingDistributionCompactness2019T24Com>` |       |          |     | From CBECC-Com.                                                                                                                                    |
| `control_type`                                      | Type of distribution system                                                                                  | `<ServiceWaterHeatingControlType2019T24Com>`             |       |          |     | From CBECC-Com.                                                                                                                                    |
| `configuration_type`                                | Type of configuration                                                                                        | `<ServiceWaterHeatingConfigurationType>`                 |       |          |     | From CBECC-Com.                                                                                                                                    |
| `is_recovered_heat_from_drain_used_by_water_heater` | Indicates whether the recovered heat from the shower drain used by the service water heater                  | `Boolean`                                                |       |          |     | From CBECC-Res.                                                                                                                                    |
| `drain_heat_recovery_efficiency`                    | Shower heat drain recovery efficiency                                                                        | `Numeric`                                                |       | `≥0, ≤1` |     | From CBECC-Com. May use the Canadian Standards Association Rated Recovery Efficiency.                                                              |
| `drain_heat_recovery_type`                          | Drain heat recovery type                                                                                     | `<ServiceWaterHeatingHeatRecoveryType>`                  |       |          |     | From CBECC-Res.                                                                                                                                    |
| `flow_multiplier_schedule`                          | service water heating Loop flow muliplier schedule name                                                      | `$ID`                                                    |       |          |     | Constraint to use when implemented :Schedule:                                                                                                      |
| `entering_water_mains_temperature_schedule`         | Temperature schedule for unheated entering water to the building site often referenced as mains temperature. | `$ID`                                                    |       |          |     | Constraint to use when implemented :Schedule:                                                                                                      |
| `is_ground_temperature_used_for_entering_water`     | Indicates whether ground temperature is the source of the entering water temperature                         | `Boolean`                                                |       |          |     |                                                                                                                                                    |

# ServiceWaterPiping
|             Name             |                                           Description                                            |        Data Type         | Units | Range | Req |                           Notes                           |
|------------------------------|--------------------------------------------------------------------------------------------------|--------------------------|-------|-------|-----|-----------------------------------------------------------|
| `id`                         | Scope-unique reference identifier for instances of this data group                               | `ID`                     |       |       | ✓   |                                                           |
| `reporting_name`             | Descriptive name used in RCT reports if id is not already a descriptive name                     | `String`                 |       |       |     |                                                           |
| `notes`                      | Supplementary information to provide context to the model reviewer                               | `String`                 |       |       |     |                                                           |
| `is_recirculation_loop`      | Indicates if service water heating piping is a loop and recirculates                             | `Boolean`                |       |       |     |                                                           |
| `insulation_thickness`       | Pipe insulation thickness                                                                        | `Numeric`                | m     | `≥0`  |     | From CBECC-Com.                                           |
| `loop_pipe_location`         | Loop pipe location                                                                               | `<ComponentLocation>`    |       |       |     | From CBECC-Com.                                           |
| `zone_location`              | Zone reference of where the component is located when IN_ZONE is selected from ComponentLocation | `$ID`                    |       |       |     | From CBECC-Com. Constraint to use when implemented :Zone: |
| `length`                     | Pipe length                                                                                      | `Numeric`                | m     | `≥0`  |     | From RESNET                                               |
| `diameter`                   | Pipe section diameter                                                                            | `Numeric`                | m     | `≥0`  |     | From CBECC-Res.                                           |
| `child_service_water_piping` | Other service water piping connected to this one as children.                                    | `[{ServiceWaterPiping}]` |       |       |     |                                                           |

# SolarThermal
|             Name             |                                 Description                                  | Data Type | Units | Range | Req |                               Notes                               |
|------------------------------|------------------------------------------------------------------------------|-----------|-------|-------|-----|-------------------------------------------------------------------|
| `id`                         | Scope-unique reference identifier for instances of this data group           | `ID`      |       |       | ✓   |                                                                   |
| `reporting_name`             | Descriptive name used in RCT reports if id is not already a descriptive name | `String`  |       |       |     |                                                                   |
| `notes`                      | Supplementary information to provide context to the model reviewer           | `String`  |       |       |     |                                                                   |
| `angle_from_true_north`      | Solar heater angle from true north, clockwise                                | `Numeric` |       |       |     | From CBECC-Com.                                                   |
| `solar_savings_fraction`     | Solar savings fraction                                                       | `Numeric` |       |       |     | Based on ICC-SRCC rating. From CBECC-Com.                         |
| `collector_area`             | Solar collector area                                                         | `Numeric` |       |       |     | From CBECC-Com.                                                   |
| `collector_type_description` | Description of solar collector type                                          | `String`  |       |       |     | From CBECC-Com.                                                   |
| `collector_slope`            | Solar slope from horizontal                                                  | `Numeric` |       |       |     | From CBECC-Com.                                                   |
| `tank`                       | Tank that is part of the solar thermal system                                | `{Tank}`  |       |       |     | Contains a storage tank that is part of the solar thermal system. |

# ServiceWaterHeatingEquipment
|                    Name                     |                                 Description                                  |                    Data Type                     | Units | Range | Req |                                                   Notes                                                   |
|---------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------|
| `id`                                        | Scope-unique reference identifier for instances of this data group           | `ID`                                             |       |       | ✓   |                                                                                                           |
| `reporting_name`                            | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                                         |       |       |     |                                                                                                           |
| `notes`                                     | Supplementary information to provide context to the model reviewer           | `String`                                         |       |       |     |                                                                                                           |
| `heater_fuel_type`                          | Service water heating heater fuel type                                       | `<EnergySourceTypeOptions>`                      |       |       |     |                                                                                                           |
| `service_water_heating_distribution_system` | Referenced to the service water heating distribution system                  | `$ID`                                            |       |       | ✓   | Constraint to use when implemented :ServiceWaterHeatingDistributionSystem:                                |
| `energy_factor`                             | Energy factor                                                                | `Numeric`                                        |       | `≥0`  |     | From CBECC-Com.                                                                                           |
| `thermal_efficiency`                        | Service water heating heater thermal efficiency                              | `Numeric`                                        |       | `≥0`  |     |                                                                                                           |
| `standby_loss_fraction`                     | Standby loss fraction                                                        | `Numeric`                                        |       |       |     | From CBECC-Com.                                                                                           |
| `uniform_energy_factor`                     | Uniform energy factor                                                        | `Numeric`                                        |       | `≥0`  |     | From CBECC-Com.                                                                                           |
| `first_hour_rating`                         | First hour rating volume                                                     | `Numeric`                                        | L     | `≥0`  |     | From CBECC-Com.                                                                                           |
| `output_validation_points`                  | Capacity validation points                                                   | `[{ServiceWaterHeaterValidationPoint}]`          |       |       |     |                                                                                                           |
| `input_power`                               | Input power                                                                  | `Numeric`                                        | W     | `≥0`  |     | From CBECC-Com.                                                                                           |
| `rated_capacity`                            | Rated capacity                                                               | `Numeric`                                        | W     |       |     | From CBECC-Com.                                                                                           |
| `minimum_capacity`                          | Minimum capacity                                                             | `Numeric`                                        | W     | `≥0`  |     | From CBECC-Com.                                                                                           |
| `recovery_efficiency`                       | Recovery efficiency                                                          | `Numeric`                                        |       |       |     | From CBECC-Com.                                                                                           |
| `setpoint_temperature`                      | Set point temperature                                                        | `Numeric`                                        | C     |       |     |                                                                                                           |
| `compressor_location`                       | Description of where the heat pump for the water heater is located           | `String`                                         |       |       |     | Used when compressor is not located in a specific zone. From CBECC-Com.                                   |
| `compressor_zone`                           | Zone reference of where the heat pump for the water heater is located        | `$ID`                                            |       |       |     | From CBECC-Com. Constraint to use when implemented :Zone:                                                 |
| `compressor_heat_rejection_source`          | Heat pump heat rejection source                                              | `<ComponentLocation>`                            |       |       |     | From CBECC-Res.                                                                                           |
| `compressor_heat_rejection_zone`            | Heat pump heat rejection zone                                                | `$ID`                                            |       |       |     | From CBECC-Res. Constraint to use when implemented :Zone:                                                 |
| `compressor_capacity_validation_points`     | Capacity validation points                                                   | `[{HeatPumpWaterHeaterCapacityValidationPoint}]` |       |       |     |                                                                                                           |
| `compressor_power_validation_points`        | Coefficient of performance validation points                                 | `[{HeatPumpWaterHeaterPowerValidationPoint}]`    |       |       |     |                                                                                                           |
| `draft_fan_power`                           | Power for the draft fan                                                      | `Numeric`                                        | W     | `≥0`  |     | From CBECC-Com.                                                                                           |
| `has_electrical_ignition`                   | Indicates whether the water heater has electrical ignition                   | `Boolean`                                        |       |       |     | From CBECC-Com.                                                                                           |
| `heater_type`                               | Service water heater type                                                    | `<ServiceWaterHeaterType>`                       |       |       |     |                                                                                                           |
| `tank`                                      | Tank that is part of the service water heating equipment                     | `{Tank}`                                         |       |       |     | Contains a storage tank that is part of the service water heating equipment.                              |
| `status_type`                               | Choice of new, existing, addition, alteration, etc. for each ruleset.        | `<GeneralStatusType2019T24>`                     |       |       |     |                                                                                                           |
| `solar_thermal_systems`                     | Solar thermal systems used for heating service water                         | `[{SolarThermal}]`                               |       |       |     | Contains a list of Solar thermal systems that are part of this service water heating distribution system. |

# ServiceWaterHeaterValidationPoint
|   Name   | Description | Data Type | Units | Range | Req |                               Notes                               |
|----------|-------------|-----------|-------|-------|-----|-------------------------------------------------------------------|
| `load`   | Load        | `Numeric` | W     |       |     | No name and id is needed since typically used as one of a series. |
| `result` | Result      | `Numeric` | W     |       |     |                                                                   |

# HeatPumpWaterHeaterCapacityValidationPoint
|             Name              |               Description               | Data Type | Units | Range | Req |                          Notes                           |
|-------------------------------|-----------------------------------------|-----------|-------|-------|-----|----------------------------------------------------------|
| `evaporator_air_temperature`  | Outside dry bulb temperatures of air    | `Numeric` | C     |       |     | No name and id is needed since used as one of a series.  |
| `condenser_water_temperature` | Entering condenser temperature of water | `Numeric` | C     |       |     |                                                          |
| `evaporator_air_flow`         | Air flow across evaporator              | `Numeric` | L/s   |       |     |                                                          |
| `condenser_water_flow`        | Water flow across condenser             | `Numeric` | L/s   |       |     |                                                          |
| `result`                      | Result                                  | `Numeric` | W     |       |     |                                                          |

# HeatPumpWaterHeaterPowerValidationPoint
|             Name              |               Description               | Data Type | Units | Range | Req |                          Notes                           |
|-------------------------------|-----------------------------------------|-----------|-------|-------|-----|----------------------------------------------------------|
| `evaporator_air_temperature`  | Outside dry bulb temperatures of air    | `Numeric` | C     |       |     | No name and id is needed since used as one of a series.  |
| `condenser_water_temperature` | Entering condenser temperature of water | `Numeric` | C     |       |     |                                                          |
| `evaporator_air_flow`         | Air flow across evaporator              | `Numeric` | L/s   |       |     |                                                          |
| `condenser_water_flow`        | Water flow across condenser             | `Numeric` | L/s   |       |     |                                                          |
| `load`                        | Load                                    | `Numeric` | W     |       |     |                                                          |
| `result`                      | Result                                  | `Numeric` | W     |       |     |                                                          |

# Tank
|         Name          |                                 Description                                  |           Data Type            | Units  | Range | Req |                                                              Notes                                                              |
|-----------------------|------------------------------------------------------------------------------|--------------------------------|--------|-------|-----|---------------------------------------------------------------------------------------------------------------------------------|
| `id`                  | Scope-unique reference identifier for instances of this data group           | `ID`                           |        |       | ✓   |                                                                                                                                 |
| `reporting_name`      | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                       |        |       |     |                                                                                                                                 |
| `notes`               | Supplementary information to provide context to the model reviewer           | `String`                       |        |       |     |                                                                                                                                 |
| `storage_capacity`    | Storage capacity of tank in distribution system                              | `Numeric`                      | L      | `≥0`  |     | From CBECC-Com.                                                                                                                 |
| `type`                | Service water heater tank type                                               | `<ServiceWaterHeaterTankType>` |        |       |     |                                                                                                                                 |
| `height`              | Tank height                                                                  | `Numeric`                      | m      | `≥0`  |     | From CBECC-Com.                                                                                                                 |
| `interior_insulation` | Tank interior insulation R-value                                             | `Numeric`                      | K-m2/W | `≥0`  |     | Insulation that is part of the tank and is inside of the housing. From CBECC-Res.                                               |
| `exterior_insulation` | Tank interior insulation R-value                                             | `Numeric`                      | K-m2/W | `≥0`  |     | A blanket of insulation that surrounds the exterior of the tank. From CBECC-Res.                                                |
| `location`            | Location                                                                     | `<ComponentLocation>`          |        |       |     | From CBECC-Res.                                                                                                                 |
| `location_zone`       | Tank zone location                                                           | `$ID`                          |        |       |     | Only used when tank_location indicates the tank is located in a zone. From CBECC-Res. Constraint to use when implemented :Zone: |

# ServiceWaterHeatingUse
|                    Name                    |                                     Description                                      |                   Data Type                   | Units | Range | Req |                                           Notes                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------|-------|-------|-----|--------------------------------------------------------------------------------------------|
| `id`                                       | Scope-unique reference identifier for instances of this data group                   | `ID`                                          |       |       | ✓   |                                                                                            |
| `reporting_name`                           | Descriptive name used in RCT reports if id is not already a descriptive name         | `String`                                      |       |       |     |                                                                                            |
| `notes`                                    | Supplementary information to provide context to the model reviewer                   | `String`                                      |       |       |     |                                                                                            |
| `area_type`                                | Service Water Heating Loop Area Type                                                 | `<ServiceWaterHeatingSpaceType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used.                                             |
| `water_serves_type`                        | The use of the water serves the type                                                 | `<ServiceWaterHeatingFixtureType>`            |       |       |     |                                                                                            |
| `served_by_distribution_system`            | ID fo the ServiceWaterHeatingDistributionSystem that serves this end use             | `$ID`                                         |       |       |     | From CBECC-Res. Constraint to use when implemented :ServiceWaterHeatingDistributionSystem: |
| `use`                                      | Usage of service hot water                                                           | `Numeric`                                     |       |       |     |                                                                                            |
| `use_units`                                | Type of units for use of service hot water                                           | `<ServiceWaterHeatingUseUnits>`               |       |       |     |                                                                                            |
| `use_multiplier_schedule`                  | Reference to the schedule containing the multiplier for the use of service hot water | `$ID`                                         |       |       | ✓   | Constraint to use when implemented :Schedule:                                              |
| `temperature_at_fixture`                   | Reference to the schedule containing the multiplier for the use of service hot water | `Numeric`                                     | C     |       |     | From RESNET                                                                                |
| `is_heat_recovered_by_drain`               | Indicates if heat is being recovered from the drain                                  | `Boolean`                                     |       |       |     | From CBECC-Res.                                                                            |
| `is_recovered_heat_used_by_cold_side_feed` | Indicates if heat is being recovered from the drain is used on the cold side feed    | `Boolean`                                     |       |       |     | From CBECC-Res.                                                                            |

# ExteriorLighting
|       Name       |                                 Description                                  |                   Data Type                    | Units | Range | Req |                              Notes                              |
|------------------|------------------------------------------------------------------------------|------------------------------------------------|-------|-------|-----|-----------------------------------------------------------------|
| `id`             | Scope-unique reference identifier for instances of this data group           | `ID`                                           |       |       | ✓   |                                                                 |
| `reporting_name` | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                                       |       |       |     |                                                                 |
| `notes`          | Supplementary information to provide context to the model reviewer           | `String`                                       |       |       |     |                                                                 |
| `type`           | The type of exterior lighting fixture  none                                  | `<ExteriorLightingAreas2019ASHRAE901TableG36>` |       |       |     |                                                                 |
| `area`           | Area of the exterior functional space.                                       | `Numeric`                                      | m2    | `>0`  |     |                                                                 |
| `length`         | Linear length measure for exterior functional space                          | `Numeric`                                      | m     | `≥0`  |     | For example, used when expressing street frontage or door width |
| `power`          | Nominal power  of exterior lighting fixtures                                 | `Numeric`                                      | W     | `>0`  |     |                                                                 |
| `fixture_height` | Installation height of exterior fixture                                      | `Numeric`                                      | m     | `>0`  |     |                                                                 |

# Refrigeration
|            Name             |                                 Description                                  |           Data Type            | Units |   Range   | Req |                                      Notes                                       |
|-----------------------------|------------------------------------------------------------------------------|--------------------------------|-------|-----------|-----|----------------------------------------------------------------------------------|
| `id`                        | Scope-unique reference identifier for instances of this data group           | `ID`                           |       |           | ✓   |                                                                                  |
| `reporting_name`            | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                       |       |           |     |                                                                                  |
| `notes`                     | Supplementary information to provide context to the model reviewer           | `String`                       |       |           |     |                                                                                  |
| `type`                      | Refrigeration equipment type                                                 | `<RefrigerationType>`          |       |           |     |                                                                                  |
| `equipment_category`        | Equipment Class from referenced standard                                     | `<RefrigerationCategory>`      |       |           |     |                                                                                  |
| `is_self_contained`         | Indicates whether unit is self-contained                                     | `Boolean`                      |       |           |     | If not self-contained, show as false, and indicates that it has remote condenser |
| `application_temperature`   | Equipment application temperature                                            | `<ApplicationTemperatureType>` |       |           |     | Based on AHRI 1200                                                               |
| `power`                     | Nominal power of refrigeration                                               | `Numeric`                      | W     | `>0`      |     |                                                                                  |
| `power_multiplier_schedule` | Refrigeration power multiplier schedule name                                 | `$ID`                          |       |           |     | Constraint to use when implemented :Schedule:                                    |
| `sensible_fraction`         | Fraction of energy that is a sensible load on the space.                     | `Numeric`                      |       | `≥-1, ≤1` |     |                                                                                  |
| `heat_gain_fraction`        | Fraction of energy that is a heat gain to the space.                         | `Numeric`                      |       | `≥-1, ≤1` |     |                                                                                  |
| `case_volume`               | volume of a refrigerated case in cubic meters                                | `Numeric`                      | m3    |           |     |                                                                                  |
| `total_display_area`        | display area of a refrigerated case in square meters                         | `Numeric`                      | m2    |           |     |                                                                                  |
| `zone_case_location`        | Zone where case is located                                                   | `$ID`                          |       |           |     |                                                                                  |

# OverallSimulationOutputs
|                       Name                        |                                 Description                                  | Data Type | Units | Range | Req |                     Notes                      |
|---------------------------------------------------|------------------------------------------------------------------------------|-----------|-------|-------|-----|------------------------------------------------|
| `id`                                              | Scope-unique reference identifier for instances of this data group           | `ID`      |       |       | ✓   |                                                |
| `reporting_name`                                  | Descriptive name used in RCT reports if id is not already a descriptive name | `String`  |       |       |     |                                                |
| `notes`                                           | Supplementary information to provide context to the model reviewer           | `String`  |       |       |     |                                                |
| `refrigeration_energy_enduse`                     | Annual refrigeration energy end use from simulation output                   | `Numeric` | kWh   |       |     |                                                |
| `service_water_heating_annual_enduse_electricity` | Annual electricity energy end_use for SWH loops                              | `Numeric` | kWh   | `≥0`  |     |                                                |
| `service_water_heating_annual_enduse_fossilfuel`  | Annual fossil fuel energy end_use for SWH loops                              | `Numeric` | J     | `≥0`  |     |                                                |
| `unmet_heating_load_hours`                        | total hours any HVAC Zone heating temperature setpoint not met               | `Numeric` | J     | `≥0`  |     | JG to verify if used in test case description. |
| `unmet_cooling_load_hours`                        | total hours any HVAC Zone cooling temperature setpoint not met               | `Numeric` | J     | `≥0`  |     | JG to verify if used in test case description. |

