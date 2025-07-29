
# Description

Instead of deleting other parameters, this tool will output a full URL for each parameter with the different parameters alongside their values to never break the context, or have a response error "missing parameter".


# Basic Usage

```bash

echo "https://example.com?param1=value1&param2=value2&param3=value3" | 7cleanparam

# Output:

https://example.com?param1=value1&param3=value3&param2=
https://example.com?param1=value1&param2=value2&param3=
https://example.com?param2=value2&param3=value3&param1=

```

# Injecting Payloads Using `sed`

```bash

echo "https://example.com?param1=value1&param2=value2&param3=value3" | 7cleanparam | sed 's/$/&PAYLOAD/'

# Output:

https://example.com?param1=value1&param2=value2&param3=PAYLOAD
https://example.com?param1=value1&param3=value3&param2=PAYLOAD
https://example.com?param2=value2&param3=value3&param1=PAYLOAD

```

# Installation

```bash

# make sure you have python3 installed

git clone https://github.com/7-th/7cleanparam.git

cd 7cleanparam

sudo chmod +x ./7cleanparam.py

sudo cp ./7cleanparam.py /usr/bin/7cleanparam

```
