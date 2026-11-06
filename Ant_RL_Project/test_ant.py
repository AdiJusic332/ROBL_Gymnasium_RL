
import gymnasium as gym

# Ant-Umgebung erstellen
env = gym.make("Ant-v5", render_mode="human")

observation, info = env.reset()

print("Observation Shape:", observation.shape)
print("Action Space:", env.action_space)
print("Initial Position:", info.get("x_position"))

for step in range(1000):

    # Zufällige Gelenkbewegungen
    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
