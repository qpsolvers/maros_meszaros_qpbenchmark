# Maros-Meszaros dense subset

| Number of problems | 62 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-09-07 14:57:17.966508+00:00 |
| CPU                | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
| Run by             | [@stephane-caron](https://github.com/stephane-caron/) |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [CPU info](#cpu-info)
* [Known limitations](#known-limitations)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [High accuracy](#high-accuracy)
    * [Low accuracy](#low-accuracy)
    * [Mid accuracy](#mid-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)

## Description

Subset of the Maros-Meszaros test set restricted to smaller dense problems.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.9.0                 |
| cvxopt   | 1.3.2                 |
| daqp     | 0.5.1                 |
| ecos     | 2.0.14                |
| gurobi   | 11.0.3 (size-limited) |
| highs    | 1.7.2                 |
| hpipm    | 0.2                   |
| osqp     | 0.6.7.post0           |
| piqp     | 0.4.1                 |
| proxqp   | 0.6.6                 |
| qpalm    | 1.2.3                 |
| qpoases  | 3.2.1                 |
| quadprog | 0.1.12                |
| scs      | 3.2.6                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.3.3.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| `count` | 4 |
| `cpuinfo_version_string` | 9.0.0 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_perfmon`, `art`, `avx`, `avx2`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fxsr`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `ibpb`, `ibrs`, `ida`, `intel_pt`, `invpcid`, `invpcid_single`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `mpx`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pti`, `pts`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `sgx`, `smap`, `smep`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tscdeadline`, `vme`, `vmx`, `vnmi`, `vpid`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `hz_actual_friendly` | 2.6000 GHz |
| `hz_advertised_friendly` | 2.5000 GHz |
| `l1_data_cache_size` | 65536 |
| `l1_instruction_cache_size` | 65536 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 256 |
| `l2_cache_size` | 524288 |
| `l3_cache_size` | 4194304 |
| `model` | 78 |
| `python_version` | 3.12.4.final.0 (64 bit) |
| `stepping` | 3 |
| `vendor_id_raw` | GenuineIntel |

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |      1000 |        1000     |       1000     |       1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   | high_accuracy   | low_accuracy   | mid_accuracy   |
|:---------|:---------------------------------|:----------|:----------------|:---------------|:---------------|
| clarabel | ``tol_feas``                     | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_rel``                  | -         | 0.0             | 0.0            | 0.0            |
| cvxopt   | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``dual_tol``                     | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``primal_tol``                   | -         | 1e-09           | 0.001          | 1e-06          |
| ecos     | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09           | 0.001          | 1e-06          |
| gurobi   | ``OptimalityTol``                | -         | 1e-09           | 0.001          | 1e-06          |
| gurobi   | ``TimeLimit``                    | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| hpipm    | ``tol_comp``                     | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_eq``                       | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_ineq``                     | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_stat``                     | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| piqp     | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| qpalm    | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| qpoases  | ``predefined_options``           | default   | reliable        | fast           | -              |
| qpoases  | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| scs      | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| scs      | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| scs      | ``time_limit_secs``              | 1000.0    | 1000.0          | 1000.0         | 1000.0         |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                51.6 |                              20793.9 |                                 304539748.1 |                                 84505.9 |                                 2.4 |
| cvxopt   |                                66.1 |                               5835.1 |                                 160672590.1 |                                 44582.8 |                                 5.8 |
| daqp     |                                30.6 |                              58795.1 |                                 440931769.1 |                                122347.0 |                                 3.4 |
| ecos     |                                12.9 |                             126497.0 |                                 547719105.2 |                                155901.6 |                                 4.2 |
| gurobi   |                                56.5 |                              16132.9 |                                 273449877.0 |                                 75875.2 |                                 2.1 |
| highs    |                                72.6 |                               1364.7 |                                  49787378.8 |                                 14012.1 |                                23.6 |
| hpipm    |                                24.2 |                              20794.6 |                                4812749808.5 |                                 84501.8 |                                 2.4 |
| osqp     |                                51.6 |                               1409.0 |                                3404366339.9 |                                592424.2 |                               577.2 |
| piqp     |                                98.4 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.1 |
| proxqp   |                                85.5 |                               2067.5 |                                  79843142.0 |                                 22154.3 |                                 1.0 |
| qpalm    |                                59.7 |                                198.1 |                                 448093182.1 |                                 37815.9 |                               147.2 |
| qpoases  |                                24.2 |                              17999.9 |                                4409382869.3 |                               3869853.2 |                                 2.2 |
| quadprog |                                32.3 |                              54380.5 |                                 430342953.5 |                                119408.9 |                                 3.3 |
| scs      |                                71.0 |                                440.7 |                                1837055027.2 |                                 61344.3 |                                71.4 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                43.5 |                                 20.1 |                                         4.6 |                                     5.1 |                                 1.9 |
| cvxopt   |                                 8.1 |                                  7.0 |                                         7.7 |                                   777.4 |                         841504147.6 |
| daqp     |                                24.2 |                                 56.4 |                                       299.6 |                                     3.5 |                           1363649.6 |
| ecos     |                                 0.0 |                                112.3 |                                         7.8 |                              24030498.5 |                           1008053.0 |
| gurobi   |                                16.1 |                                 14.3 |                                         4.3 |                                   581.0 |                             13358.4 |
| highs    |                                 0.0 |                                  1.5 |                                     14897.3 |                               5219407.6 |                       10340470841.6 |
| hpipm    |                                41.9 |                                 25.6 |                                         5.0 |                                     2.7 |                                 5.2 |
| osqp     |                                41.9 |                                 18.5 |                                         5.1 |                                     2.7 |                                 3.7 |
| piqp     |                                80.6 |                                  1.0 |                                         1.0 |                                     1.2 |                                 5.3 |
| proxqp   |                                75.8 |                                  2.8 |                                         2.2 |                                     1.0 |                                 2.4 |
| qpalm    |                                46.8 |                                  6.9 |                                         3.7 |                                     1.8 |                               291.1 |
| qpoases  |                                19.4 |                                 17.7 |                               55892436445.8 |                           95778787657.2 |                                 1.7 |
| quadprog |                                25.8 |                                 48.3 |                                        11.6 |                                    13.0 |                                11.5 |
| scs      |                                67.7 |                                  7.6 |                                         3.4 |                                     1.9 |                                 1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                48.4 |                              26095.2 |                                       150.7 |                                     6.2 |                                 2.7 |
| cvxopt   |                                51.6 |                               6589.8 |                                        75.4 |                                     2.8 |                              3672.6 |
| daqp     |                                25.8 |                              73786.0 |                                       261.7 |                                     7.7 |                                 5.4 |
| ecos     |                                11.3 |                             171259.8 |                                       271.3 |                                    10.9 |                                 3.7 |
| gurobi   |                                56.5 |                              20245.5 |                                       135.6 |                                     4.8 |                                 1.8 |
| highs    |                                58.1 |                                510.1 |                                        10.6 |                                     7.5 |                             19917.3 |
| hpipm    |                                35.5 |                              33412.9 |                                       167.0 |                                     6.2 |                                14.8 |
| osqp     |                                38.7 |                              15569.4 |                                       145.6 |                                     5.9 |                               563.3 |
| piqp     |                               100.0 |                                  1.0 |                                         1.0 |                                     1.2 |                                 1.0 |
| proxqp   |                                82.3 |                               2593.5 |                                        54.0 |                                     1.5 |                                40.3 |
| qpalm    |                                56.5 |                                250.6 |                                        60.6 |                                     1.0 |                              4435.3 |
| qpoases  |                                19.4 |                              26184.2 |                                   1244352.5 |                                150752.3 |                                 2.0 |
| quadprog |                                32.3 |                              68246.7 |                                       211.0 |                                     7.5 |                                 2.8 |
| scs      |                                80.6 |                               4618.3 |                                        94.1 |                                     3.1 |                                 1.5 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                50.0 |                                116.6 |                                        28.9 |                                     8.4 |                                 2.9 |
| cvxopt   |                                35.5 |                                 27.1 |                                        14.1 |                                    90.7 |                           4185008.3 |
| daqp     |                                25.8 |                                303.4 |                                        47.2 |                                    10.7 |                              2879.5 |
| ecos     |                                 1.6 |                                652.7 |                                        49.4 |                               7839634.2 |                            781855.6 |
| gurobi   |                                41.9 |                                 83.3 |                                        25.2 |                                     8.6 |                                30.2 |
| highs    |                                41.9 |                                  4.5 |                                        98.1 |                                 17106.6 |                          22835974.2 |
| hpipm    |                                41.9 |                                149.0 |                                        31.7 |                                     8.8 |                                 5.2 |
| osqp     |                                41.9 |                                 83.2 |                                        27.7 |                                     8.9 |                                10.0 |
| piqp     |                                98.4 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                87.1 |                                 10.7 |                                        11.1 |                                     2.3 |                                 1.5 |
| qpalm    |                                53.2 |                                  4.5 |                                        13.8 |                                     1.7 |                             20336.5 |
| qpoases  |                                19.4 |                                 85.3 |                                 778371782.1 |                             311509421.3 |                                 3.4 |
| quadprog |                                32.3 |                                280.6 |                                        39.2 |                                    10.5 |                                 3.2 |
| scs      |                                74.2 |                                 29.7 |                                        18.4 |                                     5.2 |                                 1.8 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        52 |              44 |             48 |             50 |
| cvxopt   |        66 |               8 |             52 |             35 |
| daqp     |        31 |              24 |             26 |             26 |
| ecos     |        13 |               0 |             11 |              2 |
| gurobi   |        56 |              16 |             56 |             42 |
| highs    |        73 |               0 |             58 |             42 |
| hpipm    |        24 |              42 |             35 |             42 |
| osqp     |        52 |              42 |             39 |             42 |
| piqp     |        98 |              81 |            100 |             98 |
| proxqp   |        85 |              76 |             82 |             87 |
| qpalm    |        60 |              47 |             56 |             53 |
| qpoases  |        24 |              19 |             19 |             19 |
| quadprog |        32 |              26 |             32 |             32 |
| scs      |        71 |              68 |             81 |             74 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              94 |             97 |            100 |
| cvxopt   |        92 |              39 |             76 |             60 |
| daqp     |       100 |              95 |             95 |             95 |
| ecos     |        98 |              85 |             98 |             87 |
| gurobi   |       100 |              60 |            100 |             85 |
| highs    |        81 |              10 |             61 |             48 |
| hpipm    |        73 |              97 |             89 |             97 |
| osqp     |        61 |              90 |             77 |             85 |
| piqp     |        98 |              89 |            100 |            100 |
| proxqp   |        98 |              94 |             95 |            100 |
| qpalm    |        61 |              77 |             58 |             60 |
| qpoases  |        69 |              65 |             68 |             63 |
| quadprog |       100 |              94 |            100 |            100 |
| scs      |        74 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   20793.9 |            20.1 |        26095.2 |          116.6 |
| cvxopt   |    5835.1 |             7.0 |         6589.8 |           27.1 |
| daqp     |   58795.1 |            56.4 |        73786.0 |          303.4 |
| ecos     |  126497.0 |           112.3 |       171259.8 |          652.7 |
| gurobi   |   16132.9 |            14.3 |        20245.5 |           83.3 |
| highs    |    1364.7 |             1.5 |          510.1 |            4.5 |
| hpipm    |   20794.6 |            25.6 |        33412.9 |          149.0 |
| osqp     |    1409.0 |            18.5 |        15569.4 |           83.2 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |    2067.5 |             2.8 |         2593.5 |           10.7 |
| qpalm    |     198.1 |             6.9 |          250.6 |            4.5 |
| qpoases  |   17999.9 |            17.7 |        26184.2 |           85.3 |
| quadprog |   54380.5 |            48.3 |        68246.7 |          280.6 |
| scs      |     440.7 |             7.6 |         4618.3 |           29.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |      default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|-------------:|----------------:|---------------:|---------------:|
| clarabel |  304539748.1 |             4.6 |          150.7 |           28.9 |
| cvxopt   |  160672590.1 |             7.7 |           75.4 |           14.1 |
| daqp     |  440931769.1 |           299.6 |          261.7 |           47.2 |
| ecos     |  547719105.2 |             7.8 |          271.3 |           49.4 |
| gurobi   |  273449877.0 |             4.3 |          135.6 |           25.2 |
| highs    |   49787378.8 |         14897.3 |           10.6 |           98.1 |
| hpipm    | 4812749808.5 |             5.0 |          167.0 |           31.7 |
| osqp     | 3404366339.9 |             5.1 |          145.6 |           27.7 |
| piqp     |          1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |   79843142.0 |             2.2 |           54.0 |           11.1 |
| qpalm    |  448093182.1 |             3.7 |           60.6 |           13.8 |
| qpoases  | 4409382869.3 |   55892436445.8 |      1244352.5 |    778371782.1 |
| quadprog |  430342953.5 |            11.6 |          211.0 |           39.2 |
| scs      | 1837055027.2 |             3.4 |           94.1 |           18.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   84505.9 |             5.1 |            6.2 |            8.4 |
| cvxopt   |   44582.8 |           777.4 |            2.8 |           90.7 |
| daqp     |  122347.0 |             3.5 |            7.7 |           10.7 |
| ecos     |  155901.6 |      24030498.5 |           10.9 |      7839634.2 |
| gurobi   |   75875.2 |           581.0 |            4.8 |            8.6 |
| highs    |   14012.1 |       5219407.6 |            7.5 |        17106.6 |
| hpipm    |   84501.8 |             2.7 |            6.2 |            8.8 |
| osqp     |  592424.2 |             2.7 |            5.9 |            8.9 |
| piqp     |       1.0 |             1.2 |            1.2 |            1.0 |
| proxqp   |   22154.3 |             1.0 |            1.5 |            2.3 |
| qpalm    |   37815.9 |             1.8 |            1.0 |            1.7 |
| qpoases  | 3869853.2 |   95778787657.2 |       150752.3 |    311509421.3 |
| quadprog |  119408.9 |            13.0 |            7.5 |           10.5 |
| scs      |   61344.3 |             1.9 |            3.1 |            5.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       2.4 |             1.9 |            2.7 |            2.9 |
| cvxopt   |       5.8 |     841504147.6 |         3672.6 |      4185008.3 |
| daqp     |       3.4 |       1363649.6 |            5.4 |         2879.5 |
| ecos     |       4.2 |       1008053.0 |            3.7 |       781855.6 |
| gurobi   |       2.1 |         13358.4 |            1.8 |           30.2 |
| highs    |      23.6 |   10340470841.6 |        19917.3 |     22835974.2 |
| hpipm    |       2.4 |             5.2 |           14.8 |            5.2 |
| osqp     |     577.2 |             3.7 |          563.3 |           10.0 |
| piqp     |       1.1 |             5.3 |            1.0 |            1.0 |
| proxqp   |       1.0 |             2.4 |           40.3 |            1.5 |
| qpalm    |     147.2 |           291.1 |         4435.3 |        20336.5 |
| qpoases  |       2.2 |             1.7 |            2.0 |            3.4 |
| quadprog |       3.3 |            11.5 |            2.8 |            3.2 |
| scs      |      71.4 |             1.0 |            1.5 |            1.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
