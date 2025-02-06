import argparse

# Create main parser
parser = argparse.ArgumentParser(description="Parsing for running ML workflow...")
subparsers = parser.add_subparsers(dest="command", help="Choose a subcommand")

# Deep Learning Subparsers
deep_learning = subparsers.add_parser("dl", help="Deep Learning commands")
dl_subparsers = deep_learning.add_subparsers(dest="dl_command", help="Train or Evaluate")

# Train command
tr_parser = dl_subparsers.add_parser("train", help="For training")
tr_parser.add_argument("--epochs", type=int, default=100, help="Training epochs")
tr_parser.add_argument("--lr", type=float, default=1e-5, help="Learning rate coefficient")

# Eval command
ev_parser = dl_subparsers.add_parser("eval", help="For evaluating")
ev_parser.add_argument("--epochs", type=int, default=50, help="Epochs for evaluating")

# Machine Learning Subparsers
machine_learning = subparsers.add_parser("ml", help="Classical Machine Learning commands")
ml_subparsers = machine_learning.add_subparsers(dest="ml_command", help="Choose algorithm")

# XGBoost command
xgb_parser = ml_subparsers.add_parser("xgb", help="Training with XGBoost")
xgb_parser.add_argument("--features", type=int, default=5, help="Number of features")
xgb_parser.add_argument("--columns", type=int, default=10, help="Number of columns")

# Random Forest command
rand_parser = ml_subparsers.add_parser("forest", help="Training with Random Forest")
rand_parser.add_argument("--trees", type=int, default=20, help="Number of trees in the forest")
rand_parser.add_argument("--depth", type=float, default=0.3, help="Depth of the decision tree")

# Functions to handle commands
def train_model(epochs, lr):
    print(f"Training model for {epochs} epochs with learning rate {lr}")

def eval_model(epochs):
    print(f"Evaluating model with {epochs} epochs")

def train_xgb(features, columns):
    print(f"Training XGBoost model with {features} features and {columns} columns")

def train_forest(trees, depth):
    print(f"Training Random Forest with {trees} trees and depth {depth}")

# Parse arguments
args = parser.parse_args()

# Handle commands
if args.command == "dl":
    if args.dl_command == "train":
        train_model(args.epochs, args.lr)
    elif args.dl_command == "eval":
        eval_model(args.epochs)
elif args.command == "ml":
    if args.ml_command == "xgb":
        train_xgb(args.features, args.columns)
    elif args.ml_command == "forest":
        train_forest(args.trees, args.depth)
else:
    parser.print_help()
