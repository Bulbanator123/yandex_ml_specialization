model_784_256_128_10_leaky = nn.Sequential(
    nn.Flatten(),

    nn.Linear(784, 256),
    nn.LeakyReLU(),

    nn.Linear(256, 128),
    nn.LeakyReLU(),

    nn.Linear(128, 10)
)

summary(model_784_256_128_10_leaky)