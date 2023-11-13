Code samples & snippets coming soon!

import numpy as np
from scipy import signal, datasets
import matplotlib.pyplot as plt

image = datasets.face(gray=True).astype(np.float32)
derfilt = np.array([2.0, -1, 2.0], dtype=np.float32)
ck = signal.cspline2d(image, 6.0)
