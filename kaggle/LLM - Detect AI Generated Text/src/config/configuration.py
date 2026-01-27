from pathlib import Path

import torch
import keras
import pandas as pd



class CFG:
    verbose = 0
    device = "cuda" if torch.cuda.is_available() else "cpu"
    seed = 42
    batch_size = 16
    drop_remainder = True
    sequence_length = 200

    # Paths
    data_dir = Path(__file__).resolve().parent.parent.parent / "data"
    ckpt_dir = Path(__file__).resolve().parent.parent.parent / "checkpoints"
    models_dir = Path(__file__).resolve().parent.parent.parent / "models"
    train_path = data_dir / "train_essays.csv"
    test_path = data_dir / "test_essays.csv"
    train_prompts_path = data_dir / "train_prompts.csv"

    # Model vocab paths
    vocab_path = models_dir / "vocab.spm"  # Local path
    kaggle_vocab_path = Path("/kaggle/input/keras-nlp-deberta-v3-base-en-vocab-ds/vocab.spm")  # Kaggle path

    @classmethod
    def get_vocab_path(cls):
        """Returns the appropriate vocab path (Kaggle if exists, else local)"""
        if cls.kaggle_vocab_path.exists():
            return cls.kaggle_vocab_path
        return cls.vocab_path

    # Labels
    class_names = ["real", "fake"]
    num_classes = len(class_names)
    class_labels = list(range(num_classes))
    label2name = dict(zip(class_labels, class_names))
    name2label = {v: k for k, v in label2name.items()}

    # Loaded lazily via load_data()
    train_essays: pd.DataFrame | None = None
    test_essays: pd.DataFrame | None = None
    train_prompts: pd.DataFrame | None = None

    @classmethod
    def seed_everything(cls):
        keras.utils.set_random_seed(cls.seed)

    @classmethod
    def load_data(cls):
        cls.train_essays = pd.read_csv(cls.train_path)
        cls.test_essays = pd.read_csv(cls.test_path)
        cls.train_prompts = pd.read_csv(cls.train_prompts_path)
