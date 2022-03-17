import numpy as np


class hp(object):

    # env
    joint1_range = [-5.0, 5.0]
    joint2_range = [-5.0, 5.0]
    step_size = 0.5
    goal_bound = 0.1
    margin = 0.0 #makes max value lower and min value higher and also increase node check boundary
    env_noise = 0.002 #noise in step fuction
    c_check_acc = 0.2 #accuracy of path collision(step check)
    state_dim = 4 #delta joint and goal
    action_dim = 2

    # agent
    gpu = 0
    lr_actor = 0.001
    lr_critic = 0.001
    tau = 0.005
    her_k = 4
    max_time_step = 50
    max_action = 1.

    target_noise_std = 0.2
    target_noise_clip = 0.5
    policy_delay = 2
    discount_factor = 0.98
    batch_size = 512
    memory_size = 1000000
    random_action_prob = 0.1
    action_noise_std = 0.1
    actor_update_freq = 2
    policy_noise = 0.2
    sigma = 0.1
    noise_clip = 0.5
    n_warmup = 2000
    policy_name = "TD3"

    actor_l1 = 400
    actor_l2 = 300

    critic_l1 = 400
    critic_l2 = 300

    max_step = int(1e7)

    save_model_interval =5000
