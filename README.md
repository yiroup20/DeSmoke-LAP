
# DeSmoke-LAP: Improved Unpaired Image-to-Image Translation for Desmoking in Laproscopic Surgery

Authors: Yirou Pan (<a href="mailto: yirou.pan.20@ucl.ac.uk">✉</a>), Sophia Bano, Vasconcelos Francisco, Hyun Park, Taikyeong Ted. Jeong and Danail Stoyanov

## Model Architecture

The model is built based on the architecture of <a href="https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix">CycleGAN</a> network, and two additional loss functions are added for inter-channel discrepancies and dark channel prior. 

Details of the researches can be access in our <a href="https://link.springer.com/article/10.1007/s11548-022-02595-2">paper</a>.

<img src='imgs/Proposed_flowchart.png' width=900>

## Sample Clips

Result comparisons on clips can be assess in the <a href="https://github.com/yiroup20/DeSmoke-LAP/tree/main/video%20clips">'video clips'</a> folder.

<!--  <img src='clips/Comparisons/gif/output_2.gif' width=384> -->

<!--  (a)Input (b)CycleGAN (c)FastCUT (d)GAN-DC (e)Proposed -->

## Dataset

The dataset is available to download <a href="[https://www.ucl.ac.uk/interventional-surgical-sciences/weiss-open-research/weiss-open-data-server/desmoke-lap](https://drive.google.com/drive/folders/1uxNHCQIcesUmyjWak8JoWOI6vnbGY-GB?usp=sharing)"> here</a>.

## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

### Model train/test
- You can follow the steps in our provided <a href="https://github.com/yiroup20/DeSmoke-LAP/blob/main/DeSmoke-LAP.ipynb">Colab Notebook</a> to train with your own data or use our pretrained models.

## Citation

If you use this code for your research, please cite our paper.

<!-- Pan, Y., Bano, S., Vasconcelos, F. et al. DeSmoke-LAP: improved unpaired image-to-image translation for desmoking in laparoscopic surgery. Int J CARS (2022). https://doi.org/10.1007/s11548-022-02595-2 -->

```
@article{pan2022desmoke,
  title={DeSmoke-LAP: improved unpaired image-to-image translation for desmoking in laparoscopic surgery},
  author={Pan, Yirou and Bano, Sophia and Vasconcelos, Francisco and Park, Hyun and Jeong, Taikyeong Ted and Stoyanov, Danail},
  journal={International Journal of Computer Assisted Radiology and Surgery},
  pages={1--9},
  year={2022},
  publisher={Springer}
  doi={https://doi.org/10.1007/s11548-022-02595-2}
}
```

<!-- ## Related Projects
- [contrastive-unpaired-translation](https://github.com/taesungp/contrastive-unpaired-translation) (CUT)
- [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) -->

## Acknowledgments
Our code is inspired by [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).
