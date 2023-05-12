#!/usr/bin/python3
# 4-hidden_discovery.py
# abdelkarim elaissaouy

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__") and not name.startswith("_"):
            print(name)
