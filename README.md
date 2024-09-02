
# Bilingual Text Summarizer (Nepali, English) Using Transformers

This project aims to design and implement a bilingual text summarizer capable of summarizing text in both Nepali and English using transformer-based models. The project utilizes the Google/mT5-small model, fine-tuned to handle the complexities of both languages.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Bilingual Text Summarizer is a machine learning project that focuses on summarizing text in two languages: Nepali and English. The project leverages the power of transformers, specifically the mT5-small model, which is fine-tuned to produce concise and coherent summaries in both languages.

## Features

- **Bilingual Support**: Summarizes text in Nepali and English.
- **Transformer-Based Model**: Uses the state-of-the-art mT5-small model for accurate and efficient summarization.
- **Custom Fine-Tuning**: The model has been fine-tuned on specific datasets to enhance performance in both languages.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Roshan-Chhetri28/Bilingual_text_summarizer.git
   cd Bilingual_text_summarizer
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the summarizer script:

   ```bash
   python summarizer.py --text "Your text here" --language "ne"  # For Nepali
   python summarizer.py --text "Your text here" --language "en"  # For English
   ```

2. The script will output the summarized text in the specified language.

## Methodology

This project follows the Iterative Waterfall methodology, ensuring a systematic and phased approach to development. The mT5-small model has been fine-tuned using a bilingual dataset, allowing it to handle the linguistic nuances of both Nepali and English effectively.

## Results

The model demonstrates strong performance in generating concise summaries for both languages. Further details on the results, including accuracy metrics and example summaries, can be found in the [Results](results/) directory.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
"# Bilingual_text_summarizer" 
"# Bilingual_text_summarizer" 
