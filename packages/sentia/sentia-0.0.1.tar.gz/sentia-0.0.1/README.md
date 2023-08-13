# SENTIA

SENTIA is a PyTorch implementation of a text generation model combining multiple neural network architectures like GRUs, Transformers, MHAs and MEPA.

## Installation

```bash
pip install sentia
```
# Usage
```python
import torch
from sentia import SENTIA

# Create model
model = SENTIA(vocab_size=10000, embedding_dim=512, num_heads=8, num_layers=6, hidden_dim=512)

# Forward pass
input_ids = torch.randint(0, 10000, (1,32)) 
outputs = model(input_ids)

# Generate text 
generated = model.generate(input_ids, max_length=128)
```
# Model Architecture
The SENTIA model consists of the following components:

- Embedding layer
- Rotary Embedding
- MEPA (Mutation Enhanced Plasticity Architecture) layers
- Transformer decoder layers
- Multi-head attention layer
- Output head layers
_________________________________________________________________________________________________________________________
These components are combined to leverage the strengths of multiple architectures for improved text generation capabilities.
# Training
The fit() method can bne used to train the model on a dataset. It handles the training loop, gradient accumulation, and RL calculations. Currently the scheduler parameter only supports StepLR
