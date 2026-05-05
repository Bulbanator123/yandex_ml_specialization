model_784_256_128_10 = nn.Sequential(
    nn.Flatten(),
    nn.Linear(in_features=784, out_features=256),
    nn.ReLU(),
    nn.Linear(in_features=256, out_features=128),
    nn.ReLU(),
    nn.Linear(in_features=128, out_features=10)
)

summary(model_784_256_128_10)


model_784_64_10 = nn.Sequential(
    nn.Flatten(),
    nn.Linear(in_features=784, out_features=64),
    nn.ReLU(),
    nn.Linear(in_features=64, out_features=10)
)

summary(model_784_64_10)



model_784_1024_10 = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 1024),
    nn.ReLU(),
    nn.Linear(1024, 512),
    nn.ReLU(),
    nn.Linear(512, 10)
)

summary(model_784_1024_10)