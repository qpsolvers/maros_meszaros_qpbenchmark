# Maros-Meszaros dense positive definite subset

| Number of problems | 19 |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.1 |
| Date               | 2023-12-22 11:27:08.565558+00:00 |
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

Subset of the Maros-Meszaros test set restricted to smaller dense problems with positive definite Hessian matrix.

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
| clarabel |                               100.0 |                                  1.0 |                                     27915.2 |                                 13872.7 |                               405.5 |
| cvxopt   |                                84.2 |                               1624.9 |                               90710810719.0 |                             180793932.4 |                             11124.9 |
| daqp     |                               100.0 |                                  1.6 |                                    239824.5 |                                     1.0 |                               145.5 |
| ecos     |                                36.8 |                              20389.5 |                              339387408823.0 |                             759675905.3 |                             41874.4 |
| highs    |                                89.5 |                                420.8 |                               30085386291.3 |                             143788588.4 |                              5505.9 |
| osqp     |                                78.9 |                                  1.1 |                              625461500533.7 |                            3587727674.7 |                           2261461.6 |
| piqp     |                               100.0 |                                  1.7 |                                         1.0 |                                   194.5 |                                 1.0 |
| proxqp   |                                94.7 |                                  5.3 |                                   1049423.1 |                                  1212.3 |                              7855.4 |
| qpalm    |                                63.2 |                                417.8 |                               52838547147.9 |                             554583779.3 |                            563827.4 |
| qpoases  |                                57.9 |                               3586.6 |                              254309453730.6 |                           23021254924.4 |                             18540.6 |
| quadprog |                                84.2 |                               1622.8 |                               90710810719.0 |                             180793743.1 |                             11068.5 |
| scs      |                                89.5 |                                 46.1 |                              628784911874.0 |                              80699882.9 |                            540891.7 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                84.2 |                                  1.0 |                                         1.0 |                                    25.9 |                                 4.4 |
| cvxopt   |                                 5.3 |                               1232.5 |                                        72.0 |                                   682.2 |                           3221880.0 |
| daqp     |                                78.9 |                                316.6 |                                     47830.7 |                                     1.7 |                           8430010.9 |
| ecos     |                                 0.0 |                              15463.0 |                                       264.9 |                             255925690.3 |                           6231552.4 |
| highs    |                                 0.0 |                                318.6 |                                       212.6 |                            1086949640.2 |                         105828843.9 |
| osqp     |                                63.2 |                               1885.4 |                                       143.7 |                                     4.7 |                                 2.6 |
| piqp     |                                84.2 |                               1230.7 |                                        72.0 |                                     4.2 |                                 1.5 |
| proxqp   |                                89.5 |                                 62.4 |                                        78.4 |                                     1.0 |                                 3.8 |
| qpalm    |                                68.4 |                               1885.0 |                                       159.8 |                                     3.8 |                                 3.5 |
| qpoases  |                                52.6 |                               2722.4 |                               76123735208.1 |                          288731443286.2 |                                 1.1 |
| quadprog |                                78.9 |                               1230.7 |                                        72.0 |                                     8.3 |                                 1.0 |
| scs      |                                84.2 |                               1236.5 |                                       101.0 |                                     3.8 |                                 1.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                 80028.4 |                                 2.0 |
| cvxopt   |                                73.7 |                               1091.9 |                                    820243.9 |                                147267.0 |                                 5.5 |
| daqp     |                                84.2 |                                  2.2 |                                   3733396.8 |                                     1.0 |                                12.6 |
| ecos     |                                31.6 |                              30041.0 |                                   4921592.9 |                               1203006.2 |                                 4.3 |
| highs    |                                57.9 |                                477.9 |                                    410124.1 |                              83474756.3 |                               158.7 |
| osqp     |                                57.9 |                               1078.6 |                                   1630422.9 |                                440539.5 |                              2790.1 |
| piqp     |                               100.0 |                                  1.9 |                                        75.8 |                                240172.2 |                                 1.4 |
| proxqp   |                                89.5 |                                  5.8 |                                   1114101.6 |                                 39099.7 |                               186.5 |
| qpalm    |                                68.4 |                                474.4 |                                   1561322.1 |                                146719.3 |                               225.9 |
| qpoases  |                                52.6 |                               4077.3 |                                1302408647.2 |                           22258301788.9 |                                 1.7 |
| quadprog |                                84.2 |                               1845.9 |                                   1230369.1 |                                188269.8 |                                 1.0 |
| scs      |                                89.5 |                               1122.7 |                                   1608707.5 |                                189730.3 |                                 1.7 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                    68.1 |                                 2.5 |
| cvxopt   |                                52.6 |                                942.1 |                                     92015.4 |                                 13805.5 |                              5271.8 |
| daqp     |                                84.2 |                                  2.2 |                                    350426.8 |                                     1.0 |                             13736.6 |
| ecos     |                                 0.0 |                              20016.6 |                                    506596.6 |                            2087855531.0 |                           3804441.3 |
| highs    |                                47.4 |                                412.5 |                                     46369.0 |                              83406677.6 |                            172417.1 |
| osqp     |                                68.4 |                               1593.7 |                                    203811.2 |                                   467.7 |                                 5.4 |
| piqp     |                               100.0 |                                  2.6 |                                         4.0 |                                   108.4 |                                 1.0 |
| proxqp   |                               100.0 |                                  5.1 |                                    118671.2 |                                    76.7 |                                 1.9 |
| qpalm    |                                73.7 |                                409.6 |                                    174899.1 |                                    84.4 |                               240.6 |
| qpoases  |                                52.6 |                               3521.2 |                              145864657942.8 |                           22155684364.6 |                                 1.8 |
| quadprog |                                84.2 |                               1593.1 |                                    138023.0 |                                   188.7 |                                 1.1 |
| scs      |                                89.5 |                               1035.7 |                                    135221.2 |                                   306.9 |                                 1.7 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              84 |            100 |            100 |
| cvxopt   |        84 |               5 |             74 |             53 |
| daqp     |       100 |              79 |             84 |             84 |
| ecos     |        37 |               0 |             32 |              0 |
| highs    |        89 |               0 |             58 |             47 |
| osqp     |        79 |              63 |             58 |             68 |
| piqp     |       100 |              84 |            100 |            100 |
| proxqp   |        95 |              89 |             89 |            100 |
| qpalm    |        63 |              68 |             68 |             74 |
| qpoases  |        58 |              53 |             53 |             53 |
| quadprog |        84 |              79 |             84 |             84 |
| scs      |        89 |              84 |             89 |             89 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              84 |            100 |            100 |
| cvxopt   |       100 |              21 |             84 |             63 |
| daqp     |       100 |              84 |             84 |             84 |
| ecos     |        95 |              58 |             95 |             58 |
| highs    |        95 |               5 |             63 |             53 |
| osqp     |        79 |              84 |             68 |             84 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |        95 |              89 |             89 |            100 |
| qpalm    |        68 |              89 |             74 |             79 |
| qpoases  |        84 |              79 |             79 |             79 |
| quadprog |       100 |              95 |            100 |            100 |
| scs      |        89 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |    1624.9 |          1232.5 |         1091.9 |          942.1 |
| daqp     |       1.6 |           316.6 |            2.2 |            2.2 |
| ecos     |   20389.5 |         15463.0 |        30041.0 |        20016.6 |
| highs    |     420.8 |           318.6 |          477.9 |          412.5 |
| osqp     |       1.1 |          1885.4 |         1078.6 |         1593.7 |
| piqp     |       1.7 |          1230.7 |            1.9 |            2.6 |
| proxqp   |       5.3 |            62.4 |            5.8 |            5.1 |
| qpalm    |     417.8 |          1885.0 |          474.4 |          409.6 |
| qpoases  |    3586.6 |          2722.4 |         4077.3 |         3521.2 |
| quadprog |    1622.8 |          1230.7 |         1845.9 |         1593.1 |
| scs      |      46.1 |          1236.5 |         1122.7 |         1035.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|---------------:|----------------:|---------------:|---------------:|
| clarabel |        27915.2 |             1.0 |            1.0 |            1.0 |
| cvxopt   |  90710810719.0 |            72.0 |       820243.9 |        92015.4 |
| daqp     |       239824.5 |         47830.7 |      3733396.8 |       350426.8 |
| ecos     | 339387408823.0 |           264.9 |      4921592.9 |       506596.6 |
| highs    |  30085386291.3 |           212.6 |       410124.1 |        46369.0 |
| osqp     | 625461500533.7 |           143.7 |      1630422.9 |       203811.2 |
| piqp     |            1.0 |            72.0 |           75.8 |            4.0 |
| proxqp   |      1049423.1 |            78.4 |      1114101.6 |       118671.2 |
| qpalm    |  52838547147.9 |           159.8 |      1561322.1 |       174899.1 |
| qpoases  | 254309453730.6 |   76123735208.1 |   1302408647.2 | 145864657942.8 |
| quadprog |  90710810719.0 |            72.0 |      1230369.1 |       138023.0 |
| scs      | 628784911874.0 |           101.0 |      1608707.5 |       135221.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel |       13872.7 |            25.9 |        80028.4 |           68.1 |
| cvxopt   |   180793932.4 |           682.2 |       147267.0 |        13805.5 |
| daqp     |           1.0 |             1.7 |            1.0 |            1.0 |
| ecos     |   759675905.3 |     255925690.3 |      1203006.2 |   2087855531.0 |
| highs    |   143788588.4 |    1086949640.2 |     83474756.3 |     83406677.6 |
| osqp     |  3587727674.7 |             4.7 |       440539.5 |          467.7 |
| piqp     |         194.5 |             4.2 |       240172.2 |          108.4 |
| proxqp   |        1212.3 |             1.0 |        39099.7 |           76.7 |
| qpalm    |   554583779.3 |             3.8 |       146719.3 |           84.4 |
| qpoases  | 23021254924.4 |  288731443286.2 |  22258301788.9 |  22155684364.6 |
| quadprog |   180793743.1 |             8.3 |       188269.8 |          188.7 |
| scs      |    80699882.9 |             3.8 |       189730.3 |          306.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     405.5 |             4.4 |            2.0 |            2.5 |
| cvxopt   |   11124.9 |       3221880.0 |            5.5 |         5271.8 |
| daqp     |     145.5 |       8430010.9 |           12.6 |        13736.6 |
| ecos     |   41874.4 |       6231552.4 |            4.3 |      3804441.3 |
| highs    |    5505.9 |     105828843.9 |          158.7 |       172417.1 |
| osqp     | 2261461.6 |             2.6 |         2790.1 |            5.4 |
| piqp     |       1.0 |             1.5 |            1.4 |            1.0 |
| proxqp   |    7855.4 |             3.8 |          186.5 |            1.9 |
| qpalm    |  563827.4 |             3.5 |          225.9 |          240.6 |
| qpoases  |   18540.6 |             1.1 |            1.7 |            1.8 |
| quadprog |   11068.5 |             1.0 |            1.0 |            1.1 |
| scs      |  540891.7 |             1.4 |            1.7 |            1.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
