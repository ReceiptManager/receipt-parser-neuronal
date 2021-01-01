import os
import sys

sys.path.insert(1, 'receipt-parser-neuronal')

from invoicenet.acp.acp import AttendCopyParse


def predict(filepath):
    paths = []
    if not os.path.exists(filepath):
        print("Could not find file '{}'".format(filepath))
        return
    paths.append(filepath)

    for field in [ "total", "company", "date" ]:
        model = AttendCopyParse(field=field, restore=True)
        model_predictions = model.predict(paths=paths)
        for prediction, filename in zip(model_predictions, paths):
            print("{}: {}\n".format(field, prediction))

