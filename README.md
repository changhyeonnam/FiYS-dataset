# Shoes labeler
This repo is about labeling image with fine-grained description.
We're constructing Shoes Text-Image pair dataset for our capstone project.
After Constructing dataset, we're going to share our dataset. 
## Data Filtering
 1. Image Filtering
    - Removed images less than 5KB image size.
    - Removed images with an aspect ratio greater than 3.0.
    - Removed images with min(width, height) < 200.
2. For those that do not meet the above filtering criteria, change the name of each image to unique Id
3. Enter label.
   ```python
       label = f'brand is {brand}, name is {name}, upper is {upper}, midsole is {midsole},' \
            f'outsole is {outsole}, toebox is {toebox}, tongue is {tongue}, heeltab is {heeltab},' \
            f'top is {top}, shoelace is {shoelace}.'
   ```
4. Save in the ID column and label column in the data frame.
5. Repeat 1 to 4.

## Reference
1. [COYO from kakao brain](https://github.com/kakaobrain/coyo-dataset)
2. [WIT](https://github.com/google-research-datasets/wit)


## Quick Start
```python
poetry install
poetry run python -m main
```
