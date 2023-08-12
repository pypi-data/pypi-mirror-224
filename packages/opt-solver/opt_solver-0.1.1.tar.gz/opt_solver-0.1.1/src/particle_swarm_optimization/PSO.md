Particle Swarm Optimization (PSO) algorithm.
粒子群优化算法。

Represents the configuration parameters for the Particle Swarm Optimization algorithm.
表示粒子群优化算法的配置参数。

* `n_particles`:
Number of particles in the swarm.
群体中的粒子数量。
* `n_iters`:
Number of iterations for the optimization process.
优化过程的迭代次数。
* `c1`:
Acceleration coefficient for a particle's adjustment towards its own best position. Typically in the range [0, 2].
粒子朝向其自身最佳位置调整的加速系数。通常在范围 [0, 2] 内。
* `c2`:
Acceleration coefficient for a particle's adjustment towards the swarm's best position. Typically in the range [0, 2].
粒子朝向群体最佳位置调整的加速系数。通常在范围 [0, 2] 内。
* `max_v`:
Maximum velocity ratio for particle movement.
粒子移动的最大速度比率。
* `inertia`: Coefficient representing the influence of the particle's current velocity on its next position update.
表示粒子当前速度对其下一个位置更新的影响系数。

# Example

```rust
use your_crate::PSO;

let pso = PSO {
    n_particles: 100,
    n_iters: 100,
    c1: 1.0,
    c2: 1.0,
    max_v: 0.5,
    inertia: 0.5,
};
```