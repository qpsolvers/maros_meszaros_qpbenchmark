# Maros-Meszaros sparse subset

| Number of problems | 76 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-09-07 15:23:00.654152+00:00 |
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

Subset of the Maros-Meszaros test set complementary to the dense subset.

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
| clarabel |                                40.8 |                                118.3 |                                       702.2 |                                 11838.5 |                                 1.0 |
| cvxopt   |                                42.1 |                                110.1 |                                       575.2 |                                  9648.1 |                                 4.2 |
| gurobi   |                                 1.3 |                                680.4 |                                      1192.9 |                                 20034.2 |                                 1.7 |
| highs    |                                61.8 |                                 36.5 |                                       354.0 |                                  6003.9 |                                 9.5 |
| osqp     |                                36.8 |                                  9.5 |                                      3941.8 |                                 56127.5 |                               337.4 |
| piqp     |                                93.4 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.9 |
| proxqp   |                                63.2 |                                 73.4 |                                       369.6 |                                  6207.1 |                                 2.5 |
| qpalm    |                                52.6 |                                  3.2 |                                       784.0 |                                 14213.7 |                                77.2 |
| scs      |                                55.3 |                                 17.6 |                                      2916.3 |                                 12988.0 |                                13.9 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                27.6 |                                 10.3 |                                         3.3 |                                  6536.6 |                                36.0 |
| cvxopt   |                                 3.9 |                                  9.8 |                                   2549480.8 |                                     2.0 |                        1753480544.8 |
| gurobi   |                                 1.3 |                                 52.0 |                                         4.7 |                                     2.5 |                                 1.0 |
| highs    |                                 0.0 |                                  3.5 |                                     11564.5 |                               7165193.1 |                        5554599469.9 |
| osqp     |                                13.2 |                                 17.4 |                                         3.8 |                                     2.0 |                              4100.2 |
| piqp     |                                67.1 |                                  1.0 |                                         1.0 |                                     1.0 |                              6827.6 |
| proxqp   |                                34.2 |                                 10.1 |                                         2.9 |                                     2.1 |                                 2.1 |
| qpalm    |                                 7.9 |                                  4.3 |                                         3.7 |                                     1.3 |                           1717432.3 |
| scs      |                                23.7 |                                 15.7 |                                         3.8 |                                     1.9 |                                 1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                44.7 |                                 60.9 |                                         1.7 |                                     9.9 |                                 1.9 |
| cvxopt   |                                34.2 |                                 64.7 |                                         3.2 |                                     6.3 |                              5919.2 |
| gurobi   |                                 1.3 |                                484.1 |                                         3.2 |                                     7.3 |                                 2.7 |
| highs    |                                27.6 |                                 25.3 |                                         1.0 |                                    24.1 |                             14422.5 |
| osqp     |                                 6.6 |                                 30.0 |                                         2.3 |                                     4.4 |                              5805.3 |
| piqp     |                                94.7 |                                  1.0 |                                         3.4 |                                     1.0 |                                 1.3 |
| proxqp   |                                61.8 |                                 47.2 |                                         1.3 |                                     2.7 |                                 1.8 |
| qpalm    |                                10.5 |                                  3.1 |                                         1.5 |                                     1.0 |                             20732.3 |
| scs      |                                67.1 |                                 19.0 |                                        36.7 |                                     3.3 |                                 1.0 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                38.2 |                                 35.4 |                                        11.0 |                                    36.6 |                                 1.2 |
| cvxopt   |                                13.2 |                                 30.3 |                                     10230.8 |                                     4.3 |                           3387961.2 |
| gurobi   |                                 1.3 |                                213.0 |                                        18.7 |                                     8.3 |                                 1.6 |
| highs    |                                 1.3 |                                 12.1 |                                        52.3 |                                 23640.0 |                           8676612.9 |
| osqp     |                                10.5 |                                 56.0 |                                        14.8 |                                     6.5 |                             42153.8 |
| piqp     |                                90.8 |                                  1.0 |                                         1.0 |                                     1.0 |                               166.4 |
| proxqp   |                                50.0 |                                 34.4 |                                         9.7 |                                     4.2 |                                 1.0 |
| qpalm    |                                13.2 |                                  1.8 |                                         7.8 |                                     2.0 |                           3091085.5 |
| scs      |                                46.1 |                                 26.3 |                                        17.9 |                                     4.7 |                                 1.1 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        41 |              28 |             45 |             38 |
| cvxopt   |        42 |               4 |             34 |             13 |
| gurobi   |         1 |               1 |              1 |              1 |
| highs    |        62 |               0 |             28 |              1 |
| osqp     |        37 |              13 |              7 |             11 |
| piqp     |        93 |              67 |             95 |             91 |
| proxqp   |        63 |              34 |             62 |             50 |
| qpalm    |        53 |               8 |             11 |             13 |
| scs      |        55 |              24 |             67 |             46 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              89 |             97 |             96 |
| cvxopt   |        91 |              58 |             79 |             59 |
| gurobi   |       100 |             100 |            100 |            100 |
| highs    |        92 |              34 |             58 |             33 |
| osqp     |        54 |              88 |             47 |             80 |
| piqp     |        93 |              88 |             96 |             96 |
| proxqp   |        95 |              91 |             97 |            100 |
| qpalm    |        54 |              51 |             14 |             18 |
| scs      |        75 |              92 |             93 |             96 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     118.3 |            10.3 |           60.9 |           35.4 |
| cvxopt   |     110.1 |             9.8 |           64.7 |           30.3 |
| gurobi   |     680.4 |            52.0 |          484.1 |          213.0 |
| highs    |      36.5 |             3.5 |           25.3 |           12.1 |
| osqp     |       9.5 |            17.4 |           30.0 |           56.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |      73.4 |            10.1 |           47.2 |           34.4 |
| qpalm    |       3.2 |             4.3 |            3.1 |            1.8 |
| scs      |      17.6 |            15.7 |           19.0 |           26.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     702.2 |             3.3 |            1.7 |           11.0 |
| cvxopt   |     575.2 |       2549480.8 |            3.2 |        10230.8 |
| gurobi   |    1192.9 |             4.7 |            3.2 |           18.7 |
| highs    |     354.0 |         11564.5 |            1.0 |           52.3 |
| osqp     |    3941.8 |             3.8 |            2.3 |           14.8 |
| piqp     |       1.0 |             1.0 |            3.4 |            1.0 |
| proxqp   |     369.6 |             2.9 |            1.3 |            9.7 |
| qpalm    |     784.0 |             3.7 |            1.5 |            7.8 |
| scs      |    2916.3 |             3.8 |           36.7 |           17.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   11838.5 |          6536.6 |            9.9 |           36.6 |
| cvxopt   |    9648.1 |             2.0 |            6.3 |            4.3 |
| gurobi   |   20034.2 |             2.5 |            7.3 |            8.3 |
| highs    |    6003.9 |       7165193.1 |           24.1 |        23640.0 |
| osqp     |   56127.5 |             2.0 |            4.4 |            6.5 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |    6207.1 |             2.1 |            2.7 |            4.2 |
| qpalm    |   14213.7 |             1.3 |            1.0 |            2.0 |
| scs      |   12988.0 |             1.9 |            3.3 |            4.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |            36.0 |            1.9 |            1.2 |
| cvxopt   |       4.2 |    1753480544.8 |         5919.2 |      3387961.2 |
| gurobi   |       1.7 |             1.0 |            2.7 |            1.6 |
| highs    |       9.5 |    5554599469.9 |        14422.5 |      8676612.9 |
| osqp     |     337.4 |          4100.2 |         5805.3 |        42153.8 |
| piqp     |       1.9 |          6827.6 |            1.3 |          166.4 |
| proxqp   |       2.5 |             2.1 |            1.8 |            1.0 |
| qpalm    |      77.2 |       1717432.3 |        20732.3 |      3091085.5 |
| scs      |      13.9 |             1.0 |            1.0 |            1.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
