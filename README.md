# image-based-malware-dataloader

A PyTorch dataloader implementation for various image-based malware datasets. The package is available
on [PyPI](https://pypi.org/project/image-based-malware-dataloader/).

## Supported Datasets

| Dataset                                                                                         | Implementation Complete |
|-------------------------------------------------------------------------------------------------|:-----------------------:|
| MalImg ([Google Drive](https://drive.google.com/file/d/1M83VzyIQj_kuE9XzhClGK5TZWh1T_pr-/view)) |           :x:           |
| Microsoft Challenge ([Kaggle](https://www.kaggle.com/c/malware-classification))                 |           :x:           |
| Mal-Net Tiny Image ([Author Hosted Site](https://mal-net.org/#Download))                        |   :white_check_mark:    |
| Mal-Net Full Image ([Author Hosted Site](https://mal-net.org/#Download))                        |           :x:           |
| AdvNet: Lisa-CNN ([Author Hosted Site](https://advnet.seas.upenn.edu/download.html)             |   :white_check_mark:`*`   |

`*` We note that within the implementation of the AdvNet dataset, we have renamed all class label folders to `Adv` and `Clean` respectively.
