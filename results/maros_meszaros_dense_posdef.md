# Maros-Meszaros dense positive definite subset

| Number of problems | 19 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-09-07 14:59:18.230241+00:00 |
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
| clarabel |                                84.2 |                               3424.9 |                               90710837853.7 |                             180809181.8 |                             11514.3 |
| cvxopt   |                                84.2 |                               3429.9 |                               90710810719.0 |                             180793949.5 |                             11190.1 |
| daqp     |                               100.0 |                                  3.5 |                                    239824.5 |                                     1.0 |                               146.3 |
| ecos     |                                36.8 |                              42988.4 |                              339387408823.0 |                             759675905.3 |                             42119.6 |
| gurobi   |                                89.5 |                               1999.4 |                               60322069328.7 |                             120226969.1 |                              7403.7 |
| highs    |                                94.7 |                                880.2 |                               30085386051.7 |                              59971651.7 |                              6299.3 |
| hpipm    |                                52.6 |                               5241.1 |                              527740292191.1 |                             241665469.5 |                             14881.8 |
| osqp     |                                78.9 |                                  2.3 |                              625461499517.6 |                            3587727674.7 |                           2274704.8 |
| piqp     |                               100.0 |                                  1.0 |                                         1.0 |                                   194.1 |                                 1.0 |
| proxqp   |                                78.9 |                               3427.2 |                               90711865391.1 |                             180795024.3 |                             24290.2 |
| qpalm    |                                63.2 |                                879.6 |                               52838547147.9 |                             554583779.3 |                            567129.2 |
| qpoases  |                                57.9 |                               7561.5 |                              254309453730.6 |                           23021254924.4 |                             18649.1 |
| quadprog |                                84.2 |                               3422.4 |                               90710810719.0 |                             180793743.1 |                             11133.3 |
| scs      |                                89.5 |                                 54.4 |                              628784917927.0 |                              80699931.9 |                            543995.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                68.4 |                                  3.9 |                                         2.4 |                                    17.7 |                                 4.5 |
| cvxopt   |                                 5.3 |                                  3.9 |                                         2.3 |                                   253.0 |                           3221456.7 |
| daqp     |                                78.9 |                                  1.0 |                                      1553.8 |                                     1.0 |                           8430010.9 |
| ecos     |                                 0.0 |                                 48.9 |                                         8.6 |                             152245969.9 |                           6231552.4 |
| gurobi   |                                10.5 |                                  2.3 |                                         1.6 |                                  2806.4 |                              5694.3 |
| highs    |                                 0.0 |                                  1.0 |                                         1.0 |                                 70376.5 |                         149478351.3 |
| hpipm    |                                57.9 |                                 21.7 |                                         6.2 |                                     4.1 |                                 2.0 |
| osqp     |                                63.2 |                                  6.0 |                                         4.7 |                                     2.8 |                                 2.6 |
| piqp     |                                84.2 |                                  2.3 |                                         1.6 |                                     1.9 |                                 2.0 |
| proxqp   |                                78.9 |                                  3.9 |                                         3.8 |                                     1.7 |                                 2.3 |
| qpalm    |                                68.4 |                                  6.0 |                                         5.2 |                                     2.2 |                                 3.5 |
| qpoases  |                                52.6 |                                  8.6 |                                2472929217.3 |                          171761571383.3 |                                 1.1 |
| quadprog |                                78.9 |                                  3.9 |                                         2.3 |                                     5.0 |                                 1.0 |
| scs      |                                84.2 |                                  3.9 |                                         3.3 |                                     2.2 |                                 1.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                78.9 |                               4975.6 |                                     77931.7 |                                356322.3 |                                 4.4 |
| cvxopt   |                                73.7 |                               2935.5 |                                     51954.3 |                                151706.4 |                                 8.2 |
| daqp     |                                84.2 |                                  4.9 |                                    236473.6 |                                     1.0 |                                18.7 |
| ecos     |                                31.6 |                              80893.8 |                                    311734.1 |                               1203006.1 |                                 6.4 |
| gurobi   |                                89.5 |                               2904.2 |                                     51954.3 |                                125874.5 |                                 1.0 |
| highs    |                                78.9 |                                  7.9 |                                         1.0 |                                 11085.7 |                               385.4 |
| hpipm    |                                26.3 |                              27729.3 |                                    214267.7 |                                605913.5 |                                55.0 |
| osqp     |                                57.9 |                               2905.6 |                                    103271.1 |                                440539.5 |                              4132.3 |
| piqp     |                               100.0 |                                  1.0 |                                         4.8 |                                240176.1 |                                 2.1 |
| proxqp   |                                73.7 |                               4979.5 |                                    131688.6 |                                226992.3 |                               276.6 |
| qpalm    |                                68.4 |                               1278.2 |                                     98894.3 |                                146719.3 |                               334.6 |
| qpoases  |                                52.6 |                              10981.9 |                                  82494658.7 |                           22258301788.9 |                                 2.5 |
| quadprog |                                84.2 |                               4971.9 |                                     77931.7 |                                188269.8 |                                 1.5 |
| scs      |                                89.5 |                               2958.2 |                                    101935.9 |                                210300.3 |                                 2.3 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                84.2 |                               4021.0 |                                     34332.6 |                                   267.2 |                                 3.1 |
| cvxopt   |                                52.6 |                               2372.3 |                                     22888.3 |                                 13836.0 |                              5249.6 |
| daqp     |                                84.2 |                                  4.0 |                                     87166.8 |                                     1.0 |                             13678.7 |
| ecos     |                                 0.0 |                              50468.1 |                                    126013.2 |                            2087855530.9 |                           3788408.9 |
| gurobi   |                                73.7 |                               2347.5 |                                     22888.5 |                                   487.4 |                                10.0 |
| highs    |                                68.4 |                                  6.4 |                                       440.4 |                                 11325.8 |                            282030.7 |
| hpipm    |                                52.6 |                              22408.4 |                                     91553.4 |                                   502.1 |                                 5.2 |
| osqp     |                                68.4 |                               4019.6 |                                     46850.2 |                                   484.7 |                                 6.6 |
| piqp     |                               100.0 |                                  1.0 |                                         1.0 |                                   108.5 |                                 1.0 |
| proxqp   |                                84.2 |                               4023.8 |                                     63176.6 |                                   263.2 |                                 2.9 |
| qpalm    |                                73.7 |                               1033.1 |                                     43505.2 |                                    84.4 |                               239.6 |
| qpoases  |                                52.6 |                               8876.8 |                               36283058986.1 |                           22155684364.6 |                                 1.8 |
| quadprog |                                84.2 |                               4017.8 |                                     34332.5 |                                   188.7 |                                 1.1 |
| scs      |                                84.2 |                               4032.8 |                                     44877.1 |                                   309.6 |                                 1.8 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        84 |              68 |             79 |             84 |
| cvxopt   |        84 |               5 |             74 |             53 |
| daqp     |       100 |              79 |             84 |             84 |
| ecos     |        37 |               0 |             32 |              0 |
| gurobi   |        89 |              11 |             89 |             74 |
| highs    |        95 |               0 |             79 |             68 |
| hpipm    |        53 |              58 |             26 |             53 |
| osqp     |        79 |              63 |             58 |             68 |
| piqp     |       100 |              84 |            100 |            100 |
| proxqp   |        79 |              79 |             74 |             84 |
| qpalm    |        63 |              68 |             68 |             74 |
| qpoases  |        58 |              53 |             53 |             53 |
| quadprog |        84 |              79 |             84 |             84 |
| scs      |        89 |              84 |             89 |             84 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              84 |             95 |            100 |
| cvxopt   |       100 |              21 |             84 |             63 |
| daqp     |       100 |              84 |             84 |             84 |
| ecos     |        95 |              58 |             95 |             58 |
| gurobi   |       100 |              21 |            100 |             84 |
| highs    |       100 |               5 |             79 |             68 |
| hpipm    |        74 |             100 |             68 |             95 |
| osqp     |        79 |              84 |             68 |             84 |
| piqp     |       100 |              95 |            100 |            100 |
| proxqp   |        95 |              95 |             89 |            100 |
| qpalm    |        68 |              89 |             74 |             79 |
| qpoases  |        84 |              79 |             79 |             79 |
| quadprog |       100 |              95 |            100 |            100 |
| scs      |        89 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |    3424.9 |             3.9 |         4975.6 |         4021.0 |
| cvxopt   |    3429.9 |             3.9 |         2935.5 |         2372.3 |
| daqp     |       3.5 |             1.0 |            4.9 |            4.0 |
| ecos     |   42988.4 |            48.9 |        80893.8 |        50468.1 |
| gurobi   |    1999.4 |             2.3 |         2904.2 |         2347.5 |
| highs    |     880.2 |             1.0 |            7.9 |            6.4 |
| hpipm    |    5241.1 |            21.7 |        27729.3 |        22408.4 |
| osqp     |       2.3 |             6.0 |         2905.6 |         4019.6 |
| piqp     |       1.0 |             2.3 |            1.0 |            1.0 |
| proxqp   |    3427.2 |             3.9 |         4979.5 |         4023.8 |
| qpalm    |     879.6 |             6.0 |         1278.2 |         1033.1 |
| qpoases  |    7561.5 |             8.6 |        10981.9 |         8876.8 |
| quadprog |    3422.4 |             3.9 |         4971.9 |         4017.8 |
| scs      |      54.4 |             3.9 |         2958.2 |         4032.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|---------------:|----------------:|---------------:|---------------:|
| clarabel |  90710837853.7 |             2.4 |        77931.7 |        34332.6 |
| cvxopt   |  90710810719.0 |             2.3 |        51954.3 |        22888.3 |
| daqp     |       239824.5 |          1553.8 |       236473.6 |        87166.8 |
| ecos     | 339387408823.0 |             8.6 |       311734.1 |       126013.2 |
| gurobi   |  60322069328.7 |             1.6 |        51954.3 |        22888.5 |
| highs    |  30085386051.7 |             1.0 |            1.0 |          440.4 |
| hpipm    | 527740292191.1 |             6.2 |       214267.7 |        91553.4 |
| osqp     | 625461499517.6 |             4.7 |       103271.1 |        46850.2 |
| piqp     |            1.0 |             1.6 |            4.8 |            1.0 |
| proxqp   |  90711865391.1 |             3.8 |       131688.6 |        63176.6 |
| qpalm    |  52838547147.9 |             5.2 |        98894.3 |        43505.2 |
| qpoases  | 254309453730.6 |    2472929217.3 |     82494658.7 |  36283058986.1 |
| quadprog |  90710810719.0 |             2.3 |        77931.7 |        34332.5 |
| scs      | 628784917927.0 |             3.3 |       101935.9 |        44877.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel |   180809181.8 |            17.7 |       356322.3 |          267.2 |
| cvxopt   |   180793949.5 |           253.0 |       151706.4 |        13836.0 |
| daqp     |           1.0 |             1.0 |            1.0 |            1.0 |
| ecos     |   759675905.3 |     152245969.9 |      1203006.1 |   2087855530.9 |
| gurobi   |   120226969.1 |          2806.4 |       125874.5 |          487.4 |
| highs    |    59971651.7 |         70376.5 |        11085.7 |        11325.8 |
| hpipm    |   241665469.5 |             4.1 |       605913.5 |          502.1 |
| osqp     |  3587727674.7 |             2.8 |       440539.5 |          484.7 |
| piqp     |         194.1 |             1.9 |       240176.1 |          108.5 |
| proxqp   |   180795024.3 |             1.7 |       226992.3 |          263.2 |
| qpalm    |   554583779.3 |             2.2 |       146719.3 |           84.4 |
| qpoases  | 23021254924.4 |  171761571383.3 |  22258301788.9 |  22155684364.6 |
| quadprog |   180793743.1 |             5.0 |       188269.8 |          188.7 |
| scs      |    80699931.9 |             2.2 |       210300.3 |          309.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   11514.3 |             4.5 |            4.4 |            3.1 |
| cvxopt   |   11190.1 |       3221456.7 |            8.2 |         5249.6 |
| daqp     |     146.3 |       8430010.9 |           18.7 |        13678.7 |
| ecos     |   42119.6 |       6231552.4 |            6.4 |      3788408.9 |
| gurobi   |    7403.7 |          5694.3 |            1.0 |           10.0 |
| highs    |    6299.3 |     149478351.3 |          385.4 |       282030.7 |
| hpipm    |   14881.8 |             2.0 |           55.0 |            5.2 |
| osqp     | 2274704.8 |             2.6 |         4132.3 |            6.6 |
| piqp     |       1.0 |             2.0 |            2.1 |            1.0 |
| proxqp   |   24290.2 |             2.3 |          276.6 |            2.9 |
| qpalm    |  567129.2 |             3.5 |          334.6 |          239.6 |
| qpoases  |   18649.1 |             1.1 |            2.5 |            1.8 |
| quadprog |   11133.3 |             1.0 |            1.5 |            1.1 |
| scs      |  543995.0 |             1.4 |            2.3 |            1.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
