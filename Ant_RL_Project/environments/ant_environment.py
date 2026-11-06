import gymnasium as gym


def create_ant_env(render_mode=None):

    env = gym.make(
        "Ant-v5",
        render_mode=render_mode
    )

    return env


if __name__ == "__main__":

    env = create_ant_env()

    observation, info = env.reset(seed=42)

    print("=== ANT ENVIRONMENT ===")

    print("Observation Space:")
    print(env.observation_space)

    print("\nAction Space:")
    print(env.action_space)

    print("\nObservation Shape:")
    print(observation.shape)

    print("\nAction Shape:")
    print(env.action_space.shape)

    print("\nInitial Info:")
    print(info)

    env.close()
