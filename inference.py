import torch
import pickle

from model import BiLSTM


# Device
device = torch.device("cpu")


# Load vocabulary
with open("vocab.pkl", "rb") as f:
    vocab = pickle.load(f)


# Load labels
with open("label2id.pkl", "rb") as f:
    label2id = pickle.load(f)

id2label = {v: k for k, v in label2id.items()}


max_len = 150


def encode(text):
    tokens = text.lower().split()

    ids = [vocab.get(token, 1) for token in tokens]

    if len(ids) < max_len:
        ids += [0] * (max_len - len(ids))
    else:
        ids = ids[:max_len]

    return ids


# Must match training architecture
embedding_dim = 100
hidden_dim = 128


model = BiLSTM(
    vocab_size=len(vocab),
    embedding_dim=embedding_dim,
    hidden_dim=hidden_dim,
    output_dim=len(label2id),
)


model.load_state_dict(torch.load("model.pth", map_location=device))

model.to(device)
model.eval()


def predict(text):

    ids = encode(text)

    x = torch.tensor([ids], dtype=torch.long).to(device)

    with torch.no_grad():
        output = model(x)

        pred = torch.argmax(output, dim=1).item()

    return id2label[pred]
