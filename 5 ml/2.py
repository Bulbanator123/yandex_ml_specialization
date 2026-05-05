model_784_256_128_10_bn_dropout = nn.Sequential(
    nn.Flatten(),

    nn.Linear(784, 256),
    nn.BatchNorm1d(256),
    nn.ReLU(),
    nn.Dropout(0.3),

    nn.Linear(256, 128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
    nn.Dropout(0.3),

    nn.Linear(128, 10)
)

summary(model_784_256_128_10_bn_dropout)