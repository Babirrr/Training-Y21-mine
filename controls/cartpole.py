import gym

env = gym.make("CartPole-v1")
observation = env.reset()

P = 9.8
I = 4.0
D = 4.0

force = 0
integral = 0
for _ in range(400):

  env.render()
  observe, reward, done, info = env.step(force)

  velocity = observe[1]
  angle = observe[2]
  angular_velocity = observe[3]

  integral = integral + angle

  F = P*(angle)  + I*(integral)+ D*(angular_velocity)

  force = 1
  if F > 0:
      force = 1
  else :
      force=0
  if done:
    observe = env.reset()
    integral = 0

env.close()