# Punycode Generator

## Overview

This script generates look-alike domains using IDN homographs and converts them to Punycode. It identifies visually similar Unicode characters that can be used to spoof domain names, helping security professionals analyze potential phishing or typosquatting risks.

## Why This is Useful

From a security standpoint, malicious actors often use homograph attacks to trick users into visiting fraudulent websites that appear to be legitimate. This script assists in detecting such deceptive domains by generating homoglyph variants and their corresponding Punycode representations.

## Setup

### 1. Create a Virtual Environment

It is recommended to run the script in an isolated environment:

```sh
python -m venv venv
```

### 2. Activate the Virtual Environment

- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

## Running the Script

To run the script, use:

```sh
python punycode_generator.py
```

Then, enter a domain (e.g., `google.com`), and the script will output look-alike domains along with
