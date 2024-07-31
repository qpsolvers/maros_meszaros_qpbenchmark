# Maros-Meszaros dense subset

| Number of problems | 62 |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.1 |
| Date               | 2023-12-22 12:11:30.988253+00:00 |
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

| solver   | version   |
|:---------|:----------|
| clarabel | 0.6.0     |
| cvxopt   | 1.3.2     |
| daqp     | 0.5.1     |
| ecos     | 2.0.11    |
| highs    | 1.5.3     |
| osqp     | 0.6.3     |
| piqp     | 0.2.3     |
| proxqp   | 0.6.1     |
| qpalm    | 1.2.1     |
| qpoases  | 3.2.1     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.2.0.

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
| `python_version` | 3.10.13.final.0 (64 bit) |
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
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| piqp     | ``check_duality_gap``            | -         | True            | True           | True           |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | True            | True           | True           |
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
| clarabel |                                96.8 |                                  3.0 |                                     15626.8 |                                 24838.5 |                                 1.7 |
| cvxopt   |                                66.1 |                                 90.3 |                                    252934.6 |                                400436.4 |                                 6.1 |
| daqp     |                                30.6 |                                912.5 |                                    694125.3 |                               1098902.8 |                                 3.6 |
| ecos     |                                17.7 |                               1562.8 |                                    811528.6 |                               1331833.5 |                                 4.2 |
| highs    |                                66.1 |                                 71.3 |                                    220976.5 |                                390958.7 |                                 8.8 |
| osqp     |                                51.6 |                                 26.6 |                                   4843285.0 |                               5347993.1 |                               545.3 |
| piqp     |                                83.9 |                                 37.1 |                                    141509.8 |                                224042.4 |                                 1.7 |
| proxqp   |                                96.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                59.7 |                                  3.1 |                                    836622.8 |                                599096.6 |                               166.5 |
| qpoases  |                                24.2 |                                280.3 |                                   6941355.2 |                              34758456.5 |                                 2.3 |
| quadprog |                                64.5 |                                101.9 |                                    273372.1 |                               7065698.3 |                                49.7 |
| scs      |                                72.6 |                                  7.3 |                                   2440270.0 |                                551195.9 |                                74.7 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.6 |                                  2.1 |                                         1.0 |                                    15.7 |                               269.9 |
| cvxopt   |                                 3.2 |                                 16.2 |                                         4.4 |                                   990.6 |                         790577107.3 |
| daqp     |                                24.2 |                                118.8 |                                       221.4 |                                     4.3 |                           1281345.2 |
| ecos     |                                 0.0 |                                188.3 |                                         5.5 |                              35231157.6 |                           1110724.0 |
| highs    |                                 0.0 |                                  8.6 |                                         2.9 |                             147368670.8 |                        2979942817.7 |
| osqp     |                                41.9 |                                 38.9 |                                         3.8 |                                     3.3 |                                 3.3 |
| piqp     |                                69.4 |                                 13.2 |                                         2.0 |                                     2.3 |                                 2.4 |
| proxqp   |                                85.5 |                                  1.0 |                                         1.0 |                                     1.0 |                                67.4 |
| qpalm    |                                43.5 |                                 14.6 |                                         2.9 |                                     2.4 |                               230.9 |
| qpoases  |                                19.4 |                                 37.3 |                               41313547997.7 |                          118393766305.8 |                                 1.6 |
| quadprog |                                33.9 |                                 12.3 |                                  28605929.5 |                           23686979367.1 |                       18825903233.1 |
| scs      |                                62.9 |                                 21.3 |                                         2.9 |                                     2.8 |                                 1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                93.5 |                                  6.0 |                                         1.0 |                                    14.1 |                                 1.3 |
| cvxopt   |                                51.6 |                                 78.4 |                                         7.5 |                                    24.6 |                              2777.2 |
| daqp     |                                25.8 |                                881.0 |                                        26.0 |                                    68.3 |                                 4.1 |
| ecos     |                                14.5 |                               1757.0 |                                        25.9 |                                    94.0 |                                 2.7 |
| highs    |                                50.0 |                                 68.9 |                                         7.0 |                                  2486.2 |                              4437.6 |
| osqp     |                                38.7 |                                185.9 |                                        14.3 |                                    52.5 |                               425.9 |
| piqp     |                                87.1 |                                 30.6 |                                         4.1 |                                    21.5 |                                 1.0 |
| proxqp   |                                95.2 |                                  1.0 |                                         1.6 |                                     1.0 |                                28.6 |
| qpalm    |                                54.8 |                                  3.0 |                                         5.9 |                                     9.7 |                              5752.7 |
| qpoases  |                                19.4 |                                312.9 |                                    123486.7 |                               1340042.4 |                                 1.5 |
| quadprog |                                56.5 |                                 98.4 |                                       139.6 |                                396068.7 |                             28031.3 |
| scs      |                                80.6 |                                 55.9 |                                         9.5 |                                    27.3 |                                 1.2 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                88.7 |                                 12.3 |                                         1.1 |                                   886.5 |                                 2.3 |
| cvxopt   |                                35.5 |                                 74.1 |                                         4.0 |                                   166.6 |                           3828502.2 |
| daqp     |                                25.8 |                                830.5 |                                        13.4 |                                    19.7 |                              2634.2 |
| ecos     |                                 3.2 |                               1422.3 |                                        13.2 |                              14628542.9 |                            717381.0 |
| highs    |                                29.0 |                                 64.9 |                                         3.7 |                                712060.8 |                           6118207.2 |
| osqp     |                                41.9 |                                227.8 |                                         7.8 |                                    16.4 |                                 9.2 |
| piqp     |                                82.3 |                                 44.9 |                                         2.9 |                                     6.3 |                                 1.5 |
| proxqp   |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                53.2 |                                 20.0 |                                         3.9 |                                     4.6 |                             66285.7 |
| qpoases  |                                19.4 |                                234.5 |                                 220880279.5 |                             573088542.5 |                                 3.1 |
| quadprog |                                53.2 |                                 92.8 |                                     69547.6 |                             114450498.2 |                          38652004.5 |
| scs      |                                74.2 |                                 82.1 |                                         5.0 |                                     9.7 |                                 1.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        97 |              73 |             94 |             89 |
| cvxopt   |        66 |               3 |             52 |             35 |
| daqp     |        31 |              24 |             26 |             26 |
| ecos     |        18 |               0 |             15 |              3 |
| highs    |        66 |               0 |             50 |             29 |
| osqp     |        52 |              42 |             39 |             42 |
| piqp     |        84 |              69 |             87 |             82 |
| proxqp   |        97 |              85 |             95 |            100 |
| qpalm    |        60 |              44 |             55 |             53 |
| qpoases  |        24 |              19 |             19 |             19 |
| quadprog |        65 |              34 |             56 |             53 |
| scs      |        73 |              63 |             81 |             74 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        98 |              81 |             97 |             95 |
| cvxopt   |        92 |              35 |             76 |             60 |
| daqp     |       100 |              95 |             95 |             95 |
| ecos     |        98 |              81 |             98 |             84 |
| highs    |        89 |              23 |             73 |             52 |
| osqp     |        63 |              90 |             77 |             85 |
| piqp     |        98 |              98 |            100 |            100 |
| proxqp   |        97 |              89 |             95 |            100 |
| qpalm    |        61 |              74 |             56 |             63 |
| qpoases  |        69 |              65 |             68 |             63 |
| quadprog |        92 |              61 |             84 |             81 |
| scs      |        76 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       3.0 |             2.1 |            6.0 |           12.3 |
| cvxopt   |      90.3 |            16.2 |           78.4 |           74.1 |
| daqp     |     912.5 |           118.8 |          881.0 |          830.5 |
| ecos     |    1562.8 |           188.3 |         1757.0 |         1422.3 |
| highs    |      71.3 |             8.6 |           68.9 |           64.9 |
| osqp     |      26.6 |            38.9 |          185.9 |          227.8 |
| piqp     |      37.1 |            13.2 |           30.6 |           44.9 |
| proxqp   |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |       3.1 |            14.6 |            3.0 |           20.0 |
| qpoases  |     280.3 |            37.3 |          312.9 |          234.5 |
| quadprog |     101.9 |            12.3 |           98.4 |           92.8 |
| scs      |       7.3 |            21.3 |           55.9 |           82.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   15626.8 |             1.0 |            1.0 |            1.1 |
| cvxopt   |  252934.6 |             4.4 |            7.5 |            4.0 |
| daqp     |  694125.3 |           221.4 |           26.0 |           13.4 |
| ecos     |  811528.6 |             5.5 |           25.9 |           13.2 |
| highs    |  220976.5 |             2.9 |            7.0 |            3.7 |
| osqp     | 4843285.0 |             3.8 |           14.3 |            7.8 |
| piqp     |  141509.8 |             2.0 |            4.1 |            2.9 |
| proxqp   |       1.0 |             1.0 |            1.6 |            1.0 |
| qpalm    |  836622.8 |             2.9 |            5.9 |            3.9 |
| qpoases  | 6941355.2 |   41313547997.7 |       123486.7 |    220880279.5 |
| quadprog |  273372.1 |      28605929.5 |          139.6 |        69547.6 |
| scs      | 2440270.0 |             2.9 |            9.5 |            5.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |    default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|-----------:|----------------:|---------------:|---------------:|
| clarabel |    24838.5 |            15.7 |           14.1 |          886.5 |
| cvxopt   |   400436.4 |           990.6 |           24.6 |          166.6 |
| daqp     |  1098902.8 |             4.3 |           68.3 |           19.7 |
| ecos     |  1331833.5 |      35231157.6 |           94.0 |     14628542.9 |
| highs    |   390958.7 |     147368670.8 |         2486.2 |       712060.8 |
| osqp     |  5347993.1 |             3.3 |           52.5 |           16.4 |
| piqp     |   224042.4 |             2.3 |           21.5 |            6.3 |
| proxqp   |        1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |   599096.6 |             2.4 |            9.7 |            4.6 |
| qpoases  | 34758456.5 |  118393766305.8 |      1340042.4 |    573088542.5 |
| quadprog |  7065698.3 |   23686979367.1 |       396068.7 |    114450498.2 |
| scs      |   551195.9 |             2.8 |           27.3 |            9.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.7 |           269.9 |            1.3 |            2.3 |
| cvxopt   |       6.1 |     790577107.3 |         2777.2 |      3828502.2 |
| daqp     |       3.6 |       1281345.2 |            4.1 |         2634.2 |
| ecos     |       4.2 |       1110724.0 |            2.7 |       717381.0 |
| highs    |       8.8 |    2979942817.7 |         4437.6 |      6118207.2 |
| osqp     |     545.3 |             3.3 |          425.9 |            9.2 |
| piqp     |       1.7 |             2.4 |            1.0 |            1.5 |
| proxqp   |       1.0 |            67.4 |           28.6 |            1.0 |
| qpalm    |     166.5 |           230.9 |         5752.7 |        66285.7 |
| qpoases  |       2.3 |             1.6 |            1.5 |            3.1 |
| quadprog |      49.7 |   18825903233.1 |        28031.3 |     38652004.5 |
| scs      |      74.7 |             1.0 |            1.2 |            1.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
