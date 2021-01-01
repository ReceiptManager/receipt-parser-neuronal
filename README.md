# Receipt parser neuronal
Uses a modified version of [InvoiceNet](https://github.com/naiveHobo/InvoiceNet). It allows to parse receipts
via a neuronal network.

## Installation
### Step 1: First clone the repository.
```bash
git clone https://github.com/ReceiptManager/receipt-parser-neuronal
```

### Step 2: Initialize submodules
Since the receipt dataset is in a other repository. Initialize the submodule secondly.
```bash
git submodule update --init --recursive
```

### Step 3: Install thrirt party dependencies
Install following non python dependencies with your favorite package manager
* tesseract-ocr 
* poppler-utils 
* libxext-dev 
* libsm-dev 
* libxrender-dev

e.g. if you use `Debian` or `Ubunutu` distribution.
```bash
apt install -y tesseract-ocr poppler-utils libxext-dev libsm-dev libxrender-dev
```

### Step 4: Install python dependencies
Now, install the required python dependencies.
```bash
virtualenv env -p python3
source env/bin/activate
pip install .
```

## Usage
### Data Preparation
The training data must be arranged in a single directory. The invoice documents are expected be PDF files and each invoice is expected to have a corresponding JSON label file with the same name.

**You can find the training data in the [receipt-dataset](https://github.com/ReceiptManager/receipt-dataset) repository**

Prepare the data using the following e.g. if you use the `medium` sized dataset.
```bash
python prepare_data.py --data_dir train_data/train_data_medium
```
### Train the model
Now, you can train your receipt-parser model. This might take up to a few hours. I recommend to use the `batch_size=8`.
```bash
python train.py --field company --field total --field date --field address --batch_size 8
```
### Prediction

#### Single invoice
To extract a field from a single invoice file, run the following command:

```bash
python predict.py  --field company --field total --field date --field address --invoice path-to-invoice-file
```


#### Multiple invoices
For extracting information using the trained InvoiceNet model, you just need to place the PDF invoice documents in one directory in the following format:

```
predict_data/
    invoice1.pdf
    invoice2.pdf
    ...
```

Run InvoiceNet using the following command:
```bash
python predict.py --field company --field total --field date --field address  --data_dir predict_data/
```