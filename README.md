<div align="left" style="position: relative;">
<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>MACHINE_LEARNING-TRACKING_BARBELL_EXERCISES</h1>
<p align="left">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ 

This project aims to develop a machine learning model capable of classifying different types of barbell exercises based on inertial sensor data. By utilizing data from accelerometers and gyroscopes collected during a training session, the system can recognize the type of exercise being performed and calculate the number of repetitions automatically.

This project covers the entire machine learning pipeline, from data collection and pre-processing, data exploration, feature extraction, modeling, evaluation, to result visualization.</code>

---

## 👾 Features

<code>❯

- **Barbell Exercise Classification**: Recognizes different types of barbell exercises based on the movement patterns captured by the sensor.

- **Automatic Rep Count**: Calculates the number of reps of each exercise in real-time.

- **Sensor Data Pre-processing**: Cleans and prepares data from accelerometers and gyroscopes for further analysis.

- **Feature Extraction and Selection**: Identifying important features that contribute to model accuracy.

- **Model Evaluation**: Using metrics such as accuracy and confusion matrix to assess model performance.

- **Data and Results Visualization**: Provides graphs and plots to understand data distribution and model performance.

- **Modular Project Structure**: Neat code organization with separation between data, notebooks, scripts, and models.</code>

---

## 📁 Project Structure

```sh
└── Machine_Learning-Tracking_Barbell_Exercises/
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    │   └── .gitkeep
    ├── environment.yml
    ├── models
    │   ├── .gitkeep
    │   └── __pycache__
    ├── notebooks
    │   └── .gitkeep
    ├── references
    │   └── folder_structure.txt
    ├── reports
    │   └── figures
    ├── requirements.txt
    └── src
        ├── __init__.py
        ├── data
        ├── features
        ├── models
        └── visualization
```


### 📂 Project Index
<details open>
	<summary><b><code>MACHINE_LEARNING-TRACKING_BARBELL_EXERCISES/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/environment.yml'>environment.yml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<details>
				<summary><b>features</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/features/remove_outliers.py'>remove_outliers.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/features/TemporalAbstraction.py'>TemporalAbstraction.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/features/build_features.py'>build_features.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/features/count_repititions.py'>count_repititions.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/features/DataTransformation.py'>DataTransformation.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/features/FrequencyAbstraction.py'>FrequencyAbstraction.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>visualization</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/visualization/plot_settings.py'>plot_settings.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/visualization/Visualize.ipynb'>Visualize.ipynb</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/visualization/visualize.py'>visualize.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>models</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/models/predict_model.py'>predict_model.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/models/train_model.py'>train_model.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/src/models/LearningAlgorithms.py'>LearningAlgorithms.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- references Submodule -->
		<summary><b>references</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/master/references/folder_structure.txt'>folder_structure.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Machine_Learning-Tracking_Barbell_Exercises, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Conda, Pip


### ⚙️ Installation

Install Machine_Learning-Tracking_Barbell_Exercises using one of the following methods:

**Build from source:**

1. Clone the Machine_Learning-Tracking_Barbell_Exercises repository:
```sh
❯ git clone https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises
```

2. Navigate to the project directory:
```sh
❯ cd Machine_Learning-Tracking_Barbell_Exercises
```

3. Install the project dependencies:


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda env create -f environment.yml
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run Machine_Learning-Tracking_Barbell_Exercises using the following command:
**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda activate {venv}
❯ python {entrypoint}
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda activate {venv}
❯ pytest
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 🛣️ Project Roadmap: Barbell Exercise Tracking with Machine Learning

---

### 📌 Phase 1: Project Initialization & Data Acquisition
- Define project goals (e.g., classify barbell exercises, count reps)
- Collect and examine inertial sensor datasets
  - Example: [MetaMotion Dataset](https://mega.nz/folder/m4Vi3C6K#7zCktVdNIbKDTdAdvbsvrg)
- Set up development environment
  - Python 3.x, Jupyter Notebook, Pandas, Scikit-learn, etc.

---

### 🧹 Phase 2: Data Preprocessing & Exploration
- Clean the data (missing values, duplicates, outliers)
- Perform Exploratory Data Analysis (EDA)
  - Visualize feature distributions and correlations
- Feature engineering
  - Combine or extract new features from raw signals
  - Normalize or scale numerical values if needed

---

### 🤖 Phase 3: Model Development & Evaluation
- Select machine learning models
  - Random Forest, Decision Tree, SVM, KNN, etc.
- Split the dataset into training/testing subsets
- Train models and tune hyperparameters
- Evaluate performance using:
  - Accuracy
  - Confusion Matrix
  - Cross-validation scores

---

### 🛠️ Phase 4: Deployment & User Interface
- Save trained models using `joblib` or `pickle`
- Build a minimal interface (CLI or web app) for predictions
- Integrate model predictions with live or test input data
- Display predicted exercise type and count in a user-friendly format

---

### 🚀 Phase 5: Enhancement & Real-Time Features
- Enable real-time data input from wearable sensors
- Add feedback system (e.g., form quality warnings)
- Implement online learning or allow users to add labeled data
- Deploy app using platforms like Streamlit, Flask, or Gradio

---

Feel free to fork, customize, and expand this roadmap to fit your own fitness data science applications!


---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/issues)**: Submit bugs found or log feature requests for the `Machine_Learning-Tracking_Barbell_Exercises` project.
- **💡 [Submit Pull Requests](https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=atrkhomeini/Machine_Learning-Tracking_Barbell_Exercises">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---