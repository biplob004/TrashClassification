# Image/Trash Classification Streamlit Application

## Overview
This is a Streamlit application designed to classify different types of trash (such as cardboard, glass, and plastic) based on user-uploaded images. The application utilizes a pre-trained PyTorch model (ResNet101) for image classification, providing an interactive tool to promote recycling and environmental awareness.

## Features
- Upload images or provide image URLs for classification.
- Displays predicted trash type above the uploaded image.
- User-friendly interface built with Streamlit.
- Basic CSS styling for improved aesthetics.

## Demo
[![Demo Video](https://i.ytimg.com/vi/N-1FEisedAA/maxresdefault.jpg)](https://www.youtube.com/watch?v=N-1FEisedAA)

*Click the image above to watch the demo video.*

## Requirements
To run this application, you need the following Python packages:

- `streamlit`
- `torch`
- `torchvision`
- `Pillow`
- `requests`

### Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/biplob004/TrashClassification.git
   cd trash-classification-app
   ```

    #### Create a virtual environment:

    ```python
    python -m venv venv
    ```

    #### Activate the virtual environment:

     ##### On Windows:

     ```bash
     venv\Scripts\activate
     ```

     ##### On macOS/Linux:

     ```bash 
     source venv/bin/activate
     ```

    #### Install the required packages:

    ```bash 
    pip install -r requirements.txt
    ```

### Running the Application

To start the Streamlit application, run the following command:

```bash 
streamlit run app.py
```

### Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments

Thanks to the developers of Streamlit and PyTorch for their amazing libraries. And special thanks to kaggle user here https://www.kaggle.com/code/keycdy/pytorch-garbage-translearing-ensemble-test-99-67 . Anyone want training code and dataset can visit this link.
