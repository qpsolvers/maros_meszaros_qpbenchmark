# Maros-Meszaros test set

| Number of problems | 138 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-09-07 14:41:56.482503+00:00 |
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

Standard set of problems designed to be difficult.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.9.0                 |
| cvxopt   | 1.3.2                 |
| gurobi   | 11.0.3 (size-limited) |
| highs    | 1.7.2                 |
| osqp     | 0.6.7.post0           |
| piqp     | 0.4.1                 |
| proxqp   | 0.6.6                 |
| qpalm    | 1.2.3                 |
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
| `hz_actual_friendly` | 2.2676 GHz |
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

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |          0     |
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``TimeLimit``                    | 1000.0    |        1000     |       1000     |       1000     |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``time_limit``                   | 1000.0    |        1000     |       1000     |       1000     |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| osqp     | ``time_limit``                   | 1000.0    |        1000     |       1000     |       1000     |
| piqp     | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| piqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| piqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm    | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| qpalm    | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm    | ``time_limit``                   | 1000.0    |        1000     |       1000     |       1000     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs      | ``time_limit_secs``              | 1000.0    |        1000     |       1000     |       1000     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                45.7 |                                163.8 |                                      1167.7 |                                 17990.1 |                                 1.0 |
| cvxopt   |                                52.9 |                                 94.1 |                                       819.6 |                                 12587.2 |                                 3.4 |
| gurobi   |                                26.1 |                                395.5 |                                      1603.1 |                                 24641.6 |                                 1.3 |
| highs    |                                66.7 |                                 30.7 |                                       428.9 |                                  6663.0 |                                 9.7 |
| osqp     |                                43.5 |                                 12.7 |                                      9070.8 |                                101467.5 |                               290.5 |
| piqp     |                                95.7 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.3 |
| proxqp   |                                73.2 |                                 53.3 |                                       490.8 |                                  7544.7 |                                 1.7 |
| qpalm    |                                55.8 |                                  3.6 |                                      1469.3 |                                 16117.9 |                                70.0 |
| scs      |                                62.3 |                                 15.1 |                                      5721.8 |                                 17049.7 |                                20.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                34.8 |                                 12.5 |                                         3.6 |                                  4344.3 |                                26.5 |
| cvxopt   |                                 5.8 |                                  7.8 |                                   1791394.3 |                                   225.5 |                        1473150662.9 |
| gurobi   |                                 8.0 |                                 26.9 |                                         4.5 |                                   169.2 |                              3735.2 |
| highs    |                                 0.0 |                                  2.5 |                                     12555.3 |                               6265293.5 |                        6888461608.2 |
| osqp     |                                26.1 |                                 16.1 |                                         4.2 |                                     2.1 |                              2955.0 |
| piqp     |                                73.2 |                                  1.0 |                                         1.0 |                                     1.0 |                              4920.4 |
| proxqp   |                                52.9 |                                  5.9 |                                         2.7 |                                     1.7 |                                 2.2 |
| qpalm    |                                25.4 |                                  4.8 |                                         3.7 |                                     1.4 |                           1237362.9 |
| scs      |                                43.5 |                                 10.7 |                                         3.7 |                                     1.8 |                                 1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                46.4 |                                 98.4 |                                         2.8 |                                     8.5 |                                 1.8 |
| cvxopt   |                                42.0 |                                 58.3 |                                         3.6 |                                     5.0 |                              4357.1 |
| gurobi   |                                26.1 |                                284.9 |                                         4.0 |                                     6.3 |                                 2.0 |
| highs    |                                41.3 |                                 18.0 |                                         1.0 |                                    18.0 |                             14023.4 |
| osqp     |                                21.0 |                                 52.8 |                                         3.2 |                                     4.9 |                              3286.4 |
| piqp     |                                97.1 |                                  1.0 |                                         3.1 |                                     1.1 |                                 1.0 |
| proxqp   |                                71.0 |                                 36.0 |                                         1.6 |                                     2.2 |                                13.1 |
| qpalm    |                                31.2 |                                  3.4 |                                         1.9 |                                     1.0 |                             11863.2 |
| scs      |                                73.2 |                                 24.5 |                                        34.4 |                                     3.2 |                                 1.0 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                43.5 |                                 46.3 |                                        14.8 |                                    28.0 |                                 1.4 |
| cvxopt   |                                23.2 |                                 23.5 |                                      8072.1 |                                    30.7 |                           3185883.0 |
| gurobi   |                                19.6 |                                110.6 |                                        20.1 |                                     8.4 |                                 7.2 |
| highs    |                                19.6 |                                  8.2 |                                        62.0 |                                 21640.1 |                          10674439.9 |
| osqp     |                                24.6 |                                 51.9 |                                        17.5 |                                     7.2 |                             29517.2 |
| piqp     |                                94.2 |                                  1.0 |                                         1.0 |                                     1.0 |                               116.8 |
| proxqp   |                                66.7 |                                 19.2 |                                        10.0 |                                     3.6 |                                 1.0 |
| qpalm    |                                31.2 |                                  2.2 |                                         9.1 |                                     1.9 |                           2086773.2 |
| scs      |                                58.7 |                                 22.3 |                                        18.0 |                                     4.9 |                                 1.1 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        46 |              35 |             46 |             43 |
| cvxopt   |        53 |               6 |             42 |             23 |
| gurobi   |        26 |               8 |             26 |             20 |
| highs    |        67 |               0 |             41 |             20 |
| osqp     |        43 |              26 |             21 |             25 |
| piqp     |        96 |              73 |             97 |             94 |
| proxqp   |        73 |              53 |             71 |             67 |
| qpalm    |        56 |              25 |             31 |             31 |
| scs      |        62 |              43 |             73 |             59 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              91 |             97 |             98 |
| cvxopt   |        91 |              49 |             78 |             59 |
| gurobi   |       100 |              82 |            100 |             93 |
| highs    |        87 |              23 |             59 |             40 |
| osqp     |        57 |              89 |             61 |             83 |
| piqp     |        96 |              88 |             98 |             98 |
| proxqp   |        96 |              92 |             96 |            100 |
| qpalm    |        57 |              63 |             34 |             37 |
| scs      |        75 |              96 |             96 |             98 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     163.8 |            12.5 |           98.4 |           46.3 |
| cvxopt   |      94.1 |             7.8 |           58.3 |           23.5 |
| gurobi   |     395.5 |            26.9 |          284.9 |          110.6 |
| highs    |      30.7 |             2.5 |           18.0 |            8.2 |
| osqp     |      12.7 |            16.1 |           52.8 |           51.9 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |      53.3 |             5.9 |           36.0 |           19.2 |
| qpalm    |       3.6 |             4.8 |            3.4 |            2.2 |
| scs      |      15.1 |            10.7 |           24.5 |           22.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |    1167.7 |             3.6 |            2.8 |           14.8 |
| cvxopt   |     819.6 |       1791394.3 |            3.6 |         8072.1 |
| gurobi   |    1603.1 |             4.5 |            4.0 |           20.1 |
| highs    |     428.9 |         12555.3 |            1.0 |           62.0 |
| osqp     |    9070.8 |             4.2 |            3.2 |           17.5 |
| piqp     |       1.0 |             1.0 |            3.1 |            1.0 |
| proxqp   |     490.8 |             2.7 |            1.6 |           10.0 |
| qpalm    |    1469.3 |             3.7 |            1.9 |            9.1 |
| scs      |    5721.8 |             3.7 |           34.4 |           18.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   17990.1 |          4344.3 |            8.5 |           28.0 |
| cvxopt   |   12587.2 |           225.5 |            5.0 |           30.7 |
| gurobi   |   24641.6 |           169.2 |            6.3 |            8.4 |
| highs    |    6663.0 |       6265293.5 |           18.0 |        21640.1 |
| osqp     |  101467.5 |             2.1 |            4.9 |            7.2 |
| piqp     |       1.0 |             1.0 |            1.1 |            1.0 |
| proxqp   |    7544.7 |             1.7 |            2.2 |            3.6 |
| qpalm    |   16117.9 |             1.4 |            1.0 |            1.9 |
| scs      |   17049.7 |             1.8 |            3.2 |            4.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |            26.5 |            1.8 |            1.4 |
| cvxopt   |       3.4 |    1473150662.9 |         4357.1 |      3185883.0 |
| gurobi   |       1.3 |          3735.2 |            2.0 |            7.2 |
| highs    |       9.7 |    6888461608.2 |        14023.4 |     10674439.9 |
| osqp     |     290.5 |          2955.0 |         3286.4 |        29517.2 |
| piqp     |       1.3 |          4920.4 |            1.0 |          116.8 |
| proxqp   |       1.7 |             2.2 |           13.1 |            1.0 |
| qpalm    |      70.0 |       1237362.9 |        11863.2 |      2086773.2 |
| scs      |      20.0 |             1.0 |            1.0 |            1.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
