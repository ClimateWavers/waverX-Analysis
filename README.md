

# WaverX-Analysis Microservice for Climate Wavers

## Overview

The `WaverX-Analysis` microservice is a crucial component of the Climate Wavers disaster response application. It is dedicated to analyzing disaster magnitude using climate data from past disasters. The model, known as WaverX-Analysis, pulls data from a climate data services provider to run inferences on specified dates. Built on the OpenShift Data Science platform and utilizing the Intel oneAPI toolkit, the microservice is served with Flask. The model focuses on analyzing the magnitude of Storms, Floods, and Earthquakes due to the availability of sufficient data in these categories. The model is constructed using scikit-learn with a random forest classifier and further optimized with the Intel scikit-learn extension.

## Features

- **Magnitude Analysis:** Analyzes disaster magnitude using climate data from past disasters.
- **Supported Disasters:** Specifically analyzes Storms, Floods, and Earthquakes due to data availability.
- **Data Pulling:** Pulls data from a climate data services provider for real-time analysis.
- **Intel Optimization:** The model is optimized using the Intel oneAPI toolkit and scikit-learn extension for enhanced performance.
- **Flask API:** Served through a Flask API for seamless integration with other microservices.

## Technologies Used

- Scikit-learn
- Random Forest Classifier
- Intel oneAPI Toolkit
- Intel scikit-learn Extension
- Flask
- OpenShift Data Science

## Setup

### Prerequisites

- Python installed
- Scikit-learn installed
- Intel oneAPI toolkit installed
- Flask installed

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

   - Set up necessary configurations for the data provider and Flask API.

4. Start the microservice:

```bash
python app.py
```

## Usage

Describe how users can interact with the microservice, including API endpoints, request and response formats, and any other relevant details.

## Model Training

Include information on how the WaverX-Analysis model was trained, highlighting the scikit-learn random forest classifier and Intel scikit-learn extension.

## Contributing

If you'd like to contribute to the microservice, please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This microservice is licensed under the [MIT License](LICENSE).

## Acknowledgments

Mention any libraries, platforms, or individuals you want to acknowledge in the development of this microservice.

---

Feel free to customize and expand on these sections based on your specific details and requirements.
